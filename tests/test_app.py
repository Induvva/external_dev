import unittest

from app import app


class RegistrationAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page_links_to_registration(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"/register", response.data)

    def test_registration_page_renders(self):
        response = self.client.get("/register")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'name="email"', response.data)
        self.assertIn(b'name="roll_no"', response.data)

    def test_registration_shows_submitted_details(self):
        response = self.client.post(
            "/register",
            data={
                "username": "Indu",
                "email": "indu@example.com",
                "roll_no": "123",
            },
            follow_redirects=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Registration Successful - Indu", response.data)
        self.assertIn(b"indu@example.com", response.data)
        self.assertIn(b"123", response.data)


if __name__ == "__main__":
    unittest.main()
