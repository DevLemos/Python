import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)


# Funções
"""
Nesse pacote existem alguns métodos:

re.match: determina se a expressão regular combina com o início da string. Retorna a posição da string buscada.
re.search: varre toda a string, procurando o primeiro local onde esta expressão regular tem correspondência. Retorna a posição da string buscada.
re.findall: encontra todas as substrings que têm correspondência com a expressão regular, e as retorna como uma lista. Retorna uma lista com as strings encontradas.
re.finditer: encontra todas as substrings que têm correspondência com a expressão regular, e as retorna como um iterador.
re.sub: procura onde esta expressão regular tem correspondência e faz as substituições desejadas. Retorna a string com a substituição realizada
"""

string = "frase que será analisada pelo regex porque regex é legal e útil"
a = re.match('frase', string)
print(a)

b = re.match('regex', string)
print(b)

c = re.search('regex', string)
print(c)

# Isso me retorna uma lista[‘que’, ‘que’], sendo o segundo relativo a palavra ‘porque’.
d = re.sub('analisada', 'avaliada', string)
print(d)
e = re.findall('que', string)
print(e)

f = re.finditer('regex', string)
print(f)

for i in re.finditer('regex', string):
    print(i)
