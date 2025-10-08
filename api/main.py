from fastapi import FastAPI
from routers import user, users
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    
    yield
    # shutdown 

app = FastAPI(lifespan=lifespan)




# Include routers
app.include_router(user.router)
app.include_router(users.router)

