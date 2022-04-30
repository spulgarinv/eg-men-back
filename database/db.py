from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'postgresql://txlxcpuyjviyrr:be9d5ec9f056998e6c7ddae76f6f72cbde05c1c9dd283bf8fabc1945894e4c37@ec2-52-71-69-66.compute-1.amazonaws.com:5432/d84a8okqkvk3pj'
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

session = SessionLocal()
Base = declarative_base()