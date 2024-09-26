import importlib

import streamlit as st
from charts_creator import plot_commodity, plot_inflation, plot_hicp, plot_icp
from data_loader import download_commodity_data, download_data, download_hicp, download_icp
from streamlit_option_menu import option_menu


def main() -> None:
    package_dir = importlib.resources.files("inflation")
    st.set_page_config(
        page_title="DBnomics Inflation Plots",
        page_icon=str(package_dir / "images/favicon.png"),
    )
    st.image(str(package_dir / "images/dbnomics.svg"), width=300)
    st.title(":blue[Price Indicators]")

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

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Explanations", "Inflation", "CPI","HICP","Commodity Prices Index", "Sources"],
            icons=["book", "bar-chart", "bar-chart", "bar-chart","bar-chart", "search"],
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
        )
        st.markdown("---")
        st.write(
            "**Consumer Price Index (CPI)**:\n"
            "\n"
            "A partial measure of inflation based on household consumption.\n"
            "It is calculated by observing the price changes of a fixed basket of goods and services every year.\n"
            "\n"
            "**Harmonised Index of Consumer Prices (HICP)**:\n" 
            "\n"
            "A consumer price index calculated across EU countries using a standardized methodology.\n"
        )
        st.markdown("---")
        st.write(
            "**Commodity Price**\n"
            "\n"
            "Commodity prices are the prices at which **raw materials or foods are bought and sold**.\n"
            "A \"commodity\" could be defined as a basic resource that is interchangeable with other similar goods.\n"
            "They are most often used as **inputs** in the production of goods.\n"
            "\n"
            "There are **two categories**\n"
            "- **Hard Commodities**: Metal, Energy.\n"
            "- **Soft Commodities**: Agricultar goods.\n"
            "\n"
            "**Commodity prices tend to rise when inflation accelerates.**\n"
            "Investors use commodities as a hedge against inflation, leading to an increase in the demand for these assets.\n"
        )
    if selected == "Inflation":
        tab1, tab2 = st.tabs([":bar_chart:",":file_folder:"])
        
        df = download_data()
        countries = df["Country"].unique()
        with tab1:
            
            country = st.selectbox("Select a country", countries)

            country_df = df[df["Country"] == country]
            st.write(f":blue[**Inflation for {country}:**] ")
            fig = plot_inflation(country_df)
            st.plotly_chart(fig)
        with tab2:
            st.write(f"**Data for {country}**:")
            st.write(country_df)
    if selected == "CPI":
        df = download_icp()
        countries = df["Reference Area"].unique()
        tab1, tab2 = st.tabs([":bar_chart:" , ":file_folder:"])
        with tab1:
            select_country1 = st.selectbox("Select a Country/Area", countries)
            fig = plot_icp(df, select_country1)
            st.plotly_chart(fig)
        with tab2: 
            st.write(f"Dataset for {select_country1}")
            st.write(df[df["Reference Area"] == select_country1])

    if selected == "HICP": 
        df = download_hicp()
        countries = df["Geopolitical entity (reporting)"].unique()
        tab1, tab2 = st.tabs([":bar_chart:", ":file_folder:"])
        with tab1:
            select_country = st.selectbox("Select a country/area", countries)
            fig = plot_hicp(df, select_country)
            st.plotly_chart(fig)
        with tab2:
            st.subheader(f"Dataset for {select_country}")
            st.write(df[df["Geopolitical entity (reporting)"] == select_country])
    if selected == "Commodity Prices Index":
        df = download_commodity_data()
        commodities = df["Commodity"].unique()
        tab1, tab2 = st.tabs([":bar_chart:", ":file_folder:"])
        with tab1:
            commodity = st.selectbox("**Select:**", commodities)
            commodity_df = df[df["Commodity"] == commodity]
            fig = plot_commodity(commodity_df)
            st.plotly_chart(fig)
        with tab2:
            st.write("Dataset")
            st.write(commodity_df)

    if selected == "Sources":
        st.subheader("**Data**")
        st.write(
            "[Inflation](https://db.nomics.world/OECD/KEI?tab=list)\n"
            "\n"
            "[CPI](https://db.nomics.world/IMF/CPI?tab=list)\n"
            "\n"
            "[HICP](https://db.nomics.world/Eurostat/prc_hicp_midx?tab=list)\n"
            "\n"
            "[Commodity Prices Index](https://db.nomics.world/IMF/PCPS?dimensions=%7B\"UNIT_MEASURE\"%3A%5B\"PC_CP_A_PT\"%5D%2C\"FREQ\"%3A%5B\"M\"%5D%7D&q=commodity%20prices&tab=list)\n"
        )
        st.markdown("---")
        st.write("[Source Code](https://github.com/dbnomics/inflation-dashboard)")
        st.write("[DBnomics](https://db.nomics.world)")

if __name__ == "__main__":
    main()
