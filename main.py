from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from connectors.firestore_connector import get_mishna

app = FastAPI()

# Allow CORS for all origins to enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    description: str
    model: str
    isBlack: bool

# ~~~~~~~~~~~~~~~ Routs ~~~~~~~~~~~~~~~
@app.post("/items/")
async def create_item(item: Item):
    color_item = "Black" if item.isBlack else "White"
    return f"Hello {item.name}, We received your order for {color_item} {item.model} with {item.description}."


