
def add(a,b):
     return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def divide(a,b):
    return a / b
 
opers = {'+' : add,
         '-' : sub,
         '*' : mult, 
         '/' : divide}
while True:
    expression = input('Calculate \n  >')  
    if expression:
        try:
             (op1,op,op2) = expression.split(' ')
             print(opers[op](int (op1),int(op2)))
        except:
            print('Input invalid')
    else: 
        break
    