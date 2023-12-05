# EJERCICIO EXAMEN

## 1. CREO LA INTERFAZ
En este programa vamos a trabajar únicamente con el fichero **MAIN** Y CON LA **IU**.
Añadimos los botones y las cajas de texto que vamos a necesitar.

## 2. FUNCIONALIDAD DE LOS WIDGETS

```
   val iuScope = rememberCoroutineScope()

    var countingDown by remember { mutableStateOf(false) }
    var count by remember { mutableStateOf(20) }
    var puntuacion by remember { mutableStateOf(0) }
```

Usamos la **iuSCope** para permitir la ejecución continua de coroutines incluso después de recomposiciones.
Las demás variables son  de estado mutable y almacenan un booleano que indica si hay:
- una cuenta regresiva en curso
- un entero que representa el valor actual de la cuenta regresiva
- un entero que representa la puntuación del usuario.

Así, en el botón de **START**:
```
onClick = {
          countingDown = true
                 iuScope.launch {
                    while (count > 0) {
                          delay(1000)
                               count--
                     }
               }
         },
```
Así, cuando presionarmos el botón, se inicia una cuenta regresiva que disminuirá el valor de count cada segundo hasta llegar a cero, y esta acción está envuelta en una coroutine para no bloquear el hilo principal.
<br>
`text = count.toString(),`: convertimos el valor numérico de *count* en una
de cadena para que 
pueda ser visualizado en el elemento de texto.<br>
`text =  fraseActual.value.texto,`: accedemosal valor de la propiedad texto de ese objeto y lo asignamos al texto para
mostrar en la interfaz 

## FRASES ALEATORIAS


`data class Frase(var texto: String, var verdadero: Boolean)`:
Definomos una clase de datos llamada Frase par almacenar los datos. Tinene dos propiedades, una de tipo String y otra de tipo Booleano.


`var frases: MutableList<Frase> = mutableListOf()`: creamos una lista mutable de frases y la inicializamos con una lista vacía.


`var fraseActual: MutableState<Frase> = mutableStateOf(Frase("-", true))`: creamos una variable de estado mutable que almacena una frase y la inicializamos con una frase vacía.
```
@Composable
fun aux() {
    // introducir frases en la lista
    frases.add(Frase("el torneo de rugby cinco naciones, ahora es seis naciones", true))
    frases.add(Frase("en el cielo hay cinco estrellas", false))
    frases.add(Frase("el dia cinco de diciembre del 2023 es martes", true))
    frases.add(Frase("cinco más cinco son diez", true))
    frases.add(Frase("dos mas dos son cinco", false))
    frases.add(Frase("los elefantes tienen cinco patas", false))
    frases.add(Frase("las estaciones climáticas son cinco", false))
    frases.add(Frase("tenemos cinco dedos los humanos", true))
    frases.add(Frase("cinco días tiene la semana sin el Domingo y el Sábado", true))
    frases.add(Frase("una gallina pesa menos que cinco toneladas", true))

    // asignar una frase aleatoria
    fraseActual.value = frases.random()
}
```
Por último, la clase aux es la que se encarga de introducir las frases en la lista y
de asignar una frase aleatoria a la variable de estado fraseActual.