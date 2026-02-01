import streamlit as st
    #Python library used for creating and sharing custom, interactive web applications
import pandas as pd
import plotly.express as px
from apis import apod_generator
import os

#in terminal run : streamlit run dashboard.py
#if prompts to enter email: press enter/return
#if not recognized run: python -m streamlit run dashboard.py

st.title("Water Quality Dashboard")
st.header("Internship Ready Software Development")
st.subheader("Prof. Gregory Reis")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Statistics",
     "2D Plots",
     "3D Plots",
     "NASA's APOD"]
)

with tab1:
   # st.info("Working on this") #only exists within tab1
   st.dataframe(df)
   st.caption("Raw Data")
   st.divider()
   st.dataframe(df.describe())
   st.caption("Descriptive Statistics")

with tab2:
    st.subheader("2D Plots")
    st.write("Use the dropdown to choose which water-quality variable to explore over time!")


    metric = st.selectbox(
        "Select a variable to plot over time:",
        ["Temperature (c)", "ODO mg/L", "pH"]
        )

    fig1 = px.line(df,
                   x="Time",
                   y=metric,
                   title=f"{metric} Over Time in Biscayne Bay",
                   labels={
                       "Time": "Time",
                       "Temperature (c)": "Temperature (°C)",
                       "ODO mg/L": "Dissolved Oxygen (mg/L)",
                       "pH": "pH Level"
            }
        )
    st.plotly_chart(fig1, use_container_width=True)

    st.divider()
    st.write("This scatter plot shows the relationship between dissolved oxygen and temperature.")

    fig2 = px.scatter(df,
                      x="ODO mg/L",
                      y="Temperature (c)",
                      color="pH",
                      title="Dissolved Oxygen vs Temperature",
                      labels={
                          "ODO mg/L": "Dissolved Oxygen (mg/L)",
                          "Temperature (c)": "Temperature (°C)",
                          "pH": "pH Level"
            }
        )
    st.plotly_chart(fig2, use_container_width=True)

#In-Class Code
#fig1 = px.line(df,
#              x = "Time",
#             y = "Temperature (c)")
#st.plotly_chart(fig1)
#fig2 = px.scatter(df,
#x = "ODO mg/L",
#y = "Temperature (c)",
#color = "pH")
#st.plotly_chart(fig2)

with tab3:
    st.subheader("3D Plots")
    st.write("This 3D visualization plots location (latitude/longitude) against water column depth.")

    fig3 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)",
                         title="3D Water Column Depth Across Biscayne Bay",
                         labels={
                             "Longitude": "Longitude",
                             "Latitude": "Latitude",
                             "Total Water Column (m)": "Water Depth (m)"
        }
    )

    st.plotly_chart(fig3, use_container_width=True)

#In-Class Code
#fig3 = px.scatter_3d(df,
#                    x = "Longitude",
#                   y = "Latitude",
#                  z = "Total Water Column (m)")
#fig3.update_scenes(zaxis_autorange= "reversed")
#st.plotly_chart(fig3)

with tab4:
    st.header("Astronomy Picture of the Day")
    #TODO: call a function that generates the APOD
    url = "https://api.nasa.gov/planetary/apod?api_key="
    response = apod_generator(url, os.getenv("NASA_API_KEY"))

    #TODO: (using the streamlit methods) display the APOD image and title and other features
    st.image(response["hdurl"])




