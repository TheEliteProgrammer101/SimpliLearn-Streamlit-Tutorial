import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import pydeck as pdk

@st.cache_data
def load_data(file_upload):
    if file_upload.name.endswith(".csv"):
        df = pd.read_csv(file_upload)
        df.index = df.index + 1
        return df
    elif file_upload.name.endswith(".xlsx"):
        df = pd.read_excel(file_upload)
        df.index = df.index + 1
        return df
    return None

uploaded_file = st.file_uploader("Pick a dataset", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write(df)

    select_box = st.selectbox("Select a value to filter data by:", df["Product Name"].unique())
    filtered_data = df[df["Product Name"] == select_box]
    st.write(filtered_data)

    st.write("Total no. of rows: ", len(df))
    st.write("Summary aggregates of dataset: ", df.describe())
    st.metric("Total no of rows: ", len(df.index))
    st.metric("Total no of columns: ", len(df.columns))

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 30, 40])
    st.pyplot(fig) # plot takes no argument like x=[], y=[]

    fig = px.bar(x=["A", "B", "C", "D"], y=[10, 20, 30 ,40])
    st.plotly_chart(fig) # bar takes in argument of x=[] and y=[]

    deck = pdk.Deck(initial_view_state=pdk.ViewState(latitude=40, longitiude=100, zoom=10),
    layers=[pdk.Layer(type="HexagonalLayer", data=df, get_positions=['lng', 'lat'], radius=1000)]) #the zoom is usually btwn 1 and 24

    st.pydeck_chart(deck)