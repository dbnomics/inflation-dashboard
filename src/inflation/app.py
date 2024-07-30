import importlib

import streamlit as st
from charts_creator import plot_commodity, plot_inflation
from data_loader import download_commodity_data, download_data
from streamlit_option_menu import option_menu


def main() -> None:
    package_dir = importlib.resources.files("inflation")
    st.set_page_config(
        page_title="DBnomics Inflation Plots",
        page_icon=str(package_dir / "images/favicon.png"),
    )
    st.image(str(package_dir / "images/dbnomics.svg"), width=300)
    st.title(":blue[Prices Evolution]")

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css(str(package_dir / "assets/styles.css"))
    st.markdown(
        """
        <style>
        hr {
            height: 1px;
            border: none;
            color: #333;
            background-color: #333;
            margin-top: 3px;
            margin-bottom: 3px;
        }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Explanations", "Inflation", "Commodity Prices Index", "Sources"],
            icons=["book", "bar-chart", "bar-chart", "search"],
            menu_icon=":",
            default_index=0,
        )

    if selected == "Explanations":
        st.subheader(":blue[**Definitions**]")
        st.markdown("---")
        st.write(
            "**Inflation**\n"
            "\n"
            "Inflation occurs when there is **a broad increase in the prices of goods and prices**.\n"
            "It leads to a loss of purchasing power. **With 1€, you can buy less today than you could yesterday**.\n"
            "Inflation **reduces the value of currency** over time.\n"
            "\n"
            "**Consumer Price Index (CPI)**: a partial measure of inflation → household consumption. "
        )
        st.markdown("---")
        st.write(
            "**Commodity Price**\n"
            "\n"
            "Commodity prices are the prices at which **raw materials or foods are bought and sold**.\n"
            "\"Commodity\" could be defined as basic resources that are interchangeable with other goods which are similar.\n"
            "They are most often used as **inputs** in the production of goods.\n"
            "\n"
            "There are **two categories**\n"
            "- **Hard Commodities**: Metal, Energy.\n"
            "- **Soft Commodities**: Agricultar goods.\n"
            "\n"
            "**Commodity prices increase when inflation accelerates.**\n"
            "Investors use commodities as a protection. So, the demand of commodities increases.\n"
        )
    if selected == "Inflation":
        df = download_data()
        countries = df["Country"].unique()
        country = st.selectbox("Select a country", countries)

        country_df = df[df["Country"] == country]
        st.write(f":blue[**Inflation for {country}:**] ")
        fig = plot_inflation(country_df)
        st.plotly_chart(fig)

        st.write(f"**Data for {country}**:")
        st.write(country_df.iloc[:, :-1])

    if selected == "Commodity Prices Index":
        df = download_commodity_data()
        commodities = df["Commodity"].unique()
        commodity = st.selectbox("**Select:**", commodities)

        commodity_df = df[df["Commodity"] == commodity]
        fig = plot_commodity(commodity_df)
        st.plotly_chart(fig)
        st.write(f"**Data Table**")
        st.write(commodity_df.iloc[:, :-1])

    if selected == "Sources":
        st.subheader("**Data**")
        st.write(
            "[Inflation](https://db.nomics.world/OECD/KEI?tab=list)\n"
            "\n"
            "[Commodity Prices Index](https://db.nomics.world/IMF/PCPS?dimensions=%7B\"UNIT_MEASURE\"%3A%5B\"PC_CP_A_PT\"%5D%2C\"FREQ\"%3A%5B\"M\"%5D%7D&q=commodity%20prices&tab=list)\n"
        )
        st.markdown("---")
        st.write("[Source Code](https://github.com/dbnomics/inflation-dashboard)")
        st.write("[DBnomics](https://db.nomics.world)")

if __name__ == "__main__":
    main()
