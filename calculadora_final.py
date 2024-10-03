print("Desafio do Lava Jato - Matemática Discreta - Prof. Odilon")   
print("############ ENCONTRAR O PONTO DE EQUILÍBRIO ############")
print("DIGITE APENAS NÚMEROS INTEIROS\n ")
lavagem = int(input("Digite o valor da lavagem:"))
aluguel = int(input("Digite o valor do aluguel: "))
salario = int(input("Digite o salário de cada funcionário: "))
funcionario_quant = int(input("Digite a quantidade de funcionários: "))
agua_luz = int(input("Digite o gasto mensal com Água e Luz: "))
custo_lavagem = int(input("Digite o gasto com produto de limpeza por carro: "))
comissao = int(input("Comissão por carro lavado: "))
imposto_func = 4

v = comissao*imposto_func/10
variavel = v+custo_lavagem+comissao

custo_func = funcionario_quant * salario 
imp = int(custo_func*4)/10
fixo = agua_luz + imp + aluguel + custo_func

print("")
print("O valor total de custo fixo da empresa é: R$",fixo)

lc_final = lavagem - variavel
l = lc_final - fixo

print ("Lucro por carro lavado= R$",lc_final)
print("Custo da empresa: R$",variavel+fixo)
print("Ponto de Equilíbrio da Empresa é: " , fixo/lc_final)
print("")
print("Aluna: Kátia Y. Sato - Análise e Desenvolvimento de Sistemas 1 Semestre - FATEC Americana\n")
input("Pressione <enter> para encerrar")
