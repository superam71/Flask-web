# Importamos del módulo flask la clase Flask que creará nuestra aplicación,el modulo render_template para el html,flash para mostrar un 
# mensage al pedir datos al usuario en el login y register y importo el formulario
from flask import Flask,render_template,session,flash,redirect,url_for,request,abort
from flask_wtf import Form
from forms import LoginForm,SignUpForm,SearchForm
import csv

# Paso mi proyecto a una variable.
app = Flask(__name__)
app.config['SECRET_KEY']='hola'

# Estos decoradores nos sirven para mapear qué funciones se van a llamar en el
# momento que al servidor le llegue una petición con esa URL,cuando el servidor encuentre la peticion que esta en route(lo primero que encuentra)
# ejecutara esa funcion
@app.route('/')
def home():
    return render_template("pagina.html") #asignar un html al inicio

@app.route('/index',methods=['GET','POST'])
def index():
    formulario=LoginForm()
    if formulario.validate_on_submit():
        with open("C:/Users/RAMSES/Desktop/hello_world_app/app/templates/users.csv") as archivo:
            usuarios=csv.reader(archivo)
            sinencabezado=next(usuarios)
            while sinencabezado:
                if formulario.username.data==sinencabezado[0] and formulario.password.data==sinencabezado[1]:
                    flash('Bienvenido')
                    session['username']=formulario.username.data
                    return render_template('ruta2.html')
                sinencabezado=next(usuarios, None)
            else:
                flash('Revisa tu nombre de usuario y contraseña')
                return redirect(url_for('index'))
    return render_template('lola.html',formulario=formulario)

@app.route('/registrar',methods=['GET','POST'])
def registrar():
    formulario=SignUpForm()
    if formulario.validate_on_submit():
        if formulario.password.data==formulario.password_check.data:
            with open("C:/Users/RAMSES/Desktop/hello_world_app/app/templates/users.csv","a+") as archivo:
                archivo_csv=csv.writer(archivo)
                registro=[formulario.username.data,formulario.password.data]
                archivo_csv.writerow(registro)
                flash('Usuario creado correctamente')
                return redirect(url_for('index'))
        else:
            flash('Las passwords no matchean')
    return render_template('lola2.html', formulario=formulario)

@app.route('/outindex',methods=['GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        return render_template('loggedout.html')
    else:
        return abort(403)

@app.route('/userstable')
def tabladeusuarios():
    if 'username' in session:
        with open("C:/Users/RAMSES/Desktop/hello_world_app/app/templates/clientestxt.csv","r") as csvusuarios:
            leercsv=csv.reader(csvusuarios)
            return render_template('paginaclientes.html',leercsv=leercsv)
    else:
        return abort(403)

@app.route('/loghome')
def loghome():
    if 'username' in session:
        return render_template('ruta2.html')
    else:
        return abort(403)

@app.route('/finduser',methods=['GET','POST'])
def finduser():
    formulario=SearchForm()
    coincidencias=[]
    if 'username' in session:
        if formulario.validate_on_submit():
            with open("C:/Users/RAMSES/Desktop/hello_world_app/app/templates/clientestxt.csv","r") as csvusuarios:
                leercsv=csv.reader(csvusuarios)
                for registro in leercsv:
                    if formulario.country.data==registro[3]:
                        coincidencias.append(registro)
                if coincidencias:#lista con algo
                    return render_template('usuario.html',registros=coincidencias)
                else:#lista vacia
                    return render_template('customersnotfound.html')
        return render_template('buscador.html',formulario=formulario)
    else:
        return abort(403)

@app.errorhandler(404)
def pagernotfound(e):
    return render_template('error1.html')

@app.errorhandler(403)
def noaccess(e):
    return render_template('error2.html')

# Si ejecutamos el módulo, la aplicación de Flask corre con el modo de prueba
# activo.

if __name__ == "__main__":
    app.run(debug=True)