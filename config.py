from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "LocumX API"
    admin_email: str | None
    jwt_secret_key: str 
    jwt_refresh_secret_key: str
    algorithm: str

    class Config:
        env_file = ".env"