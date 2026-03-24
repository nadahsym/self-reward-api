from fastapi import HTTPException
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
    return {"status": "success", "suggestion": random.choice(rewards)} # nosec

@app.put("/rewards/{reward_id}")
def update_reward(reward_id: int, name: str = None, points: int = None):
    for r in rewards:
        if r["id"] == reward_id:
            if name: r["name"] = name
            if points: r["points"] = points
            return {"status": "updated", "data": r}
    raise HTTPException(status_code=404, detail="Reward tidak ditemukan")

# DELETE: Menghapus reward berdasarkan ID
@app.delete("/rewards/{reward_id}")
def delete_reward(reward_id: int):
    for index, r in enumerate(rewards):
        if r["id"] == reward_id:
            removed = rewards.pop(index)
            return {"status": "deleted", "data": removed}
    raise HTTPException(status_code=404, detail="Reward tidak ditemukan")