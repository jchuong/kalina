from fastapi import FastAPI
from sqlalchemy_utils import create_database, database_exists

from kalina.api.api import API_ROUTER

from kalina.models import user
from kalina.db.session import SessionLocal, engine, db_url
from kalina.db.base_class import Base

app = FastAPI()
app.include_router(API_ROUTER)

if not database_exists(db_url):
    print('Creating DB and tables')
    create_database(db_url)
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return { "message": "Hello world" }


@app.get('/user')
async def create_user():
    db = SessionLocal()
    new_user = user.User(username='jchuong', password='test', email='test@kalin.app')
    db.add(new_user)
    db.commit()
    db.close()
    return 200


@app.get('/users')
async def get_users():
    db = SessionLocal()
    users = db.query(user.User).all()
    db.close()
    return users

