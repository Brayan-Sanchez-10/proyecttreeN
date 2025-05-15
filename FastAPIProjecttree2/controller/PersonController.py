from fastapi import APIRouter, HTTPException
from model.person import Person
from model.treeN import TreeN
from typing import Optional
from fastapi import Query, Body
from service.treeService import TreeService
router = APIRouter()

tree_service = TreeService()

@router.post("/person")
def create_person(person: Person, parent_id: Optional[str] = None):
    return {"message": tree_service.tree.add_child(person, parent_id)}




@router.get("/person/{child_id}")
def get_person_by_id(child_id: str):
    result = tree_service.tree.find_person_by_id(child_id)
    if isinstance(result, str):
        raise HTTPException(status_code=404, detail=result)
    return {"person": result.data.dict()}


@router.delete("/person/{parent_id}")
def delete_person(parent_id: str):
    result_message = tree_service.tree.remove_child(parent_id)
    if "No se encontró" in result_message:
        raise HTTPException(status_code=404, detail=result_message)
    return {"message": result_message}


@router.get("/persons")
def list_all_persons():
    result = tree_service.tree.list_all()
    if isinstance(result, str):  # Cuando devuelve el mensaje de árbol vacío
        raise HTTPException(status_code=404, detail=result)
    # Aquí result es la lista de nodos, retornamos la info de las personas
    return {"persons": [node.data.dict() for node in result]}


@router.put("/person/{person_id}")
def update_person(person_id: str, updated_person: Person):
    result = tree_service.tree.update_person(person_id, updated_person)

    if result != "La persona fue actualizada correctamente":
        raise HTTPException(status_code=404, detail=result)

    return {"message": result}



@router.get("/persons/adult-daughters")
def get_parents_with_adult_daughters():
    result = tree_service.tree.list_persons_with_adult_daughters()

    if isinstance(result, str):
        # Aquí result es un mensaje de error o aviso
        raise HTTPException(status_code=404, detail=result)

    # Si result es lista de nodos, retornamos solo los datos
    return {"parents": [node.data.dict() for node in result]}

@router.get("/persons/location/{location_code}")
def get_persons_by_location(location_code: str):
    """
    Filtra las personas del árbol según el código de ubicación o de departamento.
    """
    result = tree_service.tree.filter_by_location(location_code)

    if isinstance(result, str):  # Ej: "El árbol está vacío"
        raise HTTPException(status_code=404, detail=result)

    return {
        "filtered_persons": [node.data.dict() for node in result]
    }

@router.get("/persons/filter/{location_code}/{typedoc_code}/{gender}")
def filter_persons_by_location_type_gender(location_code: str, typedoc_code: str, gender: str):
    """
    Filtra personas por ubicación (ciudad o departamento), tipo de documento y género.
    """
    result = tree_service.tree.filter_by_location_typedoc_gender(location_code, typedoc_code, gender)

    if isinstance(result, str):  # Ej: "El arbol esta vacio"
        raise HTTPException(status_code=404, detail=result)

    return {
        "filtered_persons": [node.data.dict() for node in result]
    }