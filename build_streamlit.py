# imputing libraries
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd


#input data into dataframe

    
df_restaurant=pd.read_csv(r'C:\Users\KINGSLEY\OneDrive\Documents\GitHub\-Build_week\restaurant_data.csv') # restaurant 

    


def analysis():
    pass


      
def recommeded_analysis():
    pass


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
    st.dataframe(df_restaurant[:10])  







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
        analysis()
        


    #Fifth page
    elif page == "Conclusion and Recommendation":
        recommeded_analysis()
        
    

if __name__ == "__main__":
    main()