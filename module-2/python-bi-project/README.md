### Proyecto BI



##### Objetivo.

Utilizar herramientas de geolocalización para detectar un lugar de trabajo idóneo para una empresa.

##### Planteamiento del problema.

La creadora de una startup de comercio de ropa en línea, está en busca de una oficina para incrementar el número de empleados y al mismo tiempo, tener la oportunidad de estar en contacto con clientes pertenecientes a la industria de la moda y atraer un nuevo mercado. 

Para ello, algunas de las consideraciones que solicita son:

- La oficina debe estar ubicada en una zona donde también existan otros desarrolladores de páginas web y de e-commerce
- Debe pertenecer al estado de Nueva York, fuera de Brooklyn ya que su oficina central se encuentra ahí. 
- Debe estar cerca de transporte público, como una estación de metro. 

##### Solución

Para encontrar el área de la oficina, se consideraron como criterios de selección algunas empresas con dos oficinas, pertenecientes a la categoría de ecommerce y web de una base de datos.

A partir de ese primer filtro, se seleccionaron aquellas pertenecientes a Nueva York y se realizó un heatmap para observar de manera gráfica cuál era la zona predominante donde se localizaban las empresas. Esto dio como resultado Manhattan, particularmente la zona centro-sur. 

Se utilizó también un dataset que contenía algunos restaurantes y food trucks, con el fin de considerar que en algún momento los trabajadores puedan tener la posibilidad de acceder a ellos facilmente. 

Tomando una base de datos de propiedades del gobierno de NY, se filtraron propiedades pertenecientes al área de Manhattan para que, posteriormente se compararan con una zona específica. En este caso se seleccionó Gramercy Park, debido a su precio de renta. Una vez que se localizaron las propiedades más cercanas se realizó una segunda búsqueda para saber cuál era la propiedad más cercana a una estación de metro. 

Comparando las direcciones obtenidas con ambas condiciones, se seleccionó una oficina que cumplía con los requisitos descritos previamente.

Finalmente se construyó un mapa para reflejar la posible ubicación de la oficina, el subterráneo y el Brooklyn Bridge, como una referencia de lo distante que se encontraría la nueva oficina de las oficinas centrales. 



> Precios de renta en Gramercy Park: https://42floors.com/us/ny/new-york/251-park-ave-s?listings=1736728
>
> Dataset de propiedades: https://data.cityofnewyork.us/
>
> 



