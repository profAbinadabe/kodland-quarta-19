from flask import Flask
import random

app = Flask(__name__)

fatos = [
    "A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos.",
    "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.",
    "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna.",
    "Segundo um estudo de 2019, mais de 60% das pessoas respondem a mensagens de trabalho em seus smartphones dentro de 15 minutos após sair do trabalho.",
    "Uma forma de combater a dependência tecnológica é buscar atividades que tragam prazer e melhorem o humor.",
    "As redes sociais têm pontos positivos e negativos, e devemos estar atentos a ambos ao utilizar essas plataformas.",
    "As plataformas digitais são frequentemente projetadas para prender a atenção do usuário pelo maior tempo possível.",
    "Criar momentos sem tela durante o dia pode ajudar a reduzir o uso excessivo da tecnologia."
]

@app.route("/")
def hello_world():
    return f"""
    <html>
        <head>
            <title>Fatos que não podem ser ignorados.</title>
        </head>
        <body>
        <h1>Fato Aleatório</h1>
        <p>{random.choice(fatos)}</p>
        <p>Aperte F5 para ter um novo fato aleatório.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)