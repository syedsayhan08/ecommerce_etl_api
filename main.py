from fastapi import FastAPI
from db import SessionLocal, Sales
from sqlalchemy import func

app = FastAPI(title="E-Commerce BI ETL API")

@app.get("/")
def read_root():
    return {"message": "E-Commerce ETL BI API is live!"}

@app.get("/total_sales")
def total_sales():
    db = SessionLocal()
    total = db.query(func.sum(Sales.quantity * Sales.price)).scalar()
    db.close()
    return {"total_sales": total}

@app.get("/top_products")
def top_products():
    db = SessionLocal()
    result = db.query(Sales.product, func.sum(Sales.quantity).label("total_qty"))\
        .group_by(Sales.product).order_by(func.sum(Sales.quantity).desc()).limit(3).all()
    db.close()
    return [{"product": r[0], "quantity_sold": r[1]} for r in result]

@app.get("/daily_revenue")
def daily_revenue():
    db = SessionLocal()
    result = db.query(Sales.date, func.sum(Sales.quantity * Sales.price).label("revenue"))\
        .group_by(Sales.date).order_by(Sales.date).all()
    db.close()
    return [{"date": r[0], "revenue": r[1]} for r in result]
