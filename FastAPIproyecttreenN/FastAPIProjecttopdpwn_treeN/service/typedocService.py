from model.typedoc import Typedoc

class TypedocService:
    def __init__(self):
       self.docs = [
          Typedoc(code="C.C", description="Cedula de Ciudadania"),
          Typedoc(code="T.I", description="Tarjeta de Identidad"),
          Typedoc(code="P.P", description="Pasaporte")
          ]
    def get_all(self):
        return self.docs