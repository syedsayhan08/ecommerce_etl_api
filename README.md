# 📦 ecommerce_etl_api

A complete ETL pipeline using **FastAPI**, **SQLite**, and **Streamlit** for visualizing e-commerce sales data.

---

## 📁 Folder Structure

```
ecommerce_etl_api/
├── data/
│   └── sales_data.csv            # Upload your daily CSV here
├── templates/
│   └── index.html                # Upload UI
├── db.py                         # SQLAlchemy models & DB setup
├── etl.py                        # One-time ETL load
├── etl_job.py                    # Daily ETL loop (while + sleep)
├── main.py                       # FastAPI app with API endpoints
├── dashboard.py                  # Streamlit dashboard
├── requirements.txt              # Dependencies
├── README.md                     # You're here
```

---

## 🔄 ETL Process Flow

```
Upload CSV → Load with Pandas → Transform (clean) → Load into SQLite → View with FastAPI or Streamlit
```

---

## ⚙️ Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Prepare Your CSV Data

Place your daily `sales_data.csv` file inside the `data/` folder.

---

## 🚀 Run Components

### 🔁 Run ETL (One-Time)

```bash
python etl.py
```

### 🔂 Run Daily ETL with While Loop

```bash
python etl_job.py
```

To keep it running in background (Linux/Mac):

```bash
nohup python etl_job.py &
```

---

## ⚡ FastAPI Server

### Start FastAPI

```bash
uvicorn main:app --reload
```

Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### ✨ FastAPI Endpoints

| Method | Endpoint        | Description             |
|--------|------------------|--------------------------|
| GET    | `/`              | API welcome message      |
| GET    | `/total_sales`   | Total revenue            |
| GET    | `/top_products`  | Top 3 best-selling items |
| GET    | `/daily_revenue` | Revenue over time        |

---

## 🧾 Upload New CSV via Web Form

Run the FastAPI server and visit:

```
http://127.0.0.1:8000
```

Use the form to upload new CSV files each day. The uploaded file will replace the existing one in `data/sales_data.csv`.

---

## 📊 Streamlit Dashboard

### Run the Dashboard

```bash
streamlit run dashboard.py
```

### 📈 Included Visuals

1. **💰 Total Revenue & Quantity** – Metric widgets
2. **📈 Quantity Sold Over Time** – Line Chart
3. **🏆 Top 5 Products** – Bar Chart
4. **📊 Sales by Category** – Pie Chart
5. **📆 Daily Revenue Trend** – Area Chart

### Screenshot

*(Optional: You can add a screenshot of your dashboard here)*

---

## 🧰 Tech Stack

- Python
- FastAPI
- SQLite (via SQLAlchemy)
- Streamlit
- Pandas
- Plotly
- HTML (Jinja for upload form)

---

## ✅ To Do

- [x] Upload daily CSV files
- [x] Run ETL manually or daily
- [x] View stats with API
- [x] Visualize data on dashboard

---

## 💡 Tip

Keep `etl_job.py` running daily to always have the latest data for your dashboard and API.

---

## 👋 Author

Built for academic and portfolio learning.
