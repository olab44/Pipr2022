class NotEnoughStuffError(Exception):
    def __init__(self):
        super().__init__('not enough material for the product you need')


class Storage:
    def __init__(self, glicerine=0, aloes=0, alcohol=0, conservant=0):
        if glicerine < 0 or aloes < 0 or alcohol < 0 or conservant < 0:
            raise ValueError('amount cannot be negative')
        self.glicerine = glicerine
        self.aloes = aloes
        self.alcohol = alcohol
        self.conservant = conservant

    def print_report(self):
        print('| Zasób      | Ilość w magazynie [l] |')
        print('|', '-'*10, '|', '-'*21, '|')
        print(f'| gliceryna  | {self.glicerine}', ' '*18, '|')
        print(f'| aloes      | {self.aloes}', ' '*18, '|')
        print(f'| alkohol    | {self.alcohol}', ' '*18, '|')
        print(f'| konserwant | {self.conservant}', ' '*17, '|')


class Order:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products
        self.products = {}
        for pair in list_of_products:
            product, amount = pair
            self.products[product] = amount
        self.pair = pair

    def products_needs(self):
        needs = {'alcohol': 0, 'glicerine': 0, 'aloes': 0, 'conservant': 0}
        for pair in self.list_of_products:
            product, amount = pair
            amount = amount
            if product == 'aloes_gel':
                needs['alcohol'] += round(amount * 0.6, 2)
                needs['glicerine'] += round(amount * 0.1, 1)
                needs['aloes'] += round(amount * 0.35, 2)
            if product == 'desin_gel':
                needs['alcohol'] += round(amount * 0.72, 2)
                needs['glicerine'] += round(amount * 0.03, 2)
            if product == 'things_gel':
                needs['alcohol'] += round(amount * 0.8, 1)
                needs['glicerine'] += round(amount * 0.005, 3)
            if product == 'mask':
                needs['conservant'] += round(amount * 0.05, 2)
        return needs

    def checking_avaiability(self, storage):
        needs = self.products_needs()
        if needs['alcohol'] > storage.alcohol:
            raise ValueError('not enough stuff')
        if needs['glicerine'] > storage.glicerine:
            raise ValueError('not nenough stuff')
        if needs['aloes'] > storage.aloes:
            raise ValueError('not enough stuff')
        if needs['conservant'] > storage.conservant:
            raise ValueError('not enough stuff')
    
    def __str__(self):
        needs = self.products_needs()
        return f'for your order you need {needs["alcohol"]} of alcohol, {needs["glicerine"]} of glicerine, {needs["aloes"]} of aloes and {needs["conservant"]} of conservant'


def results():
    print(storage.print_report())
    print(order.products_needs())
    print(order.__str__())


storage = Storage(3, 5, 6, 1)
order = Order([('aloes_gel', 3), ('desin_gel', 2), ('mask', 5)])
print(results())