# CSE534-Fabric-Project-Edge-Test
This project uses "Creating FABnet IPv6 Network: Manual Configuration" from the FABRIC API examples as a baseline to create the experiment.
Once you finish compiling all of the blocks, besides the delete. Open 9 terminals in FABRIC and paste the SSH Command you get from submitting the fabric slice.
On each terminal make sure to update and add Python.

sudo dnf update
sudo dnf install python3

After that create .py files for client.py, edge.py, core.py, depending on what that is representing.
Make sure when you paste them you change the ip address at the top with what you got from the bottom of your Jupyter

Once you have done that execute the edge.py file or core.py

In the scenario you close the edge or core use these commands to kill the process that's running

sudo dnf install lsof
sudo lsof -i :8080
sudo kill -9 (PID)
