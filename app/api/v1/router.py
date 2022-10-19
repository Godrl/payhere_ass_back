from fastapi import APIRouter

from app.api.v1.endpoints import auth, household_ledger

api_v1_router = APIRouter()

api_v1_router.include_router(auth.router, prefix='/auth', tags=['auth'])
api_v1_router.include_router(household_ledger.router, prefix='/household_ledger', tags=['household_ledger'])
