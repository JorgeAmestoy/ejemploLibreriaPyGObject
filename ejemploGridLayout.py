import gi


gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk

class ejemploGridLayout(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo Grid layout")

        boton1 = Gtk.Button(label="Boton 1")
        boton2 = Gtk.Button(label="Boton 2")
        boton3 = Gtk.Button(label="Boton 3")
        boton4 = Gtk.Button(label="Boton 4")
        boton5 = Gtk.Button(label="Boton 5")
        boton6 = Gtk.Button(label="Boton 6")


        '''Formas de usar el Grid(la red, malla:
        Es como una parrilla. YA viene
        la forma predeterminada, y nosotros vamos colocándolo.
        Grid.add(control)
        Grid.attach(control,columna,fila,ancho,alto)
        Grid.attach_next_to(control, controlcercano, posicion, ancho, alto)
        Aqui mejor terminarlo y al ejecutar, cambiar si algo está mal, no 
        hacerlo durante la marcha       
        '''
        red = Gtk.Grid()
        red.add(boton1)
        red.attach(boton2,1,0,2,1)
        red.attach(boton3, 0, 1, 1, 2)
        red.attach_next_to(boton4, boton3, Gtk.PositionType.RIGHT,2,1)
        red.attach_next_to(boton5, boton4, Gtk.PositionType.BOTTOM, 1, 1)
        red.attach_next_to(boton6, boton5, Gtk.PositionType.RIGHT, 1, 1)


        self.add(red)
        self.connect("delete-event",
                     Gtk.main_quit)
        self.show_all()

if __name__ =="__main__":
    ejemploGridLayout()
    Gtk.main()

