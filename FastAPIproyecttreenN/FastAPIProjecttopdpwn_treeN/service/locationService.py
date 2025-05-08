import pandas as pd

from model import location
from model.location import Location


class LocationService:
    def __init__(self):
        self.df = pd.read_csv("./csv/DIVIPOLA-_C_digos_municipios_20250501.csv")
        self.locations = []
        for i in range(len(self.df)):
            fila = self.df.iloc[i]
            location = Location(
                code=str(fila["Código Municipio"]),
                description=fila["Nombre Municipio"],
                department_code=str(fila["Código Departamento"]),
                department_name=fila["Nombre Departamento"]
            )
            self.locations.append(location)
    def get_capitals(self):
        capitals = []
        for x in range (len(self.locations)):
            if str(self.locations[x].code) == str(self.locations[x].department_code) + "001":
                capitals.append(self.locations[x].description)
        return capitals

    def get_states(self):
        states = {}
        for location in self.locations:
            code_str = str(location.department_code)
            if code_str not in states:
                states[code_str] = location.department_name
        return states

    def get_locations_by_state_code(self, code: str):
        locations = []
        for x in range(len(self.locations)):
            code_str = str(self.locations[x].code)
            if code_str[0] == str(self.locations[x].department_code):
                locations.append(self.locations[x].description)
        return locations

    def get_location_by_code(self, code: str):
        for x in range(len(self.locations)):
            if str(self.locations[x].code) == code:
                return self.locations[x].description