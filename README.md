# Multi Threaded Server Simulation

The purpose of this project is to simulate a multithreaded web server that handles HTTP requests. 

#Functionality

1. The web server accepts and parses the HTTP request
2. Gets the requested file from the server’s file system
3. Creates an HTTP response message consisting of the requested file preceded by header lines
4. Sends the response directly to the client.
5. If the requested file is not present in the server, the server sends an HTTP “404 Not Found” message back to the client.

#Running the server

Put an HTML file (e.g., HelloWorld.html) in the same directory that the server is in. Run the server program. Determine the IP address of the host that is running the server (e.g., 136.145.181.38). From another host, open a browser and provide the corresponding URL. For example:

http://136.145.181.38:6789/HelloWorld.html

‘HelloWorld.html’ is the name of the file you placed in the server directory. Note also the use of the port number after the colon. You need to replace this port number with whatever port you have used in the server code. In the above example, we have used the port number 6789. The browser should then display the contents of HelloWorld.html. If you omit ":6789", the browser will assume port 80 and you will get the web page from the server only if your server is listening at port 80.

Then try to get a file that is not present at the server. You should get a “404 Not Found” message.
