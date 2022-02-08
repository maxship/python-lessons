mystring = "bla-bla"

name = "mr. mAx shIp"

print(name.title())

print(name.upper())

print(name.lower())

print("Privet stroka nomer1\nPrivet stroka2\n\nStroka 3")
print("Messages:\n\tMessage 1\n\tMessage2\n\tMessage3\nEND")

print("Lower name: " + name.lower())
print("-----------")
a = " ,dyadya vasya . "
print(a.rstrip())
print(a.lstrip())
print(a.strip())
a = " ,dyadya vasya ....."

print(a.strip(". ,")) #обрезка лишних символов

a = a.strip(".") #то же самое другим способом
a = a.strip()
a = a.strip(",")
print(a)