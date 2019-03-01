from flask import Flask, url_for, redirect, request, render_template


app=Flask(__name__)

@app.route('/')

def principal():
    return redirect(url_for('static', filename="index.html"))


@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']

        if (login== 'viniciussds') & (senha=="123456"):
            return render_template('oi.html',nome=login)
        else:
            return redirect(url_for('static',filename='index.html'))
    else:
        return redirect(url_for('static',filename="index.html"))



if __name__== '__main__':
    app.run(debug=True)
