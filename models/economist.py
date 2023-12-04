from datetime import datetime

from sqlalchemy import Column, Integer, String, Date

from utils.database import Base


class EconomistModel(Base):
    __tablename__ = "EconomistNews"

    __table_args__ = (
        {"mysql_engine": "Aria"},
    )

    id = Column(Integer, autoincrement=True, primary_key=True)
    Date_added = Column(Date, default=(datetime.utcnow()))
    Headline = Column(String, unique=False, nullable=False) 
    Description = Column(String, unique=False, nullable=False) 
    Body = Column(String, unique=False, nullable=False) 
    Image = Column(String, unique=False, nullable=False) 
    URL = Column(String, unique=False, nullable=False) 
    Date = Column(Date, unique=False, nullable=True) 
