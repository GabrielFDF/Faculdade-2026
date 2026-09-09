# Preços fixos do cardápio
preco_hamburguer = 25.00
preco_batata = 12.00
preco_refrigerante = 8.00
preco_sobremesa = 10.00

# Entrada das quantidades
qtd_hamburguer = int(input("Quantidade de hambúrgueres: "))
qtd_batata = int(input("Quantidade de batatas: "))
qtd_refrigerante = int(input("Quantidade de refrigerantes: "))
qtd_sobremesa = int(input("Quantidade de sobremesas: "))

# Cálculo dos subtotais
subtotal_hamburguer = preco_hamburguer * qtd_hamburguer
subtotal_batata = preco_batata * qtd_batata
subtotal_refrigerante = preco_refrigerante * qtd_refrigerante
subtotal_sobremesa = preco_sobremesa * qtd_sobremesa

# Cálculo do subtotal geral
subtotal = 0
subtotal += subtotal_hamburguer
subtotal += subtotal_batata
subtotal += subtotal_refrigerante
subtotal += subtotal_sobremesa

# Taxa de serviço de 10%
taxa_servico = subtotal * 0.10
total = subtotal + taxa_servico

# Verificação se o total ultrapassou R$ 200
if total > 200:
    print("\nAtenção! O total da conta ultrapassou R$ 200,00.")
else:
    print("\nO total da conta não ultrapassou R$ 200,00.")

# Gorjeta opcional
resposta_gorjeta = input("Deseja deixar uma gorjeta extra? (sim/não): ").lower()

if resposta_gorjeta == "sim":
    valor_gorjeta = total * 0.10
    total += valor_gorjeta
else:
    valor_gorjeta = 0

# Quantidade de pessoas
pessoas = int(input("Em quantas pessoas deseja dividir a conta? "))

# Desconto de 5% para mais de 4 pessoas
if pessoas > 4:
    desconto = total * 0.05
    total -= desconto
    print("\nFoi aplicado um desconto de 5% por dividir a conta entre mais de 4 pessoas.")
else:
    desconto = 0

# Validação da quantidade de pessoas
if pessoas > 0:
    valor_por_pessoa = total / pessoas

    # Saída formatada
    print("\n==========================================")
    print("       CONTA DO RESTAURANTE")
    print("==========================================")
    print(f"Hambúrguer:       R$ {subtotal_hamburguer:.2f}")
    print(f"Batata:           R$ {subtotal_batata:.2f}")
    print(f"Refrigerante:     R$ {subtotal_refrigerante:.2f}")
    print(f"Sobremesa:        R$ {subtotal_sobremesa:.2f}")
    print("------------------------------------------")
    print(f"Subtotal:         R$ {subtotal:.2f}")
    print(f"Taxa de serviço:  R$ {taxa_servico:.2f}")
    print(f"Gorjeta:          R$ {valor_gorjeta:.2f}")
    print(f"Desconto:         R$ {desconto:.2f}")
    print("------------------------------------------")
    print(f"Total:            R$ {total:.2f}")
    print(f"Dividido por:     {pessoas} pessoa(s)")
    print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")
    print("==========================================")
else:
    print("Quantidade de pessoas inválida. Digite um número maior que zero.")
