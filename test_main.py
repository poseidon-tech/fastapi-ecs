# test_main_unittest.py
import unittest
from fastapi.testclient import TestClient
from main import app  # assuming your FastAPI code is in main.py

class TestFastAPIApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Home Page for items")

    def test_search_product(self):
        response = self.client.get("/searchProduct/5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 5)

    def test_get_products_valid(self):
        response = self.client.get("/getProducts", params={"name": "Laptop"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "Laptop")

    def test_get_products_too_short(self):
        response = self.client.get("/getProducts", params={"name": ""})
        self.assertEqual(response.status_code, 422)  # validation error

    def test_get_products_too_long(self):
        response = self.client.get("/getProducts", params={"name": "a"*25})
        self.assertEqual(response.status_code, 422)  # validation error

    def test_add_product(self):
        item_data = {
            "id": 1,
            "name": "Laptop",
            "price": 999.99,
            "descr": "High-end laptop",
            "type": "Electronics"
        }
        response = self.client.post("/item", json=item_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), "ok")


if __name__ == "__main__":
    unittest.main()
