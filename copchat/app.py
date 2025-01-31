from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

respostas = {
    "o que é a cop 30?": "A COP 30 é a Conferência das Nações Unidas sobre Mudanças Climáticas que ocorrerá em 2025, em Belém, Brasil.",
    "onde será a cop 30?": "A COP 30 acontecerá em Belém, no estado do Pará, Brasil.",
    "qual o objetivo da cop 30?": "A COP 30 tem como objetivo discutir ações para combater as mudanças climáticas e reduzir as emissões de carbono.",
    "quais países participarão da cop 30?": "A COP 30 contará com a participação de mais de 190 países membros da ONU.",
    "qual a importância de belém para a cop 30?": "Belém é uma cidade estratégica para a COP 30 por estar localizada na Amazônia, a maior floresta tropical do mundo, que desempenha um papel crucial no combate às mudanças climáticas.",
    "quais são as iniciativas de belém contra as mudanças climáticas?": "Belém tem implementado políticas de sustentabilidade, como o reflorestamento urbano, a promoção de energias renováveis e a preservação de áreas verdes.",
    "como belém está se preparando para a cop 30?": "Belém está investindo em infraestrutura sustentável, como transporte público eficiente e hospedagens ecológicas, além de promover a conscientização ambiental entre seus cidadãos.",
    "quais são os desafios climáticos de belém?": "Belém enfrenta desafios como o desmatamento, a gestão de resíduos sólidos e a necessidade de adaptação às mudanças climáticas, especialmente em áreas vulneráveis a inundações.",
    "quais são os pontos turísticos sustentáveis em belém?": "Belém oferece pontos turísticos sustentáveis como o Mangal das Garças, o Parque Estadual do Utinga e o Mercado Ver-o-Peso, que promovem a cultura local e a conservação ambiental.",
    "qual a importância da amazônia para o clima global?": "A Amazônia é vital para o clima global, pois regula o ciclo de carbono, influencia os padrões de chuva e abriga uma biodiversidade única.",
    "quais são as principais ameaças à amazônia?": "As principais ameaças à Amazônia incluem o desmatamento, as queimadas, a mineração ilegal e a expansão agrícola desordenada.",
    "como a amazônia ajuda a combater as mudanças climáticas?": "A Amazônia absorve grandes quantidades de CO2 da atmosfera, ajudando a reduzir os efeitos das mudanças climáticas.",
    "quais são os impactos das mudanças climáticas no brasil?": "No Brasil, as mudanças climáticas causam secas prolongadas, inundações, perda de biodiversidade e impactos na agricultura.",
    "o que são energias renováveis?": "Energias renováveis são fontes de energia que se regeneram naturalmente, como solar, eólica, hidrelétrica e biomassa.",
    "como reduzir a emissão de carbono?": "Para reduzir a emissão de carbono, é necessário adotar energias renováveis, melhorar a eficiência energética, reflorestar e promover o transporte sustentável.",
    "quais são os países mais importantes na luta contra as mudanças climáticas?": "Os países mais importantes na luta contra as mudanças climáticas incluem Estados Unidos, China, União Europeia, Índia e Brasil, devido ao seu impacto global nas emissões de carbono.",
    "qual o papel do brasil na cop 30?": "O Brasil, como anfitrião da COP 30, tem o papel de liderar as discussões sobre a preservação da Amazônia e a promoção de políticas sustentáveis.",
}


sugestoes = [
    "O que é a COP 30?",
    "como reduzir a emissão de carbono?",
    "Qual o objetivo da COP 30?",
    "Quais países participarão da COP 30?",
    "Qual a importância de Belém para a COP 30?",
    "como belém está se preparando para a cop 30?",
    "quais são os países mais importantes na luta contra as mudanças climáticas?",
    "qual o papel do brasil na cop 30?"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=["POST"])
def chatbot():
    dados = request.json
    pergunta = dados.get("mensagem", "").lower()

    if pergunta == "sugestão":
        return jsonify({"resposta": "Aqui estão algumas sugestões de perguntas:", "sugestoes": sugestoes})
    elif pergunta == "suporte":
        return jsonify({"resposta": "Meu nome é Alysson Sales. O chatbot Marcos sobre a COP 30 está em desenvolvimento. Qualquer sugestão, entrar em contato: alyssonpatricks15@gmail.com."})
    else:
        resposta = respostas.get(pergunta, "Desculpe, não foi possível localizar as informações. Para mais informações, acesse o site oficial da ONU sobre mudanças climáticas: https://www.un.org/climatechange.")
        return jsonify({"resposta": resposta})

@app.route('/quem-somos')
def quem_somos():
    return render_template('quem_somos.html')

@app.route('/suporte')
def suporte():
    return render_template('suporte.html')

@app.route('/proposito')
def proposito():
    return render_template('proposito.html')

if __name__ == "__main__":
    app.run(debug=True)