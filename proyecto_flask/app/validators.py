import re

def highlight_emails(text):
    """
    Regex 1: Correos Electrónicos
    Busca patrones de email y los envuelve en un <span>.
    """
    
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    
    replacement = r'<span class="highlight-email">\g<0></span>'
    
    highlighted_text = re.sub(email_regex, replacement, text)
    return highlighted_text