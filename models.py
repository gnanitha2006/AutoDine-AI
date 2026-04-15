"""
Database models for AutoDine AI.

Tables:
  - inventory: tracks stock levels per ingredient
  - orders:    historical daily order counts per menu item
  - waste:     daily waste records per ingredient
  - forecasts: AI-generated demand predictions
"""
from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.sql import func
from database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    category = Column(String, nullable=False)          # e.g. Produce, Dairy, Meat
    current_stock = Column(Float, nullable=False)      # in kg or units
    unit = Column(String, default="kg")
    reorder_threshold = Column(Float, nullable=False)  # alert below this level
    max_capacity = Column(Float, nullable=False)
    cost_per_unit = Column(Float, nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(Date, nullable=False)
    menu_item = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    revenue = Column(Float, nullable=False)


class Waste(Base):
    __tablename__ = "waste"

    id = Column(Integer, primary_key=True, index=True)
    waste_date = Column(Date, nullable=False)
    item_name = Column(String, nullable=False)
    quantity_wasted = Column(Float, nullable=False)    # in kg
    reason = Column(String, nullable=False)            # Expired, Overcooked, Spoiled
    estimated_cost = Column(Float, nullable=False)


class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True, index=True)
    menu_item = Column(String, nullable=False)
    forecast_date = Column(Date, nullable=False)
    predicted_quantity = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)         # 0.0 – 1.0
    created_at = Column(DateTime, server_default=func.now())
