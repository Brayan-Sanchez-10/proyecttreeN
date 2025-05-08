from fastapi import FastAPI
from controller import LocationController, TypedocController, PersonController

app = FastAPI()

app.include_router(LocationController.router)
app.include_router(TypedocController.router)
app.include_router(PersonController.router)