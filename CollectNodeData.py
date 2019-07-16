import PhotoScan as ps
import csv

# Connect to Network Client
client = ps.NetworkClient()
client.connect('cisa3-sfm3.ucsd.edu')

# Get information of each node
nodes = client.nodeList()
items = nodes.get('items')

# Export as csv
with open('C:/Users/chei/Documents/AgisoftTiming/nodeInfo.csv','w') as f:
    w = csv.writer(f)
    # Mark headers
    w.writerow(items[0].keys())
    for i in range(len(items)):
        w.writerow(items[i].values())