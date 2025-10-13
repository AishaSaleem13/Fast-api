from fastapi import FastAPI
from  app.routes import auth_routes
app = FastAPI()

app.include_router(auth_routes.router)
@app.on_event("startup")
async def startup_event():
    print("FastAPI E-commerce server is running!")

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI E-commerce!"}
