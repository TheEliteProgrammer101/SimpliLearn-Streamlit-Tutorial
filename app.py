import streamlit as st
# testing the app
st.write("hello world! how re you doing")

# streamlit basics

# displaying text in streamlit
st.write("This is a simple text")

# if u want to add headers and subheaders to ur structure
st.markdown("# This is a large heading...")
st.markdown("## This is a smaller heading...")

# add interactive elements/widgets like sliders, buttons, checkboxes
# a. Slider - a slider lets the user pick a number within a defined range
number = st.slider("Pick a number", min_value=1, max_value=10000)
st.write(f"You picked {number}")

# b. Checkbox - lets add a checkbox for a user to agree to terms and conditions
check = st.checkbox("Agree to terms")
if check:
    st.write("You agreed!")
# c. media(video/image)
st.image("https://github.com/TheEliteProgrammer101/SimpliLearn-Streamlit-Tutorial/blob/main/v-finest.png")
st.video('<iframe width="560" height="315" src="https://www.youtube.com/embed/x_rDimMmx-Q?si=s2upms-HWc9wP4dy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>')


# Data Exploration with streamlit: how to upload and display files like csv and excel sheets and dive into displaying the data in a table and applying interactive filters and we'll also cover adding summary statistics and metrics to make it insightful
#.. adding/uploading csv or excel files
import pandas as pd

uploaded_file = st.file_uploader("Pick a dataset", type=["csv", "xlsx"])
df = ""
#checking if uploader contains a file or not and reads it if it does
if uploaded_file is not None:
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
#else:
    #st.button("no file uploaded...")

    # dislays the dataset
    st.write(df) #or
    #st.dataframe(df)

# lets add a interactive filtering

#create a selectbox for filtering data by column value
#print(df.columns)
if uploaded_file is not None:
    select_box = st.selectbox("Select a value to filter by: ", df["Product Name"].unique())
    filtered_data = df[df["Product Name"] == select_box]
    st.write(filtered_data)


# now we add summary statistics and metrics to give users a quick overview of the data
if uploaded_file is not None:
    st.write(df.describe())
    st.metric("Total no. of rows", len(df.index)) # or just
    #st.metric("Total no. of rows", len(df))
    st.metric("Total no. of columns", len(df.columns))


# displaying visualizations in streamlit
# using matplotlib to plot a simple chat

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1,2,3,4], [10,20,30,40])

st.pyplot(fig)

#using plotly express to make a bar chat
import plotly.express as px

fig = px.bar(x=['A', 'B', 'C', 'D'], y=[10, 20, 30, 40])
st.plotly_chart(fig)

if uploaded_file is not None:
# using pydeck to display maps for visualizations
    import pydeck as pdk
    if uploaded_file is not None:
        deck = pdk.Deck(initial_view_state=pdk.ViewState(latitude=37.7749, longitude=122.4194, zoom=10),
        layers=[pdk.Layer(type="HexagonalLayer", data=df, get_position=['lon', 'lat'], radius=1000)])
        st.pydeck_chart(deck)
    else:
        st.write("No dataset uploaded")

#A simple data app project
#making a simple dashboard for visualizing the covid-19 data
    # u can imagine something similar for stock prices where you can plot trends over time and show key metrics or the total number of cases or prise movements




# To display title
st.title("Covid-19 Dashboard")

df1 = pd.read_csv(r"C:\Users\User\Downloads\archive\covid_19_india.csv")

# fig = px.line(df1, x="Date", y="Confirmed",title= "Covid-19 Cases Over time")
fig = px.bar(df1, x="Date", y="Confirmed", title="Covid-19 Cases Over time")
st.plotly_chart(fig)

fig = px.line(df1, x="Date", y="Deaths",title= "Covid-19 Deaths Over time")
# or
# fig = px.line(df1, x=df1["Date"], y=df1["Deaths"],title= "Covid-19 Deaths Over time")
st.plotly_chart(fig)

df1.index = df1.index + 1
st.write(df1.head(100))


check_box = st.checkbox("")
select_box = st.selectbox("Pick a country to filter data by: ", df1["State/UnionTerritory"].unique())
st.write(df1[df1["State/UnionTerritory"] == select_box])