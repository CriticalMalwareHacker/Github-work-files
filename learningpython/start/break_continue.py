
#two will be skipped since its continued
items=['one','two','three','four','five']
for item in items:
    if item == 'two':
        continue
    print(item)
#break stops the entire for loop once the condition is met
items=['one','two','three','four','five']
for item in items:
    if item == 'two':
        break
    print(item)

print('\n')
print('\n')
num=0
while num<=20:
    num=num+1
    if num%2==0:
        continue
    print(num)