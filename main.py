from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from db import SessionLocal, Sales
from sqlalchemy import func
import shutil
import os

app = FastAPI(title="E-Commerce BI ETL API")

# Optional: Allow CORS if frontend is hosted separately (like localhost:3000 or via file://)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)
    file_path = os.path.join(data_folder, "sales_data.csv")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "CSV uploaded successfully!"}
