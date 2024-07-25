"""This project will be about the optimization of data, we will use this cloudlab to try our code

Instructions:
Click on any node in the topology and choose the shell menu item. Your shared NFS directory is mounted at /nfs on all nodes.""" 

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Only Ubuntu images supported.
imageList = [
    ('urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD', 'UBUNTU 20.04'),
]

# Do not change these unless you change the setup scripts too.
nfsServerName = "nfs"
nfsLanName    = "nfsLan"
nfsDirectory  = "/nfs"

# Number of NFS clients (there is always a server)
pc.defineParameter("clientCount", "Number of NFS clients",
                   portal.ParameterType.INTEGER, 4)

pc.defineParameter("dataset", "Your dataset URN",
                   portal.ParameterType.STRING,
                 "urn:publicid:IDN+utah.cloudlab.us:scalableeo-pg0+ltdataset+ArmeniaProjectt")

pc.defineParameter("osImage", "Select OS image",
                   portal.ParameterType.IMAGE,
                   imageList[0], imageList)

# Always need this when using parameters
params = pc.bindParameters()

# The NFS network. All these options are required.
nfsLan = request.LAN(nfsLanName)
nfsLan.best_effort       = True
nfsLan.vlan_tagging      = True
nfsLan.link_multiplexing = True

# The NFS server.
nfsServer = request.RawPC(nfsServerName)
nfsServer.disk_image = params.osImage
# Attach server to lan.
nfsLan.addInterface(nfsServer.addInterface())
# Initialization script for the server
nfsServer.addService(pg.Execute(shell="sh", command="sudo /bin/bash /local/repository/nfs-server.sh"))

# Special node that represents the ISCSI device where the dataset resides
dsnode = request.RemoteBlockstore("dsnode", nfsDirectory)
dsnode.dataset = params.dataset

# Link between the nfsServer and the ISCSI device that holds the dataset
dslink = request.Link("dslink")
dslink.addInterface(dsnode.interface)
dslink.addInterface(nfsServer.addInterface())
# Special attributes for this link that we must use.
dslink.best_effort = True
dslink.vlan_tagging = True
dslink.link_multiplexing = True 

# The NFS clients, also attached to the NFS lan.
for i in range(1, params.clientCount+1):
    node = request.RawPC("node%d" % i)
    node.disk_image = params.osImage
    node.total_memory = 128 * 1024  # Convertir en Mo
    node.disk = 1000  # en Go
    node.cores = 16
    nfsLan.addInterface(node.addInterface())
    
    # Initialization script for the clients

    node.addService(pg.Execute(shell="sh", command="sudo /bin/bash /local/repository/nfs-client.sh")) 
    node.addService(pg.Execute(shell="sh", command="sudo /bin/bash /local/repository/lancement.sh"))
    if i == 1:
        node.addService(pg.Execute(shell="sh", command="sudo /bin/bash /local/repository/prepare_files.sh")
    node.addService(pg.Execute(shell="sh", command="sudo /bin/bash /local/repository/premier.sh"))
    pass
    


# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request) 
