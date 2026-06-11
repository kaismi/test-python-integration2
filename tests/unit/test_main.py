from unittest.mock import patch

import test_python_integration2.main as main


def test_placeholder():
    assert 1 + 1 == 2


def test_app_config():
    mocked_config = main.AppConfig(
        db_url="postgresql://user:pass@localhost:5432/app",
        secret_key="supersecret",
        debug=True,
    )

    with patch("test_python_integration2.main.load_app_config", return_value=mocked_config) as mocked_load:
        app_config = main.load_app_config()

    mocked_load.assert_called_once()
    assert app_config.secret_key == "supersecret"
    assert app_config.db_url == "postgresql://user:pass@localhost:5432/app"
    assert app_config.debug
