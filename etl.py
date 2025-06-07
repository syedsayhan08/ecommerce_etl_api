import pandas as pd
from datetime import datetime
from db import Sales, SessionLocal, init_db

def run_etl():
    init_db()
    df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

    # Optional: Clean or filter
    df.dropna(inplace=True)

    session = SessionLocal()

    for _, row in df.iterrows():
        sale = Sales(
            order_id=row["order_id"],
            product=row["product"],
            category=row["category"],
            quantity=row["quantity"],
            price=row["price"],
            date=row["date"]
        )
        session.add(sale)
    
    session.commit()
    session.close()
