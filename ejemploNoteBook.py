import gi
from boxConBotones import BoxConBotones #del modulo boxConBotones importame la clase BoxConBotones


gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk

class ejemploNoteBook(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de NoteBook")

        notebook = Gtk.Notebook()

        pagina1 = Gtk.Box()
        pagina1.set_border_width(10)
        pagina1.add(Gtk.Label(label = "Pagina por defecto"))
        notebook.append_page(pagina1, Gtk.Label(label ="Titulo de la pagina"))

        pagina2 = Gtk.Box()#uso box pero puedo usar cualquier otro layout de los que usamos anteriormente
        pagina2.set_border_width(5)
        pagina2.add(Gtk.Label(label = "Pagina con una imagen"))
        notebook.append_page(pagina2, Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU))

        notebook.append_page(BoxConBotones(), Gtk.Label(label="Box con botones"))#llamo a la clase BoxConBotones del modulo boxConBotones

        self.add(notebook)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ =="__main__":
    ejemploNoteBook()
    Gtk.main()

