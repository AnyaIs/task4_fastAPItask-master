import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/")
async def p_index():
    return {"FIO": "Горбунова Анна Сергеевна"}


@app.get("/users", response_class=HTMLResponse)
async def p_users():
    output = "<h3> Group:1215i </h3>"
    return output

@app.get("/tools", response_class=HTMLResponse)
async def p_tools():
    output = "<h2> <center> Python <br> backend  <br> developer </center></h2>"
    return output

if __name__ == "__main__":
    uvicorn.run(app = "main:app",host="127.0.0.1",port=500)