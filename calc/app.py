# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app=Flask(__name__)

@app.route("/add")
def adding():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    res = add(a, b)
    return str(res)

@app.route("/sub")
def subtract():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    res = sub(a, b)
    return str(res)

@app.route("/mult")
def multiply():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    res = mult(a, b)
    return str(res)

@app.route("/div")
def division():
    a=int(request.args.get("a"))
    b=int(request.args.get("b"))
    res = div(a, b)
    return str(res)

ops = {
'add':add,
'sub':sub,
'mult':mult,
'div':div
}

@app.route("/math/<math_op>")
def calculate(math_op):
    a=int(request.args["a"])
    b=int(request.args["b"])
    operation=ops[math_op]
    res = operation(a,b)
    return str(res)

