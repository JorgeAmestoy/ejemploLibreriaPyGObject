import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import sqlite3 as dbapi

class primeraVentana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de TreeView Filtrado")

        self.set_default_size(250, 100)
        self.set_border_width(10)

        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)

        cajaV2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        cajaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)

        lblNome = Gtk.Label(label="Nome")
        cajaH.pack_start(lblNome, False, False, 3)

        self.txtNome = Gtk.Entry()
        cajaH.pack_start(self.txtNome, False, False, 3)

        cajaV.pack_start(cajaH, True, True, 0)

        lblDni = Gtk.Label(label = "DNI")
        cajaH.pack_start(lblDni, False, False, 3)
        self.txtDni = Gtk.Entry()
        cajaH.pack_start(self.txtDni, False, False, 3)

        cajaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        lblEdade = Gtk.Label(label = "Edade")
        cajaH2.pack_start(lblEdade, False, False,3)
        self.txtEdade = Gtk.Entry()
        cajaH2.pack_start(self.txtEdade, False, False, 3)
        cajaV.pack_start(cajaH2, True, True, 0)
        lblXenero = Gtk.Label(label= "Xenero")
        cajaH2.pack_start(lblXenero, False, False, 3)
        cajaVR = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        cajaH2.pack_start(cajaVR, False, False, 3)

        # RADIO BUTTONS
        rbtHome = Gtk.RadioButton(label="Home")
        rbtMuller = Gtk.RadioButton.new_with_label_from_widget(rbtHome, label="Muller")
        rbtOutros = Gtk.RadioButton.new_with_label_from_widget(rbtHome, label="Outro")
        cajaVR.pack_start(rbtHome, True, True, 2)
        cajaVR.pack_start(rbtMuller, True, True, 2)
        cajaVR.pack_start(rbtOutros, True, True, 2)
        rbtHome.connect("toggled", self.on_xenero_toggled, "Home")
        rbtMuller.connect("toggled", self.on_xenero_toggled, "Muller")
        rbtOutros.connect("toggled", self.on_xenero_toggled, "Outro")

        cajaH3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        cajaV.pack_start(cajaH3, False, False,3)

        # BOTONES

        self.btnNovo = Gtk.Button(label= "Novo")
        self.btnNovo.connect("clicked", self.on_btnNovo_clicked)
        cajaH3.pack_start(self.btnNovo, False, False, 3)
        self.btnEditar = Gtk.Button(label="Editar")
        self.btnNovo.connect("clicked", self.on_btnEditar_clicked)
        cajaH3.pack_start(self.btnEditar, False, False, 3)
        btnAceptar = Gtk.Button(label = "Aceptar")
        self.btnNovo.connect("clicked", self.on_btnAceptar_clicked)
        cajaH3.pack_start(btnAceptar, False, False, 3)
        btnCancelar = Gtk.Button(label = "Cancelar")
        self.btnNovo.connect("clicked", self.on_btnCancelar_clicked)
        cajaH3.pack_start(btnCancelar, False, False, 3)


        self.filtradoXenero = "None"
        modelo = Gtk.ListStore(str, str, int, str, bool)
        modelo_filtrado = modelo.filter_new()
        modelo_filtrado.set_visible_func(self.filtro_usuarios_xenero)

        try:
            bbdd = dbapi.connect("baseDatos2.dat")
            cursor = bbdd.cursor()
            cursor.execute("select * from usuarios")
            for fila in cursor:
                modelo.append(fila)
        except dbapi.DatabaseError as e:
            print("Erro insertando usuarios: " + e)
        finally:
             cursor.close()
             bbdd.close()


        #tryDatosUsarios = Gtk.TreeView(model=modelo)
        tryDatosUsarios = Gtk.TreeView(model=modelo_filtrado)  # Ver commits para entender cuando he usado un modelo y cuando otro.
        seleccion = tryDatosUsarios.get_selection()

        for i, tituloColumna in enumerate(["Dni", "Nome"]):#Aqui pongo las columnas que quiero que se muestren. La i es la posicion de la columna en la tupla y el titulo es el nombre de la columna.
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)# Para la columna necesito el titulo, la celda y el texto. El texto es la posicion de la columna en la tupla.
            tryDatosUsarios.append_column(columna)

            celda = Gtk.CellRendererProgress()
            columna = Gtk.TreeViewColumn("Edade", celda, value=2)
            tryDatosUsarios.append_column(columna)

        # Combo con un modelo
        modeloCombo = Gtk.ListStore(str)
        modeloCombo.append(("Home",))# Fijarme en que pongo una coma al final. Es una tupla de un elemento.
        modeloCombo.append(("Muller",))
        modeloCombo.append(("Outro",))
        celda = Gtk.CellRendererCombo()# Para la barra de combo del porcentaje
        celda.set_property("editable", True)
        celda.props.model = modeloCombo
        #celda.set_property("model", modeloCombo)# Es lo mismo que la linea de arriba
        celda.set_property("text-column", 0)# La columna que quiero que se muestre es la 0, la primera.
        celda.set_property("has-entry", False)# Para que no se pueda escribir en el combo
        celda.connect("edited", self.on_celdaXenero_edited, modelo_filtrado, 3)

        columna = Gtk.TreeViewColumn("Xenero", celda, text=3)
        tryDatosUsarios.append_column(columna)
        cajaV.pack_start(tryDatosUsarios, True, True, 2)

        cajaH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing=2)
        cajaV.pack_start(cajaH, True, True, 0)

        rbtHome = Gtk.RadioButton( label ="Home")
        rbtMuller = Gtk.RadioButton.new_with_label_from_widget(rbtHome, label = "Muller")
        rbtOutros = Gtk.RadioButton.new_with_label_from_widget(rbtHome, label ="Outro")
        cajaH.pack_start(rbtHome, True, True, 2)
        cajaH.pack_start(rbtMuller, True, True, 2)
        cajaH.pack_start(rbtOutros, True, True, 2)
        rbtHome.connect("toggled", self.on_xenero_toggled,"Home", modelo_filtrado)
        rbtMuller.connect("toggled", self.on_xenero_toggled, "Muller",  modelo_filtrado)
        rbtOutros.connect("toggled", self.on_xenero_toggled, "Outro", modelo_filtrado)



        self.add(cajaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def on_btnNovo_clicked(self):
        nome = self.txtNome.text()
        dni = self.txtDni.text()
        edade = self.txtEdade.text()

    def on_btnEditar_clicked(self):
        nome = self.txtNome.text()

    def on_btnAceptar_clicked(self):
        nome = self.txtNome.text()

    def on_btnCancelar_clicked(self):

        nome = self.txtNome.text()




    def on_celdaXenero_edited(self, celda, fila, texto, modelo, columna):# Para cambiar el valor de la columna xenero. Es un comboBox.
        try:
            bbdd = dbapi.connect("baseDatos2.dat")
            cursor = bbdd.cursor()
            cursor.execute("UPDATE usuarios set xenero = ? where dni = ?", (texto, modelo[fila][0]))
            bbdd.commit()

        except dbapi.DatabaseError as e:
            print("Erro insertando usuarios: " + e)
        finally:
            cursor.close()
            bbdd.close()

        modelo[fila][columna] = texto
        modelo.refilter()

    def on_xenero_toggled(self, botonSeleccionado, xenero, modelo):
        if botonSeleccionado.get_active():
            self.filtradoXenero = xenero
            modelo.refilter()


    def filtro_usuarios_xenero(self, modelo, fila, datos):
        if self.filtradoXenero is None or self.filtradoXenero == "None":
            return True
        else:
            return modelo[fila][3] == self.filtradoXenero



if __name__ =="__main__":
    primeraVentana()
    Gtk.main()

