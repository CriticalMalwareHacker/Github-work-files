#values in tuples cannot be changed once created
vehicles=('Bugatti','Lamborghini','Ford',)
for car in vehicles:
    print("The car is",car)
#the only functions that work with tuples
print(vehicles.count('Ford'))
print(vehicles.index('Ford'))
#count counts the number of occurences
#index counts the index value which begins from 0,1,2..