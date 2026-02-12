import random
import string

from app.configuration.database import SessionLocal, init_db
from app.models.models import Item


def _random_text() -> str:
    length = random.randint(10, 24)
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for _ in range(length))


def seed_database(count: int = 25) -> None:

    init_db()

    db = SessionLocal()
    try:
        existing = db.query(Item).count()
        if existing > 0:
            print("Database already contains data. Skipping seed.")
            return

        items = [Item(text=_random_text()) for _ in range(count)]
        db.add_all(items)
        db.commit()

    except Exception as exc:
        print(f"Error: {exc}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
