# 🛒 Olist E-Commerce: Business Intelligence Dashboard

<div align="center">
  
  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_URL_HERE)
  [![Python](https://img.shields.io/badge/Python-3.14-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Pandas](https://img.shields.io/badge/Pandas-2.3.3-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
  [![Plotly](https://img.shields.io/badge/Plotly-6.7.0-3f4f75.svg?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
  [![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

  *Transforming 100,000+ rows of raw relational data into actionable business strategy.*
</div>

---

## 💡 The Vision
Raw e-commerce data is often scattered across multiple SQL tables (orders, customers, payments, products). This project bridges the gap between raw data and executive decision-making. 

It is a fully interactive, end-to-end data pipeline that consolidates fragmented data into a unified, high-performance web dashboard to track real-time business metrics.

<div align="center">
  
  *(📸 Pro-Tip: Record a 10-second GIF of you clicking the filters on your dashboard and drop it here! Name the file `demo.gif` and use the code below)*
  
  `<img src="demo.gif" width="800" alt="Dashboard Demo">`
</div>

---

## 🎯 Core Business Questions Answered
This dashboard was engineered to provide immediate answers to stakeholders:
1. **Financial Health:** What is our Total Revenue and Average Order Value (AOV)?
2. **Growth Vectors:** Which specific product categories are driving the highest sales volume?
3. **Market Penetration:** Where are our most valuable customers located geographically?

---

## 🏗️ Technical Architecture & Pipeline

The project simulates a real-world ETL (Extract, Transform, Load) and Visualization workflow:

```mermaid
graph LR
    A[(SQLite DB)] -->|SQL Joins & Queries| B(Pandas)
    B -->|Feature Engineering| C{Cleaned CSV}
    C -->|Data Load| D[Streamlit App]
    D -->|Interactive UI| E((Plotly Charts))

⚙️ Under the Hood:
Data Extraction: Queried a multi-table SQLite database (olist.sqlite) containing massive datasets of Brazilian e-commerce transactions.

Data Modeling: Executed complex INNER and LEFT JOIN operations to unify order histories, product translations, and customer geography.

Feature Engineering:

Calculated Total Order Value (Price + Freight).

Isolated Delivered orders to ensure accurate revenue reporting.

Engineered time-series dimensions (Year-Month) for accurate monthly trend tracking.

Feature,Description
🎛️ Dynamic Sidebar,Filter the entire dashboard's context by specific product categories instantly.
📈 Time-Series Analysis,Responsive line charts mapping revenue trends month-over-month.
📊 Category Ranking,Horizontal bar charts automatically sorting the Top 10 revenue-generating products.
🗺️ Geographic Heatmap,State-level breakdowns showing exact customer distribution and order volume.

git clone [https://github.com/kaiffarooqui970/leipzig-ecommerce-dashboard.git](https://github.com/kaiffarooqui970/leipzig-ecommerce-dashboard.git)
cd leipzig-ecommerce-dashboard

MSc Data Science | Lancaster University Leipzig

I am a data scientist and developer currently based in Leipzig, Germany, actively seeking Working Student (Werkstudent) roles where I can leverage Python, SQL, and data visualization to solve real business problems.
