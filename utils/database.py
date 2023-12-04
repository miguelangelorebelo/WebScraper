from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base

LDB_PATH = "./lib/economist.db"

local_engine = create_engine("sqlite:///{}".format(LDB_PATH), connect_args={"check_same_thread": False})
LocalSessionMaker = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=local_engine))

Base = declarative_base()