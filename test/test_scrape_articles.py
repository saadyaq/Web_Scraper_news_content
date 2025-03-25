import unittest
from unittest.mock import patch, Mock
from src.scrape_news_articles import get_news_articles


class TestScrapeNewsArticles(unittest.TestCase):

    def setUp(self):
        self.mock_html = """
         <html>
            <head>
                <meta name="author" content="John Doe">
            </head>
            <body>
                <h1>This is the title</h1>
                <h2>This is the subtitle</h2>
                <time data-testid="timestamp__datePublished">2025-03-25</time>
                <div>This is the first paragraph of the article.</div>
                <div>This is the second paragraph of the article.</div>
            </body>
        </html>
        """

    @patch("src.scrape_news_articles.requests.get")
    def test_get_news_articles(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = self.mock_html
        mock_get.return_value = mock_response

        result = get_news_articles("https://www.example.com")
        self.assertIn("This is the title", result)
        self.assertIn("This is the subtitle", result)
        self.assertIn("2025-03-25", result)
        self.assertIn("John Doe", result)
        self.assertIn("This is the first paragraph of the article.", result)
        self.assertIn("This is the second paragraph of the article.", result)

    @patch("src.scrape_news_articles.requests.get")
    def test_get_news_articles_failed(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.text = ""
        mock_get.return_value = mock_response
        result = get_news_articles("https://www.example.com")
        self.assertEqual(result, "Failed to load page")

    @patch("src.scrape_news_articles.requests.get")
    def test_get_news_articles_no_author(self, mock_get):
        html_no_author = self.mock_html.replace(
            '<meta name="author" content="John Doe">', ""
        )
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = html_no_author
        mock_get.return_value = mock_response

        result = get_news_articles("https://www.example.com")
        self.assertIn("Author: None", result)


if __name__ == "__main__":
    unittest.main()
