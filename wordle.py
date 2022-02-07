from app import create_app, db
from app.models import *

app = create_app()

@app.shell_context_processor
def make_shell_context():
    from app.models import User, Word, UserWordLink
    return {'db': db, 'User': User, 'Word': Word, 'UserWordLink': UserWordLink }