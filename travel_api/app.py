#%%

from flask import Flask
from itineraries.routes import itineraries_bp

app = Flask(__name__)
app.register_blueprint(itineraries_bp, url_prefix='/itineraries')

if __name__ == '__main__':
    app.run(debug=True)