from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def get_metadata(url):
    try:
        # Realizar la solicitud GET a la URL
        response = requests.get(url)
        response.raise_for_status()

        # Utilizar BeautifulSoup para analizar el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Obtener el título de la página
        title = soup.title.string if soup.title else "No title found"

        # Obtener la descripción de la página (meta description)
        meta_description = soup.find('meta', attrs={'name': 'description'})
        description = meta_description.get('content') if meta_description else "No description found"

        return {'title': title, 'description': description, 'url': url}

    except requests.exceptions.RequestException as e:
        return {'error': f'Error al obtener la página: {str(e)}'}

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'Por favor, proporciona una URL'}), 400

    metadata = get_metadata(url)
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(debug=True)
