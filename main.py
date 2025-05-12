from pyscript import display, when, html

@when("click", "#meu-botao")
def clique_botao(event):
    display("Você clicou no botão! 🎉", target="mensagem")
