from fastapi import FastAPI, status, Response

from src.video_games_db import video_games_db
from src.video_game import VideoGame

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def ping():
    return


@app.post("/video_game", status_code=status.HTTP_201_CREATED)
async def post_video_game(video_game: VideoGame):
    video_games_db.handle_post_video_game(video_game)


@app.get("/video_game/{name}", status_code=status.HTTP_200_OK)
async def get_video_game(name: str, Response: Response):
    video_game = video_games_db.fetch_video_game(name)
    if not video_game:
        Response.status_code = status.HTTP_404_NOT_FOUND
        return

    return video_game.serialize()


@app.delete("/video_game/{name}", status_code=status.HTTP_200_OK)
async def delete_video_game(name: str):
    video_games_db.delete_video_game(name)


@app.get("/video_games", status_code=status.HTTP_200_OK)
async def list_video_games():
    return [video_game.serialize() for video_game in video_games_db.list_video_games()]
