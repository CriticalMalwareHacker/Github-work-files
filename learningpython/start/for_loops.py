foods=['Pizza','Sushi','Pasta']
#printing all the items in the list
for food in foods:
    print(f'my fav food is: {food}')

for food in foods:
    if food == 'Pasta':
        size=input('what size pizza would you like?')
        print(f'you ordered a {size} pizza')
#printing all the letters in a string
a='pizza'
for letter in a:
    print(letter)

#printing using dictionary
car = {
    'name':'Buggatti',
    "speed":"300km/h",
    'color':'blue'
}
for key,value in car.items():
    print(f'the key is {key} and the value is {value}')