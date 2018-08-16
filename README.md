# TODO API FLASK

## General note
For the tests, there's a test user in the DB with username `temp` and password `pass`, so don't clear the DB, you can also use this user to test the app if you don't want to sign up a new acount.


## Running

If you're running the app for the first time, install the requirements using 
```
pip install -r requirements.txt
```
After that, run the app with
```
python manage.py serve
```
If you want to add a reloader (flask debug mode) add the `-r` flag to the serve command

## Testing

To test, make sure the requirements are installed as seen above, and run the following:
```
coverage run --source TodoAPI/ tests.py
```
#### Use the --source option here because otherwise at some occasions coverage will include some random python packages like six
and use
```
coverage html
# or
coverage report
```
to see the result