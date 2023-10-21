This repository is a demo of the execution of JavaScript using Selenium with Python.

There are six use-case demos in all. You can execute test cases locally or on the [LambdaTest](https://www.lambdatest.com/) grid. But prefer the LambdaTest cloud grid for parallel and cross-browser testing functionalities. 

## Project Structure
```execute_javascript
├─ .env
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ setup
│  ├─ Setup.py
└─ teststeps
   ├─ test_alert.py
   ├─ test_change_attribute.py
   ├─ test_change_style.py
   ├─ test_login_simul_async_js.py
   ├─ test_scrolling.py
```
## How to run the test cases
Feel free to fork and clone this repo and give it a star with a follow. CD into the project root folder via the terminal and install the requirements:
```pip install -r requirements.txt```
 
Run the pytest command to execute all test cases:
```pytest```

