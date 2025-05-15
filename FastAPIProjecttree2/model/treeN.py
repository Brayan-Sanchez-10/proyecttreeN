from model.location import Location
from model.nodeN import NodeN
from model.person import Person

class TreeN:
    def __init__(self):
        self.root = None
        self.nodes = []

    def add_child(self, child: Person, parent_id: str = None):
        child_node = NodeN(child)

        if self.root is None and parent_id is None:
            self.root = child_node
            self.nodes.append(child_node)
            return "Raíz agregada correctamente"

        elif parent_id:
            for node in self.nodes:
                if node.data.id == parent_id:
                    child_node.set_parent(node)
                    self.nodes.append(child_node)
                    return "El hijo fue agregado correctamente"
            return "Padre no encontrado, no se puede agregar al árbol"

        return "Debes especificar un ID de padre para agregar un nuevo nodo (ya hay raíz)"

    def remove_child(self, parent_id: str = None):
        if self.nodes != []:
            parent_node = None
            for node in self.nodes:
                if node.data.id == parent_id:
                    parent_node = node
                    break

            if parent_node is None:
                return f"No se encontró un nodo con id '{parent_id}', nada que eliminar."

            for node in self.nodes:
                if node.parent and node.parent.data.id == parent_id:
                    node.parent = None

            if self.root == parent_node:
                self.root = None
            self.nodes.remove(parent_node)
            return f"Nodo con id '{parent_id}' eliminado correctamente y sus hijos quedaron huérfanos."

        else:
          return "El arbol esta vacio"

    def find_person_by_id(self, child_id: str):
        if self.nodes != []:
            for node in self.nodes:
                if node.data.id == child_id:
                    return node
            return "No existe persona con ese ID"
        else:
            return "El arbol esta vacio"


    def list_all(self):
        if self.nodes == []:
            return "El arbol esta vacio"
        else:
            return self.nodes

    def update_person(self, child_id: str, child: Person):
        if self.nodes != []:
            for node in self.nodes:
                if node.data.id == child_id:
                    node.data.name = child.name
                    node.data.last_name = child.last_name
                    node.data.age = child.age
                    node.data.gender = child.gender
                    node.data.type_doc = child.type_doc
                    node.data.location = child.location
                    return "La persona fue actualizada correctamente"
            return "No existe persona con ese ID"
        else:
            return "El árbol está vacío"

    def list_persons_with_adult_daughters(self):
        if self.nodes == []:
            return "El árbol está vacío"

        result = []
        for node in self.nodes:
            if node.parent and node.data.gender == "F" and node.data.age >= 18:
                if node.parent not in result:
                    result.append(node.parent)

        return result
    def filter_by_location(self, location_code: str):
        if self.nodes != []:
            result = []
            for node in self.nodes:
                if node.data.location.code == location_code or node.data.location.department_code == location_code:
                    result.append(node)
            return result
        else:
            return "El arbol esta vacio"


    def filter_by_location_typedoc_gender(self, location_code: str, typedoc_code: str, gender: str):
        if self.nodes != []:
            result = []
            for node in self.nodes:
                if (node.data.location.code == location_code or node.data.location.department_code == location_code) and node.data.type_doc.code == typedoc_code and node.data.gender == gender:
                    result.append(node)
            return result
        else:
            return "El arbol esta vacio"