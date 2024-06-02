from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/api/')
# Met de '/api/v1/endpoint' URL wordt de api() functie aangeroepen
def api(groenten: str = 'bloemkool', fruit: str = 'appel'):
    return {'groenten': groenten, 'fruit': fruit}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

# # OPTIONAL
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)