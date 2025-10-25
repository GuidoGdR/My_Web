from os import environ
import requests

def turnstileValidator(token:str):
    if token:

        turnstile_secret_key = environ["TURNSTILE_SECRET_KEY"]

        url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
        data = {
        "secret": turnstile_secret_key,
        "response": token
        }
        
        return requests.post(url, data=data).json().get("success")
    
    return False