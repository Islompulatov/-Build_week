# imputing libraries
from tkinter.tix import COLUMN
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


#input data into dataframe

    
df_restaurant=pd.read_csv(r'C:\Users\KINGSLEY\OneDrive\Documents\GitHub\-Build_week\restaurant_data.csv') # restaurant 

df_pub=pd.read_csv(r'C:\Users\KINGSLEY\OneDrive\Documents\GitHub\-Build_week\pubs_data.csv') 

df_hotel=pd.read_csv(r'C:\Users\KINGSLEY\OneDrive\Documents\GitHub\-Build_week\hotels_data.csv')

mapper_res = {'£':1, '££':2, '£££':3, '££££':4}
df_restaurant['restaurant_price'] = df_restaurant['restaurant_price'].map(mapper_res)

mapper = {'£':1, '££':2, '£££':3, '££££':4}
df_hotel['hotel_price'] = df_hotel['hotel_price'].map(mapper)
df_pub['pub_price'] = df_pub['pub_price'].map(mapper)

pub_sum, pub_price_mean = df_pub['pub_reviews'].sum(), df_pub['pub_price'].mean()
res_sum, res_price_mean = df_restaurant['restaurant_reviews'].sum(), df_restaurant['restaurant_price'].mean()
hot_sum, hotel_price_mean = df_hotel['hotel_reviews'].sum(), df_hotel['hotel_price'].mean()

res1 = df_restaurant['restaurant_ratings'].mean()
hot1 = df_hotel['hotel_ratings'].mean()
res2 = df_restaurant['restaurant_reviews'].mean()
hot2 = df_hotel['hotel_reviews'].mean()
pub2 = df_pub['pub_reviews'].mean()


res_profit , res_main_profit= res_price_mean * res_sum, res_price_mean * res2

hotel_profit , hotel_main_profit= hotel_price_mean * hot_sum, hotel_price_mean * hot2

pub_profit, pub_main_profit = pub_price_mean * pub_sum, pub_price_mean * pub2




 



res1 = df_restaurant['restaurant_ratings'].mean()
hot1 = df_hotel['hotel_ratings'].mean()
pub1 = df_pub['pub_ratings'].mean()





# objectives of work
def objectives():
    st.header('*The objectives of the project is to:* \n' )  
    st.markdown('### 1. Analysed Pubs, Hotels and Restaurants business in London \n' 

                '### 2. Present recommendation on what Business is more appealing to people in London')
        
# outline   
def outline():
    st.markdown('### 1. Project Objectives \n ' 

                '### 2. Methodology of the Work \n'

                '### 3. Result and Analysis \n'

                '### 4. Conclusion and Recommendation')
        
    
# methods and show data
def methodology():
    st.markdown('#### Data used was London Hotels, Restaurant and Pubs, scraped from [yelp](https://www.yelp.co.uk/search?find_desc=&find_loc=London%2C+United+Kingdom&ns=1) website \n')
    
    st.markdown('### ***Restaurant Data***')
    st.dataframe(df_restaurant)

    st.markdown('### ***Pubs Data***')
    st.dataframe(df_pub)

    st.markdown('### ***Hotels Data***')
    st.dataframe(df_hotel)
    pass


def bar_chart_rating():
    #Creating the dataset
    st.balloons()
    fig = plt.figure(figsize = (10, 5))
    data = {'Restaurant':res1,'Hotel': hot1, 'Pubs':pub1 }
    Courses = list(data.keys())
    values = list(data.values())
    plt.subplot(1, 2, 1)
    plt.bar(Courses, values)
    plt.title("Average Ratings")
    
    plt.subplot(1, 2, 2)
    labels = ['Restaurants', 'Hotels', 'Pubs']
    ratings = [res1, hot1, pub1]
    explode = (0.1, 0, 0)  
    
    plt.pie(ratings, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensu
    st.pyplot(fig)



def barChart_profit():
    st.balloons()
    fig = plt.figure(figsize = (10, 5))
    data = {'Restaurant':res_profit,'Hotel' :hotel_profit , 'Pubs': pub_profit}
    Courses = list(data.keys())
    values = list(data.values())
    plt.subplot(1, 2, 1)
    plt.bar(Courses, values)
    plt.title('Profit of Bussiness')
   
    plt.subplot(1, 2, 2)
    labels = ['Restaurants', 'Hotels', 'Pubs']

    profit= [res_profit, hotel_profit, pub_profit]
    explode = (0.1, 0, 0)  
    plt.pie(profit, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)



def analysis():
    ratings = [res1, hot1, pub1]
    st.bar_char(
            ['restaurant', 'hotel', 'pub'], ratings
    )
    
    pass


      
def recommeded_analysis():
    
    pass




#  Output in the Streamlit App.
def main():
    #st.title('Kojo')
    page = st.sidebar.selectbox(
        "Content", 
        [
            "Title",
            "Presentation Outline",
            "Objectives",
            "Methodology",
            "Analysis of Results",
            "Conclusion and Recommendation"
        ],
        
    )
    
    if page=='Title':
        pass

    #First Page
    elif page == "Presentation Outline":

        outline()


    #Second Page
    elif page == "Objectives":

        objectives()
        
    
    #Third Page
    elif page == "Methodology":

        methodology()
        

    #Fourth Page
    elif page == "Analysis of Results":
        bar_chart_rating()
        
        barChart_profit()
        


    #Fifth page
    elif page == "Conclusion and Recommendation":
        recommeded_analysis()
        
    

if __name__ == "__main__":
    main()