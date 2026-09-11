titulo = "Cálculo da conta do restaurante"
descricao = "Um grupo pediu quatro pratos, cada um por: "
cont = " e pagou uma taxa de serviço de: "
pergunta = "Quanto a mesa pagou no total?"
resposta = "A mesa pagou: "
preco = 28.50
quantidade = 4
taxa_servico = 11.40

subtotal = preco * quantidade
valor_final = subtotal + taxa_servico

# .2f formata os valores com 2 casas decimais
print(f"""
{titulo}
{descricao}R$ {preco:.2f}{cont}R$ {taxa_servico:.2f}
{pergunta}
{resposta}R$ {valor_final:.2f}
""")