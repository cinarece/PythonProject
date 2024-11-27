from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Merhaba Dünya!</h1><p>Bu, ilk Flask web uygulamam.</p>"

if __name__ == "__main__":
    app.run(debug=True)

