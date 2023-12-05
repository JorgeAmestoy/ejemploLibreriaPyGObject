import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import sqlite3 as dbapi

class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de TreeView Filtrado")

        self.set_default_size(250, 100)
        self.set_border_width(10)

        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        modelo = Gtk.ListStore(str, str, int, str, bool)
        try:
            bbdd = dbapi.connect("baseDatos2.dat")
            cursor = bbdd.cursor()
            cursor.execute("select * from usuarios")
            for fila in cursor:
                modelo.append(fila)
        except dbapi.DatabaseError as e:
            print("Erro insertando usuarios: " + e)
        finally:
             cursor.close()
             bbdd.close()

        tryDatosUsarios = Gtk.TreeView(model=modelo)
        seleccion = tryDatosUsarios.get_selection()

        for i, tituloColumna in enumerate(["Dni", "Nome"]):#Aqui pongo las columnas que quiero que se muestren. La i es la posicion de la columna en la tupla y el titulo es el nombre de la columna.
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)# Para la columna necesito el titulo, la celda y el texto. El texto es la posicion de la columna en la tupla.
            tryDatosUsarios.append_column(columna)

            celda = Gtk.CellRendererProgress()
            columna = Gtk.TreeViewColumn("Edade", celda, value=2)
            tryDatosUsarios.append_column(columna)

        # Combo con un modelo
        modeloCombo = Gtk.ListStore(str)
        modeloCombo.append(("Home",))# Fijarme en que pongo una coma al final. Es una tupla de un elemento.
        modeloCombo.append(("Muller",))
        modeloCombo.append(("Outro",))
        celda = Gtk.CellRendererCombo()# Para la barra de combo del porcentaje
        celda.set_property("editable", True)
        celda.props.model = modeloCombo
        #celda.set_property("model", modeloCombo)# Es lo mismo que la linea de arriba
        celda.set_property("text-column", 0)# La columna que quiero que se muestre es la 0, la primera.
        celda.set_property("has-entry", False)# Para que no se pueda escribir en el combo
        columna = Gtk.TreeViewColumn("Xenero", celda, text=3)
        tryDatosUsarios.append_column(columna)


        cajaV.pack_start(tryDatosUsarios, True, True, 2)


        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

if __name__ =="__main__":
    primeraVentana()
    Gtk.main()

