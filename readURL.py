#readURL.py
from datetime import datetime

def getURL():
    file_name = 'url_list.txt'
    errfile_name = 'err_list.txt'

    output_list = []
    err_list = []

    #open file and read 1 line
    f = open(file_name)
    all_line = f.readlines()
    f.close

    for line in all_line :
        #Validation
        if line.startswith('http://') or line.startswith('https://'):
            output_list.append(line.strip())
        else:
            err_list.append(line)

    #output error file
    for err in err_list :
        ef = open(errfile_name,'a')
        ef.write(datetime.now().strftime('%Y/%m/%d %H:%M:%S') + ' --- ' + err)
        ef.close()

    return output_list
