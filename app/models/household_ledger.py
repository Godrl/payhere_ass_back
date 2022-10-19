from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class HouseholdLedger(Base):
    __tablename__ = 'household_ledger'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)        # FK: 유저 id
    money = Column(Integer, nullable=False)                                 # 금액
    content = Column(String(256), nullable=False)                           # 내용
    is_deleted = Column(Boolean, nullable=False, default=False)             # 삭제 여부
    created_at = Column(DateTime, nullable=False, server_default=func.now())  # 생성 날짜
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())  # 정보 수정 날짜

    user = relationship('User', back_populates='household_ledgers')
