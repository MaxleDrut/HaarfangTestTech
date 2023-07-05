import unittest
from fastapi import status
from fastapi.testclient import TestClient

from src.main import app
from src.video_games_db import video_games_db


class TestsAPI(unittest.TestCase):
    client: TestClient

    @classmethod
    def tearDownClass(cls) -> None:
        video_games_db.reset()

    # Reset the state of the storage before each integration test.
    def setUp(self):
        self.client = TestClient(app)
        video_games_db.reset()

    def test_ping(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_video_game(self):
        self.client.post("/video_game", json={
            "name": "The Witcher 3 : Wild Hunt",
            "release_date": "2015-05-19",
            "studio": "CD Projekt RED",
            "ratings": 19,
            "platforms": [
                "PC",
                "PS4",
                "PS5",
                "Switch",
                "One"
            ]
        })

        self.assertEqual(len(video_games_db.list_video_games()), 1)
