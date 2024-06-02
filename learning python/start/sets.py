s = {"Item 1","Item 2","Item 3"}
print(s)
#doesnt care about the order, prints randomized order every time
#if the variables are repeated it only prints it once
s.add('Item 4')
print(s)
s.remove('Item 4')
print(s)