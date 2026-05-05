from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    path = Column(String)
    status = Column(String)
