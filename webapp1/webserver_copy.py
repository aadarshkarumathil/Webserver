#!/usr/bin/python2

import socket
import os
from threading import Thread
import time

def get_cookie(request_lines):
    print("cookie data is: " + request_lines[-3])
    data = request_lines[-3].split(":")[-1]
    return (data.split("=")[-1])

def serverside(file_name,data,method,session_id):
    lang = {
    "php":"php",
    "ruby":"ruby ",
    "lisp":"clisp ",
    "python":"python2 ",
    "js":"node ",
    "sh":"bash "
    }
    ext = file_name.split(".")[-1]
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
            resp = os.system("{} {} > output.html".format(lang[ext],file_name))
            file_name = "output.html"
            return file_name
    else :
        print("file is returned")
        return file_name



def error_handle(errornum,mime_type,isphp):
    errorname = {
        200:"OK",
        400:"Bad Request",
        401:"Unauthorized",
        403:"Forbidden",
        404:"Not Found",
        411:"Length Required",
        500:"Internal Server Error",
        501:"Not Implemented"
    }
    if(isphp):
        response = """HTTP/1.1 {} {}\r\n""".format(errornum,errorname[errornum])
    else:
        response = """HTTP/1.1 {} {}\r\nContent-type:{}\r\n\r\n""".format(errornum,errorname[errornum],mime_type)
    return response




def connhandler(csock,addr):
    request = csock.recv(1024)
    print(addr)
    #sock.sendall(index.read())
    request_lines = request.split("\n")
    print(request_lines)
    request_words = request_lines[0].split()
    print("\r\n\r\n\r\n")
    print(request)
    if(request_words[0] == "GET"):
        if(request_words[1] == "/"):
            file_name = "index.php"
        else:
            file_name = request_words[1][1:]
        if(os.path.isfile(file_name)):
            method="GET"
            data = request_lines[-1]
            #print("get data is :".format(data))
            #print(file_name.split(".")[-1])
            if(file_name.split(".")[-1]=="php"):
                isphp = True
            else:
                isphp = False
            #print(isphp)
            session_id= get_cookie(request_lines)
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

        else:
            print("Invalid request")
            logging(addr,request_words[1][1:],"error","404")
            csock.sendall(error_handle(404,"text/html",False))
            response = """<html><head><body>file not found</body></head></html>"""
            #f = open("404.html","r")
            #response = f.read()
            #f.close()
            csock.sendall(response)
            csock.close()
            #print(file_name)

    elif(request_words[0]=="POST"):
        method="POST"
        #print("POST request Success")
        file_name = request_words[1][1:]
        data = request_lines [-1]
        #print("data is: {}".format(data))
        if(file_name.split(".")[-1]=="php"):
            isphp = True
        else:
            isphp = False
        session_id = get_cookie(request_lines)
        file_name = serverside(file_name,data,method,session_id)
        mime_type = mime_type_handler(file_name.split(".")[-1],addr)
        response_file = open(file_name,"r")
        response = response_file.read()
        response_file.close()
        logging(addr,request_words[1][1:],"OK","200")
        avoid_response = ["image/x-icon","image/gif","image/jpeg","image/png"]
        if(mime_type not in avoid_response):
            #print(response)
            print("response from error handle\n\n\n")
        csock.sendall(error_handle(200,mime_type,isphp))
        csock.sendall(response)
        csock.close()




def mime_type_handler(mime,addr):
    mime_switcher = {
        "/":"text/html",
        "html":"text/html",
        "css":"text/css",
        "js":"application/javascript",
        "ico":"image/x-icon",
        "gif":"image/gif",
        "jpeg":"image/jpeg",
        "png":"image/png",
        "jpg":"image/jpeg",
        "json":"application/json",
        "ttf":"application/font-sfnt",
        "cgi":"internal/cgi"
        }
    try:
        file_type = mime_switcher[mime.split(".")[-1]]
        return file_type
    except Exception as e:
        logging(addr,e,"exception","")
        return "invalid file type"


def logging(addr,request,types,code):
    if(types == "error"):
        f = open("logs/error_log.log","a+")
        f.write("Logging at time {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))
        f.write("{} has requested {} which threw a response code {}\n".format(addr,request,code))
        f.close()
    elif(types == "exception"):
        f = open("logs/exception.log","a+")
        f.write("Logging at time {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))
        f.write("{} has requested {} which threw a exception\n".format(addr,request,code))
        f.close()
    else:
        f = open("logs/responses.log","a+")
        f.write("Logging at time {}".format(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())))
        f.write("{} has requested {} which has a response code : {}\n".format(addr,request,code))
        f.close()


host,port = "127.0.0.1",4040

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind((host,port))
sock.listen(5)
while True:
    csock,addr = sock.accept()
    handler = Thread(target = connhandler,args = (csock,addr),)
    handler.start()
    #print("handler ran")
