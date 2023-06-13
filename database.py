import sqlalchemy

print(sqlalchemy.__version__)
from sqlalchemy import create_engine
from sqlalchemy import text
import os
connection_string = os.environ['db_connection_string']
engine = create_engine(connection_string,echo=True)
def load_jobs_from_db():
  with engine.connect() as connection:
    result=connection.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

 
  
  
  