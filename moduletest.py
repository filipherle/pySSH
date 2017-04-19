# Importing the module
import ssh
# Connecting
'''
ssh.SSHConnect('192.168.0.14', 'pi', 'root') # IP, username, password
print "Connected!" # Just printing Connected!
# Executing a command
try:
    ssh.SSHExecute('ls') # Put command inside of brackets ()
except AttributeError: # If no connection...
    print "Open a connection first!" # Then open one
# Closing connection
print "Closing connection..." # Print that
ssh.SSHClose(0) # Number at the end is how many seconds to wait to close connection
print "Done!" # Finished
'''
ssh.SSHColors("green", "testme")
