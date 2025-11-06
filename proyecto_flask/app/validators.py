import re

def highlight_emails(text):
    """
    Regex 1: Correos Electrónicos
    Busca patrones de email y los envuelve en un <span>.
    """

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    replacement = r'<span class="highlight-email">\g<0></span>'
    
    
    highlighted_text = re.sub(email_regex, replacement, text, flags=re.IGNORECASE)
    return highlighted_text

def highlight_phones(text):
    """
    Regex 2: Números de Teléfono (Formato de 10 dígitos, simple)
    Busca patrones de teléfono (ej. 123-456-7890, (123) 456 7890, etc.)
    """

    phone_regex = r'\b\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\b'
    replacement = r'<span class="highlight-phone">\g<0></span>'
    
    highlighted_text = re.sub(phone_regex, replacement, text)
    return highlighted_text

def highlight_urls(text):
    """
    Regex 3: URLs (http y https)
    Busca enlaces web que comiencen con http:// o https://
    """
    
    url_regex = r'https?://[A-Za-z0-9.-]+(?:\:[0-9]+)?(?:/[^"\s]*)?'
    replacement = r'<span class="highlight-url">\g<0></span>'
    
    highlighted_text = re.sub(url_regex, replacement, text, flags=re.IGNORECASE)
    return highlighted_text