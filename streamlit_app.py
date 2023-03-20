import streamlit
import pandas
import requests
import snowflake.connector
#from urllib.error import urlerror
streamlit.title('healthy food')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.multiselect("pick a fruit:",list(my_fruit_list.index))
#streamlit.multiselect("pick a fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_selected= streamlit.multiselect("pick a fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_respone=requests.get("https://fruityvice.com/api/fruits"+ this_fruit_choice)
  fruityvice_normalized=pandas.json_normalized(fruityvice_response.json())
  return fruityvice_normalized
      
  

streamlit.header('fruityvice favourit food')
try:
  fruit_choice=streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.datafram(back_from_function)
      
except urlerror as e:
                  streamlit.error()
                  
#streamlit.write('the user entered is',fruit_choice)

streamlit.stop()




my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
#my_cur.execute("select current_user(), current_account(), current_region()")
my_cur.execute("select * from fruit_load_list")
my_row=my_cur.fetchall()
#streamlit.text("hello snowflake")
#streamlit.text(my_row)

streamlit.header("the fruit load list contains")
streamlit.dataframe(my_row)


streamlit.write('the user entered fruit is',fruit_choices)



def inser_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list(' " + ???? + "')")
    return "thankyou fro adding"+new_fruit
add_my_fruit= streamlit.text_input('what fruit would you like to add')
if streamlit.button('Add a fruit to the list'):
  my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
  
