from tinydb import TinyDB, Query
from tinydb.table import Document

from src.video_game import VideoGame


DATABASE_PATH = "data/video_games.json"


class VideoGamesDB:
    _video_games_database: TinyDB

    def __init__(self) -> None:
        self._video_games_database = TinyDB(DATABASE_PATH)

    def create_video_game(self, video_game: VideoGame) -> None:
        self._video_games_database.insert(video_game.serialize())

    def fetch_video_game(self, video_game_name: str) -> VideoGame | None:
        video_game_documents = self._video_games_database.search(
            Query()["name"] == video_game_name)
        if len(video_game_documents) > 1:
            raise Exception(
                "Unexpectedly found multiple video games with the same name!")
        if len(video_game_documents) == 0:
            # Not found.
            return None

        [video_game_document] = video_game_documents
        return VideoGame.fromDocument(video_game_document)

    def delete_video_game(self, video_game_name: str) -> None:
        self._video_games_database.remove(Query()["name"] == video_game_name)

    def handle_post_video_game(self, video_game: VideoGame) -> None:
        if self.fetch_video_game(video_game.name):
            # If the video game already exists, we replace the old one by the new one.
            self.delete_video_game(video_game.name)
        self.create_video_game(video_game)

    def list_video_games(self) -> list[VideoGame]:
        video_games_documents = self._video_games_database.all()
        video_games_list = []
        for document in video_games_documents:
            video_games_list.append(VideoGame.fromDocument(document))

        return video_games_list

    def reset(self) -> None:
        """Wipe clean the database of previous data. To be used in the context of tests."""
        self._video_games_database.truncate()


# The Database class is here meant to be used as a singleton.
video_games_db = VideoGamesDB()
