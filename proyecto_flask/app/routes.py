from app import app
from flask import render_template, request, jsonify, escape
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

    processed_text = escape(text)

    processed_text = validators.highlight_emails(processed_text)
    
    
    processed_text = validators.highlight_phones(processed_text)
    
    
    processed_text = validators.highlight_urls(processed_text)

    return jsonify({
        'highlighted_text': processed_text
    })