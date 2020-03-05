from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
db_url = 'postgres://postgres@localhost:5432/kalina'
engine = create_engine(db_url, pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)