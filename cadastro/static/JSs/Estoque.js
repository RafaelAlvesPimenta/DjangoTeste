// Exemplo de como carregar produtos no estoque com quantidades
const produtos = [
    {
        nome: 'Tecido Algodão',
        categoria: 'Tecido',
        quantidade: 50,
        total: 100,
        imagem: './imagens/tecido imagem.jpg'
    },
    {
        nome: 'Linha de Costura',
        categoria: 'Linha',
        quantidade: 30,
        total: 50,
        imagem: './imagens/linha de costura.jpg'
    },
    {
        nome: 'Botões de Metal',
        categoria: 'Botões',
        quantidade: 10,
        total: 20,
        imagem: './imagens/botão metalico.jpg'
    }
];

// Função para criar os cards dinamicamente
function carregarProdutos() {
    const container = document.getElementById('cards-container');
    produtos.forEach(produto => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.innerHTML = `
            <img src="${produto.imagem}" alt="${produto.nome}">
            <h1>${produto.nome}</h1>
            <h2>Quantidade</h2>
            <span>${produto.quantidade} / ${produto.total}</span>
            <div class="grafico">
                <div class="grafico-barra" style="width: ${(produto.quantidade / produto.total) * 100}%"></div>
            </div>
        `;
        container.appendChild(card);
    });
}

// Carregar produtos ao iniciar
document.addEventListener('DOMContentLoaded', carregarProdutos);
