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







