import streamlit as st
import streamlit.components.v1 as components
from streamlit_player import st_player
from streamlit_option_menu import option_menu

import pandas as pd

# Custom imports 
from pages import home, fundamentals, ark_portfolio #, pr, , test, corr

st.set_page_config(
     page_title="Placeholder title",
     page_icon="",
     layout="wide",
     initial_sidebar_state="expanded",
 )

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

def main():
    # Removing and add pages
    st.markdown(hide_st_style, unsafe_allow_html=True)
    pages = {
        "Home": homepage,
        'Fundamentals': fundamental_page,
        'Cathie\'s Portfolio': cathie_portfolio,
    }

    st.sidebar.write(' ')
    with st.sidebar:
        st.title('App Navigation')
        page = option_menu("", tuple(pages.keys()), 
            menu_icon="list", default_index=0)

    pages[page]()

    with st.sidebar.expander('Version'):
        st.write('Streamlit:', st.__version__)
        st.write('Pandas:', pd.__version__)

    with st.sidebar:
        st.markdown('''Placeholder text''', )
        st.markdown('''Placeholder text''', )
    
def homepage():
    home.home()

def fundamental_page():
    fundamentals.fundamentals()

def cathie_portfolio():
    ark_portfolio.app()

if __name__ == "__main__":
    main()
