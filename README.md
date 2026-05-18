# Entrega Intermediaria — Integração ViaCEP

Projeto de exemplo para a Etapa Intermediária do curso.

Visão rápida:

- Aplicação em Python que consome a API pública ViaCEP durante a etapa de build.
- Gera um site estático em `docs/` com resultados de exemplo.
- Teste de integração com mock em `tests/test_integration.py`.
- GitHub Actions: CI para rodar testes e workflow para publicar em GitHub Pages.

Como usar (local):

1. Crie e ative um virtualenv.

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

2. Instale dependências e rode testes:

```bash
pip install -r requirements.txt
pytest -q
```

Gerar relatório de coverage localmente:

```bash
pytest -q --cov=src --cov-report=xml
```

3. Gere o site estático (vai criar `docs/index.html`):

```bash
python -m src.generate_site
```

4. Para publicar no GitHub Pages: faça commit/push para o repositório e abra PR para `main`. Depois de merge, o workflow `deploy.yml` criará o deploy automático.

## Deploy (link)

O site está publicado em: **https://victor-rodrigues06.github.io/bootcamp/**

Acesse o link acima para visualizar os resultados da integração com a API ViaCEP.
