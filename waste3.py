# drag_and_drop_component.py
import streamlit as st
import streamlit.components.v1 as components

def load_html():
    with open("first.html", "r") as file:
        return file.read()

def main():
    st.title("Streamlit Drag and Drop Example")

    # Load the HTML file
    html_content = load_html()

    # Render the HTML file in Streamlit
    components.html(html_content, height=500)

if __name__ == "__main__":
    main()
