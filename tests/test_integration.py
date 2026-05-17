from unittest.mock import patch, Mock
from src.viacep_client import fetch_cep


def test_fetch_cep_mocked():
    sample_json = {
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP",
    }

    mock_resp = Mock()
    mock_resp.json.return_value = sample_json
    mock_resp.raise_for_status = Mock()

    with patch("requests.get", return_value=mock_resp) as mocked_get:
        data = fetch_cep("01001-000")
        assert data["cep"] == "01001-000"
        assert data["localidade"] == "São Paulo"
        mocked_get.assert_called_once()
