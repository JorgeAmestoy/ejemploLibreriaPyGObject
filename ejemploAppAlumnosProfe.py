import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo expediente academico")

        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)

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








        self.add(cajaPrincipal)#En gtk solo podemos poner una etiqueta..

        self.connect("delete-event",Gtk.main_quit)#se conecta a una funcion cuando ocurre un evento. Cuando cliqueamos en la esquina, creamos un delete-event.
        #En el Gtk.main_quit no poner los () finales.
        self.show_all()

#el segundo parametro de esta funcion puede ser cualquier nombre para recoger una referencia o control que genero la señal
#etiqueta es la referencia a lblEtiqueta
    def on_btnBoton_clicked(self, boton, etiqueta):
        etiqueta.set_text("Hola alumnos de Gtk")

    def on_txtSaludo_activate(self, cuadroDeTexto, etiqueta):
        etiqueta.set_text(cuadroDeTexto.get_text())

if __name__ =="__main__":
    primeraVentana()
    Gtk.main()