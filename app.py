from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

import random
import string
import logging
import json,os
import requests

from utils import Pagination



app = Flask(__name__)

@app.route('/')
def main():
    return showDir()

def showDir():
    # show the dirs in static
    datasets = sorted([x for x in os.listdir('static') if x != 'assets' and os.path.isdir(os.path.join('static',x))])
    return render_template('dirs.html',datasets=datasets)
    

# Display all things
@app.route('/method', methods=['GET'])
def showMain2():
    
    dataset = request.args.get('dataset')
    method = request.args.get('method')

 # method filter
    if method == None:
        methods_compare_list = sorted([x for x in os.listdir('static/'+dataset) if 'DS_' not in x])
    else:
        methods_compare_list = method.split(',')


    # all the datasets
    datasets = sorted([x for x in os.listdir('static') if x != 'assets' and os.path.isdir(os.path.join('static',x))])

    # all the mtehods
    methods = sorted([x for x in os.listdir('static/'+dataset) if os.path.isdir(os.path.join('static/'+dataset,x)) ])


    # get the input image list
    images = sorted([x for x in os.listdir('static/'+dataset+'/input') if '.png' in x or '.jpg' in x])

    # get all the images from current setting.

    pagex = Pagination(request.args.get("page", 1), len(images), request.path, request.args, per_page_count=1)

    index_list = images[pagex.start:pagex.end]
    html = pagex.page_html()

    return render_template('method.html',images=index_list,filter_methods=methods_compare_list
        ,html=html,datasets=datasets,methods=methods,dataset=dataset)




if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0')
