# About the Project

# Built With
Python was used to develop this project due to its simplicity in integrating API requests with simple yet friendly graphical user interfaces with Python's built-in Tkinter module. The real-time IP address information was obtained through an API provided by IP Geolocation which provided geolocation data for any IP address entered.

# Getting Started
## Prerequisites
Check whether Python is already installed with
```sh
python --version
```
If Python is not installed, you can do so from the [Python website](https://www.python.org/downloads) by selecting the appropriate installer for your required environment.

## Installation
After setting up Python, you can install the application to your local environment with the following instructions:
1. Get your free API key at <https://app.ipgeolocation.io/signup>
2. Clone the repo
   ```sh
   git clone https://github.com/Sukhman25K/IP-Lookup.git
   ```
3. Install any missing Python packages by replacing the name in the command 
   ```sh
   python -m pip install name
   ```
4. Enter your API key in ```Constants.py```
   ```py
   API_KEY = "ENTER YOUR API KEY"
   ```

## Usage
After entering your private API key in the ```Constants.py``` file, you can go ahead and run the application when the installation is complete and stored in your local environment. The application can be run in different ways where the first one would be using a terminal. Navigate to the folder where the application is stored and type:
```sh
python IP-Lookup.py
```

Another way to run the application would be by using an IDLE such as Python's default IDLE or a code editor such as VS code.
