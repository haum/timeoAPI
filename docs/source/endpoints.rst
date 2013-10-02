=============
API endpoints
=============

Liste des accès possibles aux données.

Lignes
======

.. _liste des lignes:

Liste des lignes
----------------

::

    GET /v1/lines

Renvoie une hashmap entre les codes des lignes et leur intitulé.

**Attention :** Si certaines lignes ne fonctionnent pas au moment de la requête, elle ne seront pas notées.

Exemple de résultat :

.. code:: javascript

    {
        "type": "lines",
        "lines": {
            "Ligne 11 > CLOSERIE": "11_A",
            "Ligne 11 > LE CADRAN - SAINT AUBIN": "11_R",
            "Ligne 12 > REPUBLIQUE": "12_R",
            "Ligne 12 > SAINT MARTIN": "12_A",
            "Ligne 16 > ALLONNES": "16_A",
            "Ligne 16 > GARES": "16_R",
            "Ligne 17 > CIMETIERE DE L'OUEST": "17_R",
            "Ligne 17 > OASIS": "17_A",
            "Ligne 18 > ROUILLON": "18_A",
            "Ligne 18 > SAINT-AUBIN": "18_R",
            "Ligne 19 > GUETTELOUP": "19_A",
            "Ligne 19 > LA PAIX": "19_R",
            "Ligne 2 > BEAUREGARD": "2_R",
            "Ligne 2 > GALLIERE": "2_A",
            "Ligne 20 > AIGN\u00c9": "20_R",
            "Ligne 20 > EPERON": "20_A",
            "Ligne 21 > ARNAGE": "21_A",
            "Ligne 21 > SAINT MARTIN": "21_R",
            "Ligne 22 > COMTES DU MAINE": "22_A",
            "Ligne 22 > SARGE": "22_R",
            "Ligne 23 > REPUBLIQUE": "23_R",
            "Ligne 23 > YVRE L'EVEQUE": "23_A",
            "Ligne 24 > MULSANNE": "24_A",
            "Ligne 24 > RUAUDIN": "24_R",
            "Ligne 25 > CHAMPAGN\u00c9": "25_A",
            "Ligne 25 > R\u00c9PUBLIQUE": "25_R",
            "Ligne 26 > ALLONNES": "26_A",
            "Ligne 26 > SAINT GEORGES - SAINT JOSEPH": "26_R",
            "Ligne 3 > GAZONFIER": "3_R",
            "Ligne 3 > OASIS": "3_A",
            "Ligne 33 > BELLEVUE": "33_R",
            "Ligne 33 > COMTES DU MAINE": "33_A",
            "Ligne 4 > LA PAIX": "4_A",
            "Ligne 4 > SAINT GEORGES - ST JOSEPH": "4_R",
            "Ligne 5 > ARNAGE": "5_A",
            "Ligne 5 > GARE ROUTIERE": "5_R",
            "Ligne 6 > LAFAYETTE": "6_R",
            "Ligne 6 > SAINT MARTIN": "6_A",
            "Ligne 68 > ": "68_R",
            "Ligne 69 > ": "69_R",
            "Ligne 7 > RAINERIES": "7_A",
            "Ligne 7 > SAINT MARTIN": "7_R",
            "Ligne 70 > ": "70_R",
            "Ligne 8 > LES HALLES": "8_A",
            "Ligne 8 > PARC MANCEAU": "8_R",
            "Ligne 9 > COMTES DU MAINE": "9_R",
            "Ligne 9 > ZAMENHOF": "9_A",
            "Ligne T1 > ESPAL - ANTARES MMArena": "T1_R",
            "Ligne T1 > UNIVERSITE": "T1_A"
        }
    }

.. _liste des arrêts:

Liste des arrêts par ligne
--------------------------

::

    GET /v1/lines/<lignesens>

Renvoie une hashmap entre les codes TIMEO des arrêts de la ligne spécifiée et leur nom.

**Paramètres :**

lignesens
    Code de ligne (voir `liste des lignes`_) (ex : *8_A*)

**Attention :** pour l'instant, si la ligne n'est pas en service, les sorties sont ... indéterminées.

Exemple de résultat :

.. code:: javascript


    {
        "type": "line_stations",
        "stations": {
            "186": {
                "coords": [
                    "48.0152676",
                    "0.2259572"
                ],
                "name": "CLAIREFONTAINE"
            },
            "226": {
                "coords": [
                    "48.0075036",
                    "0.2242764"
                ],
                "name": "CYGNES"
            },
            "23": {
                "coords": [
                    "48.0181341",
                    "0.2306303"
                ],
                "name": "AGADIR"
            },
            "334": {
                "coords": [
                    "48.0075809",
                    "0.2032289"
                ],
                "name": "GLADIATEURS"
            },
            "365": {
                "coords": [
                    "48.0080472",
                    "0.2078255"
                ],
                "name": "JARDIN PLANTES"
            },
            "388": {
                "coords": [
                    "48.0060752",
                    "0.2216532"
                ],
                "name": "LAMBERT"
            },
            // etc...
    }


Arrêts
======

.. todo:: /v1/stations/<code>/properties & /v1/stations/<code>/all

Coordonnées d'un arrêt
----------------------

::

    GET /v1/stations/<code>/coords

Retourne les coordonnées GPS de l'arrêt donné (données OpenStreetMap, merci à eux).

**Paramètres :**

code
    code de l'arret (voir `liste des arrêts`_)

Exemple de résultat :

.. code:: javascript


    {
        "type": "station_coords",
        "code": 251,
        "coords": [
            "0.2048117",
            "48.0241676"
        ]
    }

Prochains passages
------------------

::

    GET /v1/stations/<code>/<lignesens>

Retourne les prochains horaires de passage à l'arrêt donné pour la ligne donnée.

**Paramètres :**

code
    Code TIMEO de l'arrêt (voir `liste des arrêts`_)
lignesens
    Code de la ligne (voir `liste des lignes`_)


Un arrêts pouvant être utilisé par plusieurs lignes, les deux arguments sont obligatoires.

**Attention :** Si la ligne n'est pas en service au moment de la requête, la sortie est pour l'instant incertaine

Exemple de résultat :

.. code:: javascript


    {
        "type": "next_stops",
        "direction": "A",
        "line": "33",
        "station": 220,
        "stops": [
            "26 minutes",
            "22 H 51"
        ]
    }
