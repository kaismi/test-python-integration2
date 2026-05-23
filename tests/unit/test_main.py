from src.test_python_integration2.main import load_app_config


def test_placeholder():
    assert 1 + 1 == 2


def test_app_config():
    app_config = load_app_config()
    assert app_config.secret_key == "supersecret"
    assert app_config.db_url == "postgresql://user:pass@localhost:5432/app"
    assert app_config.debug
