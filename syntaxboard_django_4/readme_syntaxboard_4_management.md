# Django Tutorial 4
> Venkata Bhattaram (c)



## Django Management

* Management Commands
* Caching
* Django Testing


### Project

* **STEP 1** Create the project
```bash
django-admin startproject  syntaxboard_django_4
```

* **STEP 2** Create Apps
```bash
python manage.py startapp caching
python manage.py startapp djangotesting
python manage.py startapp managementcommands
```

* **STEP 3** Add Apps to `settings.py`
```bash
caching
djangotesting
managementcommands
```


### Django Custom Management Commands
* Django Custom Management Commands are applied through projects `manage.py`
  commands like startproject, runserver..
* Django management commands are designed as interfaces to execute simple to 
  complex tasks using the command `python manage.py` at the terminal
* Management commands are useful to communicate with the Django application 
  with a command line terminal 
* They provide an interface to execute website cron jobs.

### Management Commands

#### APP folder urls.py Configuration
```
from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('limited_offer/', views.limited_offer, name='limited_offer'),
]
```

#### APPs folders views.py file
* The `views.py` demonstrates the following
  * A Test page
  * An offers page, Here the offer availability is determined by the setting 
    in the config file `app.config`
```
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
```

#### APPs folders app.config file
* Here we use an `app.config` file to have the offer settings
  * 1: enable offers
  * 0: disable offers
* Below is the initial setting
* This is changed by the management command, NOT manually
```
[site]
offers = 1
```

#### Management Commands Folder Structure
* Create the management and management/commands folder in the APP folder
* Management Commands are APP specific, here we need to Create the `management`
  and `management/commands` folders
* In our app `managementcommands`, we create `management` and 
  `management/commands` folders
* Below is the folder structure for the Management Commands
```
syntaxboard_django_4/                              <-- ** Django Project Folder
 |-- managementcommands/                <-- ** Django App Folder
 |    |-- management/
 |    |    +-- commands/
 |    |         +-- current_time.py     <-- ** Print the current time
 |    |         +-- offer_control.py    <-- ** Enable / Disable a page from the view
 |    |-- migrations/
 |    |    +-- __init__.py
 |    |-- __init__.py
 |    |-- admin.py
 |    |-- apps.py
 |    |-- tests.py
 |    +-- views.py
 |-- syntaxboard_django_4/
 |    |-- __init__.py
 |    |-- settings.py
 |    |-- urls.py
 |    |-- wsgi.py
 +-- manage.py
```

>
* Add the first management-command `current_time.py`
* Management Command has a `Command Class` and the method `handle`
```
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings # correct way

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("Current Time is %s" % time)
```


>
* Add the next management-command `offer_control.py`
* This Management Command has a `Command Class` and the method `handle` and 
  arguments that are passed to the handle.
* Here we update the `app.config` file based on the argument of the 
  management command, using the `ConfigParser`.
```
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
        l_config_path = settings.BASE_DIR + "\\managementcommands\\" + "app.config"
        
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
```
>


#### Run Project and Test URLS in Browser
* At command line start the project, using the command:
```
python manage.py runserver
```
* Run a test to see the APP working
* Login using the URL:  `http://localhost:8000/managementcommands/test`
* Execute the Custom Management Commands at the command line in a separate window
```
python manage.py current_time
```
* Offers page  `http://localhost:8000/managementcommands/limited_offer` 
  will show offers present
* Execute the Custom Management Commands to disable the offer at the command line.
```
python manage.py offer_control -disable
```
* Offers page  `http://localhost:8000/managementcommands/limited_offer` 
  will show offers not available
* Enable the offers by running the following at the command line
```
python manage.py offer_control -enable
```
* Offers page  `http://localhost:8000/managementcommands/limited_offer`
  will again show offers.
