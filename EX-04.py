"""
Programa: Classificador de Carteira de Motorista
Descrição: Verifica se uma pessoa pode alugar um carro baseado na idade e posse de CNH
Regras:
- Menor de 18 anos: Aluguel negado
- 18 anos ou mais COM CNH: Aluguel liberado
- 18 anos ou mais SEM CNH: Solicitar apresentação da CNH
"""

# ============ ENTRADA DE DADOS ============

# Coletando a idade com validação (repete até digitar um número válido e não-negativo)
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
            continue  # volta pro início do while
        break  # número válido, sai do loop
    except ValueError:
        print("Entrada inválida! Digite um número inteiro para a idade.")

# Coletando a informação sobre a CNH com validação
while True:
    resposta = input("Você possui CNH? (Digite 'sim' ou 'nao'): ").strip().lower()
    if resposta in ['sim', 's', 'yes', 'y']:
        tem_cnh = True
        break
    elif resposta in ['nao', 'não', 'n', 'no']:
        tem_cnh = False
        break
    else:
        print("Resposta inválida! Digite 'sim' ou 'nao'.")

# ============ PROCESSAMENTO ============

if idade < 18:
    # Caso 1: menor de idade -> nem entra na segunda condição
    mensagem = "Aluguel não permitido"
    status = "negado"

elif idade >= 18 and tem_cnh:
    # Caso 2: idade OK e tem CNH
    mensagem = "Aluguel liberado"
    status = "permitido"

else:
    # Caso 3: idade OK mas NÃO tem CNH (único caso que sobra)
    mensagem = "Apresente sua CNH"
    status = "pendente"

# ============ SAÍDA FORMATADA ============

print("\n" + "=" * 50)
print("        RESULTADO DA CLASSIFICAÇÃO")
print("=" * 50)

print(f"Idade informada:   {idade} anos")
print(f"Possui CNH:        {'Sim' if tem_cnh else 'Não'}")
print("-" * 50)
print(f"Status:            {mensagem.upper()}")

if status == "negado":
    print("Motivo: Idade mínima para alugar é 18 anos.")
elif status == "permitido":
    print("Motivo: Idade e CNH verificadas com sucesso.")
else:
    print("Motivo: É necessário apresentar a CNH para alugar.")

print("=" * 50)