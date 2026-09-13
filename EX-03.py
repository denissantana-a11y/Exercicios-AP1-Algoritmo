def formatar_real(valor):
    """
    Formata um número float no padrão de moeda brasileira.
    Ex: 1234.5 -> "1.234,50"
    """
    # Primeiro formata no padrão americano (1,234.50), usando a vírgula
    # como separador de milhar e o ponto como separador decimal
    # Depois troca os símbolos: "," vira "X" (temporário), "." vira ",",
    # e por fim "X" vira "." -> assim invertemos pro padrão brasileiro
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# ============ ENTRADA DE DADOS ============
# Cabeçalho do sistema, só pra deixar visualmente organizado
print("=" * 50)
print("      SISTEMA DE ALUGUEL DE CARRO")
print("=" * 50)

# input() sempre retorna texto (string), por isso nome e modelo
# não precisam de conversão, mas os valores numéricos precisam
nome_cliente = input("Nome do cliente: ")
modelo_carro = input("Modelo do carro: ")
preco_diaria = float(input("Preco da diaria (R$): "))   # float aceita casas decimais
dias = int(input("Quantidade de dias: "))                # int não aceita decimais
percentual_desconto = float(input("Percentual de desconto (%): "))

# ============ PROCESSAMENTO ============
# Aqui é onde os cálculos acontecem, usando os dados que o
# usuário acabou de digitar

subtotal = preco_diaria * dias
# Transforma o percentual (ex: 10) em fração (0.10) e aplica sobre o subtotal
valor_desconto = subtotal * (percentual_desconto / 100)
total_final = subtotal - valor_desconto
valor_medio = total_final / dias

# ============ SAÍDA FORMATADA ============
# Monta o "recibo" final juntando texto fixo com os valores calculados,
# usando f-strings para inserir as variáveis dentro do texto

print("\n" + "=" * 50)
print("         RECIBO DO ALUGUEL")
print("=" * 50)

print(f"Cliente:          {nome_cliente}")
print(f"Carro:            {modelo_carro}")
print(f"Dias alugados:    {dias} dia(s)")
# Chama a função formatar_real() criada lá em cima, pra exibir
# o preço já no formato "1.234,56" em vez de "1234.56"
print(f"Preco da diaria:  R$ {formatar_real(preco_diaria)}")
print("-" * 50)
print(f"Subtotal:         R$ {formatar_real(subtotal)}")
# :.0f mostra o percentual sem casas decimais (ex: 10% em vez de 10.0%)
print(f"Desconto:         {percentual_desconto:.0f}% (R$ {formatar_real(valor_desconto)})")
print("-" * 50)
print(f"TOTAL A PAGAR:    R$ {formatar_real(total_final)}")
print(f"\nValor medio por dia: R$ {formatar_real(valor_medio)}")

print("\n" + "=" * 50)
print("          OBRIGADO PELA PREFERENCIA!")
print("=" * 50)

# end="..." faz o print não pular linha no final, e sim continuar
# na mesma linha com "..." -> dá a impressão de um carregamento
print("Processando dados", end="... ")
print("Finalizado!", end="\n\n")