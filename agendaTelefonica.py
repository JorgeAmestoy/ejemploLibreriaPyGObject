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
            col = Gtk.TreeViewColumn(nomColumna, celda, text=i)
            trvVista.append_column(col)

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        caja.pack_start(trvVista, True, True, 0)

        self.add(caja)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_objetoSeleccion_changed(self, seleccion):
        (modelo, fila) = seleccion.get_selected()
        print(modelo[fila][0], modelo[fila][1], modelo[fila][2])


if __name__ == "__main__":
    miPrimeraVentana()
    Gtk.main()