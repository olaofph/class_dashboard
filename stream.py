import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

df["total"] = df["Quantity_Sold"] + df["Sales_Amount"]
st.title("Sales Dashboard")

st.markdown("### This is a collection of all the charts from the sales record ")
col1, col2, col3 = st.columns(3)
# with col1:
#     st.metric(label="Total Quantity Sold", value=df["Quantity_Sold"].sum())

with col2:
    st.metric(label="Total Revenue Generated", value=round(df["total"].sum()))

# with col3:
#     st.metric(label="The Most Sold Product", value=df["Product_Category"].mode()[0])
#
#
#     chart 1 chart 2 = st.columns
#
# with chart 1 create 2 columns (side by side )
#
# import pandas as pd
# import matplotlib.ticker as ticker
# import seaborn as sns
# import matplotlib.pyplot as plt
# import streamlit as st
#
#
# df["total"] = df["Quantity_Sold"] * df["Sales_Amount"]
#
# st.title("Sales Rep Dashboard")
# st.markdown("#### This is a collection of all the charts from the sales record")
#
# col1, col2 = st.columns(2)
#
# with col1:
#     fig, ax = plt.subplots()
#     quantity_by_rep = df.groupby("Sales_Rep")["Quantity_Sold"].sum()
#     quantity_by_rep.plot(kind="bar", color="green", ax=ax)
#     ax.set_ylabel("Total Quantity Sold")
#     ax.set_title("Total Quantity Sold by Sales Rep")
#     plt.xticks(rotation=50)
#     ax.ticklabel_format(style='plain', axis='y')
#     st.pyplot(fig)
#
# with col2:
#     fig, ax = plt.subplots()
#     product_category = df.groupby("Product_Category")["Sales_Amount"].sum()
#     product_category.plot(kind="bar", color="black", ax=ax)
#     ax.set_ylabel("Total Sales Amount")
#     ax.set_title("Product Category Revenue")
#     ax.ticklabel_format(style='plain', axis='y')
#     st.pyplot(fig)
# import matplotlib.pyplot as plt

# from stream import product_category


df["total"]= df["Quantity_Sold"] * df["Sales_Amount"]
st.set_page_config(page_title="Sales Dashboard")
st.title("Sales Dashboard")
st.markdown("#### This is a collection of all the charts from the sales record")
# calculating the kpis
# col1, col2, col3, = st.columns(3)

with col1:
    st.metric(label="Total Quantity Sold", value=df["Quantity_Sold"].sum())
with col2:
    st.metric(label="Total Revenue Generated", value=round(df["total"].sum()))
# with col3:
#     st.metric(label="The Most Sold Product", value=df["Product_Category"].mode()[0])

    # create two charts side by side
chart1, chart2 = st.columns(2)

# Total revenue per product category
product_revenue = df.groupby("Product_Category")["total"].sum()
with chart1:
    fig,ax = plt.subplots()
    product_revenue.plot(kind="bar", color="blue", ax=ax)
    plt.title("Total Revenue per Product")
    plt.xlabel("Products")
    plt.xticks(rotation=45)
    plt.ylabel("Total Revenue")
    st.pyplot(fig)

#Total revenue per sales rep
sales_rep_revenue= df.groupby("Sales_Rep")["total"].sum()
with chart2:
    fig, ax = plt.subplots()
    sales_rep_revenue.plot(kind="line", color="green", marker="o", ax=ax)
    plt.title("Revenue per Sales Rep")
    st.pyplot(fig)
chart3, chart4 = st.columns(2)
# Most popular payment method
payment_method = df.groupby("Payment_Method")["Payment_Method"].count()
with chart3:
    fig, ax = plt.subplots()
    payment_method.plot(kind="pie", autopct="%.2f%%")
    plt.title("Payment method Distribution")
    st.pyplot(fig)
# Sales per Region
with chart4:
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="Region", ax=ax, hue="Region")
    plt.title("Total Sales per Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    st.pyplot(fig)

st.markdown("#### Data Preview")
st.dataframe(df.head(10))
