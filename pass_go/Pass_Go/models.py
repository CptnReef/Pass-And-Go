from Pass_Go.sql_models import User
from Pass_Go import db_session, login_manager

@login_manager.user_loader
def load_user(user_code):
    return db_session.query(User).filter_by(code=user_code).first()