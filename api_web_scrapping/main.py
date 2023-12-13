from web_scraping_api import app, get_metadata
from unittest import main, TestCase

class TestWebScrapingAPI(TestCase):
    def test_get_metadata(self):
        # Prueba de la función get_metadata
        url = 'https://holajuniors.com'
        metadata = get_metadata(url)
        expected_output = {
            'title': 'HolaJuniors! Empleo Para Programadores Junior',
            'description': 'Ayudamos a programadores a encontrar su primer empleo como programador junior',
            'url': 'https://holajuniors.com'
        }
        self.assertEqual(metadata, expected_output)
        print(f"title: {metadata['title']}, description: {metadata['description']}, url: {metadata['url']}")

if __name__ == '__main__':
    # Ejecutar pruebas unitarias automáticamente
    main(module='main', exit=False)

