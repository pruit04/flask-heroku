from flask import Flask, jsonify
from flask import Flask, render_template, Response 
import cv2

camera = cv2.VideoCapture('rtsp://freja.hiof.no:1935/rtplive/definst/hessdalen03.stream')

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Herok" 


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

@app.route('/name')
def name():
    return "<font color=green>พฤทธิ์ แก่นจันทร์</font> <br>เลขที่ 4 ม.4/10" 

@app.route('/hello/<string:name>')
def Home(name):
    return render_template('home.html',name_html=name)

@app.route('/video')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
