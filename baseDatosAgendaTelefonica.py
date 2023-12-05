import sqlite3 as dbapi

axendaTel = (("Pepe", "Pérez", "986 444 555" ),
             ("Ana", "Yañéz", "985 333 777" ),
             ("Roque", "Diz", "987 222 889" ))

bbdd = dbapi.connect ("bdListinTelefonico.dat")
c =bbdd.cursor()

try:
    c.execute("""create table listaTelefonos (nome text,
                              apelidos text,
                              telefono text)""")
except dbapi.DatabaseError as e:
    print ("Erro creando a táboa listaTelefonos: " + e)

try:
    for datos in axendaTel:
        c.execute ("""insert into listaTelefonos
                  values(?, ?, ?)""", datos)# va linea por linea en la agenda y guarda cada linea en la variable datos. Luego hace el insert en la tabla con los datos de dicha variable.
    bbdd.commit()
except dbapi.DatabaseError as e:
    print ("Erro o insertar usuarios: "+ e)

c.close()
bbdd.close()