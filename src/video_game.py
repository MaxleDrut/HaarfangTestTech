from tinydb.table import Document
from pydantic import BaseModel


class VideoGame(BaseModel):
    name: str
    # TODO: implement it as a date.
    release_date: str
    studio: str
    ratings: int
    # We could create an enum for the platforms, but as there is no exhaustive list of platforms provided, I am sticking to a string type.
    platforms: list[str]

    def __init__(self, name: str, release_date: str, studio: str, ratings: int, platforms: list[str]) -> None:
        super().__init__()
        self.name = name
        self.release_date = release_date
        self.studio = studio
        self.ratings = ratings
        self.platforms = platforms

    @classmethod
    def fromDocument(self, video_game_document: Document):
        self.name = video_game_document.get("name")
        self.release_date = video_game_document.get("release_date")
        self.studio = video_game_document.get("studio")
        self.ratings = video_game_document.get("ratings")
        self.platforms = video_game_document.get("platforms")

    def serialize(self) -> dict:
        return {
            "name": self.name,
            "release_date": self.release_date,
            "studio": self.studio,
            "ratings": self.ratings,
            "platforms": self.platforms
        }
