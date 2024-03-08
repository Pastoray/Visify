from flask import Flask, render_template
from blueprints.trees import trees_bp
from blueprints.graphs import graphs_bp
from blueprints.linked_lists import linked_lists_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.register_blueprint(trees_bp, url_prefix="/trees")
app.register_blueprint(linked_lists_bp, url_prefix="/linked-lists")
app.register_blueprint(graphs_bp, url_prefix="/graphs")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)