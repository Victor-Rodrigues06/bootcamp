from unittest.mock import patch, Mock
import requests
import pytest

from src.viacep_client import fetch_cep


def test_empty_cep_raises():
    with pytest.raises(ValueError):
        fetch_cep("")


def test_cep_not_found_raises():
    mock_resp = Mock()
    mock_resp.json.return_value = {"erro": True}
    mock_resp.raise_for_status = Mock()
    with patch("requests.get", return_value=mock_resp):
        with pytest.raises(ValueError):
            fetch_cep("00000-000")


def test_requests_exception_propagates():
    with patch("requests.get", side_effect=requests.RequestException):
        with pytest.raises(requests.RequestException):
            fetch_cep("01001-000")
