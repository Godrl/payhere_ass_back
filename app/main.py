from pathlib import Path

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_v1_router
from app.core.config import settings

BASE_PATH = Path(__file__).resolve().parent

root_router = APIRouter()
app = FastAPI(title='Recipe API', openapi_url=f'{settings.API_V1_STR}/openapi.json')

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        # allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

app.include_router(api_v1_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == '__main__':
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='debug')
