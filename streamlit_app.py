import streamlit
streamlit.title("Healthy Dinner Options")
streamlit.header('Vegetable Khichdi')
streamlit.text('Heat a pressure cooker, add oil in it and pressure cook lentils and rice in it.')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

fruit_list = fruit_list.set_index('Fruit')
#fruit_list = fruit_list.set_index('Serving_Size')

#To select fruits from the csv list
#streamlit.multiselect ("Pick some fruits:",list(fruit_list.Fruit))
streamlit.multiselect ("Pick some fruits:",list(fruit_list.index),['Avocado','Lime'])

#Display the overall csv table 
streamlit.dataframe(fruit_list)
