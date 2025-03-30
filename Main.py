import streamlit as st
from intro import main as intro_main
from about_us import main as about_us_main
from amrtrend import main as amrtrend_main
from association_query import main as association_query_main
from association import main as association_main
from dataset_vis import main as dataset_vis_main

# Set the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="My App", layout="wide")

# Function to update the query parameter for navigation
def set_query_params(page):
    query_params = {"page": page}
    st.set_query_params(**query_params)

# Get the current page from the query parameters
query_params = st.query_params
current_page = query_params.get("page", "Introduction")[0:]

# Debugging: Print the current page to the console
print(f"Current page from query parameters: {current_page}")

# Sidebar navigation with hyperlinks
st.sidebar.title("Navigation")
st.sidebar.markdown(
    """
    <style>
    
    /* Change the sidebar background color */
    [data-testid="stSidebar"] {
        background-color: #355E3B; /* Replace with your desired color */
        color: white; /* Change text color to white for better contrast */
    }
    
    .sidebar-link {
        display: block;
        padding: 10px;
        margin: 5px 0;
        background-color: #f0f0f0;
        border-radius: 5px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
    .sidebar-link:hover {
        background-color: #d0d0d0;
    }
    .sidebar-link::after {
        content: " →"; /* Add an arrow symbol */
        font-size: 18px; /* Make the arrow larger */
        font-weight: bold; /* Make the arrow bold */
        color: #000; /* Set the arrow color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render navigation links
st.sidebar.markdown(f'<a class="sidebar-link" href="?page=Introduction">Home</a>', unsafe_allow_html=True)
st.sidebar.markdown(f'<a class="sidebar-link" href="?page=Dataset Visualization">Dataset Visualization</a>', unsafe_allow_html=True)
st.sidebar.markdown(f'<a class="sidebar-link" href="?page=AMR Trend">AMR Trend</a>', unsafe_allow_html=True)
st.sidebar.markdown(f'<a class="sidebar-link" href="?page=Association">Association</a>', unsafe_allow_html=True)
st.sidebar.markdown(f'<a class="sidebar-link" href="?page=Association Query">Association Query</a>', unsafe_allow_html=True)
st.sidebar.markdown(f'<a class="sidebar-link" href="?page=About Us">About Us</a>', unsafe_allow_html=True)

# Load the selected page
try:
    if current_page == "Introduction":
        intro_main()
    elif current_page == "About Us":
        about_us_main()
    elif current_page == "AMR Trend":
        amrtrend_main()
    elif current_page == "Association Query":
        association_query_main()
    elif current_page == "Association":
        association_main()
    elif current_page == "Dataset Visualization":
        dataset_vis_main()
    else:
        st.error(f"Page not found! Current page: {current_page}")
except Exception as e:
    st.error(f"An error occurred while loading the page: {e}")
    print(f"Error: {e}")