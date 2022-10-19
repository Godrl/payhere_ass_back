from typing import List, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.household_ledger import HouseholdLedger
from app.schemas.household_ledger import HouseholdLedgerCreate, HouseholdLedgerUpdate


class CRUDHouseholdLedger(CRUDBase[HouseholdLedger, HouseholdLedgerCreate, HouseholdLedgerUpdate]):
    def get_total_count(self, db: Session) -> int:
        return db.query(HouseholdLedger).count()

    def get_multi(
        self, db: Session, *, user_id: int = 0, skip: int = 0, limit: int = 5000
    ) -> List[HouseholdLedger]:
        return (
            db.query(HouseholdLedger).filter(HouseholdLedger.user_id == user_id).offset(skip).limit(limit).all()
        )

    def create(self, db: Session, *, obj_in: HouseholdLedgerCreate) -> HouseholdLedger:
        db_obj = HouseholdLedger(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        return db_obj

    def get_by_user(self, db: Session, *, id: int, user_id: int) -> Optional[HouseholdLedger]:
        return db.query(HouseholdLedger).filter(HouseholdLedger.id == id, HouseholdLedger.user_id == user_id).first()


household_ledger = CRUDHouseholdLedger(HouseholdLedger)
