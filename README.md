# Lengow Test

## Development env

`git clone https://github.com/Nastyflav/test-lengow.git` \
`pip install -r requirements.txt` to install dependencies

## Run Django Server

`python manage.py migrate` to migrate the database\
`python manage.py db_init` to fill the database\
`python manage.py test` to launch the tests\
`python manage.py runserver`

## Tasks

- Créer un projet Django
- Créer une app "orders".
- Créer un modèle "Order" reflétant les données présentent dans l'API: http://test.lengow.io/orders-test.xml Vous n'êtes pas obligé de gérer tout les champs, 4-5 champs suffisent.
- Dans cette app créer une commande Django permettant de récupérer les commandes de l'API suivante et de les enregistrer en utilisant le modèle que vous venez de créer.
- Créer les vues nécessaires pour lister les commandes, lister 1 commande et rechercher selon les champs du modèle et afficher les résultats.
- Ajouter/modifier une commande