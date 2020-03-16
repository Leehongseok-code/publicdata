import folium
'''
def show_map(lat,lng):
    map_osm=folium.Map(location=[lat,lng])
'''
def add_marker(main_map,lat,lng):
    folium.Marker([lat, lng]).add_to(main_map)

map_osm=folium.Map(location=[36.8,127.1],zoom_start=12)
map_osm

