const form = document.getElementById("cadastro-form");
const errorDiv = document.getElementById("error-message");

form.addEventListener("submit", async function (e) {
  e.preventDefault();
  errorDiv.textContent = "";

  const nome = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const senha = document.getElementById("password").value;
  const confirmSenha = document.getElementById("confirm-password").value;

  // 1) valida senhas
  if (senha !== confirmSenha) {
    errorDiv.textContent = "As senhas não conferem.";
    return;
  }

  // 2) faz POST para /cadastrar-user
  try {
    const res = await fetch("/cadastrar-user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ nome, email, senha }),
    });
    const data = await res.json();

    if (res.ok) {
      // opcional: guardar user_id se vier no response
      if (data.user_id) {
        localStorage.setItem("user_id", data.user_id);
      }
      // redireciona para registro de cardápio
      window.location.href = "login/registrar-cardapio";
    } else {
      errorDiv.textContent = data.error || "Erro ao cadastrar usuário.";
    }
  } catch (err) {
    console.error(err);
    errorDiv.textContent = "Não foi possível conectar ao servidor.";
  }
});
