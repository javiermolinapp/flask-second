import io
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from flask import Flask, jsonify
import base64




app = Flask(__name__)



@app.route("/graficarbarra/<key1>/<x1>/<key2>/<x2>/<key3>/<x3>")
def generate_image(key1,x1, key2, x2, key3, x3):


    
    
    
    data = {key1:int(x1), key2:int(x2), key3:int(x3)}
    courses = list(data.keys())
    values = list(data.values())
    
    fig = pyplot.figure(figsize = (10, 5))
    
    # creating the bar plot
    pyplot.bar(courses, values, color ='green', 
            width = 0.4)
 
    pyplot.title('Frutas')
    pyplot.xlabel('Tipo')
    pyplot.ylabel('Cantidad')
    #img = str(referencia);

    # create PNG image in memory
    img= io.BytesIO()  
           # create file-like object in memory to save image without using disk
    

    pyplot.savefig(img, format='png') 
    img.seek(0) 

    #save image in file-like object
   
            
    data = img.getvalue()
       


    data = base64.b64encode(data) # convert to base64 as bytes
    data = data.decode()  # move to beginning of file-like object to read it later
   
   


    img.close()
    pyplot.clf()
    pyplot.close()
  
    return jsonify(data)



    

def create_app():
    return app
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)



    
    
    
