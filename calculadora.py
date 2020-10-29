def suma(a,b):
    s=a+b
    print("la suma es:",s)
a=float(input('Valor de a:"'))
b=float(input('Valor de b:"'))

suma(a,b)
suma(b,a)

def resta(a,b):
    r=a-b
    print("la resta es:",r)
a=float(input('Valor de a:"'))
b=float(input('Valor de b:"'))

resta(a,b)

def multiplicacion(a,b):
    p=a*b
    print("la multiplicacion es:",p)
a=float(input('Valor de a:'))
b=float(input('Valor de b:'))

multiplicacion(a,b)
multiplicacion(b,a)

def division(dividendo,divisor):
    if(divisor==0 or divisor==0.0):
        return[0, False]
    else:
        return[(dividendo/divisor), True]
a=float(input('Valor de a:'))
b=float(input('Valor de b:'))
d,status=division(a,b)
if(status):
    print("La division es:"+str(d))
else:
    print("Error-divisor=0")