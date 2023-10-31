import gi


gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk


class CajaConObjetoColor(Gtk.Box):
    def __init__(self):
        super().__init__()

        self.set_orientation(Gtk.Orientation.HORIZONTAL)


        cajaV1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 4)
        cajaV1.pack_start(self.boton_con_color("red"), True, True,2)
        cajaV1.pack_start(self.boton_con_color("yellow"), True, True, 2)
        cajaV1.pack_start(self.boton_con_color("purple"), True, True, 2)
        self.pack_start(cajaV1, True, True, 2)

        self.pack_start(self.boton_con_color("green"), True, True,2)

        cajaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10)
        cajaV2.pack_start(self.boton_con_color("blue"), True, True, 2)
        cajaV2.pack_start(self.boton_con_color("orange"), True, True, 2)
        self.pack_start(cajaV2, True, True, 2)

    def on_debuxa(self, control, cr, datos):
        contexto = control.get_style_context()
        ancho = control.get_allocated_width()
        alto = control.get_allocated_height()
        Gtk.render_background(contexto, cr, 0, 0, ancho, alto)

        r, g, b, a = datos["color"]
        cr.set_source_rgba(r, g, b, a)
        cr.rectangle(0, 0, ancho, alto)
        cr.fill()

    def boton_con_color(self, color):
        rgba = Gdk.RGBA()
        rgba.parse(color)

        boton = Gtk.Button()
        area = Gtk.DrawingArea()
        area.set_size_request(32, 24)
        area.connect("draw", self.on_debuxa, {"color": rgba})
        boton.add(area)
        return boton

class VentanaPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de Stack Layout")#Stack es apilar. Una pila de cosas.

        cajaVertical = Gtk.Box(orientation =Gtk.Orientation.VERTICAL, spacing = 6)

        tarjetas = Gtk.Stack()
        tarjetas.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        tarjetas.set_transition_duration(1000)

        #tipico boton con el check
        checkPulsame = Gtk.CheckButton(label = "Pulsame")
        tarjetas.add_titled(checkPulsame, "pulsame","Check pulsame")

        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<big>Esta es una etiqueta elegante </big>")
        tarjetas.add_titled(lblEtiqueta, "etiqueta","Una etiqueta")

        cajaConContenido = CajaConObjetoColor()
        tarjetas.add_titled(cajaConContenido,"caja", "Caja con contenido")


        botonesTarjetas = Gtk.StackSwitcher()
        botonesTarjetas.set_stack(tarjetas)
        cajaVertical.pack_start(botonesTarjetas, True, True,0)
        cajaVertical.pack_start(tarjetas, True, True,0)



        self.add(cajaVertical)
        self.connect("delete-event",
                     Gtk.main_quit)
        self.show_all()

    def on_debuxa(self,control,cr,datos):
        contexto = control.get_style_context()
        ancho = control.get_allocated_width()
        alto = control.get_allocated_height()
        Gtk.render_background(contexto,cr,0,0,ancho,alto)

        r,g,b,a = datos["color"]
        cr.set_source_rgba(r,g,b,a)
        cr.rectangle(0,0,ancho,alto)
        cr.fill()

    def boton_con_color(self,color):
        rgba = Gdk.RGBA()
        rgba.parse(color)

        boton = Gtk.Button()
        area = Gtk.DrawingArea()
        area.set_size_request(32,24)
        area.connect("draw",self.on_debuxa, {"color": rgba})
        boton.add(area)
        return boton



    def on_btnBoton_clicked(self, boton, etiqueta):
        etiqueta.set_text("Hola alumnos de Gtk")

    def on_txtSaludo_activate(self, cuadroDeTexto, etiqueta):
        etiqueta.set_text(cuadroDeTexto.get_text())

if __name__ =="__main__":
    VentanaPrincipal()
    Gtk.main()

