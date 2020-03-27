"""This is the initializor of the flaskblog"""

from flaskblog import create_app

app = create_app()

# Run under debug mode in order to refresh the page without having to reload the server
if __name__ == '__main__':
    app.run(debug=True)
