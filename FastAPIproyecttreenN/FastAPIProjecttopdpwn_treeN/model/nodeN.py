from model.person import Person

class NodeN:
    def __init__(self, data: Person):
        self.data = data
        self.children = []

    def add_child(self, child: Person):
        if self.data.id == child.parent_id:
            self.children.append(NodeN(child))
            return "Hijo agregado correctamente"
        else:
            for x in self.children:
                result = x.add_child(child)
                if result == "Hijo agregado correctamente":
                    return result

            return "Padre no encontrado"

    def remove_child(self, child_id: str):

        for i in range(len(self.children)):
            if self.children[i].data.id == child_id:

                child_to_remove = self.children[i]
                heir = None

                for j in range(len(child_to_remove.children)):
                    current_child = child_to_remove.children[j]
                    if heir is None:
                        heir = current_child
                    else:
                        if heir.data.age < current_child.data.age:
                            current_child.children.append(heir)
                            heir = current_child
                        else:
                            heir.children.append(current_child)

                if heir:
                    self.children[i] = heir
                else:
                    self.children.pop(i)
                return "Hijo eliminado correctamente"

        for child in self.children:
            result = child.remove_child(child_id)
            if result:
                return result

        return None

    def find_person_by_id(self, child_id: str):
        if child_id == self.data.id:
            return self.data
        else:
            for x in self.children:
                result = x.find_person_by_id(child_id)
                if result != None:
                    return result
        return None


    def update_person(self, person_id: str, person: Person):
        if self.data.id == person_id:
            self.data.name = person.name
            self.data.last_name = person.last_name
            self.data.age = person.age
            self.data.gender = person.gender
            self.data.type_doc = person.type_doc
            self.data.location = person.location
            return "Persona actualizada correctamente"
        else:
            for x in self.children:
                result = x.update_person(person_id, person)
                if result == "Persona actualizada correctamente":
                    return result
        return None

    def list_all(self):
        return {
            "id": self.data.id,
            "name": self.data.name,
            "last_name": self.data.last_name,
            "age": self.data.age,
            "gender": self.data.gender,
            "type_doc": vars(self.data.type_doc),
            "location": vars(self.data.location),
            "children": [child.list_all() for child in self.children]
        }

    def list_persons_with_adult_daughters(self):
        persons_with_adult_daughters = []
        for child in self.children:
            if child.data.gender.lower() == "femenino" and child.data.age >= 18:
                persons_with_adult_daughters.append(self.data)
                break
        for child in self.children:
            persons_with_adult_daughters.extend(child.list_persons_with_adult_daughters())

        return persons_with_adult_daughters

    def filter_by_location(self, location_code: str):
        list_by_location = []
        if self.data.location.code == location_code:
            list_by_location.append(self.data)
        for x in self.children:
            list_by_location.extend(x.filter_by_location(location_code))

        return list_by_location


    def filter_by_location_typedoc_gender(self, location_code: str, typedoc_code: str, gender: str):
        list_by_location_typedoc_gender = []
        if self.data.location.code == location_code and self.data.type_doc.code == typedoc_code and self.data.gender == gender:
            list_by_location_typedoc_gender.append(self.data)
        for x in self.children:
            list_by_location_typedoc_gender.extend(x.filter_by_location_typedoc_gender(location_code, typedoc_code, gender))

        return list_by_location_typedoc_gender