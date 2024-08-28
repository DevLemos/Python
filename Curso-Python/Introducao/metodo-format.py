a = 'A'
b = 'B'
c = 1.1

# Por ordem
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
print(formato)

# Por indices
formato2 = 'a={0} a={0} a={0}  b={1} c={2:.2f}'.format(a, b, c)
print(formato2)

# Nomeando parâmetros
string = 'b={nome1} a={nome2} c={nome3:.2f}'.format(nome1=a, nome2=b, nome3=c)
print(string)
