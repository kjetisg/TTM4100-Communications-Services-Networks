# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments                    
host = '129.241.206.56'#'localhost'#"10.22.66.38"# FILL IN START		# FILL IN END
port = 10123 # FILL IN START		# FILL IN END
timeout = 1 # in seconds
 
# Create UDP client socket
# FILL IN START		
clientsocket = socket(AF_INET, SOCK_DGRAM)
# Note the second parameter is NOT SOCK_STREAM
# but the corresponding to UDP

# Set socket timeout as 1 second
clientsocket.settimeout(timeout)
# FILL IN END

# Sequence number of the ping message
ptime = 0  

# Ping for 10 times
while ptime < 10: 
    ptime += 1
    # Format the message to be sent as in the Lab description	
    data =  "Ping " + str(ptime) + " " + time.asctime()# FILL IN START		# FILL IN END
    
    try:
    	# FILL IN START

	# Record the "sent time"
            RTTs = time.time()

	# Send the UDP packet with the ping message
            clientsocket.sendto(data.encode(), (host,port))   # stopper her...?

	# Receive the server response
            message, addr = clientsocket.recvfrom(1024)
	# Record the "received time"
            RTTr = time.time()
	# Display the server response as an output
            print( "RTT: " + str(RTTr-RTTs))
	# Round trip time is the difference between sent and received time
        
        # FILL IN END
    except:
        # Server does not response
	# Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
clientsocket.close()
 
