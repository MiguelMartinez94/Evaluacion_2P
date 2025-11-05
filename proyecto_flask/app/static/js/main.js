document.addEventListener('DOMContentLoaded', () => {
    const validateBtn = document.getElementById('validate-btn');
    const textInput = document.getElementById('text-input');
    const resultOutput = document.getElementById('result-output');

    validateBtn.addEventListener('click', async () => {
        const text = textInput.value;
        
        try {
            // Hacemos la petición al backend (que crearemos en el commit 2)
            const response = await fetch('/validate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text }),
            });

            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor');
            }

            const data = await response.json();
            
            // Insertamos el HTML resaltado que nos devuelve el servidor
            resultOutput.innerHTML = data.highlighted_text;

        } catch (error) {
            console.error('Error al validar:', error);
            resultOutput.textContent = 'Error al procesar la solicitud.';
        }
    });
});