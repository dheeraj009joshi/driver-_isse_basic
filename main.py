from flask import render_template, Flask,request
import threading
from function import ONLOGIN, send_email, senf_email


app = Flask(__name__)
 
app.secret_key = 'Dheeraj@2006'

@app.route("/",methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        email=request.form['recipientEmail']
        th = threading.Thread(target=senf_email, args=(email,))
        th.start()
        # print("thread is started and running ")
        return render_template('index.html')
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)