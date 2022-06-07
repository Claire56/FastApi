from fastapi  import FastAPI , Header, HTTPException
from pydantic import BaseModel

fake_secret_token = "nabagereka"
app = FastAPI()

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

class Item(BaseModel):
    id: str
    title: str
    description: Union[str, None] = None

@app.get("/")
async def root():
    return {"message": "My FastAPI world"}

@app.get("/home")
async def root():
    return {"This is a home"}

