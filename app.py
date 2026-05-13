import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="E-Commerce KPI Dashboard", layout="wide")
st.title("📊 E-Commerce Business Performance Dashboard")
st.markdown("Analyzing total revenue, order volume, and top-performing product categories.")

# 2. Load Data Directly from the SQLite Database
# The @st.cache_data decorator ensures it only runs this heavy query once!
@st.cache_data
def load_data():
    # Because the database is in the exact same folder as app.py, 
    # we don't need a long messy file path. Just the file name!
    conn = sqlite3.connect('olist.sqlite 2')
    
    # Extract tables
    orders = pd.read_sql_query("SELECT * FROM orders", conn)
    items = pd.read_sql_query("SELECT * FROM order_items", conn)
    customers = pd.read_sql_query("SELECT * FROM customers", conn)
    products = pd.read_sql_query("SELECT * FROM products", conn)
    translations = pd.read_sql_query("SELECT * FROM product_category_name_translation", conn)
    conn.close()

    # Merge tables
    master_df = pd.merge(orders, items, on='order_id', how='inner')
    master_df = pd.merge(master_df, customers, on='customer_id', how='inner')
    master_df = pd.merge(master_df, products, on='product_id', how='inner')
    master_df = pd.merge(master_df, translations, on='product_category_name', how='left')

    # Feature Engineering
    master_df['total_order_value'] = master_df['price'] + master_df['freight_value']
    master_df['order_purchase_timestamp'] = pd.to_datetime(master_df['order_purchase_timestamp'])
    master_df['year_month'] = master_df['order_purchase_timestamp'].dt.to_period('M').astype(str)
    
    # Keep only delivered orders
    master_df = master_df[master_df['order_status'] == 'delivered']
    
    return master_df

# Show a loading spinner while the database connects
with st.spinner('Connecting to Database & Crunching Numbers...'):
    df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Data")
categories = df['product_category_name_english'].dropna().unique().tolist()
categories.sort()

selected_category = st.sidebar.selectbox("Select Product Category", ["All"] + categories)

if selected_category != "All":
    filtered_df = df[df['product_category_name_english'] == selected_category]
else:
    filtered_df = df

# 4. Calculate Core KPIs
total_revenue = filtered_df['total_order_value'].sum()
total_orders = filtered_df['order_id'].nunique()
aov = total_revenue / total_orders if total_orders > 0 else 0 

# 5. Render KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
with col2:
    st.metric(label="Total Orders", value=f"{total_orders:,}")
with col3:
    st.metric(label="Average Order Value (AOV)", value=f"${aov:,.2f}")

st.markdown("---")

# 6. Build the Visualizations
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Revenue Trend by Month")
    trend_data = filtered_df.groupby('year_month')['total_order_value'].sum().reset_index()
    fig_trend = px.line(
        trend_data, 
        x='year_month', 
        y='total_order_value', 
        markers=True,
        labels={'year_month': 'Month', 'total_order_value': 'Revenue ($)'}
    )
    st.plotly_chart(fig_trend, use_container_width=True)

with col_chart2:
    if selected_category == "All":
        st.subheader("Top 10 Categories by Revenue")
        top_cats = filtered_df.groupby('product_category_name_english')['total_order_value'].sum().reset_index()
        top_cats = top_cats.sort_values('total_order_value', ascending=False).head(10)
        
        fig_bar = px.bar(
            top_cats, 
            x='total_order_value', 
            y='product_category_name_english', 
            orientation='h',
            labels={'product_category_name_english': 'Category', 'total_order_value': 'Revenue ($)'}
        )
        fig_bar.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        # If a specific category is selected, show where those customers live!
        st.subheader("Geographic Distribution")
        st.markdown(f"Showing state-level performance for **{selected_category}**")
        geo_data = filtered_df.groupby('customer_state')['order_id'].nunique().reset_index()
        fig_geo = px.bar(
            geo_data.sort_values('order_id', ascending=False).head(10),
            x='customer_state',
            y='order_id',
            labels={'customer_state': 'State', 'order_id': 'Total Orders'}
        )
        st.plotly_chart(fig_geo, use_container_width=True)