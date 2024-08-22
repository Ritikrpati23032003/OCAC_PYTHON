import tkinter as tk                # A standard Python library for creating GUI applications.
from tkinter import messagebox      #A tkinter module to show message boxes. 
import geocoder                     #A module to get geolocation data.
from gmplot import gmplot           #A library to plot data on Google Maps.
import webbrowser                   #A module to open web pages in the browser.
import requests                     #A library to make HTTP requests.
import googlemaps                   #A Python client for Google Maps APIs.

# Replace 'YOUR_NEW_GOOGLE_MAPS_API_KEY' with your actual Google Maps API key
#Your API key for Google Maps services.
GOOGLE_MAPS_API_KEY = 'AIzaSyAnDGm-3VshQI4JXl-oHtEOtO5C7T2rPPQ'

#An instance of the Google Maps client using the API key
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def detect_location():
    try:
        g = geocoder.ip('me')
        if g.ok:
            lat, lng = g.latlng
            return lat, lng
        else:
            messagebox.showerror("Error", "Unable to detect location.")
            return None, None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None, None

def get_route(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        directions = response.json()
        if directions['status'] == 'OK':
            route = directions['routes'][0]['overview_polyline']['points']
            distance = directions['routes'][0]['legs'][0]['distance']['text']
            duration = directions['routes'][0]['legs'][0]['duration']['text']
            return route, distance, duration
        else:
            messagebox.showerror("Error", f"Error fetching directions: {directions['status']} - {directions.get('error_message', 'No error message')}")
            return None, None, None
    else:
        messagebox.showerror("Error", f"HTTP error: {response.status_code} - {response.text}")
        return None, None, None

def show_map(origin_lat, origin_lng, dest_lat=None, dest_lng=None, route=None):
    gmap = gmplot.GoogleMapPlotter(origin_lat, origin_lng, 13, apikey=GOOGLE_MAPS_API_KEY)
    gmap.marker(origin_lat, origin_lng, 'blue', title="Origin")

    if route:
        decoded_route = googlemaps.convert.decode_polyline(route)
        lats, lngs = zip(*[(point['lat'], point['lng']) for point in decoded_route])
        gmap.plot(lats, lngs, 'blue', edge_width=2.5)

        if dest_lat is not None and dest_lng is not None:
            gmap.marker(dest_lat, dest_lng, 'red', title="Destination")

    with open("map.html", "w") as f:
        f.write(gmap.get())
        f.write(f"""
        <script type="text/javascript">
            function initMap() {{
                var origin = {{ lat: {origin_lat}, lng: {origin_lng} }};
                var map = new google.maps.Map(document.getElementById('map'), {{
                    zoom: 13,
                    center: origin
                }});
                var marker = new google.maps.Marker({{
                    position: origin,
                    map: map,
                    title: 'Origin',
                    icon: {{
                        path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
                        scale: 5,
                        fillColor: 'blue',
                        fillOpacity: 0.8,
                        strokeWeight: 1
                    }}
                }});
        """)

        if dest_lat is not None and dest_lng is not None:
            f.write(f"""
                var destination = {{ lat: {dest_lat}, lng: {dest_lng} }};
                var marker2 = new google.maps.Marker({{
                    position: destination,
                    map: map,
                    title: 'Destination',
                    icon: {{
                        path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
                        scale: 5,
                        fillColor: 'red',
                        fillOpacity: 0.8,
                        strokeWeight: 1
                    }}
                }});

                var routePath = new google.maps.Polyline({{
                    path: google.maps.geometry.encoding.decodePath('{route}'),
                    geodesic: true,
                    strokeColor: '#FF0000',
                    strokeOpacity: 1.0,
                    strokeWeight: 2
                }});

                routePath.setMap(map);
            """)

        f.write(f"""
            }}
        </script>
        <script async defer src="https://maps.googleapis.com/maps/api/js?key={GOOGLE_MAPS_API_KEY}&callback=initMap&libraries=geometry"></script>
        </body></html>
        """)

    webbrowser.open("map.html")

def on_detect_location():
    lat, lng = detect_location()
    if lat is not None and lng is not None:
        show_map(lat, lng)

def on_show_route():
    origin = origin_entry.get()
    destination = destination_entry.get()
    route, distance, duration = get_route(origin, destination)
    if route:
        origin_location = gmaps.geocode(origin)[0]['geometry']['location']
        dest_location = gmaps.geocode(destination)[0]['geometry']['location']
        origin_lat, origin_lng = origin_location['lat'], origin_location['lng']
        dest_lat, dest_lng = dest_location['lat'], dest_location['lng']
        show_map(origin_lat, origin_lng, dest_lat, dest_lng, route)
        
        # Update the labels with distance and duration
        distance_label.config(text=f"Distance: {distance}")
        duration_label.config(text=f"Estimated Travel Time: {duration}")
    else:
        # Clear the labels if no route is found
        distance_label.config(text="Distance: N/A")
        duration_label.config(text="Estimated Travel Time: N/A")

# Create the main window
root = tk.Tk()
root.title("GPS Location detector")

# Create and place a button to detect location
detect_button = tk.Button(root, text="Detect Location and Show Map", command=on_detect_location)
detect_button.pack(pady=10)

# Create and place labels and entry fields for origin and destination
tk.Label(root, text="Origin:").pack()
origin_entry = tk.Entry(root, width=50)
origin_entry.pack(pady=5)

tk.Label(root, text="Destination:").pack()
destination_entry = tk.Entry(root, width=50)
destination_entry.pack(pady=5)

# Create and place a button to show the route
route_button = tk.Button(root, text="Show Route", command=on_show_route)
route_button.pack(pady=10)

# Create and place labels for distance and duration
distance_label = tk.Label(root, text="Distance: N/A")
distance_label.pack(pady=5)

duration_label = tk.Label(root, text="Estimated Travel Time: N/A")
duration_label.pack(pady=5)

# Run the application
root.mainloop()
