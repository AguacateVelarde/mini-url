#  My mini url :skull:

Este proyecto es un acortador de url. El bakcend está trabajado con Flask y el frontend con Angular. Se ocupó Docker con docker compose para alzar los servicios y hacer el deploy. 

## Estructura del proyecto 
*  ### Backend 
En la carpeta backend está el proyecto con flask. dentro está una carpeta llamada test donde contiene todos los testing realizados en unittest. Para correr los test se tiene, se tiene que encontrar en la carpeta raíz del backend y ejecutar 

```
python all_url_test.py
python login_register_test.py
python url_test.py
```

Dentro de la misma carpeta está el manifiesto para ejecutar y buildear el proyecto en docker. 
Lo más importante del proyecto  : 
* /models - donde se encuentran los modelos de usuario y url. 
* /resources - donde están las clases que controlan los endpoints.
* app.py - el punto de entrada de la app 

*  ### Frontend
En la carpeta Frontend, está todo el proyecto en Angular. Si se quiere correr de forma local hay que instalar, primero, la CLI de Angular posterior a  instalar Node js con el siguiente comando: 
```
	npm install -g @angular/cli
```

y Para servir el proyecto podemos ocupar :
```
	ng serve -o
```
 
Antes, sin embargo, hay que alzar el proyecto de Flask y en la carpeta de enviroment, en el archivo de enviroment.prod o enviroment (dependiendo si está en producción o en desarrollo, hay que cambiar el apiURL al url de flask. 



## Deploy con Docker compose 

Para deployar el proyecto con docker compose, solo debemos correr el siguiente comando  directamente en la raíz del proyecto : 
```
	docker-compose -f docker-compose.yml up --build
```
Si se necesita builder antes el frontend, se utilizaría desde la raíz del proyecto: 
```
cd frontend && ng build --prod && cd .. && docker-compose -f docker-compose.yml up --build
```

## Decisiones 

El proyecto se comenzó pensando desde el backend. Flask es un micro framework que, a comparación de otros, ofrece herramientas suficientes y rápidas para hacer Servicios web como rest apis. 
La arquitectura está pensada para desacoplar todos los componentes, y organizar cada recurso de forma que fuera suficientemente lógica para encontrarlos. Utilicé SQLite por el cantidad mínima de datos que se iban a utilizar. 
E implementé un inicio de sesión y registro con JWT por la rapidez y las herramientas ya creadas que ayudan a ser eficientes como es el caso de *flask_jwt_extended*. 
Para el frontend, se utilizó Angular por la experiencia que se tiene y el corto tiempo de implementación. Se integró con Bootstrap 4 y se aplicaron algunos estilos. Se crearon dos rutas y varios componentes y servicios que se conectaron al backend en flask. 
Finalmente se dockerizó la aplicación con dos contenedores, uno en nginx que funciona como proxy reverso y servidor web para Angular, y otro que alza flask.  


El proyecto fue hecho con :heart: 