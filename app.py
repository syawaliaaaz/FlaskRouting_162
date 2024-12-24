from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        if username == 'lia' and password == 'admin123':
            return f"Welcome, {username}!"
        else:
            return "Invalid username or password. Please try again."

    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
