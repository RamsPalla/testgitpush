class practice3:
    def __init__(AHPS, name, grade, percentage):
        AHPS.name = name
        AHPS.grade = grade
        AHPS.percentage = percentage
    def __list(self):
        return padya.percentage,kaavyansh.percentage

padya = practice3("padya", "IV", 70)
kaavyansh = practice3("kaavyansh", "NURSERY", 85)
print(padya.name)
print(padya.grade)
print(padya.percentage)
print(padya._practice3__list())

class practice4(practice3):
    name = "arjun"
    _grade = "SECOND"
    __percentage = "75"
arjun = practice4("ram", "second", "65")
print(padya.name)
print(padya.grade)
print(padya.percentage)
print(padya._practice3__list())
print(arjun.name)
print(arjun._grade)
print(arjun.grade)
print(arjun.percentage)
print(arjun._practice4__percentage)
print(practice4.name)



