# The importation is necessary in order to associate the Transaction table to the sqlalchemy metadata
from models import EconomistModel
from utils.database import Base, local_engine

Base.metadata.create_all(local_engine)
