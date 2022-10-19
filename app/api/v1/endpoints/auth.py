from typing import Any

from fastapi import Response, APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from app import crud
from app import schemas
from app.api import deps
from app.core.auth import (
    authenticate,
    create_access_token,
)
from app.utils import check_regex

router = APIRouter()


@router.post('/login')
def login(
    response: Response,
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> Any:
    user = authenticate(email=form_data.username, password=form_data.password, db=db)

    if not user:
        raise HTTPException(status_code=400, detail='이메일 또는 비밀번호가 일치하지 않습니다.')

    access_token = create_access_token(sub=str(user.id))
    response.set_cookie(key='access_token', value=f'Bearer {access_token}', httponly=True, samesite='strict')

    return {
        'id': user.id,
        'email': user.email,
    }


@router.post('/signup', response_model=schemas.user.User, status_code=200)
def create_user_signup(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.user.UserCreate,
) -> Any:
    if not check_regex('email', user_in.email):
        raise HTTPException(
            status_code=400,
            detail='올바른 이메일 형식이 아닙니다.',
        )

    user = crud.user.get_by_email(db=db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail='이미 가입되어 있는 이메일입니다.',
        )

    try:
        user = crud.user.create(db=db, obj_in=user_in)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail='오류가 발생했습니다. 다시 시도해주세요.')

    return user


@router.get('/logout')
def logout(
    response: Response,
) -> Any:
    response.delete_cookie(key='access_token')
    return {}
