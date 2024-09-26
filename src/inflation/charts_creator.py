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
        line=dict(color="limegreen"),
    )

    return fig


def plot_commodity(df_percommodity):
    df_percommodity["original_period"] = pd.to_datetime(df_percommodity["original_period"])
    df_percommodity["original_period"] = df_percommodity["original_period"].dt.strftime(
        "%Y/%m"
    )
    fig = px.line(
        df_percommodity,
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
    
def plot_hicp(df_hicp, select_country):
    countries = df_hicp["Geopolitical entity (reporting)"].unique()
    for country in countries : 
        df_country = df_hicp[df_hicp["Geopolitical entity (reporting)"] == select_country]
        fig = px.line(
            df_country, 
            x = "original_period", 
            y = "original_value",
            title = f"HICP for {select_country}"
        )
        fig.update_traces(line=dict(color="limegreen"))
        fig.update_layout(
            xaxis_title = "Years" , 
            yaxis_title = f"HICP (2005 = 100) for {select_country}"
        )
    return fig 
def plot_icp(df_icp, select_country1):
    countries = df_icp["Reference Area"].unique()
    for country in countries:
        df_country = df_icp[df_icp["Reference Area"] == country]
        fig = px.line(
            df_country, 
            x = 'original_period', 
            y = 'value',
            title = f"ICP (% change previous period) for {select_country1}"
        )
        fig.update_traces(line_color = "darkgrey")
        fig.update_layout(
            xaxis_title = "Years" , 
            yaxis_title = f"ICP for {select_country1}"
        )
        
    return fig 