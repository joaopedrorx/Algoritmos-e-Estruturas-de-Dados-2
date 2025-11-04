// --- Gerenciador de Produtos (Node.js) ---
// Para executar este script:
// 1. Salve como 'produtos_nodejs.js'
// 2. No terminal, instale a dependência para ler input: npm install prompt-sync
// 3. Execute: node produtos_nodejs.js
// -----------------------------------------------------------------

const fs = require('fs');
const path = require('path');
// Usamos 'prompt-sync' para facilitar a leitura síncrona do console
const prompt = require('prompt-sync')({ sigint: true });

const ARQUIVO_DADOS = path.join(__dirname, 'produtos.json');
const LIMITE_PRODUTOS = 50;

function carregarProdutos() {
    if (!fs.existsSync(ARQUIVO_DADOS)) {
        return [];
    }
    try {
        const data = fs.readFileSync(ARQUIVO_DADOS, 'utf8');
        return JSON.parse(data);
    } catch (e) {
        console.error("Erro ao ler o arquivo de dados. Começando com lista vazia.", e);
        return [];
    }
}

function salvarProdutos(produtos) {
    try {
        const data = JSON.stringify(produtos, null, 2);
        fs.writeFileSync(ARQUIVO_DADOS, data, 'utf8');
    } catch (e) {
        console.error("Erro ao salvar os dados no arquivo.", e);
    }
}

function incluirProduto(produtos) {
    if (produtos.length >= LIMITE_PRODUTOS) {
        console.log(`\nErro: Limite de ${LIMITE_PRODUTOS} produtos atingido. Não é possível adicionar mais.`);
        return;
    }

    console.log("\n--- Inclusão de Novo Produto ---");
    try {
        const nome = prompt("Nome do produto: ");
        if (!nome) {
            console.log("Erro: O nome não pode ser vazio.");
            return;
        }

        const precoStr = prompt("Preço unitário (R$): ");
        const preco = parseFloat(precoStr);
        if (isNaN(preco) || preco < 0) {
            console.log("Erro: Preço inválido ou negativo.");
            return;
        }

        const qtdStr = prompt("Quantidade em estoque: ");
        const quantidade = parseInt(qtdStr, 10);
        if (isNaN(quantidade) || quantidade < 0) {
            console.log("Erro: Quantidade inválida ou negativa.");
            return;
        }

        const novoProduto = { nome, preco, quantidade };
        produtos.push(novoProduto);
        salvarProdutos(produtos);
        console.log(`Produto '${nome}' adicionado com sucesso!`);

    } catch (e) {
        console.log("\nOcorreu um erro durante a entrada de dados.", e);
    }
}

function listarProdutos(produtos) {
    console.log("\n--- Relação de Produtos Cadastrados ---");
    if (produtos.length === 0) {
        console.log("Nenhum produto cadastrado.");
        return;
    }

    console.log(`Total de produtos: ${produtos.length} / ${LIMITE_PRODUTOS}`);
    console.log("----------------------------------------");
    produtos.forEach((p, i) => {
        console.log(`Produto ${i + 1}:`);
        console.log(`  Nome:       ${p.nome}`);
        console.log(`  Preço:      R$ ${p.preco.toFixed(2)}`);
        console.log(`  Quantidade: ${p.quantidade} un.`);
        console.log("----------------------------------------");
    });
}

function removerProduto(produtos) {
    console.log("\n--- Remoção de Produto ---");
    if (produtos.length === 0) {
        console.log("Nenhum produto cadastrado para remover.");
        return;
    }

    const nomeRemover = prompt("Digite o nome exato do produto a ser removido: ");

    const indiceEncontrado = produtos.findIndex(p => p.nome.toLowerCase() === nomeRemover.toLowerCase());

    if (indiceEncontrado !== -1) {
        const produto = produtos[indiceEncontrado];
        
        // Confirmação
        console.log(`Produto encontrado: ${produto.nome} (Preço: R$ ${produto.preco.toFixed(2)})`);
        const confirmar = prompt("Tem certeza que deseja remover este produto? (s/n): ").toLowerCase();

        if (confirmar === 's') {
            produtos.splice(indiceEncontrado, 1); // Remove 1 item no índice encontrado
            salvarProdutos(produtos);
            console.log(`Produto '${nomeRemover}' removido com sucesso.`);
        } else {
            console.log("Remoção cancelada.");
        }
    } else {
        console.log(`Erro: Produto com o nome '${nomeRemover}' não encontrado.`);
    }
}

function main() {
    let produtos = carregarProdutos();

    while (true) {
        console.log("\n--- GERENCIADOR DE ESTOQUE (LIMITE: 50) ---");
        console.log("1 - Incluir novo produto");
        console.log("2 - Listar produtos cadastrados");
        console.log("3 - Remover produto");
        console.log("4 - Sair do programa");

        const opcao = prompt("Escolha uma opção (1-4): ");

        switch (opcao) {
            case '1':
                incluirProduto(produtos);
                break;
            case '2':
                listarProdutos(produtos);
                break;
            case '3':
                removerProduto(produtos);
                break;
            case '4':
                console.log("\nSalvando dados e saindo... Até logo!");
                return; // Encerra a função main e o script
            default:
                console.log("\nOpção inválida. Por favor, digite um número de 1 a 4.");
        }
    }
}

// Ponto de entrada do script
main();
