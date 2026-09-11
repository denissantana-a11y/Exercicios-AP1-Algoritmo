# ============ FUNÇÃO DE FORMATAÇÃO ============
def formatar_real(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ============ ENTRADA DE DADOS ============
print("=" * 50)
print("      SISTEMA DE ALUGUEL DE CARRO")
print("=" * 50)

nome_cliente = input("Nome do cliente: ")
modelo_carro = input("Modelo do carro: ")
preco_diaria = float(input("Preco da diaria (R$): "))
dias = int(input("Quantidade de dias: "))
percentual_desconto = float(input("Percentual de desconto (%): "))

# ============ PROCESSAMENTO ============
subtotal = preco_diaria * dias
valor_desconto = subtotal * (percentual_desconto / 100)
total_final = subtotal - valor_desconto
valor_medio = total_final / dias

# ============ SAÍDA FORMATADA ============
print("\n" + "=" * 50)
print("         RECIBO DO ALUGUEL")
print("=" * 50)

print(f"Cliente:          {nome_cliente}")
print(f"Carro:            {modelo_carro}")
print(f"Dias alugados:    {dias} dia(s)")
print(f"Preco da diaria:  R$ {formatar_real(preco_diaria)}")
print("-" * 50)
print(f"Subtotal:         R$ {formatar_real(subtotal)}")
print(f"Desconto:         {percentual_desconto:.0f}% (R$ {formatar_real(valor_desconto)})")
print("-" * 50)
print(f"TOTAL A PAGAR:    R$ {formatar_real(total_final)}")
print(f"\nValor medio por dia: R$ {formatar_real(valor_medio)}")

print("\n" + "=" * 50)
print("          OBRIGADO PELA PREFERENCIA!")
print("=" * 50)

print("Processando dados", end="... ")
print("Finalizado!", end="\n\n")