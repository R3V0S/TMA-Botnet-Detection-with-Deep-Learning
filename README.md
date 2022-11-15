# TMA-Botnet-Detection-with-Deep-Learning
Educational project for Network Traffic Monitoring and Analysis

Implementation a 1DCNN to be trained using the CTU-13 dataset, which is a collection of different scenarios where different botnets were generating traffic. 

Steps:

  1) Install Python 3.10 from here: https://www.python.org/downloads/release/python-3100/ _REMEMBER to add python 3.10 to the path_

Once Python has been installed correctly, then:
  1) _git clone <this_repo_by_using_SSH_or_HTTPS>_
  2) Create a new venv (in the folder 1DCNN) with: _python -m venv 1DCNN_v01.00_
  3) Go to 1DCNN_v01.00 folder -> Scripts folder -> and execute in the terminal _activate_. Once this will be completed, you will be working in a virtual environment.
  4) Install the requirements.txt when the virtual environment has already been initiated: _pip install -r requirements.txt_
  5) Return to the \TMA-Botnet-Detection-with-Deep-Learning\1DCNN Code and execute in the command line: _jupyter notebook_
  6) Wait. Then a browser web page will open, and shows the jupyter environment. Select "1DCC Stabdard Version.ipynb" and start coding.

Let's code!

For every new push:
  - _git add <only_the_script_file_updated:1DCNN_botnet_detection_v01.00.ipynb> <requirements_updated:requirements.txt>_
  - _git commit -m "Changes applied... Specify"_
  - _git push_
  
*To create a new requirements.txt : _pip freeze > requirements.txt_

Will be needed to reinstall the requirements if someone else has added more python packages!
