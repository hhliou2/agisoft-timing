import PhotoScan as ps

node_count = 7

# Connect to Network Client
client = ps.NetworkClient()
client.connect('cisa3-sfm3.ucsd.edu')

for i in range(node_count):
    # Get node statuses
    status = client.nodeStatus(i)

    # Extract console text
    console_log = status.get('console_log')[0].get('text')
    #logs = console_log.split('\n')

    # Write to new text document for access to Pandas package
    file_name = "C:/Users/chei/Documents/Output" + str(i) + ".txt"
    with open(file_name, "w") as text_file:
        text_file.write(console_log)

# Store as series
#df = pd.Series(logs)

#print(df)