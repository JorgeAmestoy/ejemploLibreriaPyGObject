import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Primera ventana con Gtk")

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)

        imagen = Gtk.Image()
        imagen.set_from_file("paisaje.png")
        caja.pack_start(imagen,True,True,5)#expand,fill,padding. Buscar diferencias.
        lblEtiqueta = Gtk.Label(label="Hola a todos")
        caja.pack_start(lblEtiqueta,False,False,5)
        txtSaludo = Gtk.Entry()
        txtSaludo.connect("activate", self.on_txtSaludo_activate, lblEtiqueta)
        caja.pack_start(txtSaludo, True, False, 5)#que si se extienda, que no se llene y de padding(relleno?) -> 5
        btnBoton = Gtk.Button(label="Púlsame")
        btnBoton.connect("clicked",self.on_btnBoton_clicked, lblEtiqueta)
        caja.pack_start(btnBoton, False, False, 5)#Lo bueno de las cajas es que puedes añadir toddo lo que quieras (etiqueta, boton..)

        self.add(caja)#En gtk solo podemos poner una etiqueta..
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

