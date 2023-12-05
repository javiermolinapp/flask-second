import io
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import base64




app = Flask(__name__)


CORS(app)

@cross_origin
########################GRAFICO DE LINEAS
@app.route("/graficarlinea/<x1>/<x2>")
def generate_image2(x1, x2):
    return x1+x2;



    

def create_app():
    return app
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)



    
    
    
