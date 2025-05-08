from fastapi import APIRouter, HTTPException
from service.locationService import LocationService

router = APIRouter(prefix="/locations", tags=["Locations"])
location_service = LocationService()


@router.get("/capitals")
def get_capitals():
    capitals = location_service.get_capitals()
    if not capitals:
        raise HTTPException(status_code=404, detail="No se encontraron capitales.")
    return capitals


@router.get("/states")
def get_states():
    states = location_service.get_states()
    if not states:
        raise HTTPException(status_code=404, detail="No se encontraron departamentos.")
    return states


@router.get("/state/{code}")
def get_locations_by_state_code(code: str):
    result = location_service.get_locations_by_state_code(code)
    if not result:
        raise HTTPException(status_code=404, detail=f"No se encontró un departamento con código {code}")
    return {"department": result}


@router.get("/{code}")
def get_location_by_code(code: str):
    result = location_service.get_location_by_code(code)
    if not result:
        raise HTTPException(status_code=404, detail=f"No se encontró municipio con código {code}")
    return {"municipality": result}