from model.nodeN import NodeN
from model.person import Person

class TreeN:
    def __init__(self):
        self.root = None

    def add_person(self, person: Person):
        if self.root == None:
            self.root = NodeN(person)
            return "Adicionado como raíz"
        else:
            return self.root.add_child(person)

    def remove_person(self, person_id: int):
        if self.root is None:
            return "El árbol está vacío"

        if self.root.data.id == person_id:
            if not self.root.children:
                self.root = None
                return "Root eliminado correctamente"
            else:
                heir = None
                for child in self.root.children:
                    if heir is None:
                        heir = child
                    else:
                        if heir.data.age < child.data.age:
                            child.children.append(heir)
                            heir = child
                        else:
                            heir.children.append(child)
                self.root = heir
                return "Root eliminado correctamente y reemplazado por heredero"

        return self.root.remove_child(person_id)

    def find_person_by_id(self, person_id: int):
        if self.root == None:
            return "El árbol está vacío"
        else:
            return self.root.find_person_by_id(person_id)

    def update_person(self, person_id: int, person: Person):
        if self.root == None:
            return "El árbol está vacío"
        else:
            return self.root.update_person(person_id, person)

    def list_all(self):
        if self.root == None:
            return "El árbol está vacío"
        else:
            return self.root.list_all()

    def list_persons_with_adult_daughters(self):
        if self.root == None:
            return "El árbol está vacío"
        else:
            return self.root.list_persons_with_adult_daughters()

    def filter_by_location(self, location_code: str):
        if self.root == None:
            return "El árbol está vacío"
        else:
            return self.root.filter_by_location(location_code)

    def filter_by_location_typedoc_gender(self, location_code: str, typedoc_code: str, gender: str):
        if self.root == None:
            return "El árbol está vacío"
        else:
            return self.root.filter_by_location_typedoc_gender(location_code, typedoc_code, gender)

