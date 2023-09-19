from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])

def bfhl():
    if request.method=='GET':
        response = {
            'operation_code': 1
        }
        return jsonify(response), 200

    if request.method == 'POST':
        try:
            data = request.get_json()

            # Extracting data from the JSON request
            user_id = 'madanagopal_chandrasekhar_16062002'
            college_email = 'madanagopal.c2020@vitstudent.ac.in'
            college_roll_number = '20BCE0602'
            in_list = data.get('data',[])
            alphabet_array = []
            number_array = []

            for item in in_list:
                if item.isalpha():
                    alphabet_array.append(item)
                elif item.isdigit():
                    number_array.append(item)

            # Finding the highest alphabet in the alphabet_array
            highest_alphabet = max(alphabet_array, key=lambda x: x.lower())

            response = {
                'status': 'Success',
                'user_id': user_id,
                'college_email_id': college_email,
                'college_roll_number': college_roll_number,
                'number_array': number_array,
                'alphabet_array': alphabet_array,
                'highest_alphabet': highest_alphabet
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'status': 'Error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
