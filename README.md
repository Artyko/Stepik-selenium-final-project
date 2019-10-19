[![Build Status](https://travis-ci.org/Artyko/Stepik-selenium-final-project.svg?branch=master)](https://travis-ci.org/Artyko/Stepik-selenium-final-project)
[![Coverage Status](https://coveralls.io/repos/github/Artyko/Stepik-selenium-final-project/badge.svg?branch=master)](https://coveralls.io/github/Artyko/Stepik-selenium-final-project?branch=master)

# Selenium with python
This is the final project to the course: [Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575)

The project implemented autotests based on a Page Object pattern for the [Training site](http://selenium1py.pythonanywhere.com/) 


### Requirements
```
pytest==5.1.1
selenium==3.14.0
```
### Getting started
These instructions will get you a copy of the project up and running on your local machine for testing purposes.
```
git clone https://github.com/Artyko/Stepik-selenium-final-project.git
cd Stepik-selenium-final-project
pip install -r requirements.txt 
cd page_objects
```
## Running the tests
Before running the tests, make sure that you are in the 'page_objects' folder.

To run the basic tests for a review:
```
pytest -v --tb=line --language=en -m need_review
```

### More tests

The project also presents autotests of two different pages for guests and authorized users:

```
pytest --tb=line test_main_page.py
pytest --tb=line test_product_page.py
pytest --tb=line -m register_user
pytest --tb=line -m login_guest
```

### Thanks

<img src="https://media.giphy.com/media/heIX5HfWgEYlW/giphy.gif">

