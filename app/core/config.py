from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'Sinair Minecraft Admin'
    http_port: int = Field(
        default=8000,
        validation_alias='UVICORN_PORT'
    )
    host: str = Field(
        default='0.0.0.0',
        validation_alias='UVICORN_HOST'
    )
    management_api_base_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        populate_by_name=True
    )


settings = Settings()
