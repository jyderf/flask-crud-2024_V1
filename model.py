from flask import Flask, jsonify # type: ignore
from database import init_db

app = Flask(__name__)
mysql = init_db(app)

class DepartamentoModel:
    @staticmethod
    def leer_departamentos():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM departamento")
        data = cur.fetchall()
        cur.close()
        return data    
    
    @staticmethod
    def ingresar_departamento(departamento):  
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO departamento(departamento) VALUES(%s);",(departamento,))
        mysql.connection.commit()#finaliza la transacción actual y guarda permanentemente los cambios realizados en la base de datos.
        cur.close()

    @staticmethod
    def traer_registro(id):
        cur = mysql.connection.cursor()
        cur.execute("SELECT D.departamento FROM departamento AS D WHERE D.iddepartamento = %s;",(id,))
        mysql.connection.commit()
        data = cur.fetchone()
        cur.close
        return data    
    
    @staticmethod
    def actualizar_departamento(iddepartamento,departamento):     
            cur = mysql.connection.cursor()
            cur.execute("UPDATE departamento SET departamento = %s WHERE iddepartamento = %s;", (departamento, iddepartamento))
            mysql.connection.commit()
            cur.close()

    @staticmethod
    def eliminar_departamento(id):
         cur = mysql.connection.cursor()
         cur.execute("DELETE FROM departamento WHERE iddepartamento = %s;",(id,))
         mysql.connection.commit()
         cur.close()
         return jsonify(id)


            
       
       
       
        
        

   

