## ¿Qué pasa si añadimos un nuevo campo?  los anteriores registros no lo tendrían, entonces ¿Con qué valor se actualizarán?
Depende ,si lo que cambiamos le hemos puesto o tiene  valor por default,se cambiaria a ese,sino entonces le podemos indicar que puede ser nulo con null=true  

## ¿Cómo crearía un campo que sea obligatorio?  

Pasando como parametro blank=false,pero haciendo pruebas se observo que por defecto los campos son requeridos
## ¿Cuáles de estos elementos afectarían  a la base de datos?¿Cuáles no?  

Cuales sí  

default=True, el valor por defecto será True (Si creo un nuevo field y le digo q u valor x default es true toda la base de datos que no tenia el field nuevo tendra true)  

null=true ,esto hara que si no se le envia algo ,se almacena NULL en la base de datos  

Cuales no  

blank=True,Ssimplemente el valor no sera requerido cuando creemos nuevos registros en la base de datos
Como hemos visto ,django nos da opciones como darle un valor x default, o tambien se podria borrar la base de datos y empezar de nuevo  
## ¡Cree más vistas!  

Se crearon las vistas anotherView y vistaCreada que se observan al utilizar los urls another/ y observar/ respectivamente  

## ¡CREE SUS PROPIAS PLANTILLAS!  
Se creara la plantilla home2.html  

## Revise la documentación sobre el objeto request y pruebe otras de sus propiedades (atributos o métodos)  
Se reviso la documentación y se utilizo los atributos is_anonymous,is_staff  
## Realice sus propias plantillas usando la Base y cree más bloques  
Se creo plantilla utilizabase.html y se crearon más bloques ,como el block contenido  
## Verifique las opciones de navegación que aparecen en el resto de sus vistas  
En el resto de mis vistas igual aparece la barra de navegación,puessto que todas mis vistas utilizan base.html como basee  
# DJANGO 3  
## Revisar el objeto forloop en la documentación oficial y hacer experimentos  
Se revisó la documentación y se utilizó lo siguiente : forloop.counter0,forloop.revcounter tambien existen los atributos forloop.first , forloop.last , forloop.parentloop  
## Revisar la documentación oficial sobre if, hacer experimentos con otros operadores de comparación
Se revisó la documentación y se utilizó los operadores: in ,not in ,is not  
## Probar la aplicación de varios otros filtros a variables y  bloques, revisando la documentación oficial  
Se probo truncatechars,upper y add,ademáss adslashes capfirst y cut  
## Complete la descripción del modelo de persona  
Se completo descripcion.html para que tenga todos los campos  
## Intente llenar el formulario para hacerlo inválido  
Se intento llenar el formulario para que sea inválido,los campos nombres y apellidos tienen un limite de palabras,ademas en edad solo se puede poner numeros,al poner otra cosa aparece un mensaje que dice,ingrese un numero entero,si lo quiero enviar vacio no deja  
## Pruebe qué ocurre si no incluímos el campo “donador” en el formulario
Si no se incluye el campo donador dentro de forms.py ,nos da el error IntegrityError at /agregar/
NOT NULL constraint failed: personas_persona.donador
## ¿De qué se trata este error?
Trata de que en la base de datos,donador es un campo obligatorio ,por lo tanto al no enviarle nada no puede guardarlo 
## ¿Cómo se puede solucionar?
Agregando el campo donador a forms.py para que se muestre ,o si no hacer que el campo donador no sea requerido ,o darle un valor por defecto a donador  
## Note que una de nuestras vistas se invoca con GET y luego con POST
Si,esa vista es personaCreateView  

## ¿En qué momento se hace llamada GET y en qué momento se hace la llamada POST?
Se hace la llamada GET cuando entramos en la pagina ,pues tenemos que darle el html al cliente ,se hace la llamada POST cuando enviamos el formulario








