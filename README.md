# IPC2_Proyecto2_202004765
Utilizando las estructuras de datos abstractas, se realizó un programa para simular el proceso de ensamblaje de productos descritos en un archivo XML según las configuraciones en la máquina que se utilizará para este fin, siendo ejecutado en tiempo real los diferentes procesos mostrándose en una lista el proceso que se está llevando.
Para de ultimo poder crear reportes en formato XML y HTML acerca del proceso que se llevó a cabo para la simulación seleccionada, también creando imágenes de la cola de componentes utilizada para cada producto que se simuló.

**TDA:** En ciencias de la computación un tipo de dato abstracto o tipo abstracto de datos es un modelo matemático compuesto por una colección de operaciones definidas sobre un conjunto de datos para el modelo.

**Cola: **Una cola es una estructura de datos, caracterizada por ser una secuencia de elementos en la que la operación de inserción push se realiza por un extremo y la operación de extracción pull por el otro. También se le llama estructura FIFO, debido a que el primer elemento en entrar será también el primero en salir.

**Lista enlazada simple:** es una estructura de datos en la que cada elemento apunta al siguiente. De este modo, teniendo la referencia del principio de la lista podemos acceder a todos los elementos de la misma.

**Expresiones Regulares:** son patrones que se utilizan para hacer coincidir combinaciones de caracteres en cadenas.

**Autómata Finito:** es un modelo computacional que realiza cómputos en forma automática sobre una entrada para producir una salida. Este modelo está conformado por un alfabeto, un conjunto de estados finito, una función de transición, un estado inicial y un conjunto de estados finales.

**XML:** es un lenguaje de marcado similar a HTML. Significa Extensible Markup Language (Lenguaje de Marcado Extensible) y es una especificación de W3C como lenguaje de marcado de propósito general. ... El propósito principal del lenguaje es compartir datos a través de diferentes sistemas, como Internet.

**HTML: **(Lenguaje de Marcas de Hipertexto, del inglés HyperText Markup Language) es el componente más básico de la Web. Define el significado y la estructura del contenido web.

**CSS:** (Hojas de estilo en cascada), es un lenguaje de diseño gráfico para definir y crear la presentación de un documento estructurado escrito en un lenguaje de marcado.

**Hilo:** es simplemente una tarea que puede ser ejecutada al mismo tiempo que otra tarea.


Para la realización del proyecto se utilizaron los conceptos planteados anteriormente siendo empleados para los principales módulos y procedimientos para establecer los tiempos de realización de los productos y la configuración de las maquinas. Siendo el XML utilizado como archivos de entrada para darle configuración a la máquina de ensamblaje, así como la simulación de los elementos que se quieren realizar para una prueba, utilizando la librería de “xml etree” de Python para la lectura de estos archivos.
Continuando con pasar la lista de componentes obtenida por un Autómata finito para analizar la expresión regular establecida para obtener línea y componente necesario, almacenándolos en una cola para utilizarlos mas adelante. Estableciendo ambos archivos en una lista de objetos con los datos de simulación, nombre de objeto y componentes necesarios. Comenzando a ejecutar la simulación se comenzará por el primer objeto en la lista de obtenida del archivo de simulación utilizando la cola de componentes para comenzar a ensamblar.
Durante la ejecución del programa que se realiza desde un hilo se podrá apreciar la actualización en tiempo real de los movimientos de los brazos al ensamblar. Al final se pueden generar graficas utilizando Graphviz para diagramar la cola de cada producto en la simulación, además de generar reportes en HTML y XML de los movimientos que se ejecutaron para ensamblar el producto.

Imagen de diagrama de clases empleado

![IPC2P2 (1)_page-0001](https://user-images.githubusercontent.com/78063271/134774135-a77e2b27-cf06-4a75-875c-6ab6c9ca2ea7.jpg)



Imagen del diagrama del arbol para procesar la expresion regular

![Untitled Diagram drawio](https://user-images.githubusercontent.com/78063271/134774139-5142bf4e-c53e-461e-9dc3-0a1c99753ab4.png)



