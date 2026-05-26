import docker
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Conecta ao Docker Engine através do socket mapeado no volume
client = docker.from_env()

@app.route('/')
def index():
    # Lista os nós para mostrar o status do cluster (Manager/Workers)
    nodes = client.nodes.list()
    # Lista os serviços ativos para mostrar os jogos rodando
    services = client.services.list()
    return render_template('index.html', nodes=nodes, services=services)

@app.route('/deploy_flappy')
def deploy_flappy():
    try:
        client.services.create(
            image="meuhub/jogo_flappybird:latest",
            name="flappy-bird-service",
            networks=["rede_swarm_hub"],
            endpoint_spec=docker.types.EndpointSpec(ports={8085: 80}),
            mode=docker.types.ServiceMode("replicated", replicas=2) # 2 réplicas para Alta Disponibilidade [cite: 67]
        )
    except Exception as e:
        # Se o serviço já existir, ele apenas ignora o erro e redireciona
        print(f"Aviso: O serviço já pode estar ativo. Erro: {e}")
    
    return redirect('/')

if __name__ == '__main__':
    # Roda na porta 5000 interna, que será mapeada para a 80 ou 8081 externa
    app.run(host='0.0.0.0', port=5000)