from flask import url_for, render_template, request, make_response
from pasta import app
import os
import redis

pasta_root = os.environ['PASTA_ROOT']
pasta_files = pasta_root + '/files'

cache = redis.Redis('redis')

@app.route('/')
def index() :
    infile_text = cache.get('pasta_text')

    if (not infile_text) :
        cache.set('pasta_text', '')
        infile_text = ''
    else :
        infile_text = infile_text.decode('utf-8')
    
    ls_list = [x for x in os.listdir(pasta_files) if (not (x == '.' or x == '..'))] 
    file_list = [(x, file_size_str(os.stat(pasta_files + '/' + x).st_size)) for x in ls_list]
    
    return render_template('pasta.html', pasta_text=infile_text, files=file_list)

@app.route('/', methods=['POST'])
def upload() :
    try :
        if (request.form and request.form['pasta_text']) :
            return savepasta(request)
    except Exception as e:
        return 'Exception when saving pasta_text!! ' + str(e)

    try :
        if (request.files and request.files['picfile']) :
            return savefile(request)
    except Exception as e:
        return 'Exception when saving file!! ' + str(e)

    return "Error '/' POST"

@app.route('/files/<filename>', methods=['GET'])
def returnfile(filename) :
    infile = open(pasta_files + '/' + filename, "rb")
    data = infile.read()
    infile.close()

    response = make_response(data)
    if (filename.lower().endswith('jpeg') or
        filename.lower().endswith('jpg') or
        filename.lower().endswith('png') or
        filename.lower().endswith('gif')) :
        response.headers.set('Content-Type', 'image/jpeg')

    elif (filename.lower().endswith('txt')) :
        response.headers.set('Content-Type', 'text/plain')
    else :
        response.headers.set('Content-Type', 'application/octet-stream')
    
    return response


def savepasta(request) :
    str_input = request.form['pasta_text']
    cache.set('pasta_text', str_input)

    return index()

def savefile(request) :
    files_input = request.files.getlist('picfile')
    for f in files_input :
        f.save(pasta_files + '/' + f.filename) 
    
    return index()

def file_size_str(size) :
    if (size > 1e9) :
        return str(round(size / 1e9, 1)) + ' GB'
    elif (size > 1e6) :
        return str(round(size / 1e6, 1)) + ' MB'
    elif (size > 1e3) :
        return str(int(round(size / 1e3, 0))) + ' kB'
    else :
        return str(size) + ' B'


