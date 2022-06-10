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

