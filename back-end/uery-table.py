from flask import Flask
from models import db, BayTable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'cockroachdb://dat:a8yS_VjWUTTMdhfXLQ70Cw@waning-reptile-6926.g8z.gcp-us-east1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance with the Flask app
db.init_app(app)

# Function to query a specific table
def get_class_by_tablename(tablename):
    for mapper in db.Model.registry.mappers:
        cls = mapper.class_
        classname = cls.__name__
        if not classname.startswith('_'):
            tblname = cls.__tablename__
            db.Model.TBLNAME_TO_CLASS[tblname] = cls

get_class_by_tablename('BayTable1')