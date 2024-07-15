from sqlalchemy import create_engine, text
import json,os

engine = create_engine(os.environ["DB_CONNECTION"],
    connect_args={
        # "ssl": {
        #     "ca": "/home/gord/client-ssl/ca.pem",
        #     "cert": "/home/gord/client-ssl/client-cert.pem",
        #     "key": "/home/gord/client-ssl/client-key.pem"
        # }
    }
    )

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = [row._asdict() for row in result]

        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text
        ("SELECT * FROM jobs WHERE id = :val")
        )
        val = id
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])