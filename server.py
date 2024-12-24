from flask import Flask, send_file, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_file(r'E:\Portfolio\PortfolioProject\index.html')

@app.route('/download-resume', methods=['GET'])
def download_resume():
    return send_file(r'E:\Portfolio\PortfolioProject\resume.pdf', as_attachment=True)

@app.route('/download-cv', methods=['GET'])
def download_cv():
    return send_file(r'E:\Portfolio\PortfolioProject\CV.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
