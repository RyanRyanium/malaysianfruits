from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Local Fruit Atlas")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

FRUITS = [
    {
        "name": "Mango",
        "emoji": "🥭",
        "number": "01",
        "tag": "Sun-ripened",
        "description": "Silky, fragrant, and full of sunshine. A ripe mango is lovely eaten fresh or blended into a cool afternoon drink.",
        "flavor": "Honey · peach · citrus",
        "color": "mango",
    },
    {
        "name": "Pineapple",
        "emoji": "🍍",
        "number": "02",
        "tag": "Bright & juicy",
        "description": "Sweet with a lively tang, pineapple brings a little sparkle to fruit plates, grilled dishes, and chilled juice.",
        "flavor": "Tropical · tart · floral",
        "color": "pineapple",
    },
    {
        "name": "Watermelon",
        "emoji": "🍉",
        "number": "03",
        "tag": "Cool season",
        "description": "Crisp, refreshing flesh makes watermelon a natural share-around fruit on hot days. Keep it cold and serve in generous wedges.",
        "flavor": "Fresh · mellow · crisp",
        "color": "watermelon",
    },
    {
        "name": "Banana",
        "emoji": "🍌",
        "number": "04",
        "tag": "Everyday favorite",
        "description": "Soft, naturally sweet, and easy to take along. Bananas are just as good in a quick snack as they are folded into warm pancakes.",
        "flavor": "Creamy · mellow · sweet",
        "color": "banana",
    },
    {
        "name": "Coconut",
        "emoji": "🥥",
        "number": "05",
        "tag": "From the grove",
        "description": "Enjoy the cool, clear water first, then scoop out the tender flesh. Coconut adds a gentle richness to both drinks and cooking.",
        "flavor": "Clean · nutty · delicate",
        "color": "coconut",
    },
]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"fruits": FRUITS},
    )
