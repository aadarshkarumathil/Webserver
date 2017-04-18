root_dir="../webapp1/"
host="127.0.0.1"
port=4040
good_req_logs_path = "../webapp1/logs/"
bad_req_logs_path = "../webapp1/logs/"
root_file = "index.php"

post_enable = True
get_enable = True
put_enable = True
delete_enable = True
connect_enable = True

lang = {
"php":"php",
"ruby":"ruby ",
"lisp":"clisp ","logs/exception.log"
"python":"python2 ",
"js":"node ",
"sh":"bash "
}

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
