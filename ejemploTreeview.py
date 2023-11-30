import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Pango

#DECLARO TUPLAS
columnass = ("Nome", "Apellido", "Número de teléfono")# Son todos Strings, como declar'en el modelo ListStore
agendaTelefono = (("Jorge", "Amestoy", "669 823 235"),
                  ("Lucia", "Balsa", "633 472 356"),
                  ("Angi", "Casella", "555 555 555"),
                  )
class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Primera ventana con Gtk")

        #USo self para hacer referencia a la window
        self.set_default_size(250,100)#Tamaño por defecto
        self.set_border_width(10)

        modelo = Gtk.ListStore(str,str,str)# Elementos vacios

        for usuario in agendaTelefono:#HAgo append de una tupla pero podria ser de una base de datos también
            modelo.append(usuario)

        treeVista = Gtk.TreeView(model=modelo)
        objetoSeleccion = treeVista.get_selection()# NOs da referencia a un objeto que nos permite trabajar con la seleccion de los elkementos.
        objetoSeleccion.connect("changed", self.on_objectoSeleccion_changed) # Así tiene señales, una de ellas la changed.

        for i,nomColumna in enumerate(columnass):# Dentro de columnas creo la celda. POr cada columna va a hacer lo que esté dentro y lo guarda en la variable columna. Recorro la tupla que declare arriba de toddo, antes de la clase. i empieza por cero, leugo 1 y luego 2. SERÁ PRIMERO nombre, luego apellido y luego telefono.
            celda = Gtk.CellRendererText()
            if i ==0:# Cuando i sea cero, la celda tendrá la siguiente propiedad
                celda.props.weight_set = True
                celda.props.weight_set = Pango.Weight.BOLD
            col = Gtk.TreeViewColumn(nomColumna,celda,text=i)#Diferencia columnas, de columna y col.  La i te dice la columna. SI estoy n la celda de nombre, es i =0, ape =1 y tlf = 2.

            treeVista.append_column(col)# Añadimos la columna
            # Esto de crear celda, etc lo tendria que hacer tres veces porque puse que iab a tener tres columnas(nom,ape y tlf). Uso for para no hacerlo 3 veces.


        cajaV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing =10)
        cajaV.pack_start(treeVista, True, True, 0)# expand es para lo de coger al esquina y poder estirarlo mas, como las ventanas de google.


        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_objectoSeleccion_changed(self, seleccion):
        (modelo, fila) = seleccion.get_selected()# seleccion tiene este metodo qyue nos permite obetener una refrencia al modelo y a las filas (es una tupla??). Fijarse con que elemento (modelo, columna, celda..) estoy usando para saber cual usar y conectar.
        print(modelo[fila][0], modelo[fila][1], modelo[fila][2])




if __name__ =="__main__":
    primeraVentana()
    Gtk.main()

