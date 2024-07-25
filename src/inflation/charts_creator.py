import pandas as pd
import plotly.express as px


def plot_inflation(df_country):
    df_country["original_period"] = pd.to_datetime(df_country["original_period"])
    df_country["original_period"] = df_country["original_period"].dt.strftime("%Y/%m")
    fig = px.line(
        df_country,
        x="original_period",
        y="inflation",
        title="Inflation Evolution",
        labels={
            "original_period": "Date",
            "inflation": "Inflation ",
            "Country": "Country",
        },
        custom_data=["original_period", "inflation", "Country"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Country: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "Inflation (%): %{customdata[1]}",
            ]
        ),
        line=dict(color="deepink"),
    )

    return fig


def plot_commodity(df_commodity):
    df_commodity["original_period"] = pd.to_datetime(df_commodity["original_period"])
    df_commodity["original_period"] = df_commodity["original_period"].dt.strftime(
        "%Y/%m"
    )
    fig = px.line(
        df_commodity,
        x="original_period",
        y="commodity prices",
        title="Commodity Prices Evolution",
        labels={
            "original_period": "Date",
            "commodity prices": "Commodity Price Evolution",
            "Commodity": "Commodity",
        },
        custom_data=["original_period", "commodity prices", "Commodity"],
    )

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "Commodity: %{customdata[2]}",
                "Date: %{customdata[0]}",
                "Commodity Prices (%): %{customdata[1]}",
            ]
        ),
        line=dict(color="gold"),
    )

    return fig
