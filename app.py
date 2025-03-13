from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>OWASP ZAP Web Scanner</h1><p>Click the button below to start a scan.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
