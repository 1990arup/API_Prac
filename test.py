from flask import Flask, request, jsonify

def sum(a,b):
    return a+b

x= sum(4,5)
print(x)