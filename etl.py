import pandas as pd
from datetime import datetime
from db import Sales, SessionLocal, init_db
from sqlalchemy.exc import SQLAlchemyError

def run_etl():
    print(f"📦 Running ETL at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Initialize database and create tables
    init_db()

    # Extract
    df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])
    
    # Transform: clean the data
    df.dropna(inplace=True)

    # Load
    session = SessionLocal()
    inserted_count = 0

    try:
        for _, row in df.iterrows():
            # Prevent duplicate entries by checking order_id
            existing = session.query(Sales).filter_by(order_id=row["order_id"]).first()
            if existing:
                continue

            sale = Sales(
                order_id=row["order_id"],
                product=row["product"],
                category=row["category"],
                quantity=row["quantity"],
                price=row["price"],
                date=row["date"]
            )
            session.add(sale)
            inserted_count += 1

        session.commit()
        print(f"✅ ETL complete. {inserted_count} new records inserted.\n")

    except SQLAlchemyError as e:
        print("❌ Error during ETL:", e)
        session.rollback()

    finally:
        session.close()
