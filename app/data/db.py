from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PriceBar(Base):
    __tablename__ = 'price_bars'

    id = Column(Integer, primary_key=True)
    ticker = Column(String, nullable=False)
    trade_date = Column(Date, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

DATABASE_URL = "sqlite:///market_data.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)


