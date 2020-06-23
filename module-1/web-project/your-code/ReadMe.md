# Creación de base de datos

##### Objetivos

* Crear una base de datos de canciones de Lady Gaga a partir de diferentes fuentes. 
* Aplicar web scraping y manejo de API's.



##### Limpieza de datos 

Para la creación de esta base de datos, se utilizó como elemento principal un dataset obtenido de la plataforma de Kaggle.com que contenía las letras de más de 50,000 autores de géneros musicales y compositores diversos. En este caso, se determinó que se utilizaría un artista en particular: Lady Gaga.

En un principio, se realizó un análisis del contenido general del dataset y posteriormente se eliminaron valores nulos y columnas que contenían información irrelevante para la base de datos. Asimismo, se compararon los datos obtenidos con aquellos que se buscaba obtener, de acuerdo a los discos de la artista, sus canciones y se eliminó información que no coincidía con los datos deseados. Finalmente, se categorizaron los datos, en este caso cada canción, por álbum y se almacenó en un primer csv para continuar trabajando con él. 

##### Web scraping

Para complementar la información de las canciones, se añadieron datos relevantes tales como: autores y  año de lanzamiento, para ello se realizó web scraping en páginas com wikipedia y sitios de interés. Los datos obtenidos se agregaron y organizaron en el dataset original. 

##### API

Utilizando la API de lastfm.com, se añadió el link para acceder a cada una de las canciones dentro de la plataforma. Este vínculo se añadió al dataset para cada una de las canciones. 

###### Pasos a seguir

Este dataset puede incrementarse considerando:

* Seleccionar múltiples compositores
* Manejar API's diferente (Spotify, Youtube) para facilitar el acceso a las canciones en otras plataformas.
* Utilizar web scraping para conseguir datos más específicos. 

