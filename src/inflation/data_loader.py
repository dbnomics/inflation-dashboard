from dbnomics import fetch_series


# Download DBnomics data for inflation
def download_data():
    df_inflation = fetch_series(
        [
            "OECD/KEI/CPALTT01.ARG.GY.M",
            "OECD/KEI/CPALTT01.AUS.GY.M",
            "OECD/KEI/CPALTT01.AUT.GY.M",
            "OECD/KEI/CPALTT01.BRA.GY.M",
            "OECD/KEI/CPALTT01.CAN.GY.M",
            "OECD/KEI/CPALTT01.CHN.GY.M",
            "OECD/KEI/CPALTT01.ESP.GY.M",
            "OECD/KEI/CPALTT01.FRA.GY.M",
            "OECD/KEI/CPALTT01.GBR.GY.M",
            "OECD/KEI/CPALTT01.IDN.GY.M",
            "OECD/KEI/CPALTT01.IND.GY.M",
            "OECD/KEI/CPALTT01.ITA.GY.M",
            "OECD/KEI/CPALTT01.KOR.GY.M",
            "OECD/KEI/CPALTT01.MEX.GY.M",
        ]
    )

    print(df_inflation.columns)

    col_inf = ["original_period", "original_value", "Country"]

    inflation = (
        df_inflation[col_inf].rename(columns={"original_value": "inflation"}).dropna()
    )
    print(inflation.columns)
    return inflation


def create_df():
    df = download_data()
    countries = df["Country"].unique()

    for country in countries:
        df_country = df[df["Country"] == country]
        print(f"Data for {country}:")
        print(df_country.head())
    return df_country


def download_commodity_data():
    df_commodity = fetch_series(
        [
            "IMF/PCPS/M.W00.PGOLD.PC_CP_A_PT",
            "IMF/PCPS/M.W00.PNRG.PC_CP_A_PT",
            "IMF/PCPS/M.W00.PNGAS.PC_CP_A_PT",
            "IMF/PCPS/M.W00.PGASO.PC_CP_A_PT",
            "IMF/PCPS/M.W00.PCERE.PC_CP_A_PT",
            "IMF/PCPS/M.W00.PCOCO.PC_CP_A_PT",
            "IMF/PCPS/M.W00.PCOFF.PC_CP_A_PT",
            "IMF/PCPS/M.W00.POILAPSP.PC_CP_A_PT",
        ]
    )
    col_com = ["original_period", "original_value", "Commodity"]

    df_commodity = (
        df_commodity[col_com]
        .rename(columns={"original_value": "commodity prices"})
        .dropna()
    )

    return df_commodity


def create_commodity_df():
    df = download_commodity_data()
    commodities = df["Commodity"].unique()
    for commodity in commodities:
        df_percommodity = df[df["Commodity"] == commodity]
        print(f"Data for {commodity}:")
        print(df_percommodity.head())
    return df_percommodity
