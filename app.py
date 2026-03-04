from flask import Flask, render_template, jsonify
import requests
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_advice')
def get_advice():
    try:
        resposta = requests.get("https://api.adviceslip.com/advice")
        data = resposta.json()
        ingles_texto = data['slip']['advice']
        
        portugues_texto = GoogleTranslator(source='en', target='pt').translate(ingles_texto)
        
        return jsonify({'advice': portugues_texto})
    except:
        return jsonify({'advice': 'Erro ao buscar sabedoria...'})

if __name__ == '__main__':
    app.run(debug=True)