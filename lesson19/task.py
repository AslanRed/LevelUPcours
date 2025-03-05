# Fast API 
#root /GET(welcome to API, send text, i will repeat it(/echo))
#/echo POST (repeat)

from fastapi import FastAPI
from pydantic import BaseModel

class Message(BaseModel):
    text:str


app = FastAPI(title = 'echo')

@app.get('/', summary = 'Повторение текста')
def repeat():
    return {'message': 'Перейдите по ссылке /echo, для повтора сообщения'}

@app.post('/echo', summary = 'Текст для повторения')
def add_text(message: Message):
    return {'message': message.text}