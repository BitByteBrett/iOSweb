from flask import Flask

app = Flask(__name__)
app.run(host='0.0.0.0', port=80)

from app import routes
