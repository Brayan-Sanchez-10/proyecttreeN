from fastapi import APIRouter, HTTPException
from model.person import Person
from service.treeService import TreeService

router = APIRouter()
tree_service = TreeService()

@router.post("/person")
def add_person(person: Person):
    try:
        result = tree_service.tree.add_person(person)
        if result == "Padre no encontrado":
            raise HTTPException(status_code=404, detail="Padre no encontrado")
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/person/{person_id}")
def delete_person(person_id: str):
    result = tree_service.tree.remove_person(person_id)
    if result == "El árbol está vacío" or result == "Padre no encontrado":
        raise HTTPException(status_code=404, detail=result)
    return {"message": result}

@router.get("/person/{person_id}")
def get_person(person_id: str):
    person = tree_service.tree.find_person_by_id(person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return person

@router.put("/person/{person_id}")
def update_person(person_id: str, person: Person):
    result = tree_service.tree.update_person(person_id, person)
    if result is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return {"message": result}

@router.get("/persons")
def list_all():
    result = tree_service.tree.list_all()
    if result == "El árbol está vacío":
        raise HTTPException(status_code=404, detail=result)
    return result

@router.get("/persons/adult-daughters")
def list_persons_with_adult_daughters():
    result = tree_service.tree.list_persons_with_adult_daughters()
    return result


@router.get("/persons/filter")
def filter_persons(location_code: str = "", typedoc_code: str = "", gender: str = ""):
    if location_code and typedoc_code and gender:
        result = tree_service.tree.filter_by_location_typedoc_gender(location_code, typedoc_code, gender)
    elif location_code:
        result = tree_service.tree.filter_by_location(location_code)
    else:
        raise HTTPException(status_code=400, detail="Parámetros insuficientes")

    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron resultados para los filtros proporcionados.")

    return result