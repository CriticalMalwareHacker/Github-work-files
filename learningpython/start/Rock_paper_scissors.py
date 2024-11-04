import random
print('Welcome to rock, paper and scissors')
num=0

def select():
    var=input('Select Rock, Paper or Scissors: or type quit to quit:')
    return var

while num<1:
    op=select()
    op2=random.choice(['Rock','Paper','Scissors'])
    if(op.lower()=='quit'):
        break
    print('I choose',op2,'\n')
    print('You choose',op,'\n')
    if(op.lower()==op2.lower()):
        print('Tied!')
        continue
    if(op.lower()=='rock' and op2.lower()=='scissors'):
        print('You win!')
        break
    elif(op.lower()=='scissors' and op2.lower()=='paper'):
        print('You win!')
        break
    elif(op.lower()=='paper' and op2.lower()=='rock'):
        print('You win!')
        break
    elif(op.lower()!='rock' and op.lower()!='scissors'and op.lower()!='paper'and op.lower()!='quit'):
        print('Please choose a correct option')
        continue
    else:
        print('You lose! Try again')
        continue

