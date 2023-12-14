Calculate - is a flask project, that converts the expression into polish notation and calculates it. 

To run the program: 
  1) Set up venv for your project and source it;
  2) Install requirements: pip install -r requirements.txt;
  3) Run the app: flask run
  4) Send http request: curl -H "Content-Type: application/json" -d '{ "expression": "4 / (2 - 1)" }' http://127.0.0.1:5000/calculate -X POST - as an example 
