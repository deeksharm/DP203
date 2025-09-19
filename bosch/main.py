pip install fastapi 
pip install uvicorn

------------------

from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

# Create a basic GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

------------------------------
uvicorn main:app --reload

