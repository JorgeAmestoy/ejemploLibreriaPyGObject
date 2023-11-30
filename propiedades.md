## TREEVIEW<br>


[referencia](./ejemploTreeview.py)<br><br>

**Gtk.ListStore(str,str,str)**

- Uso de **tuplas**,**enumerate**, 
- **Append** -> soloa admite un parametro. POdemos mandar una lista/tupla de 20 elemetnos
pero tiene que mandarse como un solo elemento, como una lista vaya. Si la lista es de un solo elemento, igual.

- EN el treeview esta el modelo, luego la vista, el treeview, que sería como la tabla, la columna y la celda. Así,. hay que saber dependiendo del caso,
con cual de estos vamos a interactuar.

**CellRenderer**: hay varios tipos de este:
text para texto,
Pixbuf para imagenes
Toggle para checkbox, radiobutton
Combo para combobox.
Progress, una barra de progreso para porcentajes(es limitado por estar dentro de una tabla)
Spiner..

**celda.props** -> nos permite acceder a las propiedades de la celda, en exte caso un cellrendeerertext. Por ejemplo, poner
el texto en negrilla. EStas propiedades se ven en el [navegador](https://lazka.github.io/pgi-docs/Gtk-3.0/classes/CellRendererText.html) .
 **celda.props.weight_set = Pango.Weight.BOLD** -> Pango es una libreria 

boxCOnBotones no funciona porque lo usamos para importar en otros proectos.

expand: 

fill: No ocupa todo el espacio dispnible si pongo false.

padding:

LOs controles de textos dejarlos crecer(expand true). Cuadros de texto y botones tampoco. PROBAR.<br>
