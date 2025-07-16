import os
from app import create_app, db
from app.models import User

config_name =  os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    app.run(debug=True, port=5000)