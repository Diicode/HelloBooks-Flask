from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/auth/register')
def register():
    return render_template("registration.html")


@app.route('/api/auth/login')
def login():
    return render_template("login.html")


@app.route('/api/user/dashboard')
def user():
    return render_template("client's-dashboard.html")


@app.route('/api/books' )
def books():
    return render_template("catalogue.html")


@app.route('/api/Admin/dashboard')
def admin():
    return render_template("admin-dashboard.html")


@app.route('/api/dashboard/features')
def features():
    return render_template("admin-features.html")
if __name__ == '__main__':
    app.run(debug=True)