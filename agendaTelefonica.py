import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Pango
import sqlite3 as dbapi

"""
agendaTel = (("Pepe", "Pérez", "986 444 555"),
             ("Ana", "Yáñez", "986 333 666"),
             ("Roque", "Diz", "986 777 888"))
"""


class miPrimeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejemplo listin telefonico con Treeview")
        self.set_default_size(250, 100)
        self.set_border_width(10)

        modelo = Gtk.ListStore(str, str, str)

        try:
            bbdd = dbapi.connect("bdListinTelefonico.dat")
            cursor = bbdd.cursor()
            cursor.execute("select * from listaTelefonos")
            for usuarioListin in cursor:
                modelo.append(usuarioListin)
            cursor.close()
            bbdd.close()
        except dbapi.StandardError as e:
            print(e)
        except dbapi.DatabaseError as e:
            print(e)

        trvVista = Gtk.TreeView(model=modelo)
        objetoSeleccion = trvVista.get_selection()
        objetoSeleccion.connect("changed", self.on_objetoSeleccion_changed)

        columnas = ("Nombre", "Apellido", "Número de teléfono")
        for i, nomColumna in enumerate(columnas):
            celda = Gtk.CellRendererText()  # Creo la celda en la columna
            if i == 0:
                celda.props.weight_set = True
                celda.props.weight = Pango.Weight.BOLD
            if i==2:
                celda.props.editable = True
                celda.connect("edited", self.on_celdaTelefono_edited, modelo, i)# La i está redundante, pero es para que se vea que es la columna 2, que es la del telefono

            col = Gtk.TreeViewColumn(nomColumna, celda, text=i)
            trvVista.append_column(col)

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caja.pack_start(trvVista, True, True, 0)
        grid = Gtk.Grid()
        caja.pack_start(grid, True, True, 0)

        lblNome = Gtk.Label(label="Nome")
        lblApellidos = Gtk.Label(label="Apellidos")
        lblTelefono = Gtk.Label(label="Telefono")
        self.txtNome = Gtk.Entry()
        self.txtApellidos = Gtk.Entry()
        self.txtTelefono = Gtk.Entry()
        btnEngadir = Gtk.Button(label="Engadir")
        btnBorrar = Gtk.Button(label="Borrar")
        grid.add(lblNome)
        grid.attach_next_to(self.txtNome, lblNome, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(lblApellidos, self.txtNome, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.txtApellidos, lblApellidos, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(lblTelefono, lblNome, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(self.txtTelefono, lblTelefono, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(btnEngadir, self.txtTelefono, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(btnBorrar, btnEngadir, Gtk.PositionType.BOTTOM, 2, 1)
        btnEngadir.connect("clicked", self.on_btnEngadir_clicked, modelo)
        btnBorrar.connect("clicked", self.on_btnBorrar_clicked, objetoSeleccion)#el objetoSeleccion es el metodo getSelection en la vista del treeview. Nos permite seleccionar elementos. Con el NONE decimos que no se pueda

        self.add(caja)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_objetoSeleccion_changed(self, seleccion):
        (modelo, fila) = seleccion.get_selected()
        print(modelo[fila][0], modelo[fila][1], modelo[fila][2])

    def on_btnBorrar_clicked(self, boton, seleccion):
        (modelo, fila) = seleccion.get_selected()# seleccion tiene este metodo qyue nos permite obetener una refrencia al modelo y a las filas (es una tupla??). Fijarse con que elemento (modelo, columna, celda..) estoy usando para saber cual usar y conectar.

        try:
            bbdd = dbapi.connect("bdListinTelefonico.dat")
            cursor = bbdd.cursor()
            cursor.execute("""delete from listaTelefonos where telefono = ?""", (modelo[fila][2],))# el elemento 2 es el telefono. Pongo la , final porque es una tupla.
            bbdd.commit()
            cursor.close()
            bbdd.close()
        except dbapi.Error as e:
               print(e)
        except dbapi.DatabaseError as e:
               print(e)

        modelo.remove(fila)# apunta a la fila que queremos borrar>

    def on_btnEngadir_clicked(self, boton, modelo):

        if self.txtNome.get_text() != "" and self.txtApellidos.get_text() != "" and self.txtTelefono.get_text() != "":
            elemento = self.txtNome.get_text(), self.txtApellidos.get_text(), self.txtTelefono.get_text()

        modelo.append(elemento)
        self.txtNome.set_text("")
        self.txtApellidos.set_text("")
        self.txtTelefono.set_text("")

        try:
            bbdd = dbapi.connect("bdListinTelefonico.dat")
            cursor = bbdd.cursor()
            cursor.execute("""insert into listaTelefonos values(?, ?, ?)""", elemento)
            bbdd.commit()
            cursor.close()
            bbdd.close()
        except dbapi.Error as e:
               print(e)
        except dbapi.DatabaseError as e:
               print(e)


    def on_celdaTelefono_edited(self, celda, fila, texto, modelo, columna):# Para editar pulso dos veces en el telefono y me deja escribir. El texto es lo que escribo. El modelo es el modelo de la tabla. La columna es la columna que estoy editando.
        modelo[fila][columna] = texto
        try:
            bbdd = dbapi.connect("bdListinTelefonico.dat")
            cursor = bbdd.cursor()
            cursor.execute("""update listaTelefonos set telefono = ? where nome = ?""", (texto, modelo[fila][0]))
            bbdd.commit()
            cursor.close()
            bbdd.close()
        except dbapi.Error as e:
               print(e)
        except dbapi.DatabaseError as e:
               print(e)


if __name__ == "__main__":
    miPrimeraVentana()
    Gtk.main()
