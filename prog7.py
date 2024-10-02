"""
=========================
Mapa cloropetico
=========================

DESC
"""

import geopandas as gpd
import matplotlib.pyplot as plt

# Cargar la capa temática
natalidad = "data/natalidad.geojson"
map_data = gpd.read_file(natalidad)
map_data.head()

# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(figsize=(10, 10))
 
# Control del título y los ejes
ax.set_title('Natalidad por Provincias en España, 2018', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
 
# Mostrar el mapa finalizado
map_data.plot(column='NAT2018', cmap='plasma', ax=ax, zorder=5)

# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
 
# Control del encuadre (área geográfica) del mapa
ax.axis([-12, 5, 32, 48])
 
# Control del título y los ejes
ax.set_title('Natalidad por Provincias en España, 2018', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
 
# Añadir la leyenda separada del mapa
from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.2)
 
# Generar y cargar el mapa
map_data.plot(column='NAT2018', cmap='plasma', ax=ax,
              legend=True, cax=cax, zorder=5)
 
# Cargar un mapa base con contornos de países
oceanos = "natural_earth/ne_50m_ocean.shp"
map_oceanos = gpd.read_file(oceanos)
map_oceanos.plot(ax=ax, color='#89c0e8', zorder=0)