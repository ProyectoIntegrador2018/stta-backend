# Despliegue del proyecto

## Backend

### Ejecutar el proyecto
* Dentro del folder del proyecto ejecutar:
```
$ python -m flask run -p 3000
```

* Instalar la gema localtunnel
```
$ sudo gem install localtunnel
```

* Ejecutar la gema en el puerto donde se encuentre el proyecto de backend
```
$ localtunnel 5000
```

## Frontend

### Construir el proyecto
Dentro del folder del proyecto ejecutar:
```
$ npm run build
```
Esto generara el proyecto en html y JS para monatarlo en cualquier servidor web.


* Ejecutar la gema en el puerto donde se encuentre el proyecto de frontend
```
$ localtunnel 5000
```
