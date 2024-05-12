from config import settings

#import asyncio
#from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_session
from sqlalchemy import insert, select
from sqlalchemy import create_engine, text
from mode.good import Base, User

#ur_p = 'postgresql://postgres:1234@localhost:5432/dbtest04'





ur_s = settings.POSTGRES_DATABASE_URLS
ur_a = settings.POSTGRES_DATABASE_URLA

print(ur_s)

engine_s = create_engine(ur_s, echo=True)
#engine = create_async_engine(ur_p, echo=True)


def create_tables():
    Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)
def f():
    with engine_s.connect() as conn:
        answer = conn.execute(text('select * from users;'))
        print(f"answer = {answer.all()}")

def f_bilder():
    with engine_s.connect() as conn:
        query = insert(User).values([
            {"name": "SSSuiu", "hashed_password": "123545"},
            {"name": "CSidorkin", "hashed_password": "123545"}
        ])
        conn.execute(query)
        conn.execute(text('commit;'))
        query = select(User)
        answer = conn.execute(query)
        print(f"answer = {answer.all()}")

    #asyncio.run(f())
   # asyncio.get_event_loop().run_until_complete(f())