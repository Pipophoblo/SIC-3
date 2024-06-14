from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    temperature = data.get('temperature', None)
    
    if temperature is not None:
        response = {
            "status": "success",
            "message": f"Received temperature: {temperature} °C"
        }
        return jsonify(response), 200
    else:
        response = {
            "status": "error",
            "message": "No temperature data provided"
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
