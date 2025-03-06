from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing - Start offereing your skills online!"
]

money_quotes = [
    "earn more and more money"
]

@app.get("/side_hustles")
def get_side_hustles(apiKey:str):
    """Return a random side hustle"""
    if apiKey != "123456":
     return {"Error": "Invalid API"}
    return {"side_hustles":random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apiKey:str):
    """Return a random money quote"""
    if apiKey != "123456":
     return {"Error": "Invalid API"}
    return {"money_quotes":random.choice(money_quotes)}