from flask import flash, g, redirect, render_template, request, url_for

from app import app


@app.route('/')
def index():
    return "Hello World?"