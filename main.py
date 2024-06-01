import streamlit as st
import Data_interaction as di
import json
import streamlit.components.v1 as com
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="INSIGHTHUB",
    page_icon=":Worldwide_Exploration:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.markdown("""
<style>
.stDeployButton
{
    visibility:hidden;
}       
</style>
""",unsafe_allow_html=True)

# just to denote the analysis process
with st.sidebar:
    with open("animation.json", encoding='utf-8') as source:
        animation=json.load(source)
        temp=st_lottie(animation,width=290,height=187,quality="medium",)

st.sidebar.success("**Lets Take a Tour !!!**")
with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=["Home","data interaction"],
        default_index=0,
        menu_icon="cast"
    )

if selected == "Home":
    st.markdown('Home')
elif selected =="data interaction":
    data=di.data()