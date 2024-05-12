from flask import Flask, render_template, jsonify, Blueprint,redirect,url_for,redirect,request
from model import DepartamentoModel
from database import init_db

app = Flask(__name__)
mysql = init_db(app)
my_blueprint = Blueprint('controller', __name__)

@app.route('/')
def index():
    data = DepartamentoModel.leer_departamentos()
    return render_template('departamentos.html', data=data)

@app.route('/formulario_departamento')
def formulario_departamento():
    return render_template('formulario_departamento.html')

@app.route('/ingresar_departamento', methods=['POST'])
def ingresar_departamento():
    departamento = request.form['departamento']
    DepartamentoModel.ingresar_departamento(departamento)
    return redirect(url_for('index'))

@app.route('/buscar_departamento/<id>',methods=['GET','POST'])
def editar_departamento(id):
    dep = DepartamentoModel.traer_registro(id)
    return render_template('editar_departamento.html',dep=dep,id=id)

@app.route('/actualizar_departamento', methods=['POST'])
def actualizar_departamento():  
    departamento = request.form['departamento']
    iddepartamento = request.form['iddepartamento']
    DepartamentoModel.actualizar_departamento(iddepartamento, departamento)
    mysql.connection.commit() 
    return redirect(url_for('index'))

@app.route('/eliminar_departamento/<id>', methods=['GET'])   
def eliminar_departamento(id):
    DepartamentoModel.eliminar_departamento(id)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)
