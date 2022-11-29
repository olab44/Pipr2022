from definitions import Person

# jurek = Person()
# jurek.first_name = 'Jurek'
# jurek.last_name = 'Ogórek'

# karolina = Person()
# karolina.first_name = 'Karolina'
# karolina.last_name = 'Malina'

# strawberry = Object()
# strawberry.color = 'red'
# strawberry.name = 'strawberry'

# agata = Person()
# agata.introduce()

jurek = Person('Jurek', 'Ogórek', 19)
karolina = Person('Karolina', 'Malina')
agata = Person('Agata', 'Pomiata')
agata.introduce()

print(jurek.introduce())
