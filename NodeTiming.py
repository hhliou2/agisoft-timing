import PhotoScan as ps
import csv

# Connect to Network Client
client = ps.NetworkClient()
client.connect('cisa3-sfm3.ucsd.edu')

# Get information of each node
nodes = client.nodeList()
items = nodes.get('items')
item_cnt = len(items)

# Find starting and ending times for each node
times = dict()
for i in range(item_cnt):
    try:
        times[i] = items[i].get('time_disconnected') - items[i].get('time_connected')
    except(TypeError):
        # In the case that the node has not disconnected yet
        print('Node ' + str(i) + ' has not disconnected')

# Export as csv
with open('C:/Users/chei/Documents/mycsvfile.csv','w') as f:
    w = csv.writer(f)
    for key, value in times.items():
        w.writerow([key, value])