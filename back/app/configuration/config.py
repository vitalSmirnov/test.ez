class Settings:
    app_name: str = "Test"
    port: int = 3000
    debug: bool = True
    database_url: str = "postgresql://postgres:0000@localhost:5432/postgres"
    static_dir: str = "../front/dist"


settings = Settings()
