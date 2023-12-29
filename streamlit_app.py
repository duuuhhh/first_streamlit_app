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
fruits_selected=streamlit.multiselect ("Pick some fruits:",list(fruit_list.index),['Avocado','Lime'])
fruits_to_show = fruit_list.loc[fruits_selected]

#Display the overall csv table 
streamlit.dataframe(fruits_to_show)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
# To linearize the array formatted json fields (nutrition fields)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#to display the json in tabular format on the screen
streamlit.dataframe(fruityvice_normalized)

#Asking user input
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
add_my_fruit=streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('The user entered ', add_my_fruit)
streamlit.text("Thanks for adding jackfruit:")
streamlit.text(my_data_row)


