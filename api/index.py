from flask import Flask, jsonify, request
from .db import supabase

app = Flask(__name__)

@app.route("/", rule=SyncClient)
def home():
    a = supabase()
    return a

