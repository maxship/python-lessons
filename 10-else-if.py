x = 26

if x == 25:
  print("It's true")
else:
  print("It's not")

print("============")

age = 12

if age <= 4:
  print("Baby")
elif age > 4 and age < 12:
  print("Kid")
elif age >= 12 and age <= 19:
  print("Teen")
elif age >= 19:
  print("Adult")

print("============")

all_cars = ['bmw', 'wolksvagen', 'opel', 'lada', 'shkoda', 'KIA', 'Toyota', 'ford', 'renault']
german_cars = ['bmw', 'wolksvagen', 'opel']

if 'lada' in all_cars:
  print("Yes, Lada is in the list")
else:
  print("No, Lada is not in the list")

print("============")

for x in all_cars: # цикл по большому списку
  if x in german_cars: # сравнение со значениями малого списка
    print(x + " is German car")
  # else:
  #   print(x + " is not German car")