"""
REST - REpresentational State Transfer -> is an architectural style for providing standards between computer systems
on the web, making it easier for systems to communicate with each other

REST-compliant systems, also called RESTful systems are characterized by how they are stateless and separate the
concerns of client and server
    -> stateless = sa nu aiba in memoie o lista cu baza de date (cu toate elementele)
    -> client = cel care face requests pentru a obtine (acele) datele
    -> server = cel care contine datele

For an API to be considered RESTful it must have the following constrains:
    * client-server architecture
    * statelessness: the server does not store any client context between requests, so each request contains all the
    information needed to complete it
    * cache ability: clients can cache response data, reducing the number of requests to the server and
    improving performance -> cache = zona mica de memorie care stocheaza pentru o perioada foarte scurta date
    * use of http methods: GET, POST, PUT, DELETE etc.
    * use of http status codes: success(200), failure(400), not found(404) etc.
"""
