from fastapi import FastAPI
import random

app = FastAPI()

# Data sementara (karena kita belum pakai database)
rewards = [
    {"id": 1, "name": "Beli Es Kopi", "points": 10},
    {"id": 2, "name": "Nonton Netflix 2 Jam", "points": 20}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to Self-Reward Planner API!"}

@app.get("/rewards")
def get_rewards():
    return {"status": "success", "data": rewards}

@app.post("/rewards")
def add_reward(name: str, points: int):
    new_id = len(rewards) + 1
    new_reward = {"id": new_id, "name": name, "points": points}
    rewards.append(new_reward)
    return {"status": "reward added", "data": new_reward}

@app.get("/suggestion")
def get_suggestion():
    if not rewards:
        return {"message": "Daftar hadiah kosong, ayo tambah dulu!"}
    return {"status": "success", "suggestion": random.choice(rewards)}