import docker
import time
from flask import Flask, render_template, redirect

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def index():
    nodes = client.nodes.list()
    services = client.services.list()
    return render_template('index.html', nodes=nodes, services=services)

@app.route('/deploy_flappy')
def deploy_flappy():
    try:
        # 1. Tenta remover o serviço antigo se ele existir
        try:
            servico = client.services.get("flappy-bird-service")
            servico.remove()
            time.sleep(2) 
        except:
            pass
            
        # 2. Criação do serviço com a sintaxe correta para portas
        # O dicionário {8085: 80} mapeia Porta_do_Windows:Porta_do_Container
        client.services.create(
            image="meuhub/jogo_flappybird:latest",
            name="flappy-bird-service",
            networks=["rede_swarm_hub"],
            endpoint_spec=docker.types.EndpointSpec(ports={8085: 80}),
            mode=docker.types.ServiceMode("replicated", replicas=2),
            constraints=["node.role == manager"]
        )
        return redirect('/')
        
    except Exception as e:
        return f"<h1>Erro crítico ao provisionar:</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)