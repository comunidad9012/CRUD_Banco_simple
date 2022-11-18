import mysql.connector
from datetime import datetime

def listar(cur):
    cur.execute("SELECT * FROM clientes")
    resultado = cur.fetchall()
    for x in resultado:
        print(f"Nombre:{x[1]}\nDNI:{x[0]}\nNacimiento:{x[3]}\nDireccion:{x[4]}\nLocalidad:{x[5]}\nTelefono:{x[6]}\nEmail:{x[7]}\nGrupo:{x[9]}\nFondos:{x[10]}\n")
    
def listar1(cur,user):
    cur.execute(f"SELECT * FROM clientes WHERE dni={user}")
    resultado = cur.fetchall()
    for x in resultado:
        print(f"Nombre:{x[1]}\nDNI:{x[0]}\nNacimiento:{x[3]}\nDireccion:{x[4]}\nLocalidad:{x[5]}\nTelefono:{x[6]}\nEmail:{x[7]}\nGrupo:{x[9]}\nFondos:{x[10]}\n")

def alta(con,cur):
    cnom=input("Ingrese Nombre:")
    dni=input("Ingrese DNI:")
    pin=input("Ingrese PIN:")
    cnac=input("Ingrese Nacimiento:")
    cdir=input("Ingrese Direccion:")
    cloc=input("Ingrese Localidad:")
    ctel=input("Ingrese Telefono:")
    cem=input("Ingrese Email:")
    cal=datetime.now()
    cgr=input("Ingrese Grupo:")
    fondos=0  
    sql = "INSERT INTO clientes (dni, nombre_cliente, pin, fecha_nacimiento, direccion, localidad, telefono, email, fecha_alta, grupo_clientes, fondos) VALUES (%s, %s,%s, %s,%s, %s, %s, %s, %s,%s,%s)"    #create list of values typed from user to insert in customer table
    valores = (dni,cnom, pin, cnac, cdir, cloc, ctel, cem, cal, cgr, fondos)
    cur.execute(sql, valores)
    con.commit()
    print(cur.rowcount, "Cliente ingresado.")

def baja(con,cur):
    cid=input("Ingrese dni del cliente a eliminar: ")
    sql = f"DELETE FROM clientes WHERE dni={cid}"
    cur.execute(sql)
    con.commit()
    print(cur.rowcount, "Registro borrado.")

def modificacion(con,cur,):
    dni=int(input("Inserte DNI del usuario a modificar: "))
    cnom=input("Ingrese Nombre:")
    pin=input("Ingrese PIN:")
    cnac=input("Ingrese Nacimiento:")
    cdir=input("Ingrese Direccion:")
    cloc=input("Ingrese Localidad:")
    ctel=input("Ingrese Telefono:")
    cem=input("Ingrese Email:")
    cgr=input("Ingrese Grupo:")
    sql = f"UPDATE clientes SET nombre_cliente='{cnom}', pin='{pin}', fecha_nacimiento='{cnac}', direccion='{cdir}', localidad='{cloc}', telefono='{ctel}', email='{cem}', grupo_clientes='{cgr}' WHERE dni={dni}"
    cur.execute(sql)
    con.commit()
    print(cur.rowcount, "Cliente modificado.")

def optiones_admin():
    print("Ingrese 1 para listar datos de cliente.")
    print("Ingrese 2 para ingresar datos de cliente.")
    print("Ingrese 3 para editar datos de cliente.")
    print("Ingrese 4 para eliminar datos de cliente")
    print("Ingrese 5 para Salir")

def optiones_user():
    print("Ingrese 1 para listar sus datos.")
    print("Ingrese 2 para ingresar fondos.")
    print("Ingrese 3 para retirar fondos.")
    print("Ingrese 4 para salir")

def ingresar_monto(dni,monto,con,cur):
    monto=abs(monto)
    cur.execute("SELECT fondos FROM clientes WHERE dni="+str(dni))
    valor=cur.fetchone()
    sql =f"UPDATE clientes set fondos={monto+valor[0]} WHERE dni={str(dni)}"
    cur.execute(sql)
    con.commit()
    print(cur.rowcount, "Registros actualizados.")

def retirar_monto(dni,monto,con,cur):
    monto=abs(monto)
    cur.execute("SELECT fondos FROM clientes WHERE dni="+str(dni))
    valor=cur.fetchone()
    if valor[0]<monto:
        print("Fondos insuficientes para la transaccion")
    else:
        sql =f"UPDATE clientes set fondos={valor[0]-monto} WHERE dni={str(dni)}"
        cur.execute(sql)
        con.commit()
        print(cur.rowcount, "Record updated.")

def login(con,cur):
    clave_correcta=False
    salir=False
    while clave_correcta==False:
        if salir==True:
            break
        usuario=input("Ingrese nro de documento: ")
        contrasena=input("Ingrese pin: ")
        if usuario!='admin' and contrasena!='admin':
            usuario=int(usuario)
            contrasena=int(contrasena)
        else:
            return usuario
        cur.execute("SELECT pin FROM clientes WHERE dni="+str(usuario))
        pin=cur.fetchone()
        if pin==None:
            pin="no"
        if contrasena==pin[0]:
            clave_correcta=True
            return usuario
        else:
            print("Usuario o contraseña incorrecta")
            print ("Quiere intentar de nuevo?\nSi:1\nNo:2")
            while 0==0:
                respuesta=input()
                if respuesta!="1" and respuesta!="2":
                    print ("Por favor ingrese un valor valido")
                else:
                    if respuesta=="2":
                        salir=True
                        break
                    else:
                        break
                    
def main():

    con = mysql.connector.connect( 
        host="localhost",
        user="root",
        passwd="",
        database="banco"
        )
    cur = con.cursor()
    usuario=login(con,cur)
    if usuario=='admin':
        while True:
            optiones_admin()
            option = int(input())
            if option == 1:
                listar(cur)
            elif option == 2:
                alta(con, cur)
            elif option == 3:
                modificacion(con,cur)
            elif option == 4:
                baja(con,cur)
            elif option == 5:
                break
            else:
                print("Opcion no valida")
    else:
        while True:
            optiones_user()
            option = int(input())
            if option == 1:
                listar1(cur,usuario)
            elif option == 2:
                monto=float(input("Ingrese el monto a ingresar: "))
                ingresar_monto(usuario,monto,con,cur)
            elif option == 3:
                monto=float(input("Ingrese el monto a retirar: "))
                retirar_monto(usuario,monto,con,cur)
            elif option == 4:
                break
            else:
                print("Opcion no valida")
main()