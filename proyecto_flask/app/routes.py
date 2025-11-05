from app import app
from flask import render_template, request, jsonify
from . import validators 

@app.route('/')
def index():
    """
    Renderiza la página principal.
    """
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate_text():
    """
    Endpoint para recibir texto y devolverlo resaltado.
    """
    data = request.get_json()
    text = data.get('text', '')

    
    highlighted_text = validators.highlight_emails(text)

    return jsonify({
        'highlighted_text': highlighted_text
    })