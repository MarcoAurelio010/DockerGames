from flask import Flask, render_template, redirect

app = Flask(__name__)

JOGOS_DISPONIVEIS = {
    "flappybird": {
        "nome": "Flappy Bird",
        "descricao": "Desvie dos obstáculos e faça a maior pontuação!",
        "porta": 8085,
        "cor_fundo": "bg-emerald-600",
        "icone": "🐦",
        "tipo": "web"
    },
    "2048": {
        "nome": "2048",
        "descricao": "Junte os números e chegue ao bloco 2048!",
        "porta": 8086,
        "cor_fundo": "bg-yellow-600",
        "icone": "🔢",
        "tipo": "web"
    }
}

@app.route('/')
def index():
    return render_template('index.html', jogos=JOGOS_DISPONIVEIS)

@app.route('/jogar/<id_jogo>')
def jogar(id_jogo):
    jogo = JOGOS_DISPONIVEIS.get(id_jogo)
    if jogo and jogo["tipo"] == "web":
        return redirect(f"http://localhost:{jogo['porta']}")
    return "Jogo não encontrado na plataforma!", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)