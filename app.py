from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (you can replace this with a database)
items = [
    {"id": 1, "name": "sadad"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]
data1 = []

# GET request to fetch all items
@app.route('/bhfl',methods=['GET', 'POST'])
def api():

    if request.method == 'POST':
        try:
            request_data = request.get_json()  # Parse JSON data from the request
            print("error1")
            data1.append(request_data)  # Add the data to the data store
            print("error2")
            return jsonify({"message": "Data added successfully"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    elif request.method == 'GET':

        return jsonify(items)

# # POST request to add a new item
# @app.route('/bhfls', methods=['POST'])
# def create_item():
#     # data = request.get_json()
#     # if data and 'name' in data:
#     #     new_id = max(item['id'] for item in items) + 1
#     #     new_item = {"id": new_id, "name": data['name']}
#     #     items.append(new_item)
#     #     return jsonify(new_item), 201
#     # return jsonify({"message": "Invalid data"}), 400





#     # data = request.get_json()

#     # # Extracting data from the JSON request
#     # user_id = 'madanagopal_chandrasekhar_16062002'
#     # college_email = 'madanagopal.c2020@vitstudent.ac.in'
#     # college_roll_number = '20BCE0602'
#     # in_list = data.get('data',[])
#     # alphabet_array = []
#     # number_array = []

#     # for item in in_list:
#     #     if item.isalpha():
#     #         alphabet_array.append(item)
#     #     elif item.isdigit():
#     #         number_array.append(item)

#     # # Finding the highest alphabet in the alphabet_array
#     # highest_alphabet = max(alphabet_array, key=lambda x: x.lower())

#     # response = {
#     #     'status': 'Success',
#     #     'user_id': user_id,
#     #     'college_email_id': college_email,
#     #     'college_roll_number': college_roll_number,
#     #     'number_array': number_array,
#     #     'alphabet_array': alphabet_array,
#     #     'highest_alphabet': highest_alphabet
#     # }

#     # return jsonify(response), 400











if _name_ == '__main__':
    app.run(debug=True)
