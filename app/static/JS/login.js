document
  .getElementById("login-form")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const senha = document.getElementById("password").value;
    const errorDiv = document.getElementById("error-message");
    errorDiv.textContent = ""; // limpa mensagem anterior

    try {
      const res = await fetch("/autencar-user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, senha }),
      });

      const data = await res.json();

      if (res.ok) {
        // 1) salva o ID do usuário no localStorage
        //    supondo que o backend retorne { user_id: "42" }
        localStorage.setItem("user_id", data.user_id);

        // 2) redireciona para a área interna
        window.location.href = "/login/registrar-cardapio";
      } else {
        // erro de autenticação: mostra a mensagem vinda do backend
        errorDiv.textContent = data.error || "Dados de login inválidos.";
      }
    } catch (err) {
      console.error(err);
      errorDiv.textContent = "Não foi possível conectar ao servidor.";
    }
  });
