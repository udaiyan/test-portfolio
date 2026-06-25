from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(title="Testing Demo API")

# CORS middleware - DEMO ONLY: In production, replace "*" with specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For demo/testing - restrict to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory data store
items_db = {
    1: {"id": 1, "name": "Sample Item 1", "description": "This is a sample item"},
    2: {"id": 2, "name": "Sample Item 2", "description": "Another sample item"},
}
next_id = 3


# Pydantic models
class Item(BaseModel):
    name: str
    description: Optional[str] = None


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


# API endpoints
@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}


@app.get("/api/items")
async def get_items():
    """Get all items"""
    return {"items": list(items_db.values())}


@app.post("/api/items", response_model=ItemResponse)
async def create_item(item: Item):
    """Create a new item"""
    global next_id
    new_item = {
        "id": next_id,
        "name": item.name,
        "description": item.description,
    }
    items_db[next_id] = new_item
    next_id += 1
    return new_item


@app.get("/api/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """Get a specific item by ID"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]


@app.delete("/api/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item by ID"""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item}


# Mount static files (must be last)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
