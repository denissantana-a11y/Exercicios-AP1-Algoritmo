"""
Programa: Classificador de Carteira de Motorista
Descrição: Verifica se uma pessoa pode alugar um carro baseado na idade e posse de CNH
Regras:
- Menor de 18 anos: Aluguel negado
- 18 anos ou mais COM CNH: Aluguel liberado
- 18 anos ou mais SEM CNH: Solicitar apresentação da CNH
"""

# ============ ENTRADA ============

# Coletando a idade com validação (repete até digitar um número válido e não-negativo)
while True:
    try:
        # Tenta converter o que foi digitado para número inteiro.
        # Se a pessoa digitar uma letra ou algo que não seja número,
        # o Python gera um ValueError e cai no except
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
            continue  # volta pro início do while, pedindo a idade de novo
        break  # número válido, sai do loop
    except ValueError:
        print("Entrada inválida! Digite um número inteiro para a idade.")

# Coletando a informação sobre a CNH com validação
while True:
    # strip() remove espaços em branco no início/fim, e lower() deixa tudo minúsculo
    # -> assim "Sim", " SIM ", "sim" são todos tratados da mesma forma
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
# A partir daqui, o programa decide qual das 3 situações se aplica,
# usando os dados coletados acima

if idade < 18:
    # Caso 1: menor de idade -> nem entra na segunda condição,
    # já é barrado aqui independente de ter CNH ou não
    mensagem = "Aluguel não permitido"
    status = "negado"

elif idade >= 18 and tem_cnh:
    # Caso 2: idade OK e tem CNH -> libera o aluguel
    mensagem = "Aluguel liberado"
    status = "permitido"

else:
    # Caso 3: só sobra essa possibilidade -> idade OK mas SEM CNH
    mensagem = "Apresente sua CNH"
    status = "pendente"

# ============ SAÍDA ============
# Monta o resultado final na tela, mostrando os dados informados
# e o status calculado acima

print("\n" + "=" * 50)
print("        RESULTADO DA CLASSIFICAÇÃO")
print("=" * 50)

print(f"Idade informada:   {idade} anos")
# Expressão condicional dentro da f-string: se tem_cnh for True, mostra "Sim",
# senão mostra "Não" -> é um jeito resumido de escrever um if/else numa linha só
print(f"Possui CNH:        {'Sim' if tem_cnh else 'Não'}")
print("-" * 50)
# .upper() deixa a mensagem toda em maiúsculo, só para dar destaque visual
print(f"Status:            {mensagem.upper()}")

# Esse if/elif/else é só para escolher qual frase de "Motivo" exibir,
# de acordo com o status definido no processamento
if status == "negado":
    print("Motivo: Idade mínima para alugar é 18 anos.")
elif status == "permitido":
    print("Motivo: Idade e CNH verificadas com sucesso.")
else:
    print("Motivo: É necessário apresentar a CNH para alugar.")

print("=" * 50)