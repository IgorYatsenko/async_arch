from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import RedirectResponse
import httpx
from starlette.config import Config
import base64
import requests


config = Config('.env')

oauth_service = "http://localhost:3000/"
client_id = "o49_sXfD1Wl9dj0yqQhe4YsJCS4-JH1oEWgZ1MlKRGI"
CLIENT_SECRET = "rhRsbrn2HLvWb4Z3qth7u4dwOKxtraWrX6bX5xxinZE"
redirect_uri = "http://localhost:4000/token"
response_type = "code"
scope = "read"

app = FastAPI()

app.session = None 

def get_current_account():
    request.get()

@app.get('/login',response_class=RedirectResponse)
async def redirect_typer():
    return oauth_service

@app.post('/authorize')
def authorize():

    url = f"{oauth_service}oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type={response_type}&scope={scope}"
    print(url)
    response = requests.post(url)

    return response.status_code

@app.post('/token')
def token(request: Request):
    print(request.url)
    print("here")
    code = request.query_params["code"]
    app.code = code
    url = f"{oauth_service}oauth/token?client_id={client_id}&client_secret={CLIENT_SECRET}&grant_type=authorization_code&code={code}&redirect_uri={redirect_uri}"
    response = requests.post(url)
    print(response.json())
    return response.json()