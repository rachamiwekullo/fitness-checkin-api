import unittest

from fastapi.testclient import TestClient

from main import app, checkins


class FitnessCheckInApiTests(unittest.TestCase):
    def setUp(self):
        checkins.clear()
        self.client = TestClient(app)

    def test_create_and_list_checkin(self):
        response = self.client.post("/api/checkins", json={
            "name": "Sample Member",
            "sleep": 8,
            "water": 8,
            "steps": 10_500,
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()["stored"]["hit_goal"])
        self.assertEqual(len(self.client.get("/api/checkins").json()), 1)

    def test_out_of_range_values_are_rejected(self):
        response = self.client.post("/api/checkins", json={
            "name": "Sample Member",
            "sleep": 30,
            "water": 8,
            "steps": 10_500,
        })
        self.assertEqual(response.status_code, 422)
        self.assertEqual(checkins, [])

    def test_home_serves_the_form(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Fitness Check-in", response.text)


if __name__ == "__main__":
    unittest.main()
