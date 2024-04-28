The main.py file imports the GrahQl client from the tokenizer.py file.

In main.py the GraphQl client class is initialized and passed to the query class.
The GraphQl class has a decorator function which is used to renew the token.
The functions of the query class i.e risk and activity functions are passed through the decorator to check the validity of the token before making a request.

The queries.py file holds the query string and variable value that is passed as a payload to the graphql endpoint.
