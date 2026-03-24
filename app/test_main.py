from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test READ (Semua Rewards)
def test_get_all_rewards():
    response = client.get("/rewards")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

# Test CREATE (Tambah Reward Baru)
def test_create_reward():
    payload = {"id": 99, "name": "Beli Seblak", "points": 15}
    response = client.post("/rewards", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["data"]["name"] == "Beli Seblak"

# Test UPDATE (Ubah Reward)
def test_update_reward():
    # Kita update ID 1 (Kopi) yang sudah ada di list awal
    response = client.put("/rewards/1?name=Kopi%20Susah%20Gula&points=12")
    assert response.status_code == 200
    assert response.json()["data"]["points"] == 12

# Test DELETE (Hapus Reward)
def test_delete_reward():
    # Kita hapus ID 99 yang baru kita buat tadi
    response = client.delete("/rewards/99")
    assert response.status_code == 200
    assert response.json()["status"] == "deleted"

# Test ERROR (Cek kalau ID tidak ketemu)
def test_delete_non_existent_reward():
    response = client.delete("/rewards/9999")
    assert response.status_code == 404