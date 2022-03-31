import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
 

def average():
    page1 = st.sidebar.selectbox(
            "Select a Page",
            [
            "Average Rating",

            'Box Plot'
          
        ]
            )

    #First Page
    if "Select a Page"=="Average Rating":
        st.subheader('comparision of Avarage Ratings of Data')   
        st.sidebar.checkbox('Show data') 
        if page1 == "Average Rating ":
            st.sidebar.checkbox('Show data')
    
            #st.header('Body Mass Index data')
            

    elif page1== 'Box Plot':
        pass


    
        
        
    
    





def main():
    st.title('Kojo')
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
        #homepage()

        pass

    #Second Page
    elif page == "Objectives":
        
        pass
    
    #Third Page
    elif page == "Methodology":
        
        pass

    #Fourth Page
    elif page == "Analysis of Results":
        average()


    #Fifth page
    elif page == "Conclusion and Recommendation":
        
        pass
    

if __name__ == "__main__":
    main()