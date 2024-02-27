from flask import render_template, Flask,request
import threading
from function import ONLOGIN


app = Flask(__name__)
 
app.secret_key = 'Dheeraj@2006'

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        obj=ONLOGIN()
        title=obj.auto_email()
        th = threading.Thread(target=obj.auto_email, args=())
        # print("thread is started and running ")
        return render_template('index.html',title=title)
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)