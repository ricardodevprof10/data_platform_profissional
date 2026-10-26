# South America Economic Data Platform

Projeto educacional de Engenharia de Dados.

## Objetivo

Processar indicadores economicos publicos utilizando
Python e arquitetura Bronze, Silver e Gold.

## Tecnologias

- Python
- Pandas
- Pytest
- DuckDB
- GitHub Actions

## Estrutura

- src/: modulos Python
- tests/: testes automatizados
- .github/workflows/: integracao continua

## Executar os testes

```bash
pip install -r requirements.txt
python -m pytest tests/ -v
```

## Fonte dos dados

World Bank Open Data API.

## Observacao

Esta etapa demonstra transformacoes e testes locais.
A ingestao da API foi desenvolvida no projeto anterior.
