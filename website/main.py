import streamlit as st
import pandas as pd
import numpy as np
from scrapping import scrapping

class Program:
    def main():
        # Title of the page
        st.title('Testing website')
        
        # Setting a DataFrame manually
        st.write('DataFrame')
        df = pd.DataFrame({ 'column 1': [0, 1, 3], 'column 2': [4, 5, 6]})
        st.write(df)
        
        # Writing a table
        st.write('Static table')
        st.table(df)

        # Creating a DataFrame through numpy
        st.write('Simple numpy dataframe')
        dataframe = np.random.randn(10, 30)
        st.dataframe(dataframe)
        
        # Creating a DataFrame and highlight the max values of each column
        dataframe2 = pd.DataFrame(
            np.random.randn(10, 20),
            columns=('col %d' % i for i in range(20)))
        st.dataframe(dataframe2.style.highlight_max(axis=0))
        
        soup = scrapping.Scrapper.main()
        print(soup)
        st.write(soup)
        
        

if __name__ == '__main__':
    Program.main()
