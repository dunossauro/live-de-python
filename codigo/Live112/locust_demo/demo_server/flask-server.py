from random import randint

from flask import Flask, request, jsonify, redirect, make_response

app = Flask(__name__)

auth = randint(100, 50000)


@app.route('/get-auth', methods=['POST'])
def get_auth_cookie():
    req = request.get_json()
    if req['pass'] == '1234':
        res = make_response(jsonify({'auth': str(auth)}))
        res.set_cookie('auth', str(auth))
    else:
        res = make_response(jsonify({'erro': 'nao autorizado'}), 401)
        res.set_cookie('auth', '0')
    return res


@app.route('/get-complex-object', methods=['GET'])
def get_complex_object():
    print(bool(request.args.get('returnObject')))
    if bool(request.args.get('returnObject')):

        return_object = {
            "complexObj":
                [
                    {
                        "id": "0001",
                        "type": "donut",
                        "name": "Cake",
                        "ppu": 0.55,
                        "batters":
                            {
                                "batter":
                                    [
                                        {"id": "1001", "type": "Regular"},
                                        {"id": "1002", "type": "Chocolate"},
                                        {"id": "1003", "type": "Blueberry"},
                                        {"id": "1004", "type": "Devil's Food"}
                                    ]
                            },
                        "topping":
                            [
                                {"id": "5001", "type": "None"},
                                {"id": "5002", "type": "Glazed"},
                                {"id": "5005", "type": "Sugar"},
                                {"id": "5007", "type": "Powdered Sugar"},
                                {"id": "5006", "type": "Chocolate with Sprinkles"},
                                {"id": "5003", "type": "Chocolate"},
                                {"id": "5004", "type": "Maple"}
                            ]
                    },
                    {
                        "id": "0002",
                        "type": "donut",
                        "name": "Raised",
                        "ppu": 0.55,
                        "batters":
                            {
                                "batter":
                                    [
                                        {"id": "1001", "type": "Regular"}
                                    ]
                            },
                        "topping":
                            [
                                {"id": "5001", "type": "None"},
                                {"id": "5002", "type": "Glazed"},
                                {"id": "5005", "type": "Sugar"},
                                {"id": "5003", "type": "Chocolate"},
                                {"id": "5004", "type": "Maple"}
                            ]
                    },
                    {
                        "id": "0003",
                        "type": "donut",
                        "name": "Old Fashioned",
                        "ppu": 0.55,
                        "batters":
                            {
                                "batter":
                                    [
                                        {"id": "1001", "type": "Regular"},
                                        {"id": "1002", "type": "Chocolate"}
                                    ]
                            },
                        "topping":
                            [
                                {"id": "5001", "type": "None"},
                                {"id": "5002", "type": "Glazed"},
                                {"id": "5003", "type": "Chocolate"},
                                {"id": "5004", "type": "Maple"}
                            ]
                    }
                ]
        }
        return jsonify(return_object)
    return jsonify({"erro": "erro"})


@app.route('/nao-autorizado-param', methods=['GET'])
def get_redirect():
    if request.args.get('auth') and int(request.args.get('auth')) == auth:
        return jsonify({'redirected': False})
    return redirect("http://localhost:5000/redirected", code=302)


@app.route('/nao-autorizado-cookie', methods=['GET'])
def get_redirect_cookie():
    if 'auth' in request.cookies and request.cookies['auth'] == str(auth):
        return jsonify({'redirected': False})
    return redirect("http://localhost:5000/redirected", code=302)


@app.route('/redirected', methods=['GET'])
def redirected():
    return jsonify([{"redirected": True}])


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  # run app in debug mode on port 5000.
