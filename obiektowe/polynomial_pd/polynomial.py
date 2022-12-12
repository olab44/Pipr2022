class Polynomial:
    def __init__(self, representation=None):
        '''
        Class Polynomial. Contains atributes:

        :param representation: list of pairs of degrees and coefficients
        :param type: list of tuples
        '''
        representation = sorted(representation, reverse=True)
        degrees = []
        coefficients = []
        for pair in representation:
            self._degree, self._coeff = pair
            if self._coeff == 0:
                raise ValueError('coefficeint cannot be equal to zero')
            if self._degree in degrees:
                raise ValueError('this degree is already in the list')
            if self._degree < 0:
                raise ValueError('degree cannot be negative')
            if self._degree >= 0:
                degrees.append(self._degree)
                coefficients.append(self._coeff)
        self._degrees = degrees
        self._coefficients = coefficients
        self._representation = representation

    def __str__(self):
        '''
        returns mathematic form of the polymonial
        '''
        description = []
        for pair in self._representation:
            self._degree, self._coeff = pair
            symbol = '+' if self._coeff > 0 else ''
            if self._degree == 1:
                description.append(f'{symbol}{self._coeff}x')
            if self._degree == 0:
                description.append(f'{symbol}{self._coeff}')
            else:
                description.append(f'{symbol}{self._coeff}x^{self._degree}')
        description = "" .join(description)
        if description[0] == '+':
            return description[1:]
        return description

    @property
    def degree(self):
        '''
        returns the degree of the polymonial
        '''
        self._max_degree = max(self._degrees)
        return self._max_degree

    def coefficient(self, power):
        '''
        returns the coefficient by the given degree
        '''
        for pair in self._representation:
            self._degree, self._coeff = pair
            if power not in self._degrees:
                raise ValueError('given power is not in the list')
            if self._degree == power:
                return self._coeff

    def value(self, number):
        '''
        returns the value of polymonial for given number
        '''
        value = 0
        for pair in self._representation:
            self._degree, self._coefficient = pair
            value += self._coefficient * (number ** self._degree)
        return value

    def __eq__(self, other: "Polynomial") -> bool:
        return self._representation == other._representation

    def __add__(self, other: "Polynomial") -> "Polynomial":
        deg_coeffs = {}
        for pair in self._representation:
            self._degree, self._coeff = pair
            for other_pair in other._representation:
                other._degree, other._coeff = other_pair
            for degree in self._degrees:
                if degree in other._degrees:
                    deg_coeffs[degree] = self._coeff + other._coeff
                else:
                    deg_coeffs[self._degree] = self._coeff
        for other._degree in other._degrees:
            if other._degree not in self._degrees:
                deg_coeffs[other._degree] = other._coeff
        list = []
        for key in deg_coeffs:
            key, deg_coeffs[key] = pair
            list.append(pair)
            return list

        return list
