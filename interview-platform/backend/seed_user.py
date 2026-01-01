import uuid
from app.db.session import SessionLocal
from app.db.models.user import User

def seed_test_user():
    db = SessionLocal()
    # Use the specific ID from your error log
    test_id = uuid.UUID("ad2f2ff8-2986-4bd3-bc50-3288a3445520")
    
    # Check if user already exists
    user = db.query(User).filter(User.id == test_id).first()
    
    if not user:
        new_user = User(
            id=test_id,
            email="test@example.com",
            name="Test Interviewer",
            provider="local",
            provider_id="test-123"
        )
        db.add(new_user)
        db.commit()
        print(f"Successfully created test user with ID: {test_id}")
    else:
        print("Test user already exists.")
    db.close()

if __name__ == "__main__":
    seed_test_user()