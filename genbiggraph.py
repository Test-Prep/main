import osmnx as ox
G = ox.graph_from_place(input("county:\n "), network_type='drive')
ox.save_load.save_graph_osm(G, filename='networkgraph.osm')