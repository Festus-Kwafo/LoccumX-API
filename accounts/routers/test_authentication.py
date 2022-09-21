from fastapi.testclient import TestClient
from .authentication import router

client = TestClient(router)

def test_login():
    response = client.post("/login", 
    json={'username':"peter@test.com", 'password':'1234'})
    assert response.status_code == 200
