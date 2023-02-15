"""
In urma executarii unui request prin oricare din metodele de mai sus, se returneaza un cod de status ca si raspuns care reflecta rezultatul requestului
Codurile de raspuns se grupeaza in felul urmator:
    1. coduri informationale (1XX) - sunt coduri care reflecta faptul ca o informatie a fost pur si simplu procesata
    2. coduri de succes (2XX) - sunt coduri care reflecta faptul ca informatia a fost procesata cu succes
        - 200 -> informatia a fost citita cu succes
        - 201 -> informatia a fost creata sau modificata cu succes (apare atunci cand scriem informatii de orice fel in baza de date)
        - 204 -> informatia a fost stearsa cu succes
    3. coduri de redirectionare (3XX) - inseamna ca pagina pe care am accesat-o a fost mutata la o alta adresa
    4. coduri de eroare client (4XX) - inseamna ca utilizatorul a transmis o informatie gresita
        - 400 -> informatia transmisa este invalida si nu poate fi procesata
        - 401 -> unauthorised - inseamna ca utilizatorul nu este logat si sistemul nu poate decide daca acesta are acces la anumite informatii sau nu
        - 403 -> forbidden - inseamna ca utilizatorul este logat dar nu este autorizat sa acceseze anumite informatii
        - 404 -> pagina nu a fost gasita
    5. coduri de eroare server (5XX)
        - 500 Internal Server Error -> informatia transmisa catre server cel mai probabil a fost corecta, dar serverul nu a putut sa o proceseze
        - 503 Service Unavailable -> momentan serverul care ar trebui sa proceseze informatia nu functioneaza. Se foloseste de multe ori atunci cand aplicatia web este in mentenanta
"""
