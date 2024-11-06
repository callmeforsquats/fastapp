from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,async_session
from sqlalchemy.orm import DeclarativeBase,Mapped
from sqlalchemy.testing.schema import mapped_column



basa=create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)
new_secc=async_sessionmaker(basa,expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskTable(Model):
    __tablename__="tasks"
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]
    description:Mapped[str|None]

async def create_tables():
    async with basa.begin() as conn:
        await  conn.run_sync(Model.metadata.create_all)
async def delete_tables():
    async with basa.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

