num1=eval(input('Entra el primer nombre :'))
num2=eval(input('Entra el segon nombre :'))

for n in range(num1,num2+1):
    if n%2==0:
        print(n,'és parell')
    else:
        print(n,'és imparell')
