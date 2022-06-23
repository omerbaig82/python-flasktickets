import os

db_host = os.environ.get('DB_HOST', default='44.203.115.153')
db_name = os.environ.get('DB_NAME', default='dashboard')
db_user = os.environ.get('DB_USERNAME', default='dashboard')
db_password = os.environ.get('DB_PASSWORD', default='secure_password')
db_port = os.environ.get('DB_PORT', default='5432')

SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI=f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
