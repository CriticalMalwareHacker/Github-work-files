
"""try:
    a=10
    b=0
    c=a/b
    print(c)

except:
    print("can't divide by 0")"""

try:
    a=int(input("Enter the value of A"))
    b=int(input("Enter the value of B"))
    c=a/b
    print(c)
except (ValueError,ZeroDivisionError):
    print("Entered value is wrong")
except ZeroDivisionError:
    print("Can't divide by zero")
else:#only executes if the try block has no exceptions, output is correct
    print("This is an else block")
finally:#will be executed in each and every condition
    print("This is a finally block")
