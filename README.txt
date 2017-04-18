How to run my web server:-
Cd webserver
./webserver
Where to edit configurations:-
Conf.py
Root_file denotes the index file which will displayed when the url is typed.
Dictionary  lang has the server side languages which can be run. Adding a extension type and the way to run it would integrate it to run that server side language too.
We can disable any kind of request by changing the mehtod_enable variable Eg- making post_enable=false would make the POST requests disabled.
Good_req_log_path has the response logs and bad_req_log_path has the error logs.

What all this webserver can do : - 

Handles GET,POST,PUT,DELETE,CONNECT.
Returns response codes 200,400,401,403,404,411,500,505 Executes server-side
To execute nodejs files the file has to be put inside the nodefiles directory. 
Logs good,bad and exception requests
Has a config files with all the mentioned params.
