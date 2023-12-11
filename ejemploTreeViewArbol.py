import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk


class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de TreeView Filtrado")

        self.set_default_size(250, 100)
        self.set_border_width(10)

        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        modelo = Gtk.TreeStore(str,int)

        for abuelo in range(5):
            punteroAbuelo = modelo.append(None, ['Abuelo', abuelo])# Aqui tengo que poner None porque es el primer elemento, no tiene padre. ¿?
            for padre in range(4):
                punteroPadre = modelo.append(punteroAbuelo, ['Padre %i del abuelo %i '% (padre, abuelo), padre])
                for hijo in range(3):
                   punteroHijo = modelo.append(punteroPadre, ['Hijo %i del padre %i del abuelo %i '% (hijo, padre, abuelo), hijo])
                   for nieto in range(2):
                       modelo.append(punteroHijo, ['Nieto %i del hijo %i del padre %i del abuelo %i '%(nieto, hijo, padre, abuelo), nieto])

        treeView = Gtk.TreeView(model=modelo)
        tryColumna = Gtk.TreeViewColumn("Parentesco")
        treeView.append_column(tryColumna)
        celda = Gtk.CellRendererText()
        tryColumna.pack_start(celda, True)
        tryColumna.add_attribute(celda, "text", 0)

        tryColumna = Gtk.TreeViewColumn("Orden")
        treeView.append_column(tryColumna)
        celda = Gtk.CellRendererText()
        tryColumna.pack_start(celda, True)
        tryColumna.add_attribute(celda, "text", 1)

        cajaV.pack_start(treeView, True, True, 0)


        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()



if __name__ =="__main__":
    primeraVentana()
    Gtk.main()
