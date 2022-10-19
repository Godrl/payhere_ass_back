from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(256), nullable=False)                 # 이메일
    password = Column(String(256), nullable=False)              # 해시된 비밀번호
    created_at = Column(DateTime, nullable=False, server_default=func.now())    # 가입 날짜
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())  # 정보 수정 날짜

    household_ledgers = relationship('HouseholdLedger', cascade='all,delete-orphan', back_populates='user', uselist=True)
