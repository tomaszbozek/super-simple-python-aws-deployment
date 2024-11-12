from flask import Flask

application = Flask(__name__)

@application.route('/welcome')
def home():
    return "Hello, Elastic Beanstalk!"

if __name__ == "__main__":
    application.run()
