# Sangkak-Challenge-IA

**SANGKAK-CHALLENGE-IA** est un challenge inter-datascientist et de chercheurs / ingénieurs en Traitement Automatique des Langues (TAL) visant à créer des solutions d'intélligence artificielle concrètes sur un jeu de données open-source en langues africaines.

SANGKAK peut se traduire "Calculer en jouant" en yémba (langue parlé dans le département de la Menoua à l'Ouest du Cameroun).

# Pourquoi créer ce challenge ?


L'Afrique dispose d'un patrimoine culturel et linguistique sans précèdent. Ses 3000 langues sont encore parmi les langues les plus sous-dotées du monde et ce malgré toutes les initiatives créées ces dernières années sur le continent. Le défis est très grand et nous avons un avantage de taille aujourd'hui pour radicalement changer les choses: les technologies et applications de la data science.

Des groupes de travail se sont constitués sur le continent ces dernières années et ils ont produit des quantités importantes de ressources structurées et non structurées pour les langues africaines. En plus des ressources lexicographiques de l'association NTeALan Social Network, on peut aussi citer celles du collectif Masahkane, de Google Research, de Meta et bien d'autres organismes et universités à travers le monde.

Quelques ressources existent et  bien même qu'une bonne partie de ces ressources soient privées, il faudrait maintenant les exploiter pour créer de la valeur au sein des sociétés linguistiques concernées. Tout ceci implique aussi d'identifier les problématiques locales, de trouver un lien possible entre ces problématiques et les ressources disponibles. C'est l'une des raisons principales de ce projet.

# Edition 2022: infos organisationelles 

|                      |                                                                                                | Status           |
|----------------------|------------------------------------------------------------------------------------------------|------------------|
| Site web officiel    | https://sangkak-challenge-ia.ntealan.net                                                       | In progress |
| Edition              | Février 2022                                                                                           | OK               |
| Thématique           | Name Entities Recognition (NER)                                                                | OK               |
| Données sources | MasakhaNER 2.0                                                                              | OK               |
| Langues africaines     | bbj, bam, ewe, fon, hau, ibo, kin, lug, mos, nya, pcm , sna, swa, tsn, twi, wol, xho, yor, zul | OK               |


# Comment participer à cette session ?

## Contexte

Le collectif Masahkane, dans le cadre d'un projet commun Lacuna Fund 2022, a créé et évalué des corpus annotés NER, appelé **African NER Datasets**, dans 20 langues d'Afrique subsaharienne. Les corpus NER produits sous le format CoNLL-03 sont actuellement partagés en open accès sur leur [répertoire Github officiel](https://github.com/masakhane-io/masakhane-ner/tree/main/MasakhaNER2.0/data)  ou dans le dossier *data_source* de ce [répertoire Github](https://github.com/NTeALan/Sangkak-Challenge-IA/data_source/masakhane-ner/MasakhaNER2.0/data).

Les corpus produits ont été évalués sur des taches de NER en se focalisant sur les technologies d'apprentissage par transfert (Transformer) tels que AfriBERTA, AfroXLMR, XLM-R, mBERT, etc. Les résultats obtenus ont été détaillés dans un article accepté à la conférence [EMNLP 2022](https://2022.emnlp.org/) et accéssible à cette adresse https://arxiv.org/abs/2210.12391. A la lecture de ce document, nous constatons que le Ghomala, langue parlée à l'Ouest du Cameroun, a des résultats moins intéressants en terme de performance comparé aux autres langues évaluées.

## Objectifs

L'objectif de cette session est de challenger les participants sur la production d'algorithmes d'IA plus performants pour détecter les entités nommés dans la langue Ghomala en prenant appui sur les travaux réalisés par le collectif Masahkane. Ces questions peuvent vous orienter dans le choix de votre thématique:

- Quel algorithme d'IA serait plus approprié pour détecter les entités nommés en Ghomala et par extension aux langues bantu ?
- Comment mieux organiser les données pour ce type de tache en TAL ?
- Le Ghomala peut-elle être traitée comme toutes les autres langues ? Doit-on parler d'une spécificité Ghomala en TAL ?
- Quelle application pouvons-nous mettre en place pour aider les linguistes ou locuteurs ghomalaphones à mieux traiter ce problème ?
- Quelle méthodologie serait mieux adapté pour traiter ce type de tache ?
- Combinaison approche déterministe / probabiliste serait-elle un plus ?

Dans tous les cas, c'est aux participants de définir leurs objectifs et approches pour proposer une solution de détection NER éfficace sur ces données.

## Participer à la session de Février 2023

Pour participer à cette session et challenger les autres participants:

- Chaque participant ou groupe de participants devra s'approprier les corpus [**African NER Datasets**](https://github.com/NTeALan/Sangkak-Challenge-IA/data_source/masakhane-ner/MasakhaNER2.0/data) en clonant ce répertoire git.

- Vous deviez ensuite créer un répertoire dans votre propre espace Github en adoptant cette structure: 

    - /data_source (étant la référence aux corpus NER Masahkane/facultatif)
    - /evaluation
    - /training
    - methodology.md
    - license.md

- Vous devez ensuite proposer votre solution en respectant cette structure. Vous êtes libre d'ajouter d'autres dossiers ou fichiers supplémentaires de votre choix. 

- Renommez votre dossier par les initiales de votre projet (Exemple: **ENR**) et créez ensuite une branche avec les mêmes initiales, suivi d'un numéro de version (Exemple: **ENR-0.1**) et pushez là sur votre repertoire Github personnel. (Nous utiliserons ce lien comme sous-module git du dossier **propositions** dans ce répertoire officiel du challenge)

- Revenez sur ce repertoire et inscrivez votre proposition dans le fichier [PARTICIPANTS](./propositions/README.md) suivant les champs fournis. Faites ensuite un pull request pour que le comité d'organisation valide votre proposition et lie votre repertoire à ce repertoire officiel.

Merci de respecter scrupleusement cette procédure afin que le comité d'organisation puisse au mieux intégrer votre travail au répertoire officiel.

## Comité d'organisation

Ce challenge est organisé par NTeALan Cameroun et NTeALan France en collaboration avec NTeALan Research and Developpement.

- Elvis MBONING (Lead Data scientist NLP/NLU/Chatbot)
- Jean-Marc Bassahak (Lead Design Motion and web developer)
- Jules Assoumou (Vice rector of University of Ngaoundéré)
- ...


Pour toute question complémentaire, n'hésitez pas à contacter le comité d'organisation du challenge par [mail](sangkak-challenge-ia@ntealan.org) ou sur la [plateforme Slack](https://join.slack.com/t/sangkak-challenge-ia/shared_invite/zt-1kxxxu4af-lQk~Kn6hmVI_OVNk6lqk~w).
