import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    project_id: str = Field(env="PROJECT_ID")
    dataset_id: str = Field(env="DATASET_ID")
    table_id: str = Field(env="TABLE_ID")

    google_application_credentials:str = Field(env="GOOGLE_APPLICATION_CREDENTIALS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.google_application_credentials