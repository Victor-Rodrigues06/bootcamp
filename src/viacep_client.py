import requests


def fetch_cep(cep: str) -> dict:
    """Fetch address information for a Brazilian CEP using ViaCEP.

    Args:
        cep: CEP string (may contain hyphen).

    Returns:
        Parsed JSON as dict.

    Raises:
        ValueError: if CEP not found or API returns error.
        requests.RequestException: on network/HTTP errors.
    """
    cep_clean = "".join(ch for ch in cep if ch.isdigit())
    if not cep_clean:
        raise ValueError("Empty CEP")
    url = f"https://viacep.com.br/ws/{cep_clean}/json/"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    if data.get("erro"):
        raise ValueError("CEP not found")
    return data
