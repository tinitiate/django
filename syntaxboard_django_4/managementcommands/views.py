from django.shortcuts import render
from configparser import ConfigParser
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def test(request):
    return HttpResponse("Management Commands")


def limited_offer(request):
    
    # Path of the APP Config File
    l_config_path = settings.BASE_DIR + "\\managementcommands\\" + "app.config"

    # Read the config file
    config = ConfigParser()
    data = open(l_config_path,'r')
    config.read_file(data)

    # Check the Offer status and render the page as per the offer settings
    offer_status = config.get("site", "offers")

    if str(offer_status) == "1":
        return HttpResponse("This is Limited Offer")
    else:
        return HttpResponse("No offers now")
