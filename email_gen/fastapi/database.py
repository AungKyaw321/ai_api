from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://skyhigh_insights_user:vy7IMA5GKrdgRvofUytHBhFxycfKKBWN@dpg-cqn77olds78s7399e9i0-a.oregon-postgres.render.com/skyhigh_insights"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



    

