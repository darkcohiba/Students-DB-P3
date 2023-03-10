from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Students, Teachers


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///students.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# clear database
    session.query(Students).delete()
    session.query(Teachers).delete()

