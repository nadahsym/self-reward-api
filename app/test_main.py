from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# 1. Test READ
def test_get_all_rewards():
    response = client.get("/rewards")
    assert response.status_code == 200

# 2. Test CREATE (Sesuaikan dengan cara kita ngetes di /docs tadi)
def test_create_reward():
    # Kita kirim data lewat URL/Query, bukan JSON body
    response = client.post("/rewards?id=99&name=Beli%20Seblak&points=15")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

# 3. Test UPDATE
def test_update_reward():
    response = client.put("/rewards/1?name=Kopi%20Enak&points=12")
    assert response.status_code == 200

# 4. Test DELETE
def test_delete_reward():
    # Sekarang ID 99 sudah ada, jadi bisa dihapus
    response = client.delete("/rewards/99")
    assert response.status_code == 200

# 5. Test SUGGESTION
def test_get_suggestion():
    response = client.get("/suggestion")
    assert response.status_code == 200