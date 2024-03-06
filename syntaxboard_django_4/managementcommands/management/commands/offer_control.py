from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from configparser import ConfigParser

class Command(BaseCommand):

    help = 'Use this to control Offer Link'

    # Create Arguments Handler
    def add_arguments(self, parser):
        parser.add_argument('-enable', action='store_true', help='Enables the Offers Link')
        parser.add_argument('-disable', action='store_true', help='Disables the Offers Link')

    # Handle the Custom Management Command
    def handle(self, *args, **kwargs):
    
        # Read arguments
        l_enable = kwargs['enable']
        l_disable = kwargs['disable']
        
        # Path of the APP Config File
        l_config_path = settings.BASE_DIR + "\\app_management_commands\\" + "app.config"
        
        # Read the config file
        config = ConfigParser()
        data = open(l_config_path,'r')
        config.read_file(data)

        # Based on the Argument of the Management Command 
        # update the config file.
        if l_enable:
            config["site"]["offers"] = "1"
        elif l_disable:
            config["site"]["offers"] = "0"

        with open(l_config_path, 'w') as configfile:
            config.write(configfile)
