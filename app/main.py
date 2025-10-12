from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("FastAPI E-commerce server is running!")

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI E-commerce!"}
