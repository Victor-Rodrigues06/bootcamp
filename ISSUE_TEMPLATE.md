Title: Integrar ViaCEP para enriquecer dados de endereço

Descrição:

Adicionar integração com a API pública ViaCEP (https://viacep.com.br/) para buscar dados de endereço a partir de um CEP e exibir esses dados no site gerado. A integração ocorrerá durante o build (script Python) e os resultados serão incluídos no site estático em `docs/`.

Critérios de aceitação:
- Implementar função `fetch_cep(cep)` em `src/viacep_client.py` que consome ViaCEP.
- Gerar o site estático com `python -m src.generate_site` que produz `docs/index.html` com exemplos.
- Adicionar teste de integração (mock) em `tests/test_integration.py`.
- Incluir GitHub Actions para rodar testes (CI) e publicar em GitHub Pages.

Relação com branch:
Crie a branch `entrega-intermediaria` a partir da branch principal e desenvolva nela.
