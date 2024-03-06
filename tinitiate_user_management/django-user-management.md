# Python Django User Management
Authentication is a critical aspect of web development, ensuring that users can securely access and interact with the application. Django, a high-level Python web framework, comes with a built-in authentication system that simplifies the implementation of user authentication features. In this write-up, we will explore the key concepts and steps involved in implementing authentication with Django.

## Make sure poetry is installed
## Django project with python poetry
* **STEP 1**. Create project folder `mkdir django-user-management`
* **STEP 2**. Navigate into project folder `cd django-user-management`
* **STEP 3**. Create project folder `poetry init`
  * Follow the prompts with the values in **BOLD**
  * Package name [django-user-management]:  **tinitiate-user-authentication**
    * Version [0.1.0]: <PRESS-ENTER>
    * Description []:  **Tinitiate django user management and authentication**
    * Author [Syntax Board <“syntaxboard@gmail.com”>, n to skip]:  **n**
    * License []:  <PRESS-ENTER>
    * Compatible Python versions [^3.10]: <PRESS-ENTER>
    * Would you like to define your main dependencies interactively? (yes/no)     * [yes] **no**
    * Would you like to define your development dependencies interactively? (yes/ * no) [yes] **no**
```toml
Generated file

[tool.poetry]
name = "tinitiate_user_management"
version = "0.1.0"
description = "Venkata Bhattaram / TINITIATE"
authors = ["Your Name <you@example.com>"]
readme = "README.md"
[tool.poetry.dependencies]
python = "^3.10"
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
Do you confirm generation? (yes/no) [yes] **yes**

### Edit the pyproject.toml
* Add the required libs in the `[tool.poetry.dependencies]`
```toml
[tool.poetry]
name = "tinitiate_user_management"
version = "0.1.0"
description = "Venkata Bhattaram / TINITIATE"
authors = ["Your Name <you@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
django = "^5.0.1"
pymysql = "^1.1.0"
djoser = "^2.2.2"
djangorestframework = "^3.14.0"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```
* Run `poetry update`

### Steps for Project Setup with Poetry
* **STEP 1**. Create the Project `poetry run django-admin startproject tinitiate_user_management`
* **STEP 2**. Navigate to the folder `cd tinitiate_user_management`
* **STEP 3**. Run the project `poetry run python manage.py runserver`
* **STEP 4**. Test the project setup by opening the url `http://127.0.0.1:8000/` in a browser 
* **STEP 5**. Close the command window and create an App called `accounts`
using `poetry run python manage.py startapp accounts`

* **STEP 6**. Close the command window and create an App called `securedata`
using `poetry run python manage.py startapp securedata`

### Project Code Explanation
* PROEJCT **settings.py**
```python
```

* PROEJCT **urls.py**
```python
```

* APP **views.py**
```python
```

* APP **urls.py**
```python
```

* APP **models.py**
```python
```
#### Steps for Running the Code without POETRY
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py runserver`

#### Steps for Running the Code with POETRY
* **STEP 1:** Add the above content to the files
* **STEP 2:** Make the Migrations `poetry run python manage.py makemigrations`
* **STEP 3:** Make the Migrate `poetry run python manage.py migrate`
* **STEP 4:** Run the project `poetry run python manage.py runserver`
* **STEP 5:** Testing
##### Register and Login
* Register
  * `http://127.0.0.1:8000/accounts/users`
* Login and Get Token
  * `http://127.0.0.1:8000/accounts/api/v1/token/login
  * Pass UserName Password with **Body JSON** `{"username": "admin","password": "Test!2345678"}`
  * Read the TOKEN from the response.
##### Check secured content
* Access the secure content using URL `http://127.0.0.1:8000/securecontent/securedata`
* Pass Login UserName with **Body JSON** `{"username": "admin"}`
* Pass TOKEN with **Header JSON** `{"Authorization":"Token YOUR_TOKEN_HERE"}`
* Logout `http://127.0.0.1:8000/usermanagement/token/logout/`
