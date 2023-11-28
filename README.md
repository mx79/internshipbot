# MailBot

## Que pouvez-vous faire avec ce projet ?

Vous pouvez envoyer par email une table de recherche sans avoir à ajouter les destinataires un par un comme sur Outlook ou Gmail.

## Comment ça marche ?

Ce InternshipBot est très facile à utiliser mais il n'y a pas d'interface web pour le moment.

Il suffit d'avoir des connaissances de base en Python.

1) Le premier script permet de créer une liste d'email à partir d'une liste de noms de domaine.

2) Le deuxième script permet d'envoyer un email à chaque adresse mail de la liste.

## Les deux scripts

### Script pour créer une liste d'email à partir d'une liste de noms de domaine

1) Remplissez le fichier web/sites.csv avec les noms de domaine des entreprises que vous voulez contacter.

2) Lancez le script scripts/create_email_pattern.py

3) Le script va remplir le fichier email/mail.csv avec les emails de chaque entreprise (info, hello, contact).

### Script d'envoi d'email

A chaque utilisation du script, les emails utilisés seront ajoutés à la liste used_emails.csv pour éviter de les réutiliser, vous pourrez ainsi vous rendre compte du nombre de mail que vous avez envoyé.

Le template d'email contenu dans le script send_email.py est un simple exemple, vous pouvez le modifier à votre guise.

1) Chargez vos identifiants pour vous connecter à votre adresse dans un fichier .env à la racine du projet.

La structure est la suivante :
- EMAIL="votre_adresse_email"
- PASSWORD="votre_mot_de_passe"

2) Changer les informations souhaitées dans le template de l'email dans le script send_email.py

3) Remplaceez les <...> par les informations dans le template de l'email (nom, prenom, date, etc...)

4) Attachez le fichier éventuel avec la fonction load_attachment(), remplacer le <your_cv>.pdf par le chemin du fichier.

5) Et bien sûr, remplissez la liste de courrier du fichier mail.csv après le nom de la colonne "mails".

6) Essayer de vous envoyer un email à vous même d'abord pour vérifier si le mail ressemble à ce que vous voulez et que tout fonctionne bien.

C'est tout, vous pouvez maintenant lancer le script send_email.py et votre mail sera envoyé à chaque adresse mail instanciée dans mail.csv.

Le script va crash en cas de problème.
