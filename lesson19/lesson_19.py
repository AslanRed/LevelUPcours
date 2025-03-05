from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title = 'Random advice')

class Advice(BaseModel):
    text:str

advice_list = ['1', '2', '3']

@app.get('/advice', summary = 'get random advice')
def get_random_advice():
    return {'advice': random.choice(advice_list)}

@app.get('/', summary = 'Main')
def read_root():
    return {'message': 'Welcome to API of random advice, go to /advice - to get advice'}

@app.post('/advice', summary = 'New advice')
def add_advice(advice: Advice):
    if advice.text in advice_list:
        raise HTTPException(status_code = 400, detail = 'Already exists')
    advice_list.append(advice.text)
    return {'message': 'Succes'}