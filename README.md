# TMA-Botnet-Detection-with-Deep-Learning
Educational project for Network Traffic Monitoring and Analysis

## Model Implementation

Implementation a 1DCNN to be trained using the CTU-13 dataset, which is a collection of different scenarios where different botnets were generating traffic. 

Steps (for Windows):

  1) Install Python 3.10 from here: https://www.python.org/downloads/release/python-3100/ _REMEMBER to add python 3.10 to the path_

Once Python has been installed correctly, then:
  1) _git clone <this_repo_by_using_SSH_or_HTTPS>_
  2) Create a new venv (in the folder 1DCNN) with: _python -m venv <name_venv>
  3) Go to /<name_venv> folder -> /Scripts folder -> and execute in the terminal _activate_. Once this will be completed, you will be working in a virtual environment.
  4) Install the requirements.txt (located in Venv folder from the git repository) when the virtual environment has already been initiated: _pip install -r requirements.txt_
  5) Return to the \TMA-Botnet-Detection-with-Deep-Learning\Working Tests Code and execute in the command line: _jupyter notebook_
  6) Wait. Then a browser web page will open, and shows the jupyter environment. Select "1DCNN-CTU13-READY.ipynb" and start coding.

Let's code!

For every new push:
  - _git add <only_the_script_file_updated:1DCNN_botnet_detection_v01.00.ipynb> <requirements_updated:requirements.txt>_
  - _git commit -m "Changes applied... Specify"_
  - _git push_
  
*To create a new requirements.txt : _pip freeze > requirements.txt_

Will be needed to reinstall the requirements if someone else has added more python packages!

TYPICAL ERRORS:
 When you are doing a push -> "LF will be replaced by CRLF" for each doc added or changed, please, do before the push the next: _git config --global core.autocrlf false_
 
## The Network Scenario

The network is configured to be used in a Linux environment and we recommend Ubuntu 20.04

Install requirements:
- python 3.8 (not 3.10)

And run the following commands to create the setup:

- _sudo apt-get install build-essential
- _sudo apt-get install mininet
- _sudo apt install xterm
- _echo 'xterm*font: *-fixed-*-*-*-18-*' > .Xresources
- _xrdb -merge ~/.Xresources
- _sudo apt install git
- _git clone https://github.com/mininet/mininet.git
- _mininet/util/install.sh -fw
- _git clone https://github.com/osrg/ryu.git
- _cd ryu
- _sudo pip3 install ryu
- _sudo pip3 uninstall eventlet
- _sudo pip3 install eventlet==0.30.2
- _sudo apt install curl
- Modify the file at ~/ryu/ryu/app/simple_switch_rest_13.py:
  -  Replace line 88 and 102 for the following line:
  -  dpid = dpid_lib.str_to_dpid(kwargs['dpid'])
- Run the following commands to configure the firewall in the switch r1:

- _wget https://dl.influxdata.com/influxdb/releases/influxdb_1.8.4_amd64.deb
- _sudo dpkg -i influxdb_1.8.4_amd64.deb
- _sudo apt-get update
- _sudo apt-get install -yq python3-influxdb
- _wget https://dl.influxdata.com/telegraf/releases/telegraf_1.17.3-1_amd64.deb
- _sudo dpkg -i telegraf_1.17.3-1_amd64.deb
- Modify the telegraf configuration file in /etc/telegraf/telegraf.conf as following:
  - omit_hostname = true
  - inside [[outputs.influxdb]] section:
    - urls = ["http://:8086"]
    - database = "RYU"
    - skip_database_creation = false
    - timeout = "5s"
  - inside [[inputs.socket_listener]] section:
    - service_address = "udp://:8094"
    - data_format = "influx"
- _sudo systemctl restart telegraf
- _sudo systemctl start influxdb

If needed at some point you can flush the topology of mininet by running: 
  _sudo mn -c

Now you have configured all the needed services.

### General Steps

- Run the Ryu Firewall: _sudo ryu-manager rest_controller.py
- Run the Mininet Topology: _sudo mn --custom Topology/myTopo.py --topo mytopo --switch ovsk --controller remote
- Set the initial configuration: _sh initialConfig.sh
- Command to show the flow tables in each switch: _sh Topology/switchFlowRules.sh
- Run the app: _sudo python3 App/ManagerApp.py

### Attack

- Run the Mininet servers: _mininet> xterm server1 server2 server3
- In each server run the following command in xterm: _python3 -m http.server 80
- Run attackers' terminals: _xterm a1 a2
- Then you can run the script _dos.py_ to do the attack from an attacker to the server
 
## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
