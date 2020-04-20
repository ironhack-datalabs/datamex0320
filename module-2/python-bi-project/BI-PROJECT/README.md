# **BI PROJECT**

Saúl Romero Bárcenas



## **Cliente**

Ek-Chuah es una app de e-commerce que pertenece al brazo de Ciencia y Tecnología de RUMEC. 

Con el lanzamiento de la aplicación RUMEC se encuentra interezado en entablecerse en un cowork fuera de México para tener alcance internacional. Algunas de las peticiones fué que de preferencia no se ubicara en USA, tuviera infraestructura suficiente para trabajar (escritorio, silla, ventana, etc..),  que se encontrara cerca de empresas e-commerce, con un presupuesto de $40,000 mensuales, facil traslado desde Aeropuerto.



## **Metodo**

Para tener una solución al cliente, se realizaron los pasos siguientes:

- Se adquirieron datos desde el documento companies localizada en MongoDB. Estos datos fueron filtrados, por lo que solo trabajamos con aquellos que estvieran en la categoria de e-commerce y que estuvieran establecidas por más de 5 años.
-  Se visualizaron los datos en mapas de calor utilizando la libreria 'folium' por medio de python, ubicando todas los e-commerce. Se determinó que la mayoria de estas empresas se encuentran en USA y parte de Europa. 
- Con las peticiones del cliente nos enfocamos en las ubicaciones de e-commerce europeas. 
- Dentro de U.K. se encontraron puntos de interes para las ubicaciones de cowork que se pudieran interesar. Se realizó una consulta con respecto a los precios de renta de coworks que se encontraban en zonas conjuntas a donde se encontraban las e-commerce.
-  Se estimó que Servcorp Canary Wharf es el lugar de consideración 

## **Conclusiones**

Mediante el uso de una base de datos e implementando librerias de python, se llevó a cabo una geolocalización en un mapa considerando peticiones del cliente. La uicación de Servcorp Canary Wharf es en U.K. (51.5024412,-0.0189649)



****

