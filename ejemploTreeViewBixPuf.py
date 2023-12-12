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

        modelo = Gtk.ListStore(str,str)
        modelo.append(("Novo", "document-new"))
        modelo.append(("Abrir", "document-new"))
        modelo.append(("Gardar", "document-new"))

        treeview = Gtk.TreeView(model=modelo)
        celdaTexto = Gtk.CellRendererText()
        col_texto = Gtk.TreeViewColumn("Texto", celdaTexto, text=0)
        treeview.append_column(col_texto)

        celdaImaxe = Gtk.CellRendererPixbuf()
        col_imaxe = Gtk.TreeViewColumn("Imaxe", celdaImaxe, icon_name=1)
        treeview.append_column(col_imaxe)

        cajaV.pack_start(treeview, True, True, 0)





        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()



if __name__ =="__main__":
    primeraVentana()
    Gtk.main()