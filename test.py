

# import streamlit as st
# import pandas as pd
# import datetime as dt
# import matplotlib.pyplot as plt

# # Set page configuration
# st.set_page_config(
#     page_title="Sales Dashboard",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Navbar
# st.markdown(
#     """
#     <style>
#     .navbar {
#         background-color: #004466;
#         padding: 10px;
#         text-align: center;
#         color: white;
#         font-size: 24px;
#         font-weight: bold;
#     }
#     </style>
#     <div class="navbar">Sales Dashboard</div>
#     """,
#     unsafe_allow_html=True
# )

# # Welcome message
# current_time = dt.datetime.now()
# st.write(f"## Welcome, Dhruv! Today's date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')} \n")

# # Sidebar menu
# menu = st.sidebar.radio("Menu", ("Home", "Insights", "Forecast"))
# chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Plot", "Bar Chart"])

# # File upload section
# st.sidebar.subheader("Upload Your Dataset")
# if menu == "Insights":
#     insights_file = st.sidebar.file_uploader("Upload dataset for insights (CSV format)", type=["csv"])
#     if insights_file is not None:
#         insights_data = pd.read_csv(insights_file)
#         st.sidebar.success("Dataset uploaded successfully!")
        
#         # Check required columns
#         required_columns = ['Month', 'Overall Sales', 'Product_1_sales', 'Product_2_sales', 'Product_3_sales', 'Product_4_sales', 'Product_5_sales']
#         if not all(col in insights_data.columns for col in required_columns):
#             st.sidebar.error("Uploaded dataset is missing required columns.")
#             insights_data = None
#     else:
#         st.sidebar.warning("Please upload a dataset to display insights.")

# if menu == "Forecast":
#     forecast_file = st.sidebar.file_uploader("Upload dataset for forecasting (CSV format)", type=["csv"])
#     if forecast_file is not None:
#         forecast_data = pd.read_csv(forecast_file)
#         st.sidebar.success("Dataset uploaded successfully!")
        
#         # Check required columns
#         required_columns_forecast = ['Day', 'Last 7 Days Sales', 'Forecast Next 3 Days']
#         if not all(col in forecast_data.columns for col in required_columns_forecast):
#             st.sidebar.error("Uploaded dataset is missing required columns.")
#             forecast_data = None
#     else:
#         st.sidebar.warning("Please upload a dataset to display forecasting.")

# # Insights
# if menu == "Insights" and insights_file is not None and insights_data is not None:
#     st.subheader("Overall Sales Insights")

#     months = insights_data['Month']
#     overall_sales = insights_data['Overall Sales']
#     product_sales_columns = [col for col in insights_data.columns if col.startswith('Product_')]

#     if chart_type == "Bar Chart":
#         fig, ax = plt.subplots(figsize=(10, 6))
#         ax.bar(months, overall_sales, label='Overall Sales', color='skyblue')
#         for product_col in product_sales_columns:
#             ax.bar(months, insights_data[product_col], label=product_col.replace('_', ' '), alpha=0.7)

#         ax.set_title("Monthly Sales Data", fontsize=16)
#         ax.set_xlabel("Months")
#         ax.set_ylabel("Sales")
#         ax.legend()

#         st.pyplot(fig)

#     elif chart_type == "Line Plot":
#         fig, ax = plt.subplots(figsize=(10, 6))
#         ax.plot(months, overall_sales, label='Overall Sales', marker='o', color='skyblue')
#         for product_col in product_sales_columns:
#             ax.plot(months, insights_data[product_col], label=product_col.replace('_', ' '), marker='o')

#         ax.set_title("Monthly Sales Data", fontsize=16)
#         ax.set_xlabel("Months")
#         ax.set_ylabel("Sales")
#         ax.legend()

#         st.pyplot(fig)

# # Forecast
# elif menu == "Forecast" and forecast_file is not None and forecast_data is not None:
#     st.subheader("Sales Forecast")

#     days = forecast_data['Day']
#     last_7_days_sales = forecast_data['Last 7 Days Sales']
#     forecast_next_3_days = forecast_data['Forecast Next 3 Days']

#     if chart_type == "Bar Chart":
#         fig, ax = plt.subplots(figsize=(10, 6))
#         ax.bar(days[:7], last_7_days_sales[:7], label='Last 7 Days Sales', color='blue')
#         ax.bar(days[7:], forecast_next_3_days[:3], label='Forecast (Next 3 Days)', color='red', alpha=0.7)
        
#         ax.set_title("Sales Forecast", fontsize=16)
#         ax.set_xlabel("Days")
#         ax.set_ylabel("Sales")
#         ax.legend()

#         st.pyplot(fig)

#     elif chart_type == "Line Plot":
#         fig, ax = plt.subplots(figsize=(10, 6))
#         ax.plot(days[:7], last_7_days_sales[:7], label='Last 7 Days Sales', marker='o', color='blue')
#         ax.plot(days[7:], forecast_next_3_days[:3], label='Forecast (Next 3 Days)', marker='o', color='red', linestyle='--')
        
#         ax.set_title("Sales Forecast", fontsize=16)
#         ax.set_xlabel("Days")
#         ax.set_ylabel("Sales")
#         ax.legend()

#         st.pyplot(fig)

# # Home
# elif menu == "Home":
#     st.subheader("Welcome to the Sales Dashboard")
#     st.write("Use the menu on the left to navigate through the dashboard.")



import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Navbar
st.markdown(
    """
    <style>
    .navbar {
        background-color: #004466;
        padding: 10px;
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    <div class="navbar">Sales Dashboard</div>
    """,
    unsafe_allow_html=True
)

# Welcome message
current_time = dt.datetime.now()
st.write(f"## Welcome, Dhruv! Today's date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')} \n")

# Sidebar menu
menu = st.sidebar.radio("Menu", ("Home", "Insights", "Forecast"))
chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Plot", "Bar Chart"])

# File upload section
st.sidebar.subheader("Upload Your Dataset")
if menu == "Insights":
    insights_file = st.sidebar.file_uploader("Upload dataset for insights (CSV format)", type=["csv"])
    if insights_file is not None:
        insights_data = pd.read_csv(insights_file)
        st.sidebar.success("Dataset uploaded successfully!")
        
        # Check required columns
        required_columns = ['Month', 'Overall Sales', 'Product_1_sales', 'Product_2_sales', 'Product_3_sales', 'Product_4_sales', 'Product_5_sales']
        if not all(col in insights_data.columns for col in required_columns):
            st.sidebar.error("Uploaded dataset is missing required columns.")
            insights_data = None
    else:
        st.sidebar.warning("Please upload a dataset to display insights.")

if menu == "Forecast":
    forecast_file = st.sidebar.file_uploader("Upload dataset for forecasting (CSV format)", type=["csv"])
    if forecast_file is not None:
        forecast_data = pd.read_csv(forecast_file)
        st.sidebar.success("Dataset uploaded successfully!")
        
        # Check required columns
        required_columns_forecast = ['Day', 'Last 7 Days Sales', 'Forecast Next 3 Days']
        if not all(col in forecast_data.columns for col in required_columns_forecast):
            st.sidebar.error("Uploaded dataset is missing required columns.")
            forecast_data = None
    else:
        st.sidebar.warning("Please upload a dataset to display forecasting.")

# Insights
if menu == "Insights" and insights_file is not None and insights_data is not None:
    st.subheader("Overall Sales Insights")

    months = insights_data['Month']
    overall_sales = insights_data['Overall Sales']
    product_sales_columns = [col for col in insights_data.columns if col.startswith('Product_')]

    if chart_type == "Bar Chart":
        fig, ax = plt.subplots(figsize=(10, 6))
        bottom = [0] * len(months)  # Initialize bottom for stacking bars

        # Stacked bar chart for each product
        for product_col in product_sales_columns:
            ax.bar(months, insights_data[product_col], label=product_col.replace('_', ' '), bottom=bottom)
            bottom = [i + j for i, j in zip(bottom, insights_data[product_col])]

        ax.set_title("Monthly Sales Data (Stacked by Product)", fontsize=16)
        ax.set_xlabel("Months")
        ax.set_ylabel("Sales")
        ax.legend()

        st.pyplot(fig)

    elif chart_type == "Line Plot":
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(months, overall_sales, label='Overall Sales', marker='o', color='skyblue')
        for product_col in product_sales_columns:
            ax.plot(months, insights_data[product_col], label=product_col.replace('_', ' '), marker='o')

        ax.set_title("Monthly Sales Data", fontsize=16)
        ax.set_xlabel("Months")
        ax.set_ylabel("Sales")
        ax.legend()

        st.pyplot(fig)

# Forecast
elif menu == "Forecast" and forecast_file is not None and forecast_data is not None:
    st.subheader("Sales Forecast")

    days = forecast_data['Day']
    last_7_days_sales = forecast_data['Last 7 Days Sales']
    forecast_next_3_days = forecast_data['Forecast Next 3 Days']

    if chart_type == "Bar Chart":
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(days[:7], last_7_days_sales[:7], label='Last 7 Days Sales', color='blue')
        ax.bar(days[7:], forecast_next_3_days[:3], label='Forecast (Next 3 Days)', color='red', alpha=0.7)
        
        ax.set_title("Sales Forecast", fontsize=16)
        ax.set_xlabel("Days")
        ax.set_ylabel("Sales")
        ax.legend()

        st.pyplot(fig)

    elif chart_type == "Line Plot":
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(days[:7], last_7_days_sales[:7], label='Last 7 Days Sales', marker='o', color='blue')
        ax.plot(days[7:], forecast_next_3_days[:3], label='Forecast (Next 3 Days)', marker='o', color='red', linestyle='--')
        
        ax.set_title("Sales Forecast", fontsize=16)
        ax.set_xlabel("Days")
        ax.set_ylabel("Sales")
        ax.legend()

        st.pyplot(fig)

# Home
elif menu == "Home":
    st.subheader("Welcome to the Sales Dashboard")
    st.write("Use the menu on the left to navigate through the dashboard.")
