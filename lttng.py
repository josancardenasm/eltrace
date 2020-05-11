import sys
import os
import json

#https://www.elmundoenbits.com/2014/04/crear-daemon-servicio-python.html#.XrkZ-hbta0k

LTTNG_CONFIG_PATH="configs/"
LTTNG_DFT_CONFIG_FILE=LTTNG_CONFIG_PATH+".lttng.json"
LLTNG_HOME_ENV="LTTNG_HOME"

LTTNG_STEPS=("config", "create", "start", "stop", "destroy" )

class lttng:

    def __init__(self, config=LTTNG_DFT_CONFIG_FILE):
        """ Constructor funcion """
        self.settings={}
        self.configFile=LTTNG_DFT_CONFIG_FILE
        self.step=LTTNG_STEPS[0]

        if LLTNG_HOME_ENV is not os.environ:
            print("Lttng Home folder is set to default path: "+os.environ["HOME"])
            print("make \"export LTTNG_HOME=/path/to/new/home\" to set new home folder (if you want...)")
            self.settings[LLTNG_HOME_ENV]=os.environ["HOME"]
        else:
            print("Home folder is defined to: "+print(os.environ.get(LLTNG_HOME_ENV)))
            self.settings[LLTNG_HOME_ENV]=os.environ.get(LLTNG_HOME_ENV)

    def saveConfigurationFile(self):
        try:
            with open(self.configFile,'w') as f:
                json.dump(self.settings,f)
        except FileNotFoundError:
            print("No se encontro el archivo")


    def loadConfiguration(self):
        try:
            with open(self.configFile) as f:
                self.settings=json.load(f)
                print(self.settings)
        except FileNotFoundError:
            print("File Not foud. Saving default file")
            self.saveConfigurationFile()

    def setHomeFolder(self, homeDir):
        """ set home folder where traces and configuration will be stored"""
        self.homeFolder=homedir.strip()

    def scanPrerequisites(self):
        """ Scan for prerequisites """

    def readConfigFile(self, config):
        """ Read config file for saved configuration """
        if configfile: 
            self.configFile=LTTNG_CONFIG_PATH+config
        
        
    
    def listConfigFiles(self):
        """ print a list of available config files """