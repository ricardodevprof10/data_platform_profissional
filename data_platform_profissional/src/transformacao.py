
import pandas as pd


def transformar_dados(registros):
    linhas = []

    for item in registros:
        linhas.append({
            "codigo_pais": item.get("countryiso3code"),
            "pais": (item.get("country") or {}).get("value"),
            "ano": item.get("date"),
            "pib_usd": item.get("value")
        })

    df = pd.DataFrame(
        linhas,
        columns=[
            "codigo_pais",
            "pais",
            "ano",
            "pib_usd"
        ]
    )

    df["ano"] = pd.to_numeric(
        df["ano"], errors="coerce"
    )

    df["pib_usd"] = pd.to_numeric(
        df["pib_usd"], errors="coerce"
    )

    df = df.dropna(
        subset=["codigo_pais", "pais", "ano", "pib_usd"]
    ).copy()

    df = df[df["pib_usd"] > 0].copy()

    df["ano"] = df["ano"].astype(int)

    df = df.drop_duplicates(
        subset=["codigo_pais", "ano"]
    )

    return df.sort_values(
        ["codigo_pais", "ano"]
    ).reset_index(drop=True)


def gerar_gold(df):
    gold = df.copy()

    gold["pib_bilhoes_usd"] = (
        gold["pib_usd"] / 1_000_000_000
    )

    return gold[
        ["codigo_pais", "pais", "ano", "pib_bilhoes_usd"]
    ]
