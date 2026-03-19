from flask import Flask, render_template, request, redirect, url_for, flash
from models import Business, BusinessDirectory
from datetime import datetime

app = Flask(__name__)
app.secret_key = "csc202_secret_key_2025"

# Global directory instance (acts as our in-memory database)
directory = BusinessDirectory()