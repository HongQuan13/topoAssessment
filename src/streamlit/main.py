import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_data_from_api(endpoint, params=None):
    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None


st.title("FastAPI Data Visualization")

api_url = "http://127.0.0.1:8000/api/data"

data_type = st.selectbox("Select Data Type", ["ALL", "CSV", "PPTX", "PDF", "JSON"])

if data_type == "ALL":
    data = get_data_from_api(f"{api_url}")
    if data:
        st.write(data)

elif data_type == "CSV":
    data = get_data_from_api(f"{api_url}/csv")
    df = pd.json_normalize(data["data"])
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y", errors="coerce")
    st.dataframe(df)

    # Visualization 1: Total Revenue by Activity (Bar Chart)
    st.subheader("Total Revenue by Activity")

    # Group by activity and sum the revenue
    activity_revenue = df.groupby("activity")["revenue"].sum().reset_index()

    # Bar chart of revenue by activity
    sns.barplot(x="activity", y="revenue", data=activity_revenue)
    plt.title("Total Revenue by Activity")
    plt.xticks(rotation=45)
    st.pyplot()

    # Visualization 2: Revenue Over Time (Line Graph)
    st.subheader("Revenue Over Time")

    # Group by date and sum the revenue for each day
    daily_revenue = df.groupby("date")["revenue"].sum().reset_index()

    # Line plot of revenue over time
    sns.lineplot(x="date", y="revenue", data=daily_revenue)
    plt.title("Revenue Over Time")
    plt.xticks(rotation=45)
    st.pyplot()

    st.subheader("Raw Data")
    st.write(data)

elif data_type == "PPTX":
    data = get_data_from_api(f"{api_url}/pptx")
    # Display page 1 - Annual Summary
    st.subheader(data["data"]["page_1"]["text"])

    # Display page 2 - Quarterly Metrics Table
    st.subheader("Quarterly Metrics")
    quarterly_metrics_df = pd.DataFrame(data["data"]["page_2"]["table"])
    st.dataframe(quarterly_metrics_df)

    # Visualization 1: Bar chart of Revenue by Quarter
    st.subheader("Revenue by Quarter")
    sns.barplot(x="Quarter", y="Revenue (in $)", data=quarterly_metrics_df)
    plt.title("Revenue per Quarter")
    st.pyplot()

    st.subheader(data["data"]["page_3"]["text"])

    st.subheader("Raw Data")
    st.write(data)

elif data_type == "PDF":
    data = get_data_from_api(f"{api_url}/pdf")
    data = data["data"]

    # Display the text from page_1
    st.subheader(data["page_1"]["text"])

    # Convert the table data into a pandas DataFrame
    df = pd.DataFrame(data["page_1"]["table"])

    # Display the table in Streamlit
    df["Year"] = pd.to_datetime(df["Year"], format="%Y", errors="coerce")
    st.subheader("Quarterly Metrics")
    st.dataframe(df)

    # Visualization 1: Bar chart of Revenue by Quarter
    st.subheader("Revenue by Quarter (Bar Chart)")

    # Plotting a bar chart for Revenue per Quarter
    sns.barplot(x="Quarter", y="Revenue (in $)", data=df, palette="Blues_d")
    plt.title("Revenue per Quarter")
    plt.ylabel("Revenue (in $)")
    st.pyplot()

    # Visualization 2: Line chart of Revenue Over Time
    st.subheader("Revenue Over Time (Line Chart)")

    # Plotting a line chart for Revenue Over Time
    sns.lineplot(x="Quarter", y="Revenue (in $)", data=df, marker="o", color="blue")
    plt.title("Revenue Over Time")
    plt.ylabel("Revenue (in $)")
    st.pyplot()

    st.subheader("Raw Data")
    st.write(data)

elif data_type == "JSON":

    st.subheader("Company and Employee Data Visualization")

    data = get_data_from_api(f"{api_url}/json")
    companies_df = pd.json_normalize(data["data"]["companies"])
    employees_df = pd.json_normalize(data["data"]["employees"])

    # Display the company data
    st.subheader("Company Information")
    st.dataframe(companies_df)

    # Display employee data
    employees_df["hired_date"] = pd.to_datetime(
        employees_df["hired_date"], format="%d-%m-%Y", errors="coerce"
    )
    st.subheader("Employee Information")
    st.dataframe(employees_df)

    # Visualization: Salary Distribution for the selected company
    company_selection = st.selectbox("Select Company", companies_df["name"].unique())
    filtered_employee_df = employees_df[
        employees_df["company_name"] == company_selection
    ]

    st.subheader(f"Salary Distribution for Employees in {company_selection}")

    if not filtered_employee_df.empty:
        sns.barplot(x="name", y="salary", data=filtered_employee_df)
        plt.title(f"Salary Distribution in {company_selection}")
        plt.xticks(rotation=90)
        st.pyplot()
    else:
        st.write("No employees found for this company.")

    st.subheader("Raw Data")
    st.write(data)
