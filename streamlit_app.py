import streamlit
#streamlit.title("Healthy Dinner Options")
#streamlit.header('Vegetable Khichdi')
#streamlit.text('Heat a pressure cooker, add oil in it and pressure cook lentils and rice in it.')

#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
