dn = input("Digite a data de nascimento (dd/mm/aaaa): ")
dn = dn.replace("/","")

acres = 0 

for n in dn:
	acres += int(n)

print(dn[0], "+", dn[1], "+", dn[2], "+", dn[3], "+", dn[4], "+", dn[5], "+", dn[6], "+", dn[7], "=", acres)
