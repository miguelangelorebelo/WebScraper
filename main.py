from services import DontPayEconomist
from models import EconomistModel
from utils.database import Base, local_engine, LocalSessionMaker
from sqlalchemy import text
import pandas as pd

pd.options.display.max_columns = 10

# if not created
Base.metadata.bind = local_engine
Base.metadata.create_all(local_engine)

if __name__ == '__main__':
    dpe = DontPayEconomist()
    latest_news = dpe._collect_news_links()
    instances = dpe.bulk_extraction()

    with LocalSessionMaker() as s:

        s.bulk_insert_mappings(EconomistModel, instances)
        s.commit()

    print(f'Inserted {len(instances)} novel news from economist.com into local db')
    
    query = "SELECT * FROM EconomistNews"
    df = pd.DataFrame(local_engine.connect().execute(text(query)))
    print(f'df.head():\n\n{df.head()}')
