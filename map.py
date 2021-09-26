import folium
import pandas

data = pandas.read_csv('Allstates.txt')
lat = list(data['Latitude'])
lon = list(data['Longitude'])
conf = list(data['TotalConfirmed'])
dis = list(data['discharged'])

print('hai all changes made')

def colour_producer(el):
    if el <10000:
        return 'green'
    elif 10000<=el<30000:
        return 'orange'
    else:
        return 'red'
        
    


map = folium.Map(location = [22.00, 77], zoom_start = 6, tiles = "Stamen Terrain") #Bottom layer added because of stamen terrain


fg = folium.FeatureGroup(name = "My Map")


#Zip will help to loop both loops at a time
for lt,ln,conf,dis in zip(lat,lon,conf,dis):

    #fg.add_child(folium.Marker(location =[lt,ln], popup = str(el)+"m", icon = folium.Icon(color = colour_producer(el))))
    fg.add_child(folium.Marker(location =[lt,ln], popup ="confirmed:"+str(conf)+ "\nDischarged:"+str(dis) , icon = folium.Icon(color = colour_producer(conf))))



map.add_child(fg)

map.add_child(folium.LayerControl())

map.save('India_Covid.html')
