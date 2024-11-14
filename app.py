from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Definir las preguntas y respuestas predefinidas
qa_data = {
    "1": {"question": "Catálogos de productos", "answer": "¡Estoy bien, gracias! ¿Y tú?"},
    "2": {"question": "Compras", "answer": "Soy un chatbot creado con Flask."},
    "3": {"question": "Asesoría comercial", "answer": "Lo siento, no tengo acceso al reloj en este momento."}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    user_choice = request.json.get('choice')
    response = qa_data.get(user_choice, {"answer": "Lo siento, no entendí esa pregunta."})
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
