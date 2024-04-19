from flask import Flask, render_template
from flask import g, session, send_from_directory
from rest import app_sec
#import os



#app = Flask(__name__, static_folder='')
app = Flask(__name__)

app.secret_key = b'qwe_qwezhgh@24qhkpiirzx_cvbnwd'

app.register_blueprint(app_sec, url_prefix='/rest')


@app.route('/assets/<path:filename>')
def accessing_assets(filename):
    return send_from_directory('assets', filename)


@app.route('/static/<path:filename>')
def accessing_statics(filename):
    return send_from_directory('static', filename, as_attachment=True)


@app.route("/", methods=['GET'])
def main():
   return render_template("main.html")


@app.route("/search", methods=['GET','POST'])
def search():
   return render_template('search.html')
 


@app.route("/contact", methods=['GET'])
def contact():
   return render_template('contact.html')
 
 
@app.route("/genre", methods=['GET'])
def genre():
   return render_template('genre.html')
    
 
 
@app.errorhandler(404)
def errror(e):
   return "error doesn't exist", 404

 
   
   
if __name__ == '__main__':
    app.run(debug=True)


"""
app.debug = True
port = 8888
app.run('0.0.0.0',port)
"""
