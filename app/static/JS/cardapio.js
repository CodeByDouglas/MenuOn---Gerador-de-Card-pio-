document.addEventListener("DOMContentLoaded", () => {
  const userId = localStorage.getItem("user_id");
  if (!userId) {
    window.location.href = "/login";
    return;
  }

  // Function to create an item card displaying name, image, description, and value
  function createCard(item) {
    let imgSrc = "";
    if (item.imagem) {
      imgSrc = "data:image/jpeg;base64," + item.imagem;
    }
    const card = document.createElement("div");
    card.className = "item-card";
    card.innerHTML = `
        <h3 class="item-name">${item.nome}</h3>
        ${
          imgSrc
            ? `<img class="item-image" src="${imgSrc}" alt="${item.nome}">`
            : ""
        }
        <p class="item-description">${item.descricao || ""}</p>
        <p class="item-valor">Valor: R$ ${
          item.valor ? parseFloat(item.valor).toFixed(2) : "0.00"
        }</p>
      `;
    return card;
  }

  // Renders items for a given category (pratos, bebidas, sobremesas)
  function renderItems(category, items) {
    const container = document.getElementById(category);
    container.innerHTML = "";
    if (items.length === 0) {
      container.innerHTML = `<p>Nenhum item encontrado em ${category}.</p>`;
      return;
    }
    items.forEach((item) => container.appendChild(createCard(item)));
  }

  // Fetch the cardápio data from backend
  fetch(`/consultar-itens-cardapio?restaurante_id=${userId}`)
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        document.getElementById("error-message").textContent = data.error;
        return;
      }
      renderItems("pratos", data.pratos || []);
      renderItems("bebidas", data.bebidas || []);
      renderItems("sobremesas", data.sobremesas || []);
    })
    .catch((error) => {
      document.getElementById("error-message").textContent =
        "Erro ao carregar cardápio.";
      console.error("Erro:", error);
    });

  // Tab switching functionality
  const tabButtons = document.querySelectorAll(".tab-button");
  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      tabButtons.forEach((btn) => btn.classList.remove("active"));
      document
        .querySelectorAll(".content-section")
        .forEach((sec) => (sec.style.display = "none"));

      button.classList.add("active");
      const tab = button.getAttribute("data-tab");
      document.getElementById(tab).style.display = "block";
    });
  });
});
