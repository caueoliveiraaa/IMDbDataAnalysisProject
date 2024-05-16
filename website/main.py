import streamlit as st
import pandas as pd
import numpy as np


class Main:
    def __init__(): 
        pass

    
    def run_website():
        st.title('Testing website')
        
        st.write('DataFrame')
        df = pd.DataFrame({ 'column 1': [0, 1, 3], 'column 2': [4, 5, 6]})
        
        st.write(df)
        st.write('Static table')
        st.table(df)

        st.write('Simple numpy dataframe')
        dataframe = np.random.randn(10, 30)
        st.dataframe(dataframe)
        
        
        

if __name__ == '__main__':
    Main.run_website()
