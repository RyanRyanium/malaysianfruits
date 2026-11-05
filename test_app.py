import unittest

from fastapi.testclient import TestClient

from main import app


class FruitAtlasTests(unittest.TestCase):
    def test_homepage_renders_five_fruits_and_local_stylesheet(self) -> None:
        client = TestClient(app)

        page = client.get("/")
        stylesheet = client.get("/static/styles.css")

        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.text.count('<article class="fruit-card'), 5)
        for fruit in ("Mango", "Pineapple", "Watermelon", "Banana", "Coconut"):
            self.assertIn(fruit, page.text)
        self.assertEqual(stylesheet.status_code, 200)
        self.assertIn(".fruit-grid", stylesheet.text)


if __name__ == "__main__":
    unittest.main()
