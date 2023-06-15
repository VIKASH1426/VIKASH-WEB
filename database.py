import sqlalchemy

print(sqlalchemy.__version__)
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
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
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
#def add_application_to_db(job_id,data):
  #with engine.connect() as conn:
    #sql=text("INSERT INTO application(id,job_id,fullname,email,linkedin,education,experience,resumeurl) VALUES (:job_id,:fullname,:email,:linkedin,:education,:experience,:resumeurl)")
    #conn.execute(job_id=job_id,fullname=data['fullname'],email=data['email'],linkedin=data['linkedin'],education=data['education'],experience=data['experience'],resumeurl=data['resumeurl'])
  
  
  