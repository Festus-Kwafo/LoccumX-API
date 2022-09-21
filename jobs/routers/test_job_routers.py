from fastapi.testclient import TestClient
from .jobs_routers import router

# client = TestClient(router)

# def test_create_jobs():
#     response = client.post(
#         '/create/jobs',
#         headers= f'bearer'
#     )