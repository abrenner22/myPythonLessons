# multiply without * operation in py 

num1 = int(input('Insert the first number'))
num2 = int(input('Insert the second number'))

def multiply_machine(num1, num2):
    product = 0
    i = 0
    
    while i < num2:
        product += num1
        i = i + 1
    
    return product

result = multiply_machine(num1, num2)

print(f'The result is: {result}')

#Essa primeira versão está funcional, mas não realiza multiplicações de números negativos. 
