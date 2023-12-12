import os
from flask import Flask, render_template 
#  importing Flask class

app = Flask (__name__) # creating an istance of this class and storing it in a variable called app

@app.route("/") # using root decorator or py notation - a way of wrapping the functions. Root directory is a forward slash /
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), #  looking for ip vaariable if it exists
        port=int(os.environ.get("PORT", "8080")), # this port works http://172.20.10.3:8080/ 
        debug=True) # WARNING !!!! never have debug as True in a production application!!!!
