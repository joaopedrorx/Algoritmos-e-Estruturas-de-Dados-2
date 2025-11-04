import json
import os

ARQUIVO_DADOS = "produtos.json"
LIMITE_PRODUTOS = 50

def carregar_produtos():
    """Carrega os produtos do arquivo JSON."""
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(produtos, f, indent=2, ensure_ascii=False)

def incluir_produto(produtos):
    """Adiciona um novo produto à lista, respeitando o limite."""
    if len(produtos) >= LIMITE_PRODUTOS:
        print(f"\nErro: Limite de {LIMITE_PRODUTOS} produtos atingido. Não é possível adicionar mais.")
        return

    print("\n--- Inclusão de Novo Produto ---")
    try:
        nome = input("Nome do produto: ")
        # Validação simples para evitar nomes vazios
        if not nome:
            print("Erro: O nome não pode ser vazio.")
            return

        preco = float(input("Preço unitário (R$): "))
        if preco < 0:
            print("Erro: O preço não pode ser negativo.")
            return

        quantidade = int(input("Quantidade em estoque: "))
        if quantidade < 0:
            print("Erro: A quantidade não pode ser negativa.")
            return

        novo_produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        produtos.append(novo_produto)
        salvar_produtos(produtos)
        print(f"Produto '{nome}' adicionado com sucesso!")

    except ValueError:
        print("\nErro: Entrada inválida. Preço deve ser um número (ex: 10.50) e quantidade um inteiro (ex: 100).")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

def listar_produtos(produtos):
    """Exibe todos os produtos cadastrados."""
    print("\n--- Relação de Produtos Cadastrados ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print(f"Total de produtos: {len(produtos)} / {LIMITE_PRODUTOS}")
    print("-" * 40)
    for i, p in enumerate(produtos, 1):
        print(f"Produto {i}:")
        print(f"  Nome:       {p['nome']}")
        print(f"  Preço:      R$ {p['preco']:.2f}")
        print(f"  Quantidade: {p['quantidade']} un.")
        print("-" * 40)

def remover_produto(produtos):
    """Remove um produto da lista pelo nome."""
    print("\n--- Remoção de Produto ---")
    if not produtos:
        print("Nenhum produto cadastrado para remover.")
        return

    nome_remover = input("Digite o nome exato do produto a ser removido: ")

    produto_encontrado = None
    indice_encontrado = -1

    for i, p in enumerate(produtos):
        if p['nome'].lower() == nome_remover.lower():
            produto_encontrado = p
            indice_encontrado = i
            break

    if produto_encontrado:
        # Confirmação
        print(f"Produto encontrado: {produto_encontrado['nome']} (Preço: R$ {produto_encontrado['preco']:.2f})")
        confirmar = input("Tem certeza que deseja remover este produto? (s/n): ").lower()

        if confirmar == 's':
            produtos.pop(indice_encontrado)
            salvar_produtos(produtos)
            print(f"Produto '{nome_remover}' removido com sucesso.")
        else:
            print("Remoção cancelada.")
    else:
        print(f"Erro: Produto com o nome '{nome_remover}' não encontrado.")

def main():
    """Função principal que exibe o menu e gerencia o loop."""
    produtos = carregar_produtos()

    while True:
        print("\n--- GERENCIADOR DE ESTOQUE (LIMITE: 50) ---")
        print("1 - Incluir novo produto")
        print("2 - Listar produtos cadastrados")
        print("3 - Remover produto")
        print("4 - Sair do programa")
        
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            incluir_produto(produtos)
        elif opcao == '2':
            listar_produtos(produtos)
        elif opcao == '3':
            remover_produto(produtos)
        elif opcao == '4':
            print("\nSalvando dados e saindo... Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, digite um número de 1 a 4.")

# Ponto de entrada do script
if __name__ == "__main__":
    main()
