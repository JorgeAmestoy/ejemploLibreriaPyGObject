import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con check e radio button")

        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)


        frameMarco = Gtk.Frame(label = "Opciones excluyentes")
        caja.pack_start(frameMarco, False, False, 2)
        cajaRadioButton = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)


        rbtBoton1 = Gtk.RadioButton.new_with_label_from_widget(None,"Boton 1")
        rbtBoton1.connect("toggled", self.on_rbtBoton_toggled,"1")#El evento de estos controles es el toggled
        cajaRadioButton.pack_start(rbtBoton1,"False", "False", 2)

        rbtBoton2 = Gtk.RadioButton.new_from_widget(rbtBoton1)
        rbtBoton2.set_label("Boton 2")
        rbtBoton2.connect("toggled", self.on_rbtBoton_toggled,"2")
        cajaRadioButton.pack_start(rbtBoton2, "False", "False", 2)#Para meterlo en la caja

        rbtBoton3= Gtk.RadioButton.new_with_mnemonic_from_widget(rbtBoton1, "_Boton 3")#ES otra forma. Con una combinacion de teclas me permite activar el boton3, en este caso pulsando alt+ b en el teclado, te va a la opcion 3
        rbtBoton3.connect("toggled", self.on_rbtBoton_toggled,"3")
        cajaRadioButton.pack_start(rbtBoton3, "False", "False", 2)
        frameMarco.add(cajaRadioButton)

        checkBoton4 = Gtk.CheckButton()
        checkBoton4.set_label("Check 4")
        checkBoton4.connect("toggled", self.on_checkBoton_toggled)
        caja.pack_start(checkBoton4, False, False,2)

        #Otra forma de hacerlo con el new with label
        checkBoton5 = Gtk.CheckButton.new_with_label("Check 5")
        checkBoton5.connect("toggled",self.on_checkBoton_toggled)
        caja.pack_start(checkBoton5, False, False, 2)




        self.add(caja)

        self.connect("delete-event",Gtk.main_quit)
        self.show_all()

    #Cuando se selecciona una opcion, ocurren  dos "eventos". La opcion a se vuelve true y la b, por no pulsarla, false.
    def on_rbtBoton_toggled(self, boton, numero):
        if boton.get_active():
            print("Boton ", numero, "foi activado")
        else:
            print("Boton ", numero, "foi desactivado")


    def on_checkBoton_toggled(self, checkBoton):
        if checkBoton.get_active():
            print("CheckButton activado: ", checkBoton.get_label())
        else:
            print("ChkButton desactivado: ", checkBoton.get_label())


    def on_btnBoton_clicked(self, boton, etiqueta):
        etiqueta.set_text("Hola alumnos de Gtk")

    def on_txtSaludo_activate(self, cuadroDeTexto, etiqueta):
        etiqueta.set_text(cuadroDeTexto.get_text())

if __name__ =="__main__":
    primeraVentana()
    Gtk.main()

