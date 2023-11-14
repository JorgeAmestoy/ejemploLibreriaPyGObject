import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo expediente académico")

        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)

        #Si hubiese que poner 100 alumnos, habria que buscar forma de repetir esto para no escribirlo 100 veces
        cajaAlumno = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing = 10)
        cajaPrincipal.pack_start(cajaAlumno, True, True, 0)
        lblAlumno = Gtk.Label(label="Alumno")
        cajaAlumno.pack_start(lblAlumno, False, True, 2)#Pongo 100 de padding a la label Alumno, es decir, quiero que haya mas espacio a su alrededor
        self.txtNombre = Gtk.Entry()
        cajaAlumno.pack_start(self.txtNombre, False, False, 5)
        self.txtApellidos = Gtk.Entry()
        cajaAlumno.pack_start(self.txtApellidos, True, False, 5)  # que si se extienda, que no se llene y de padding(relleno?) -> 5

        listBox = Gtk.ListBox()
        cajaPrincipal.pack_start(listBox, True, True, 0)
        fila = Gtk.ListBoxRow()

        cajaVerticalFila = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 4)
        fila.add(cajaVerticalFila)

        cajaHorizontalFila1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lblModulo = Gtk.Label(label ="Cod")
        cajaHorizontalFila1.pack_start(lblModulo, False, False, 2)

        self.checkButtonBilingueCod = Gtk.CheckButton()
        self.checkButtonBilingueCod.set_label("Bilingüe")
        cajaHorizontalFila1.pack_start(self.checkButtonBilingueCod, False, False, 2)

        cajaHorizontalFila2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lblNota = Gtk.Label(label ="Nota")
        cajaHorizontalFila2.pack_start(lblNota, False, False, 2)

        self.txtNotaCod = Gtk.Entry()
        cajaHorizontalFila2.pack_start(self.txtNotaCod, False, False, 2)
        cajaVerticalFila.pack_start(cajaHorizontalFila1, True, True, 0)
        cajaVerticalFila.pack_start(cajaHorizontalFila2, True, True, 0)

        listBox.add(fila)

        fila = Gtk.ListBoxRow()

        cajaVerticalFila = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        fila.add(cajaVerticalFila)

        cajaHorizontalFila1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lblModulo = Gtk.Label(label="Prog")
        cajaHorizontalFila1.pack_start(lblModulo, False, False, 2)

        self.checkButtonBilingueProg = Gtk.CheckButton()
        self.checkButtonBilingueProg.set_label("Bilingüe")
        cajaHorizontalFila1.pack_start(self.checkButtonBilingueProg, False, False, 2)

        cajaHorizontalFila2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lblNota = Gtk.Label(label="Nota")
        cajaHorizontalFila2.pack_start(lblNota, False, False, 2)

        self.txtNotaProg = Gtk.Entry()
        cajaHorizontalFila2.pack_start(self.txtNotaProg, False, False, 2)
        cajaVerticalFila.pack_start(cajaHorizontalFila1, True, True, 0)
        cajaVerticalFila.pack_start(cajaHorizontalFila2, True, True, 0)

        listBox.add(fila)

        botonGuardar = Gtk.Button(label="Guardar")
        cajaPrincipal.pack_start(botonGuardar, False, False, 4)
        botonGuardar.connect("clicked", self.on_botonGuardar_clicked)


        self.add(cajaPrincipal)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


    def on_botonGuardar_clicked(self, boton):
        lista = list()#lista=[]. Esºta sería otra forma de hacerlo.
        lista.append(self.txtNombre.get_text())
        lista.append(self.txtApellidos.get_text())
        modulo = list()
        modulo.append("Cod")
        modulo.append(float(self.txtNotaCod.get_text()))
        modulo.append(self.checkButtonBilingueCod.get_active())#Nos de vuelve si es true o false
        lista.append(modulo)
        modulo = list()
        modulo.append("Prog")
        modulo.append(float(self.txtNotaProg.get_text()))
        modulo.append(self.checkButtonBilingueProg.get_active()) #Nos devuelve si es true o false
        lista.append(modulo)
        print(lista)
        return lista



if __name__ =="__main__":
    primeraVentana()
    Gtk.main()