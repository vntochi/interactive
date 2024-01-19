import configparser

# Read the authentication status from the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

authentication_status = config['AUTHENTICATION'].getboolean('authenticated', fallback=False)

if authentication_status:
    print("User is authenticated.")
else:
    print("User is not authenticated.")