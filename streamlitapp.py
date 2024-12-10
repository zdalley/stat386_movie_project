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

# Create histogram figure outside st.pyplot
fig, ax = plt.subplots()
ax.hist(frame2[hist_column], bins=20, color="blue", edgecolor="black")
ax.set_title(f"Histogram of {hist_column}")
ax.set_xlabel(hist_column)
ax.set_ylabel("Frequency")

# Pass the figure to st.pyplot
st.pyplot(fig)


st.header("Scatterplots")

col1, col2, col3 = st.columns(3)

# Create figures for scatterplots
fig1, ax1 = plt.subplots()
ax1.scatter(frame2["budget"], frame2["rev_worldwide"], alpha=0.7, color="blue")
ax1.set_title(f"Budget vs Worldwide Revenue")
ax1.set_xlabel("Budget")
ax1.set_ylabel("Worldwide Revenue")

fig2, ax2 = plt.subplots()
ax2.scatter(frame2["rev_opening_weekend_NA"], frame2["rev_NA"], alpha=0.7, color="blue")
ax2.set_title(f"Opening Weekend vs Total Revenue (North America)")
ax2.set_xlabel("Opening Weekend Revenue (North America)")
ax2.set_ylabel("Total Revenue (North America)")

fig3, ax3 = plt.subplots()
ax3.scatter(frame2["user_rating"], frame2["critic_rating"], alpha=0.7, color="blue")
ax3.set_title(f"User vs Critic Rating")
ax3.set_xlabel("User Rating")
ax3.set_ylabel("Critic Rating")

# Pass the figures to st.pyplot
with col1:
    st.pyplot(fig1)
with col2:
    st.pyplot(fig2)
with col3:
    st.pyplot(fig3)


