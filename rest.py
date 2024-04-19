from flask import Blueprint


app_sec = Blueprint("qwez", __name__)

@app_sec.route('/')
def about():
    var = " __"
    return f" rest {var}"


@app_sec.route('/contact')
def contact():
    contact = " __"
    return f" rest {contact}"


@app_sec.route('/about')
def About():
    about = " __"
    return f" rest {about}"
    
    
@app_sec.route('/rules')
def Rules():
    rules = " __"
    return f" rules {rules}"    
