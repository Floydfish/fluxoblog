from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

# Decorator that handles the backend for me
@main.route("/")

@main.route("/home")
def home():
    """The homepage route"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts) # Import do render_template necessário

# Creating children sites
@main.route("/about")
def about():
    """Go to the about page"""
    return render_template('about.html', title='About')


