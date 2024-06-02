import streamlit as st
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# We establish a connection to the MySQL database using SQLAlchemy's create_engine() function, passing the MySQL connection string. 

class DatabaseConnector:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def create_database(self, database_name):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                auth_plugin='mysql_native_password'
            )
            cursor = self.connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
            self.connection.commit()
            st.success(f"Database '{database_name}' created successfully!")
            cursor.close()
        except mysql.connector.Error as e:
            st.error(f"Error creating database: {e}")

    def connect_to_database(self, database_name):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=database_name,
                auth_plugin='mysql_native_password'
            )
            st.success("Connected to the database successfully!")
        except mysql.connector.Error as e:
            st.error(f"Error connecting to the database: {e}")
            self.connection = None

    def import_csv_to_table(self, table_name, dataframe,session_name):
        try:
            engine = create_engine(f'mysql+mysqlconnector://{self.user}:{self.password}@{self.host}/{session_name}')
            dataframe.to_sql(table_name,engine, if_exists='replace', index=False)

            st.success(f"Dataset imported with table name ='{table_name}' successfully!!!")
            return True

        except mysql.connector.Error as e:
            st.error(f"Error importing dataset: {e}")
            return False

class Sql_Queries:
    def __init__(self,datasets):
        self.datasets=datasets
        self.dataset_names=[]
        self.dataset_names.append(self.datasets)

    def choose_the_datasets(self):
        try:
            
            # Multi-select widget for selecting datasets
            selected_datasets = st.multiselect("Select Datasets:", self.dataset_names)

            # Display selected datasets with numbering 
            st.write("Selected Datasets:")
            for i, dataset in enumerate(selected_datasets, start=1):
                st.write(f"{i}. {dataset}")
        except:
            pass

def main():
    st.markdown('<h3 style="text-align:center; font-size: 50px; font-weight: bold;">Data Playground 📊</h3>',
                unsafe_allow_html=True)
    st.markdown("---")

    session_name = st.text_input("Enter Session Name:",help="It will be used as a Database name")
    if session_name:
        db_host = st.text_input("Enter MySQL Hostname:",help="The MySQL hostname is the address of the MySQL server that your application needs to connect to in order to access the database. If your MySQL server is running on the same machine as your application, the hostname is usually localhost")
        db_user = st.text_input("Enter MySQL Username:",help="The MySQL username is the account name used to log in to the MySQL database.For example =(root)")
        db_password = st.text_input("Enter MySQL Password:", type="password",help="password to access the database.")

        if db_host and db_user and db_password:
            db_connector = DatabaseConnector(db_host, db_user, db_password)

            # Create database
            db_connector.create_database(session_name)

            if st.button("Connect to the Database !!!"):

                # Connect to database dynamically
                db_connector.connect_to_database(session_name)

            # Upload datasets
            uploaded_files = st.file_uploader("Upload CSV Datasets:", accept_multiple_files=True, type=['csv'])
            if uploaded_files:
                st.subheader("Uploaded Data:")
                for uploaded_file in uploaded_files:
                    dataframe = pd.read_csv(uploaded_file)
                    st.write(dataframe)
                    table_name = uploaded_file.name.split('.')[0]  # Use file name as table name
                    st.write("Table Name   =  ",table_name)
                    if db_connector.import_csv_to_table(table_name,dataframe,session_name):
                        query = Sql_Queries(table_name)
                        query.choose_the_datasets()


if __name__ == "__main__":   
    main()

# pd.read_sql('SELECT int_column, date_column FROM test_data', conn)
#pandassql recently - it lets you run sql queries in python. that’s something i’ve added for myself. 
