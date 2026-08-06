from django.test import TestCase, Client


class TestUsers(TestCase):

    def setUp(self):
        self.client = Client()

    def test_magic_password_login(self):
        response = self.client.get("/", {
            "password": "CSE270Rocks!"
        })
        self.assertEqual(response.status_code, 200)

    def test_admin_login(self):
        response = self.client.get("/", {
            "username": "admin",
            "password": "qwerty"
        })
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        response = self.client.get("/", {
            "password": "incorrect"
        })
        self.assertEqual(response.status_code, 401)

    def test_ingest_endpoint(self):
        response = self.client.get("/ingest")
        self.assertEqual(response.status_code, 200) 
