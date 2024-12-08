# Streamlit App
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

frame2 = pd.read_csv("movie_final.csv")
st.title("Movie Data Analysis")
st.text("Data frame:")
sort_option = st.radio("Sort by:", options = ["rev_worldwide", "rev_opening_weekend_NA", "year", "budget", "critic_rating", "user_rating"], index = 0)
sorted_frame = frame2.sort_values(by = sort_option, ascending = False)
st.dataframe(sorted_frame)
st.text("Histogram:")
hist_column = st.radio(
    "Select a field for the histogram:",
    options=["rev_worldwide", "rev_opening_weekend_NA", "year", "budget", "critic_rating", "user_rating"],
    index=0 
)
fig, ax = plt.subplots()
ax.hist(frame2[hist_column], bins=20, color="blue", edgecolor="black")
ax.set_title(f"Histogram of {hist_column}")
ax.set_xlabel(hist_column)
ax.set_ylabel("Frequency")
st.pyplot(fig)
