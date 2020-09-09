# Python examples
Python is an interpreted language.
You can open the interpreter, usually just by something similar to  
`$ python3`

You can run a Python file with something similar to  
`$ python3 testFile.py`

You can also execute a Python file, if it's been set to executable, ie  
`$ ./testFile.py`

Note that only works if you explicitly specify an interpreter in the source file as the first line


Python has some nifty command line tools to set up minimal virtual environments with specific Python versions/packages, etc  
`sudo apt-get install python3-virtualenv`
`$ python3 -m venv new_vert`  
`$ source new_vert/bin/activate`  
`(new_vert) $ deactivate`


Pip is Python's package manager  
`$ sudo apt-get install python3-pip`  
`$ pip3 search <something>`  
`$ pip3 install <something>`

Can use pip to install packages in the virutal environment, keeping things isolated