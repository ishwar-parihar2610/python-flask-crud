from flask import Flask




appmain=Flask(__name__)

@appmain.route('/')
def welcome():
    return "Hello world"

@appmain.route('/home')
def home():
    return "Welcome to home page"

from controller import *
    

