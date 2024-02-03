from models import db
from models.userModel import User


def create_admin(email_address):
    get_admin = db.session.query(User).filter_by(role="admin").first()
    if get_admin:
        pass 
    else:
        db.session.add(
            User(
                email=email_address,
                password="admin",
                name="admin",
                role="admin",
                approved=1,
            )
        )
        db.session.commit()
