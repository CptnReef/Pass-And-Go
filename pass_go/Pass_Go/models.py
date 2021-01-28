from Pass_Go.models import User


@login_manager.user_loader
def load_user(user_code):
    return db.session.query(User).filter_by(code=user_code).first()