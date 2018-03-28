from flask import Flask, jsonify, request

books = [{'Title','Author':'Mindset','Carol Dweck' {'Title','Author':'Unshakable','Tony Robbins'} {'Title','Author':'Mastery','Robert Greene'}


@app.route('/api/books' methods=['POST'])
def add_books():
	return jsonify ({'books': books})

@app.route(/api/books/<bookld> methods=['PUT'])
def modify_book():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/books/<bookld>' methods=['DELETE'])
def remove_book():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/books' methods=['GET'])
def retrieve_allbooks():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/books/<bookld>' methods=['GET'])
def get_book():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/users/books/<bookld>' methods=['POST'])
def borrow_book():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/auth/register' methods=['POST'])
def create_user():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/auth/login' methods=['POST'])
def login_user():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/auth/logout' methods=['POST'])
def logout_user():
	return jsonify ({'messages': 'Its cool'})

@app.route('/api/auth/reset-password' methods=['POST'])
def reset_password():
	return jsonify ({'messages': 'Its cool'})



if __name__ == '__main__':
	app.run(debug=True, port=8080 main()