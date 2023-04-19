
from pydantic import BaseSettings

class Settings(BaseSettings):
    # #database_password: str = "localhost"
    # #path: int
    # database_username: str = "postgres"
    # secret_key: str = "343243243243"

    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    
    class Config:
        env_file = ".env"


settings = Settings()





