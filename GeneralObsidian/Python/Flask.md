# FlaskIntroduction

  

This repo has been updated to work with `Python v3.8` and up.

  

## How To Run

1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Open a terminal in the project root directory and run:

```
$ virtualenv env
```
3. Then run the command:

```
$ .\env\Scripts\activate
```
4. Then install the dependencies:

```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:

```
$ (env) python app.py
```
This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

  

```python

if __name__ == "__main__":

    app.run(debug=True, port=<desired port>)

```

  

## Contributing

  

Since this is a repository for a tutorial, the code should remain the same as the code that was shown in the tutorial. Any pull requests that don't address security flaws or fixes for language updates will be automatically closed. Style changes, adding libraries, etc are not valid changes for submitting a pull request.









# Notes

pip install virtualenv

  

```python
 # Create a new directory for your project (optional but recommended)
    mkdir myproject
    cd myproject
    # Create a virtual environment named 'venv'
    python3 -m venv venv
    # Activate the virtual environment (on Unix/Linux/macOS)
    source venv/bin/activate
    # Activate the virtual environment (on Windows)
    venv\Scripts\activate

```  

After creating app.py now you have to go to venv run
python
from app import db
db.create_all_()
exit()




