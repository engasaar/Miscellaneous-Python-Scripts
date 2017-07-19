import random
y=random.randint(0,9)
x=0
while(x!='exit'):
    x=input("please guess the number:")
    if(x>y):
        print "your guess is greater than the value try again"
    elif(x<y):
        print "your guess is less than the value try again"
    else:
        break
        
print "your guess is perfect"
    
