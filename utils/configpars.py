import configparser
from pathlib import Path

cfgFile = 'configs.ini'
cfgDir = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
CFG_FILE = BASE_DIR.joinpath(cfgDir).joinpath(cfgFile)

config.read(CFG_FILE)

def getFlaskURL():
    baseURL = 'http://' + config['flaskapp']['url'] + ':' + config['flaskapp']['port'] + '/api/'
    return baseURL
