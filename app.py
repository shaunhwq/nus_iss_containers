import os
import random

import fastapi
import fastapi.staticfiles
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates


app = fastapi.FastAPI()
app.mount("/images", fastapi.staticfiles.StaticFiles(directory="images"), name="images")
templates = Jinja2Templates(directory="templates")


sample_text = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "dynamic_text": random.choice(sample_text),
    })


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)