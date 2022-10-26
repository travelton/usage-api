from flask import Flask, request, Response
import json, datetime

app = Flask(__name__)
stats = dict()
			
@app.route('/', methods=['GET'])
def root():
    output =   """
                <!DOCTYPE html>
                <body>  
                    <h3>Usage Stats API Online</h3>
                    <div>See README for more information!</div>
                </body>
                """
    return output

def _get_stats(req):
    return Response(json.dumps(stats), status=200, mimetype="application/json")

def _save_stats(req):
    request_data = request.get_json()
    required_params = ["date", "count"]
    if not all(p in request_data.keys() for p in required_params):
        response_payload = {
            "message": "Missing one or all required parameters."
        }
        status_code = 400
    else:
        global stats
        stats[request_data.get("date")] = request_data.get("count")
        response_payload = {
            "message": "Data received!",
            "data": {
                "date": request_data.get("date"),
                "count": request_data.get("count"),
            }
        }
        status_code = 201
    return Response(json.dumps(response_payload), status=status_code, mimetype="application/json")

@app.route('/stats/users', methods=['GET', 'POST'])
def stats_endpoint():
    if request.method == "GET":
        return _get_stats(request)

    if request.method == "POST":
        return _save_stats(request)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0',port=5000)
