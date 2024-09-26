from dbnomics import fetch_series


# Download DBnomics data for inflation
def download_data():
    df_inflation = fetch_series(provider_code= "OECD", dataset_code="KEI",series_code="CPALTT01..GP.M")
    col_inf = ["original_period", "original_value", "Country"]

    inflation = (
        df_inflation[col_inf].rename(columns={"original_value": "inflation"}).dropna()
    )
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
    df_commodity = fetch_series(provider_code= "IMF", dataset_code="PCPS",series_code="M.W00..PC_CP_A_PT", max_nb_series= 200)

    col_com = ["original_period", "original_value", "Commodity"]

    df_commodities= (
        df_commodity[col_com]
        .rename(columns={"original_value": "commodity prices"})
        .dropna()
    )

    return df_commodities


def create_commodity_df(df_commodities):
    commodities = df_commodities["Commodity"].unique()
    for commodity in commodities:
        df_percommodity = df_commodities[df_commodities["Commodity"] == commodity]
    return df_percommodity

def download_hicp():
    df_hicp = fetch_series(provider_code="Eurostat", dataset_code= "prc_hicp_midx", series_code="M.I05.CP00") 
    return df_hicp

def download_icp():
    df_icp = fetch_series(provider_code= "IMF", dataset_code= "CPI", series_code= "M..PCPI_PC_PP_PT", max_nb_series=200) 
    return df_icp