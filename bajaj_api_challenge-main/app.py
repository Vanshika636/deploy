from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/customer-analytics-34146.my.salesforce-sites.com/services/apexrest/createAccount', methods=['POST'])
def welcome():
    print(request.json["data"])
    numbers = []
    alphabets = []
    for data in request.json["data"]:
        if data.isalpha():
            alphabets.append(data)
        else:
            numbers.append(data)
    return jsonify({
        "is_success": True,
        "name": "john",
        "email" : "john@xyz.com",
        "roll_number":"ABCD123",
        "phone" : "9996665050",
        "numbers": numbers,
        "alphabets": alphabets}
                   
    )

if __name__ == '__main__':
    app.run()
