import pathlib

import gi
from gi.overrides.Gio import Gio

gi.require_version("Gtk","3.0")
from gi.repository import Gtk


class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de TreeView Filtrado")

        self.set_default_size(250, 100)
        self.set_border_width(10)

        area = Gtk.FlowBox()
        contidoCarpeta = pathlib.Path('.')

        for elemento in contidoCarpeta.iterdir():
            caixa = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
            tipo = 'folder' if elemento.is_dir() else 'text-x-generic'
            icono = Gio.ThemedIcon(name=tipo)
            imaxe = Gtk.image.new_from_gicon(icono, Gtk.IconSize.MENU)
            caixa.pack_start(imaxe, True, True, 0)
            caixa.pack_start(Gtk.Label(label=elemento.name), True, True, 0)






        self.add(area)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()



if __name__ =="__main__":
    primeraVentana()
    Gtk.main()