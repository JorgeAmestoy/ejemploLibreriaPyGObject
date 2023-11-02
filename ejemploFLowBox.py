import gi


gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk

class ejemploFlowBox(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Exemplo FlowBox")
        self.set_default_size(300,250)

        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)#EL primero digo que no salga el scroll de forma horizontal, el segundo digo que si salga de forma vertical

        flowBox = Gtk.FlowBox()
        flowBox.set_valign(Gtk.Align.START)
        flowBox.set_max_children_per_line(30)#maximo numero de elementos que puede haber por linea¿?
        flowBox.set_selection_mode(Gtk.SelectionMode.NONE)#Para seleccionar elementos. Con el NONE decimos que no se pueda
        self.crearFlowBox(flowBox)


        scroll.add(flowBox)
        self.add(scroll)
        self.connect("delete-event", Gtk.main_quit)
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

    def crearFlowBox(self, flowb):
        colores = ["AliceBlue",
                   "AntiqueWhite",
                   "AntiqueWhite1",
                   "AntiqueWhite2",
                   "AntiqueWhite3",
                   "AntiqueWhite4",
                   "aqua",
                   "aquamarine",
                   "aquamarine1",
                   "aquamarine2",
                   "aquamarine3",
                   "aquamarine4",
                   "azure",
                   "azure1",
                   "azure2",
                   "azure3",
                   "azure4",
                   "beige",
                   "bisque",
                   "bisque1",
                   "bisque2",
                   "bisque3",
                   "bisque4",
                   "black",
                   "BlanchedAlmond",
                   "blue",
                   "blue1",
                   "blue2",
                   "blue3",
                   "blue4",
                   "BlueViolet",
                   "brown",
                   "brown1",
                   "brown2",
                   "brown3",
                   "brown4",
                   "burlywood",
                   "burlywood1",
                   "burlywood2",
                   "burlywood3",
                   "burlywood4",
                   "CadetBlue",
                   "CadetBlue1",
                   "CadetBlue2",
                   "CadetBlue3",
                   "CadetBlue4",
                   "chartreuse",
                   "chartreuse1",
                   "chartreuse2",
                   "chartreuse3",
                   "chartreuse4",
                   "chocolate",
                   "chocolate1",
                   "chocolate2",
                   "chocolate3",
                   "chocolate4",
                   "coral",
                   "coral1",
                   "coral2",
                   "coral3",
                   "coral4"]
        for color in colores:
            boton = self.boton_con_color(color)
            flowb.add(boton)



    def on_btnBoton_clicked(self, boton, etiqueta):
        etiqueta.set_text("Hola alumnos de Gtk")

    def on_txtSaludo_activate(self, cuadroDeTexto, etiqueta):
        etiqueta.set_text(cuadroDeTexto.get_text())

if __name__ =="__main__":
    ejemploFlowBox()
    Gtk.main()

