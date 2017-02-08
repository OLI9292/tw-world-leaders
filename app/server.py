from flask import Flask, render_template, make_response, request, Response
from stream import stream
import json
import os

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()
