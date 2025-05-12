from js import document

def mostrar_mensagem(event=None):
    mensagem = document.getElementById("mensagem")
    mensagem.innerText = "Você clicou no botão! 🎉"

# conecta a função ao botão
botao = document.getElementById("meu-botao")
botao.addEventListener("click", mostrar_mensagem)
