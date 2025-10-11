from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user, reviews
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    yield
    # shutdown 


app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

# Include routers
app.include_router(user.router)
app.include_router(reviews.router)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")