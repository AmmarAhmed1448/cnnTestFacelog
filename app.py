from flask import Flask, jsonify, request
from b64code import imgCodeJsonArray
import base64
from io import BytesIO
from PIL import Image
from flask_cors import CORS
from b64test import testCode
import os


app = Flask(__name__)
CORS(app)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/save-images-training", methods = ['GET'])
def saveImagesTraining():
    try:
        email = "ali@email.com"
        # imgCodeJsonArray = request.json
        for i in range(len(imgCodeJsonArray)):
            imgCodeJson = imgCodeJsonArray[i]
            imgBytes = base64.b64decode(imgCodeJson)
            imgStream = BytesIO(imgBytes)
            image = Image.open(imgStream)
            save_path = f"D://Ammar//HTML Coursera//React//FaciLog//CNN simulator//Images//{email}//training//"
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            image.save(os.path.join(save_path, f"{i}.jpeg"))
        
        return jsonify({"msg":"Training Image decoded"})
        
    except Exception as e:
        return jsonify({"msg":list({str(e)})})
    

@app.route("/save-images-testing", methods = ['GET'])
def saveImagesTesting():
    try:
        email = "moin@email.com"
        imgCodeJson = testCode[0]
        imgBytes = base64.b64decode(imgCodeJson)
        imgStream = BytesIO(imgBytes)
        image = Image.open(imgStream)
        save_path = f"D://Ammar//HTML Coursera//React//FaciLog//CNN simulator//Images//{email}//testing//"
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        image.save(os.path.join(save_path, "test.jpeg"))
        
        return jsonify({"msg":"Test Image decoded"})
        
    except Exception as e:
        return jsonify({"msg":list({str(e)})})