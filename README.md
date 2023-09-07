# Librería de números complejos 
El proyecto presentado a continuación tiene como objetivo el de ser una herramienta para poder realizar operaciones básicas con los números complejos, y tambien en espacios vectoriales complejos.
# Instalación y requisitos 
Para el manejo de matrices y vectores, usamos para su facilidad la libreria Numpy, por lo que debe estar descargado en su interprete, ademas se necesita un programa como PyCharm, Visual Studio, para poder ver el desarrollo y ejecución del proyecto.
# Ejecución de las pruebas 
Para cada operación ofrecida en esta calculadora básica de complejos, se tienen definidas 2 pruebas, para ver si en principio esta es funcional con la ayuda de la librería unittest comparamos los valores que nos deberían dar en un principio, teniendo solo que dar ejecutar para ver si hay errores.
# ¿Por qué estas pruebas?
A lo largo de las pruebas se implementaron ejemplos con diferentes números complejo.
En suma, se realiza una operación con los 2 siguientes números (-7 + 4i) + (4.2 - 3i) esto debido a que queríamos ver si se comportaba adecuadamente cuando la parte real da como resultado un decimal y si la parte imaginaria suma bien cuando no son del mismo signo, siguiendo esta lógica en las diferentes operaciones usamos operaciones con una complejidad idónea para ver que se realizara correctamente.
En resta, se realiza una operación con estos números (-8-4i) - (10+4i) ya que, queríamos ver si respetaba el signo menos de formula teniendo que realizar así la operación, separamos parte real e imaginaria (-8-(10)) = (-8 -10) = -18, (-4i - (4i)) = -8i, dándonos así este complejo -18 - 8i.
En división se escogen estas pruebas, ya que sabemos que iba a dar un numero complejo con parte real e imaginaria decimal, para verificar si con estos números se pueden tener problemas.
En modulo se escoge el siguiente número (9i) debido a que sabemos que debería dar el 9 debido que la raíz cuadrada de un numero al cuadrado, es el mismo número.
En conjugado escogemos estos números, debido a que la parte imaginaria no tienen el mismo signo, uno es positivo y otro negativo.
Usando muchas de las funciones ya establecidas definimos nuevas herramientas para el desarrollo de funciones.
En la multiplicacion por una escalar/vector, definimos que el escalar puede ser tan solo un real, imaginario o complejo, dandonos en los tres casos correcto, En los inversos se puso tanto componentes de las matrices o vectores con partes solo real, imaginaria o compleja, en los conjugados hicimos un ejemplo tanto con vectores como para matrices.
# Autor
Daniel Fernando Aldana Bueno
