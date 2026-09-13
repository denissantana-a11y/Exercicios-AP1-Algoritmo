"""
EXEMPLO SIMPLES DE ESTRUTURAS DE SELECAO EM PYTHON
Sistema de avaliação de carros para uma concessionária
COM ENTRADA DE DADOS PELO USUARIO
"""

# ============================================
# 1. ESTRUTURA ANINHADA (if dentro de if)
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

    # Primeira verificação: revisão em dia
    if revisado.lower() == "s":
        print("Revisão OK")

        # Segunda verificação: só acontece se a primeira for verdadeira
        if km <= 100000:
            print("RESULTADO: LIBERADO - Revisão e km dentro do esperado")
        else:
            print(f"RESULTADO: NAO LIBERADO - Revisão OK, mas km {km} muito alta")
    else:
        print("RESULTADO: NAO LIBERADO - Revisão pendente")

# ============================================
# 2. ESTRUTURA ENCADEADA COM ELIF
# ============================================

def classificar_estado_carro():
    """
    Classifica o estado do carro usando elif,
    de acordo com a quilometragem.
    """
    print("\n=== CLASSIFICACAO DO CARRO ===")

    km = float(input("Digite a quilometragem para classificar: "))

    print(f"Km: {km}")

    # Ordem: do mais específico (menor km) para o mais geral
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
# 3. ESTRUTURA MATCH CASE
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

    match opcao:
        # Padrão simples
        case "1":
            print("OPCAO 1: Agendar revisão")

        case "2":
            print("OPCAO 2: Trocar óleo")

        case "3":
            print("OPCAO 3: Alinhamento e balanceamento")

        # Padrão com múltiplos valores aceitos
        case "4" | "sair":
            print("OPCAO 4: Sair do sistema")

        # Wildcard para qualquer valor não tratado
        case _:
            print(f"OPCAO INVALIDA: {opcao}")

# ============================================
# 4. MATCH CASE COM GUARDA
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

    dados = (ano, km)

    match dados:
        # Guarda: condição adicional para combinar
        case (a, _) if a >= 2023:
            print(f"{modelo}: SEMINOVO DESTAQUE - Ano {a}")

        case (a, k) if a >= 2018 and k <= 80000:
            print(f"{modelo}: BOM NEGOCIO - Ano {a}, Km {k}")

        case (a, k) if a >= 2013 and k <= 120000:
            print(f"{modelo}: NEGOCIO REGULAR - Ano {a}, Km {k}")

        case (a, k) if a < 2013 or k > 120000:
            print(f"{modelo}: NECESSITA AVALIACAO EXTRA - Ano {a}, Km {k}")

        # Caso geral
        case _:
            print(f"{modelo}: SITUACAO INDEFINIDA")

# ============================================
# 5. FUNCAO PRINCIPAL COM MENU INTERATIVO
# ============================================

def main():
    """
    Função principal com menu interativo.
    """
    print("=" * 50)
    print("SISTEMA DA CONCESSIONARIA")
    print("Demonstracao de estruturas de selecao")
    print("=" * 50)

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
            break
        else:
            print("\nOPCAO INVALIDA! Tente novamente.")

        input("\nPressione Enter para continuar...")

# ============================================
# PONTO DE ENTRADA
# ============================================

if __name__ == "__main__":
    main()