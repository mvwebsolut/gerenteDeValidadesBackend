// script.js
document.addEventListener("DOMContentLoaded", function () {
    const productList = document.getElementById("product-list");
    const addCategoryBox = document.getElementById('add-category-box');

    function addCategory(categoryName) {
        // Define o payload da requisição
        const payload = {
            name: categoryName
        };

        // Configurações da requisição
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        };

        // Envia a requisição para a rota localhost/categorys/add
        fetch('/categorys/add', options)
            .then(response => {
                if (!response.ok) {
                    // Se a resposta não for bem-sucedida, lança um erro
                    Toastify({
                      text: "Erro ao adicionar a categoria.",
                      duration: 3000,
                      close: false,
                      gravity: "top", // `top` or `bottom`
                      position: "right", // `left`, `center` or `right`
                      stopOnFocus: false, // Prevents dismissing of toast on hover
                      style: {
                        background: "linear-gradient(to right, #FF5F6D, #FFC371)",
                        borderRadius: "10px",
                      }
                    }).showToast();
                    throw new Error('Erro ao adicionar categoria');
                }
                // Se a resposta for bem-sucedida, retorna o corpo da resposta
                return response.json();
            })
            .then(data => {
                Toastify({
                  text: "Categoria adicionada com sucesso",
                  duration: 3000,
                  close: false,
                  gravity: "top", // `top` or `bottom`
                  position: "right", // `left`, `center` or `right`
                  stopOnFocus: false, // Prevents dismissing of toast on hover
                  style: {
                    background: "linear-gradient(to right, #00b09b, #96c93d)",
                    borderRadius: "10px",
                  }
                }).showToast();
                setTimeout(()=>{
                    window.location.reload();
                }, 2000);
                return data;

            })
            .catch(error => {
                Toastify({
                  text: "Erro ao adicionar a categoria.",
                  duration: 3000,
                  close: false,
                  gravity: "top", // `top` or `bottom`
                  position: "right", // `left`, `center` or `right`
                  stopOnFocus: false, // Prevents dismissing of toast on hover
                  style: {
                    background: "linear-gradient(to right, #FF5F6D, #FFC371)",
                    borderRadius: "10px",
                  }
                }).showToast();
                throw error;
            });
    }

    // Função para abrir o modal para adicionar categoria
    function openModal() {
        const categoryName = prompt('Digite o nome da categoria:');
        if (categoryName) {
            console.log(categoryName);
            addCategory(categoryName);
        }
    }

    // Evento de clique para abrir o modal ao clicar no box de adicionar categoria
    addCategoryBox.addEventListener('click', openModal);
});

