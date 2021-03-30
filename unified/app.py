from flask import Flask,render_template
from controllers.todos_controller import todos_blueprint

app = Flask(__name__)
app.register_blueprint(todos_blueprint,url_prefix='/todos')

@app.route('/')
def index():
     return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 , debug=True) 
