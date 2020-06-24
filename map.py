import folium

# create map object (Boston)

m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Generate Map

m.save('map3.html')

