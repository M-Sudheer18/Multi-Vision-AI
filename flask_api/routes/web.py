from flask import Blueprint, render_template
web_bp = Blueprint("web", __name__)

@web_bp.route('/', methods = ['GET'])
def home():
    # It gets (Serves) the Main HTML Page..
    return render_template("index.html")