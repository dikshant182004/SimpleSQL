import streamlit as st
import mysql.connector
import pandas as pd

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="your_database"
)

class data:
    def __init__(self):
        self.main()

    def main(self):
        st.markdown('<h3 style="text-align:center; font-size: 50px; font-weight: bold;">  DATA PLAYGROUND 📊</h3>',
                    unsafe_allow_html=True)
        st.markdown("---")
        # st.markdown('<h1 style="text-align:center; font-size: 30px; font-weight: bold;"> Welcome to the Data Playground! Upload your datasets to explore and analyze your data effortlessly.</h3>',
        #             unsafe_allow_html=True)

        uploaded_files = st.file_uploader("UPLOAD YOUR FILES HERE...", accept_multiple_files=True, type=['csv', 'xlsx', 'xls', 'json', 'pickle', 'txt', 'html'])
        
        if uploaded_files:
            st.subheader("Uploaded Data:")
            for uploaded_file in uploaded_files:
                file_ext = uploaded_file.name.split('.')[-1]
                if file_ext == 'csv':
                    dataframe = pd.read_csv(uploaded_file)
                    st.write(dataframe.info())
                elif file_ext == 'xlsx' or file_ext == 'xls':
                    dataframe = pd.read_excel(uploaded_file)
                elif file_ext == 'json':
                    dataframe = pd.read_json(uploaded_file)
                elif file_ext == 'pickle':
                    dataframe = pd.read_pickle(uploaded_file)
                elif file_ext == 'txt':
                    dataframe = pd.read_csv(uploaded_file, delimiter='\t')
                elif file_ext == 'html':
                    dataframe = pd.read_html(uploaded_file)
                else:
                    st.error(f"Unsupported file format: {file_ext}")
                    continue
                
                st.write(dataframe)

