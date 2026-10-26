
import pandas as pd

from src.transformacao import (
    transformar_dados,
    gerar_gold
)


def test_transformacao_valida():
    dados = [{
        "countryiso3code": "BRA",
        "country": {"value": "Brazil"},
        "date": "2024",
        "value": 2000000000000
    }]

    resultado = transformar_dados(dados)

    assert len(resultado) == 1
    assert resultado.iloc[0]["ano"] == 2024
    assert resultado.iloc[0]["codigo_pais"] == "BRA"


def test_remover_registros_invalidos():
    dados = [
        {
            "countryiso3code": "BRA",
            "country": {"value": "Brazil"},
            "date": "2024",
            "value": 2000000000000
        },
        {
            "countryiso3code": "ARG",
            "country": {"value": "Argentina"},
            "date": "2024",
            "value": None
        }
    ]

    resultado = transformar_dados(dados)

    assert len(resultado) == 1
    assert resultado.iloc[0]["codigo_pais"] == "BRA"


def test_calculo_gold():
    silver = pd.DataFrame([{
        "codigo_pais": "BRA",
        "pais": "Brazil",
        "ano": 2024,
        "pib_usd": 2000000000000
    }])

    gold = gerar_gold(silver)

    assert gold.iloc[0]["pib_bilhoes_usd"] == 2000
