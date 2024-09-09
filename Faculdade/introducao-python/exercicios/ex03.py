"""
Faça a conversão para um novo tipo de comprimento conhecido como N9. Utilize a seguinte fórmula para isso:  N9=(metros∗Euler)+1/3
"""

metros = 35
euler = 2.718281

N9 = (((metros * euler) * 1/3))
print(N9)
print(type(N9))
