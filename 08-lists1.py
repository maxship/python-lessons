cities = ['New York', 'Moskow', 'new dehly', 'Simpheropol', 'Toronto']

print(cities)

print(len(cities))
print(cities[0]) #указание индекса
print(cities[-2]) #указание позиции с конца
print(cities[2].title())

cities[2] = 'Tula'
print(cities)

cities.append('Kursk') #добавление в конец списка
cities.append('Yalta') 
cities.insert(2, 'Feodosia')  #добавление внутрь списка на указанную позицию
print(cities)

del cities[-1] #удалить индекс
print(cities) 

cities.remove('Tula') #удаление конкретного значения
print(cities)

cities.sort(reverse=True) #sort
print(cities)

cities.reverse() #reverse
print(cities)