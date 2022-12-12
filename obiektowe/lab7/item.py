
class Item:
    def __init__(self, mass):
        if int(mass) <= 0:
            raise ValueError('mass has to be greater than zero')
        self.mass = int(mass)

    def mass(self):
        return self.mass

    def __eq__(self, other: "Item") -> bool:
        return self.mass == other.mass


class Container(Item):
    def __init__(self, mass, lift_cap):
        super().__init__(mass)
        if int(lift_cap) <= 0:
            raise ValueError('lifting capacity has to be greater than zero')
        self.lift_cap = lift_cap
        self.list_of_items = []

    def put_item(self, thing):
        if not thing:
            raise ValueError('you have to give something to put')
        if thing.mass <= self.lift_cap:
            self.list_of_items.append(thing)

    def remove_item(self, thing):
        if not thing:
            raise ValueError('you have to give something to pull out')
        if thing not in self.list_of_items:
            raise ValueError('you cannot pull out sth that is not in the box')
        if thing.mass <= self.lift_cap:
            self.list_of_items.remove(thing)

    def items_in_box(self):
        return self.list_of_items
