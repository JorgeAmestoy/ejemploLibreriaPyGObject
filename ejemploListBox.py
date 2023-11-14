import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class FilaListBoxConDatos(Gtk.ListBoxRow):

    def __init__(self, palabra):#Una clase a la que le asocio una palabra
        super().__init__()
        self.palabra = palabra#Inicializamos la palabra
        self.add(Gtk.Label(label=palabra))#Para que se vea en la interfaz

#https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ListBox.html#Gtk.ListBox.do_row_activated
class PrimeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplom ListBox")

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)

        listbox = Gtk.ListBox()
        caja.pack_start(listbox, True, True, 0)

        elementos = "Esto es una cadena para ordenar en el ListBox, para el ListBox".split()
        for palabra in elementos:
            listbox.add(FilaListBoxConDatos(palabra))

        def funcion_ordenacion(fila1,fila2):
            return fila1.palabra.lower()>fila2.palabra.lower()

        #Para filtrar que no salga una palabra, por ejemplo: listbox
        def funcion_filtrado(fila):
            return False if fila.palabra == "ListBox" else True#Otra forma de poner un if else normal

        listbox.set_sort_func(funcion_ordenacion)#Me pone que tambiçen tengo poner user_data, pero como no usamos, no hace falta
        listbox.set_filter_func(funcion_filtrado)#FIJARNOS QUE LLAMAMOS A LA FUNCION SIN PONER LOS () FINALES A funcion_filtrado cuando por defecto los coge
        listbox.connect("row-activated", self.on_row_activated)


        self.add(caja)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

    def on_row_activated(self, listbox, fila):
        print(fila.palabra)



if __name__ =="__main__":
    PrimeraVentana()
    Gtk.main()