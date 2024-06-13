name=input('Hi what is your name? ')
def somename(name,food,food2='Pizzas'):
    if name.lower()=='tanay':
        print(f'welcome {name} to the restaurant')
    print(f"hello {name}. Let's eat some {food} and some {food2}")

somename(name,'bananas')#passing values from a function

#returing from a function

def somefunction():
    return "a value"

thing=somefunction()
print(thing)

#exponent calculator
def exp(num1,num2):
    total=num1**num2
    return total

number=exp(25,4)
print(number)
