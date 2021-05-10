tabela = {
	61: "Brasilia",
	71: "Salvador",
	11: "São Paulo",
	21: "Rio de Janeiro",
	32: "Juiz de Fora",
	19: "Campinas"
}

codigo = int(input("Digite o código de área: "))

if codigo not in tabela:
	print(f"DDD {codigo} não cadastrado")
else:
	print(tabela[codigo])