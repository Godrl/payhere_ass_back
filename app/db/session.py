import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = f'mysql+pymysql://{os.getenv("DB_MYSQL_USER")}:{os.getenv("DB_MYSQL_PW")}' \
         f'@{os.getenv("DB_MYSQL_HOST")}/{os.getenv("DB_MYSQL_TABLE")}'

engine = create_engine(
    db_url,
    echo=(os.getenv('APP_ENV') == 'dev'),  # query logging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
