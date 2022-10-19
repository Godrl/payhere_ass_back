from pydantic import BaseModel
from typing import Optional, Sequence
from datetime import datetime
from . import user


class HouseholdLedgerBase(BaseModel):
    id: int


class HouseholdLedgerCreate(HouseholdLedgerBase):
    user_id: int
    money: int
    content: Optional[str] = None


class HouseholdLedgerUpdate(HouseholdLedgerBase):
    money: int
    content: Optional[str] = None
    pass


class HouseholdLedgerDelete(BaseModel):
    id: int
    is_deleted: bool


# Properties shared by models stored in DB
class HouseholdLedgerInDBBase(HouseholdLedgerBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Properties to return to client
class HouseholdLedger(HouseholdLedgerInDBBase):
    content: str
    created_at: datetime
    user: user.User
    pass


# Properties properties stored in DB
class HouseholdLedgerInDB(HouseholdLedgerInDBBase):
    pass


class HouseholdLedgerList(BaseModel):
    household_ledgers: Sequence[HouseholdLedger]
    total_consumption: int
