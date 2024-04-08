from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

engine = create_async_engine(
    'postgresql+psycopg://app_user:app_password@sausage:5432/app_db'
)


async def get_session():
    async with AsyncSession(engine) as session:
        yield session
