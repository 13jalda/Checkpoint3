# variables
phrase = "mañana me levantare con energia"
members = 40
animals = ["dog", "cat", "bird"]
is_alone = True

# exercise
three_letters = phrase[0:3]
print(three_letters)

animal = animals[0]
print(animal)

new_members = members + 10
print(new_members)

last_animal = animals[-1]
print(last_animal)

names = 'harry,alex,susie,jared,gail,conner'
lnames = names.split(',')
print(lnames)

sub_phrase = phrase[0:6]
rest_phrase = phrase[6:]
new_phrase =sub_phrase.upper() + rest_phrase
print(new_phrase)


text_interpolation = f"The members that the club has are {members}"

print(text_interpolation)

print('hello world')


cadena = "Frase que contega Hola"
print(cadena.find("Hola"))

cadena = cadena.replace("Hola", "Adiós")
print(cadena)