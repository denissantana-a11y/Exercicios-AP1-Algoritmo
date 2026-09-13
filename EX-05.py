"""
Sistema simples de avaliação de carros para uma concessionária
"""

# ============================================
# 1. IF DENTRO DE IF
# ============================================

def verificar_liberacao_carro():
    """
    Verifica se o carro pode ser liberado para venda,
    usando estrutura aninhada.
    """
    print("\n=== VERIFICACAO DE LIBERACAO ===")

    km = float(input("Digite a quilometragem do carro: "))
    revisado = input("O carro está com a revisão em dia? (s/n): ")

    print(f"Km: {km} - Revisado: {revisado}")

    # Primeira verificação: revisão em dia.
    # Só se essa condição for verdadeira o Python "entra" no bloco
    # de dentro, onde está o segundo if -> por isso é chamado de "aninhado"
    if revisado.lower() == "s":
        print("Revisão OK")

        # Segunda verificação: só é avaliada se a primeira já passou
        if km <= 100000:
            print("RESULTADO: LIBERADO - Revisão e km dentro do esperado")
        else:
            print(f"RESULTADO: NAO LIBERADO - Revisão OK, mas km {km} muito alta")
    else:
        # Se a revisão não estiver em dia, nem chega a checar a km
        print("RESULTADO: NAO LIBERADO - Revisão pendente")

# ============================================
# 2. ESTRUTURA COM ELIF
# ============================================

def classificar_estado_carro():
    """
    Classifica o estado do carro usando elif,
    de acordo com a quilometragem.
    """
    print("\n=== CLASSIFICACAO DO CARRO ===")

    km = float(input("Digite a quilometragem para classificar: "))

    print(f"Km: {km}")

    # O Python testa cada condição de cima para baixo e para
    # na primeira que for verdadeira -> por isso a ordem importa:
    # do mais específico (menor km) para o mais geral
    if km <= 10000:
        classificacao = "SEMINOVO"
    elif km <= 50000:
        classificacao = "BOM ESTADO"
    elif km <= 100000:
        classificacao = "USADO"
    elif km <= 150000:
        classificacao = "RODADO"
    else:
        classificacao = "MUITO RODADO"

    print(f"CLASSIFICACAO: {classificacao}")

# ============================================
# 3. MATCH CASE SIMPLES
# ============================================

def processar_menu_oficina():
    """
    Processa opções de menu da oficina usando match case.
    """
    print("\n=== MENU DA OFICINA ===")
    print("1 - Agendar revisão")
    print("2 - Trocar óleo")
    print("3 - Alinhamento e balanceamento")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    # match compara "opcao" com cada "case" de cima para baixo,
    # parecido com um if/elif, mas pensado pra comparar um valor
    # com várias opções fixas
    match opcao:
        # Padrão simples: compara direto com o texto "1"
        case "1":
            print("OPCAO 1: Agendar revisão")

        case "2":
            print("OPCAO 2: Trocar óleo")

        case "3":
            print("OPCAO 3: Alinhamento e balanceamento")

        # O "|" funciona como "ou" -> aceita "4" OU "sair" como entrada válida
        case "4" | "sair":
            print("OPCAO 4: Sair do sistema")

        # "_" é o coringa: pega qualquer valor que não bateu em nenhum case acima
        case _:
            print(f"OPCAO INVALIDA: {opcao}")

# ============================================
# 4. MATCH CASE
# ============================================

def avaliar_carro():
    """
    Avalia a situação do carro usando match case com guarda,
    baseado no ano e na quilometragem.
    """
    print("\n=== AVALIACAO DO CARRO ===")

    modelo = input("Digite o modelo do carro: ")
    ano = int(input("Digite o ano do carro: "))
    km = float(input("Digite a quilometragem: "))

    print(f"Carro: {modelo} - Ano: {ano} - Km: {km}")

    # Agrupa os dois valores numa tupla, pra poder comparar os dois
    # de uma vez só dentro do match
    dados = (ano, km)

    match dados:
        # "Guarda" é a condição extra depois do "if" dentro do case.
        # Aqui, (a, _) captura o ano em "a" e ignora a km (usa "_" pra km,
        # já que ela não importa nessa condição)
        case (a, _) if a >= 2023:
            print(f"{modelo}: SEMINOVO DESTAQUE - Ano {a}")

        # Aqui capturamos os dois valores (ano em "a", km em "k")
        # e exigimos que as duas condições sejam verdadeiras
        case (a, k) if a >= 2018 and k <= 80000:
            print(f"{modelo}: BOM NEGOCIO - Ano {a}, Km {k}")

        case (a, k) if a >= 2013 and k <= 120000:
            print(f"{modelo}: NEGOCIO REGULAR - Ano {a}, Km {k}")

        case (a, k) if a < 2013 or k > 120000:
            print(f"{modelo}: NECESSITA AVALIACAO EXTRA - Ano {a}, Km {k}")

        # Caso nenhuma guarda acima seja satisfeita, cai aqui
        case _:
            print(f"{modelo}: SITUACAO INDEFINIDA")


# ============================================
# 5. MENU INTERATIVO
# ============================================

def main():
    """
    Função principal com menu interativo.
    """
    print("=" * 50)
    print("SISTEMA DA CONCESSIONARIA")
    print("Demonstracao de estruturas de selecao")
    print("=" * 50)

    # while True cria um loop que só para quando um "break" é executado
    # -> assim o menu continua aparecendo até o usuário escolher sair
    while True:
        print("\n" + "-" * 50)
        print("MENU PRINCIPAL")
        print("-" * 50)
        print("1 - Verificar Liberacao (Estrutura Aninhada)")
        print("2 - Classificar Estado do Carro (Estrutura ELIF)")
        print("3 - Menu da Oficina (Match Case)")
        print("4 - Avaliar Carro (Match Case com Guarda)")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção (1-5): ")

        # Chama a função correspondente à opção escolhida
        if opcao == "1":
            verificar_liberacao_carro()
        elif opcao == "2":
            classificar_estado_carro()
        elif opcao == "3":
            processar_menu_oficina()
        elif opcao == "4":
            avaliar_carro()
        elif opcao == "5":
            print("\nSaindo do sistema...")
            break  # encerra o while True, finalizando o programa
        else:
            print("\nOPCAO INVALIDA! Tente novamente.")

        # Pausa a tela até o usuário apertar Enter, pra dar tempo
        # de ler o resultado antes do menu aparecer de novo
        input("\nPressione Enter para continuar...")

# ============ PONTO DE ENTRADA ============
# Esse "if" garante que main() só roda quando o arquivo é executado
# diretamente (e não quando ele é importado por outro script)
if __name__ == "__main__":
    main()