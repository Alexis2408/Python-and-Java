people = [
    {"name":"Dominik", "S.O":"Windows"},
    {"name":"Aldahir", "S.O":"Mac"},
    {"name":"Alexis", "S.O":"Linux"},
]
#def f(person):
    #return person["name"]
#people.sort(key=f)
#ambos funcionan de la misma forma
people.sort(key=lambda person: person["S.O"])
print(people)