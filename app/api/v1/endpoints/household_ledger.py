from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.household_ledger import (
    HouseholdLedger,
    HouseholdLedgerList,
    HouseholdLedgerCreate,
    HouseholdLedgerUpdate,
    HouseholdLedgerDelete,
)

router = APIRouter()


@router.get('/list', status_code=200, response_model=HouseholdLedgerList)
def get_household_ledgers(
    *,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    household_ledgers = crud.household_ledger.get_multi(db=db, user_id=current_user.id)
    total_consumption = 0
    for household_ledger in household_ledgers:
        total_consumption += household_ledger.money

    return {
        'household_ledgers': household_ledgers,
        'total_consumption': total_consumption
    }


@router.get('/detail', status_code=200, response_model=HouseholdLedger)
def get_household_ledger(
    *,
    db: Session = Depends(deps.get_db),
    household_ledger_id: int,
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    household_ledger = crud.household_ledger.get_by_user(db=db, id=household_ledger_id, user_id=current_user.id)
    if not household_ledger:
        raise HTTPException(status_code=400, detail='존재하지 않거나 본인이 작성한 가계부가 아닙니다.')

    return household_ledger


@router.post('/create', status_code=200, response_model=HouseholdLedger)
def create_household_ledger(
    *,
    household_ledger_in: HouseholdLedgerCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    HouseholdLedgerCreate.user_id = current_user.id
    try:
        household_ledger = crud.household_ledger.create(db=db, obj_in=household_ledger_in)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail='오류가 발생했습니다. 다시 시도해주세요.')

    return household_ledger


@router.post('/update', status_code=200, response_model=HouseholdLedger, dependencies=[Depends(deps.get_current_user)])
def update_household_ledger(
    *,
    household_ledger_in: HouseholdLedgerUpdate,
    db: Session = Depends(deps.get_db),
) -> dict:
    household_ledger = crud.household_ledger.get(db, id=household_ledger_in.id)
    if not household_ledger:
        raise HTTPException(status_code=400, detail='존재하지 않는 가계부 입니다.')

    try:
        updated_household_ledger = crud.household_ledger\
            .update(db=db, db_obj=household_ledger, obj_in=household_ledger_in)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail='오류가 발생했습니다. 다시 시도해주세요.')

    return updated_household_ledger


@router.post('/delete', status_code=200, response_model=HouseholdLedger, dependencies=[Depends(deps.get_current_user)])
def delete_household_ledger(
    *,
    household_ledger_in: HouseholdLedgerDelete,
    db: Session = Depends(deps.get_db),
) -> dict:
    household_ledger = crud.household_ledger.get(db, id=household_ledger_in.id)
    if not household_ledger:
        raise HTTPException(status_code=400, detail='존재하지 않는 가계부 입니다.')

    try:
        updated_household_ledger = crud.household_ledger\
            .update(db=db, db_obj=household_ledger, obj_in=household_ledger_in)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail='오류가 발생했습니다. 다시 시도해주세요.')

    return updated_household_ledger
