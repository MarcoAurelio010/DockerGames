from flask import Flask, render_template, redirect

app = Flask(__name__)

# Princípio Aberto/Fechado (OCP): Fácil expansão para novos jogos sem alterar a lógica
JOGOS_DISPONIVEIS = {
    "flappybird": {
        "nome": "Flappy Bird",
        "descricao": "Desvie dos obstáculos e faça a maior pontuação!",
        "porta": 8085,
        "cor_fundo": "bg-emerald-600",
        "icone": "🐦"
    }
    # Exemplo para o futuro:
    # "pacman": {"nome": "Pac-Man", "descricao": "Fuja dos fantasmas!", "porta": 8086, "cor_fundo": "bg-yellow-500", "icone": "👾"}
}

@app.route('/')
def index():
    return render_template('index.html', jogos=JOGOS_DISPONIVEIS)

@app.route('/jogar/<id_jogo>')
def jogar(id_jogo):
    jogo = JOGOS_DISPONIVEIS.get(id_jogo)
    if jogo:
        # Redireciona diretamente para a porta do cluster onde o jogo já está a rodar
        return redirect(f"http://localhost:{jogo['porta']}")
    return "Jogo não encontrado na plataforma!", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)