from app import app, db, QA

with app.app_context():
    db.drop_all()  # Drop all tables (for debugging, to start fresh)
    db.create_all()
    print("Tables created successfully")
