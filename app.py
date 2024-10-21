from flask import Flask,render_template,request,session, redirect,url_for
app = Flask(__name__)
# nesesario cuando se usa session
app.secret_key = 'unaclavesecreta'
@app.route("/")
def coche ():
    #verifica si lista esta en la session
    if 'lista' not in session:
        #inicializar la sista
        session['lista'] = []
    return render_template('index.html',lista = session['lista'])
@app.route("/proceso",methods=['GET','POST'])
def proceso():
    producto = request.form.get("producto")
    if 'lista' in session and producto:
        # producto adicionado en la lista
        session['lista'].append(producto)
        #aseguramos que la session ha sido modificada
        session.modified = True
    return redirect(url_for("coche"))
@app.route("/vaciar",methods=["GET"])
def vaciar():
    #elimina de session lista
    session.pop("lista",None)
    return redirect(url_for("coche"))
if __name__== "__main__":
    app.run(debug=True)
