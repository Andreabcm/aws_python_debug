import pdb

def suma(a, b):
    resultado = a + b
    pdb.set_trace()  
    return resultado

x = 5
y = 3
z = suma(x, y)
print(z)

