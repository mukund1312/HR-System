from app.db.session import SessionLocal
# from app.db.dependencies import get_db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
