#         0         1           2       3
cars = ['bmw', 'wolksvagen', 'lada', 'shkoda']

for car in cars:
  print(car.upper())

for x in range(1, 6):
  print(x)

my_number_list = list(range(0,10))
print(my_number_list)
print("---------------------")

for x in my_number_list:
  x = x*2
  print(x)

my_number_list.sort(reverse=True)
print(my_number_list)

print('Max number is: ' + str(max(my_number_list)))
print('Min number is: ' + str(min(my_number_list)))
print('Sum is: ' + str(sum(my_number_list)))
print("---------------------")

my_cars = cars[1:3] #take range of indexes from other list: 1 - start index, 4 - number of indexes from 0
print(my_cars)

my_cars = cars[:4]
print(my_cars)

my_cars = cars[-2:]
print(my_cars)

my_cars = cars[-2:-1]
print(my_cars)

mycars = cars[:] #copy list, ":" is needed

