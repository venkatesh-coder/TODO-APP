
from flask import Flask , render_template, redirect, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def task():
    if "todos" not in session:
            session["todos"] = []
    if len(session["todos"]) == 0:
        return render_template("task.html", length = 0)
    return render_template("task.html", todos=session["todos"])

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task")
        session["todos"].append(todo)
        return redirect("/")
            
            
@app.route("/del", methods=["POST", "GET"])
def delete():
    if request.method == "GET":
        return render_template("del.html", length = len(session["todos"]))
    else:
        num = request.form.get("dele")
        if num.isdigit() == True:
            num = int(num)
            if (num > len(session["todos"])):
                return render_template("invalidNum.html", num = num, length = len(session["todos"]))
        elif num.isdigit() == False:
            return render_template("noAlpha.html", length = len(session["todos"]))    
        elif len(session["todos"]) == 0:
            return redirect("task.html", length = 0)
        session["todos"].pop(num-1)
        return redirect("/")
            
        
    
