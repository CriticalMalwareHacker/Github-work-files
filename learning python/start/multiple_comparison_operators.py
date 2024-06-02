age=18
name='Tanay'
if age>=18:
    if name == 'Tanay':
        print('I can drive')       
else: 
    print('nothing')
#using and statement both statements have to be true
if age>=18 and name=='Tanay':
    print('I can drive')  
else:
    print('nothing')
#using 'or' statement atleast one of the conditions have to be true
if age>=18 or name=='Tanay':
    print('I can drive')  
else:
    print('nothing')