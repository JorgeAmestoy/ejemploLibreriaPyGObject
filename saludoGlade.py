import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk

class Aplicacion():#NO HEREDA DE GTK WINDOW. NO HAY HERENCIA.
    def __init__(self):

       builder = Gtk.Builder()#Para hacer una interfaz en base a un xml¿?
       builder.add_from_file("ejemplo1.glade")

       wndVentanaPrincipal = builder.get_object("wndVentanaPrincipal")
       self.lblEtiqueta = builder.get_object("lblEtiqueta")
       self.txtNombre = builder.get_object("txtNombre")#Lo de verde tiene que llamarse igual a como lo llamaste en xml
       self.btnSaludar = builder.get_object("btnSaludar")
       senales = {
           "on_btnSaludar_clicked" : self.on_btnBoton_clicked,#Le quitó los parentesis
           "on_txtNombre_activate":self.on_txtNombre_activate#Fijarse en que tiene mismos nombres
       }

       builder.connect_signals(senales)

        #Cambiar en los metodos de abajo de onbotom...




    def on_btnBoton_clicked(self, boton):
        self.lblEtiqueta.set_text("Hola "+ self.txtNombre.get_text())

    def on_txtNombre_activate(self, cuadroDeTexto):
        self.lblEtiqueta.set_text("Hola "+ cuadroDeTexto.get_text())

if __name__ =="__main__":
    Aplicacion()
    Gtk.main()

