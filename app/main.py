from fastapi import FastAPI

from app.routes import auth_routes, link_routes, to_routes


app = FastAPI()


app.include_router(auth_routes.router)
app.include_router(link_routes.router)
app.include_router(to_routes.router)
