#function with inputs

def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet('guilherme')

#function with more than 1 input

def greet_with_more_parameters(name, location):
    print(f"Hi {name}")
    print(f"what isd it like in {location}")
greet_with_more_parameters('guilherme', 'divinopolis')