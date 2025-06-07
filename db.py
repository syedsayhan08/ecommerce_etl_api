from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///ecommerce.db")
SessionLocal = sessionmaker(bind=engine)

class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    product = Column(String)
    category = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    date = Column(Date)

def init_db():
    Base.metadata.create_all(bind=engine)
