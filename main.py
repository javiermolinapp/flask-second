from flask import Flask, jsonify
import os

app = Flask(__name__)




@app.route("/graficarlinea/<x1>/<x2>")
def generate_image2(x1, x2):
    return x1+x2;


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
