from flask import Flask,request,redirect,send_file,send_from_directory
from flask.templating import render_template

app = Flask(__name__)
app.debug=True

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/download',methods=['POST'])
def download():
    name = request.form.get("name")
    password= request.form.get("password")
    if name != '' and password != ''  :
        return render_template('download.html')

    else:
        return redirect("/")


@app.route('/download',methods=['GET'])
def download_file():
    print("1")
    p="chat.csv"
    return send_file(p, as_attachment=True)

@app.route('/file',methods=['GET'])
def download_file_2():
    print("2")
    Q="youtube.csv"
    return send_file(Q,as_attachment=True)
@app.route('/down',methods=['GET'])
def download_file3():
    r="business.csv"
    return send_file(r,as_attachment=True)
@app.route('/download4',methods=['GET'])
def download_file4():
    s="annual.csv"
    return send_file(s,as_attachment=True)
@app.route('/download5',methods=['GET'])
def download_file5():
    t="economic.csv"
    return send_file(t,as_attachment=True)





if __name__ == '__main__':
    app.run(host='0.0.0.0')






