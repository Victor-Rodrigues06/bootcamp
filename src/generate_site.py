from pathlib import Path
from src.viacep_client import fetch_cep


SAMPLE_CEPS = ["01001-000", "01311-000"]


def build_docs(out_dir: Path = Path("docs")):
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for cep in SAMPLE_CEPS:
        try:
            data = fetch_cep(cep)
        except Exception as e:
            data = {"erro": str(e)}
        rows.append((cep, data))

    html = [
        "<!doctype html>",
        "<html lang=\"pt-BR\">",
        "<head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"><title>Entrega Intermediaria - ViaCEP</title></head>",
        "<body><h1>Consulta ViaCEP (exemplo gerado)</h1>",
    ]
    for cep, data in rows:
        html.append(f"<h2>CEP: {cep}</h2>")
        if data.get("erro"):
            html.append(f"<p>Erro: {data['erro']}</p>")
            continue
        html.append("<ul>")
        for k in ("logradouro", "bairro", "localidade", "uf", "cep"):
            html.append(f"<li><strong>{k}</strong>: {data.get(k, '')}</li>")
        html.append("</ul>")

    html.append("</body></html>")
    Path(out_dir / "index.html").write_text("\n".join(html), encoding="utf-8")


if __name__ == "__main__":
    build_docs()
