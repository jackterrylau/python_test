from flask import Flask, render_template

# new Flask API
# render template html must in templates folder or it will raise TemplateNotFound Error in Mac.
app = Flask(__name__, template_folder='templates')

# Generate route path and function
@app.route("/", methods=["GET"])
def index():
    return "Hello Flask API"

@app.route("/webhook", methods=["GET"])
def webhook():
    return "Webhook Fake Page"

@app.route("/initFunc", methods=["GET"])
def initFunc():
    return render_template("initFunc-3.html")
                            

if __name__=="__main__":
    app.run()