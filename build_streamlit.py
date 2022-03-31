import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


#input data into dataframe

    
df_restaurant=pd.read_csv(r'C:\Users\KINGSLEY\OneDrive\Documents\GitHub\-Build_week\restaurant_data.csv')
    
print(df_restaurant)

def average():
    page1 = st.sidebar.selectbox(
            "Select a Page",
            [
            "Average Rating",

            'Box Plot'
          
        ]
            )

    #First Page
     
    st.sidebar.checkbox('Show data') 
    st.subheader('comparision of Avarage Ratings of Data')  
    if page1 == "Average Rating ":
        st.sidebar.checkbox('Show data')
    
            #st.header('Body Mass Index data')
            

    elif page1== 'Box Plot':
        pass


    
def objectives():
    st.header('*The objectives of the project is to:* \n' )  
    st.markdown('### 1. Analysed Pubs, Hotels and Restaurants business in London \n' 

                '### 2. Present recommendation on what Business is more appealing to people in London')
        
    
def outline():
    st.markdown('### 1. Project Objectives \n ' 

                '### 2. Methodology of the Work \n'

                '### 3. Result and Analysis \n'

                '### 4. Conclusion and Recommendation')
        
    

def methodology():
    st.dataframe(df_restaurant[:10])  





def main():
    #st.title('Kojo')
    page = st.sidebar.selectbox(
        "Content", 
        [
            "Presentation Outline",
            "Objectives",
            "Methodology",
            "Analysis of Results",
            "Conclusion and Recommendation"
        ],
        
    )
    
    #First Page
    if page == "Presentation Outline":
        outline()

        pass

    #Second Page
    elif page == "Objectives":
        objectives()
        
    
    #Third Page
    elif page == "Methodology":

        methodology()
        

    #Fourth Page
    elif page == "Analysis of Results":

        average()


    #Fifth page
    elif page == "Conclusion and Recommendation":
        
        pass
    

if __name__ == "__main__":
    main()