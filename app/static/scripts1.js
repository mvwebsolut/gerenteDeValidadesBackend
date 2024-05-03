document.addEventListener("DOMContentLoaded", function () {
    const params = new URLSearchParams(window.location.search);
    const category = params.get('category');

    const categoryTitle = document.getElementById('category-title');
    const productList = document.getElementById('product-list');

    // Define o título da categoria na página
    categoryTitle.textContent = category;

    // Função para buscar e exibir os produtos da categoria
    function displayProducts(category) {
        // Aqui você deve implementar a lógica para buscar os produtos da categoria
        // e adicionar cada produto à lista de produtos (productList)
        // Exemplo:
        const products = getProductsByCategory(category);
        products.forEach(product => {
            const listItem = document.createElement('li');
            listItem.textContent = product.name + " - Lote: " + product.lot + " - Validade: " + product.expiration_date;
            productList.appendChild(listItem);
        });
    }

    // Chamada da função para exibir os produtos da categoria
    displayProducts(category);

    // Aqui você pode adicionar mais lógica conforme necessário
});

// Função de exemplo para buscar produtos por categoria (substitua por sua própria lógica)
function getProductsByCategory(category) {
    // Simulação de busca de produtos por categoria
    // Aqui você pode implementar a lógica real para buscar os produtos da categoria
    const products = {
        'CategoriaA': [{ name: 'Produto 1', lot: '123', expiration_date: '2024-05-01' }, { name: 'Produto 2', lot: '456', expiration_date: '2024-05-15' }],
        'CategoriaB': [{ name: 'Produto 3', lot: '789', expiration_date: '2024-06-01' }, { name: 'Produto 4', lot: '012', expiration_date: '2024-06-15' }]
        // Adicione mais categorias conforme necessário
    };
    return products[category] || [];
}

