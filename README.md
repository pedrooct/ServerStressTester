# ServerStressTester
This was built in python , and is a script and uses argv parameters  


#How to use it
You can use get and post (only with application/json via data.json) , threads and how many request you can use.  

- python3.6 stress_test_rest_api.py  threads number request type link  

ex: python3.6 8 10000 get http://localhost:3000  
ex: python3.6 1 2000 post http://localhost:3000  
ex: python3.6 2 2000 get http://localhost:3000  

If you insert 1 in thread, this will run on a single thread!  


This is for fun so don't take it seriously.   
