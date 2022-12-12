
class Price:
    def __init__(self, value=0, currency='gr'):
        if currency not in exchanges:
            raise ValueError('this value is not reachable, not in our options')
        if value < 0:
            raise ValueError('price cannot be negative')
        self.value = int(value)
        self.currency = currency

    def __str__(self):
        return f'the price is {self.value} {self.currency}'

    def exchange_currency(self, new_currency):
        if self.currency == 'gr':
            return round(self.value * exchanges_from_gr[new_currency])
        if self.currency == 'eurocent':
            return round(self.value * exchanges_from_eurocent[new_currency])
        if self.currency == 'cent':
            return round(self.value * exchanges_from_cent[new_currency])

    def __eq__(self, other: 'Price') -> 'Price':
        return self.value == other.value

    def __add__(self, new_currency, other: 'Price') -> 'Price':
        return Price(self.value + other.value)

    def __sub__(self, new_currency, other: 'Price') -> 'Price':
        return Price(self.value - other.value)

    def __mul__(self, multiplier: 'float') -> 'float':
        return Price(multiplier * self.value)

    def __rmul__(self, multiplier: 'float') -> 'float':
        return Price(self.value * multiplier)


exchanges_from_gr = {'eurocent': 0.208, 'cent': 0.224, 'gr': 1}
exchanges_from_cent = {'eurocent': 0.929, 'cent': 1, 'gr': 4.46}
exchanges_from_eurocent = {'eurocent': 1, 'cent': 1.076, 'gr': 4.80}
