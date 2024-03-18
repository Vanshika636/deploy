from flask import Flask,jsonify,request
api_url = " https://customer-analytics-34146.my.salesforce-sites.com/services/apexrest/buyStocks"
app = Flask(__name__)

@app.route('/customer-analytics-34146.my.salesforce-sites.com/services/apexrest/buyStocks', methods=['POST'])
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
        "company": "Bajaj",
        "currentPrice" : "₹8,384.90",
        "accountNumber":"ABCD123",
        "githubRepoLink":"https://github.com/Vanshika636/deploy.git",
        "numbers": numbers,
        "alphabets": alphabets}
                   
    )

if __name__ == '__main__':
    api2.run()
