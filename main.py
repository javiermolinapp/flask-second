from flask import Flask
from flask_cors import CORS, cross_origin





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



    
    
    
