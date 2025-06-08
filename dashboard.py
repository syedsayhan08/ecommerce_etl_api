import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime

# Load data from SQLite
@st.cache_data
def load_data():
    conn = sqlite3.connect("sales.db")
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

st.set_page_config(page_title="📊 E-Commerce Dashboard", layout="wide")
st.title("📊 E-Commerce Sales Dashboard")

st.markdown("Get insights from daily uploaded sales CSV files.")

# Date filter
min_date = df['date'].min()
max_date = df['date'].max()
date_range = st.date_input("📅 Filter by Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

if date_range:
    df = df[(df['date'] >= pd.to_datetime(date_range[0])) & (df['date'] <= pd.to_datetime(date_range[1]))]

# Row 1: Total Sales and Quantity
col1, col2 = st.columns(2)
with col1:
    total_sales = (df["quantity"] * df["price"]).sum()
    st.metric("💰 Total Revenue", f"${total_sales:,.2f}")

with col2:
    total_qty = df["quantity"].sum()
    st.metric("📦 Total Quantity Sold", f"{total_qty:,}")

# Row 2: Revenue Over Time
fig1 = px.line(df.groupby('date').agg({"quantity": "sum", "price": "mean"}).reset_index(),
               x="date", y="quantity", title="📈 Quantity Sold Over Time")
st.plotly_chart(fig1, use_container_width=True)

# Row 3: Top Products
top_products = df.groupby("product")["quantity"].sum().nlargest(5).reset_index()
fig2 = px.bar(top_products, x="product", y="quantity", title="🏆 Top 5 Products by Quantity Sold",
              color="product", text="quantity")
st.plotly_chart(fig2, use_container_width=True)

# Row 4: Sales by Category
category_sales = df.groupby("category").agg({"quantity": "sum"}).reset_index()
fig3 = px.pie(category_sales, names="category", values="quantity", title="📊 Sales Distribution by Category")
st.plotly_chart(fig3, use_container_width=True)

# Row 5: Daily Revenue
df['revenue'] = df['quantity'] * df['price']
fig4 = px.area(df, x="date", y="revenue", title="📆 Daily Revenue Trend", color_discrete_sequence=["green"])
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Plotly")
