import re
##arq = open("calculadora.cpp", "r")
arq = open("codigo.c", "r")
tokens = []
palavra_reservada = ["const", "while", "While", "WHILE", "if",
 "IF", "iF", "If", "#include", "<iostream>", "using", "namespace", "std", "int", "float", "string", "return", ";", "<stdio.h>"]
operadores = ["+", "-", "*", "/"]
atribuidor = ["="]
operadores_comparacao = ["<", ">", "<=", ">=", "==", "!="]
delimitadores = ["{", "}", "[", "]", "(", ")"]
for x in arq:
    x = x.strip()
    lista = x.split()
    for y in lista:
        y = y.strip()
        if(";" in y):
            y = y.split(";")
            tokens.append(y[0])
            tokens.append(";")
        elif("(" in y):
            y = y.split("(")
            tokens.append(y[0])
            tokens.append("(")
            tokens.append(")")
        else:
            tokens.append(y)
for x in tokens:
    if x in operadores:
        print(x+" - Operador")
    elif x in atribuidor:
        print(x+" - Comando de atribuição")
    elif x in palavra_reservada:
        print(x+" - Palavra reservada")
    elif x in operadores_comparacao:
        print(x+" - Operadores de comparação")
    elif x in delimitadores:
        print(x+" - Delimitadores")
    elif re.match('".*"', x):
        print(x+" - Literal")  
    elif re.match("\d", x):
        print(x+" - Número")  
    else:
        print(x+" - Variável/Função")  
     
        
            