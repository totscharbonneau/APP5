#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Ce fichier contient la classe markov, à utiliser pour solutionner la problématique.
    C'est un gabarit pour l'application de traitement des fréquences de mots dans les oeuvres d'auteurs divers.

    Les méthodes aparaissant dans ce fichier définissent une API qui est utilisée par l'application
    de test testmarkov.py
    Les paramètres d'entrée et de sortie (Application Programming Interface, API) sont définis,
    mais le code est à écrire au complet.
    Vous pouvez ajouter toutes les méthodes et toutes les variables nécessaires au bon fonctionnement du système

    La classe markov est invoquée par la classe testmarkov (contenue dans testmarkov.py):

        - Tous les arguments requis sont présents et accessibles dans args (dans le fichier testmarkov.py)
        - Note: vous pouvez tester votre code en utilisant les commandes:
            + "python testmarkov.py"
            + "python testmarkov.py -h" (donne la liste des arguments possibles)
            + "python testmarkov.py -v" (mode "verbose", qui indique les valeurs de tous les arguments)

    Copyright 2018-2022, F. Mailhot et Université de Sherbrooke
"""

import os
import glob
import ntpath
import numpy
import math


class markov():
    """Classe à utiliser pour coder la solution à la problématique:

        - Contient certaines fonctions de base pour faciliter le travail (recherche des auteurs).
        - Les interfaces du code à développer sont présentes, mais tout le code est à écrire
        - En particulier, il faut compléter les fonctions suivantes:
            - find_author(oeuvre)
            - gen_text(auteur, taille, textname)
            - get_nth_element(auteur, n)
            - analyze()

    Copyright 2018-2022, F. Mailhot et Université de Sherbrooke
    """

    # Le code qui suit est fourni pour vous faciliter la vie.  Il n'a pas à être modifié
    # Signes de ponctuation à retirer (compléter la liste qui ne comprend que "!" et "," au départ)
    PONC = [',', '.', '«', '»', "'", '!', '?', '  ', '\n', '-', ';', ':', '(', ')', '[', ']']

    def set_ponc(self, value):
        """Détermine si les signes de ponctuation sont conservés (True) ou éliminés (False)

        Args:
            value (boolean) : Conserve la ponctuation (Vrai) ou élimine la ponctuation (Faux)

        Returns:
            void : ne fait qu'assigner la valeur du champs keep_ponc
        """
        self.keep_ponc = value

    def print_ponc(self):
        print("Signes de ponctuation à retirer: ", self.PONC)

    def set_auteurs(self):
        """Obtient la liste des auteurs, à partir du répertoire qui les contient tous

        Note: le champs self.rep_aut doit être prédéfini:
            - Par défaut, il contient le répertoire d'exécution du script
            - Peut être redéfini par la méthode set_aut_dir

        Returns:
            void : ne fait qu'obtenir la liste des répertoires d'auteurs et modifier la liste self.auteurs
        """
        files = self.rep_aut + "/*"
        full_path_auteurs = glob.glob(files)
        for auteur in full_path_auteurs:
            self.auteurs.append(ntpath.basename(auteur))
        return

    def get_aut_files(self, auteur):
        """Obtient la liste des fichiers (avec le chemin complet) des oeuvres d'un auteur

        Args:
            auteur (string): le nom de l'auteur dont on veut obtenir la liste des oeuvres

        Returns:
            oeuvres (Liste[string]): liste des oeuvres (avec le chemin complet pour y accéder)
        """
        auteur_dir = self.rep_aut + "/" + auteur + "/*"
        oeuvres = glob.glob(auteur_dir)
        return oeuvres

    def set_aut_dir(self, aut_dir):
        """Définit le nom du répertoire qui contient l'ensemble des répertoires d'auteurs

        Note: L'appel à cette méthode extrait la liste des répertoires d'auteurs et les ajoute à self.auteurs

        Args (string) : Nom du répertoire en question (peut être absolu ou bien relatif au répertoire d'exécution)

        Returns:
            void : ne fait que définir le nom du répertoire qui contient les répertoires d'auteurs
        """
        cwd = os.getcwd()
        if os.path.isabs(aut_dir):
            self.rep_aut = aut_dir
        else:
            self.rep_aut = os.path.join(cwd, aut_dir)

        self.rep_aut = os.path.normpath(self.rep_aut)
        self.set_auteurs()
        return

    def set_ngram(self, ngram):
        """Indique que l'analyse et la génération de texte se fera avec des n-grammes de taille ngram

        Args:
            ngram (int) : Indique la taille des n-grammes (1, 2, 3, ...)

        Returns:
            void : ne fait que mettre à jour le champs ngram
        """
        self.ngram = ngram

    def __init__(self):
        """Initialize l'objet de type markov lorsqu'il est créé

        Args:
            aucun: Utilise simplement les informations fournies dans l'objet Markov_config

        Returns:
            void : ne fait qu'initialiser l'objet de type markov
        """

        # Initialisation des champs nécessaires aux fonctions fournies
        self.DATA = {}
        self.keep_ponc = True
        self.rep_aut = os.getcwd()
        self.auteurs = []
        self.ngram = 1

        # Au besoin, ajouter votre code d'initialisation de l'objet de type markov lors de sa création

        self.wordCountAuthor = {}
        self.identity = {}
        self.orderedIdentity = {}
        self.numberKey = {}
        return

    # Ajouter les structures de données et les fonctions nécessaires à l'analyse des textes,
    #   la production de textes aléatoires, la détection d'oeuvres inconnues,
    #   l'identification des n-ièmes mots les plus fréquents
    #
    # If faut coder les fonctions find_author(), gen_text(), get_nth_element() et analyse()
    # La fonction analyse() est appelée en premier par testmarkov.py
    # Ensuite, selon ce qui est demandé, les fonctions find_author(), gen_text() ou get_nth_element() sont appelées

    def find_author(self, oeuvre):
        """Après analyse des textes d'auteurs connus, retourner la liste d'auteurs
            et le niveau de proximité (un nombre entre 0 et 1) de l'oeuvre inconnue avec les écrits de chacun d'entre eux

        Args:
            oeuvre (string): Nom du fichier contenant l'oeuvre d'un auteur inconnu

        Returns:
            resultats (Liste[(string,float)]) : Liste de tuples (auteurs, niveau de proximité), où la proximité est un nombre entre 0 et 1)
        """

        resultats = []  # Exemple du format des sorties

        # Ajouter votre code pour déterminer la proximité du fichier passé en paramètre avec chacun des auteurs
        # Retourner la liste des auteurs, chacun avec sa proximité au fichier inconnu
        # Plus la proximité est grande, plus proche l'oeuvre inconnue est des autres écrits d'un auteur
        #   Le produit scalaire entre le vecteur représentant les oeuvres d'un auteur
        #       et celui associé au texte inconnu pourrait s'avérer intéressant...
        #   Le produit scalaire devrait être normalisé avec la taille du vecteur associé au texte inconnu:
        #   proximité = (A . B) / (|A| |B|)   où A est le vecteur du texte inconnu et B est celui d'un auteur,
        #           . est le produit scalaire, et |X| est la norme (longueur) du vecteur X

        oeuvrePath = os.path.join(os.getcwd() + "/" + oeuvre)

        currentText = open(oeuvrePath, 'r', encoding='utf-8').read()

        oeuvreData = {}
        currentText = currentText.lower()
        oeuvreGramCount = 0

        # retirer la ponctuation
        if not self.keep_ponc:
            for separator in self.PONC:
                currentText = currentText.replace(separator, ' ')

        # separation du string en list
        wordList = currentText.split()

        # separation en bigrammes si besoin
        if self.ngram == 2:
            tempString = ""
            for x in range(1, len(wordList)):
                tempString = wordList[x - 1] + " " + wordList[x]
                if tempString not in oeuvreData:
                    oeuvreData[tempString] = 1

                else:
                    oeuvreData[tempString] += 1
                oeuvreGramCount += 1

        if self.ngram == 1:
            for word in wordList:
                if word not in oeuvreData:
                    oeuvreData[word] = 1
                else:
                    oeuvreData[word] += 1
                oeuvreGramCount += 1
            # retirer les mots de 2 caracteres ou moins
            for word in list(oeuvreData):
                if len(word) <= 2:
                    oeuvreData.pop(word)

        # normalisation
        for word in oeuvreData:
            oeuvreData[word] = oeuvreData[word] / oeuvreGramCount
        oeuvreData = dict(sorted(oeuvreData.items(), key=lambda item: item[1], reverse=True))

        # comparaison des auteurs
        for author in self.auteurs:
            total = 0
            for word in oeuvreData:
                if word in self.orderedIdentity[author]:
                    total += oeuvreData[word] * self.orderedIdentity[author][word]
            total = total / (math.sqrt(sum(i ** 2 for i in oeuvreData.values())) * math.sqrt(
                sum(b ** 2 for b in self.orderedIdentity[author].values())))
            resultats.append((author, total))

        return resultats

    def gen_text(self, auteur, taille, textname):
        """Après analyse des textes d'auteurs connus, produire un texte selon des statistiques d'un auteur

        Args:
            auteur (string): Nom de l'auteur à utiliser
            taille (int): Taille du texte à générer
            textname (string): Nom du fichier texte à générer.

        Returns:
            void : ne retourne rien, le texte produit doit être écrit dans le fichier "textname"
        """
        newFile = open(textname, "w", encoding='utf-8')
        for nbOfWords in range(int(taille/self.ngram)):
            word = numpy.random.choice(list(self.orderedIdentity[auteur].keys()),
                                       p=list(self.orderedIdentity[auteur].values()))
            newFile.write(word)
            newFile.write(" ")
        newFile.close()
        return

    def get_nth_element(self, auteur, n):
        """Après analyse des textes d'auteurs connus, retourner le n-ième plus fréquent n-gramme de l'auteur indiqué

        Args:
            auteur (string): Nom de l'auteur à utiliser
            n (int): Indice du n-gramme à retourner

        Returns:
            ngram (List[Liste[string]]) : Liste de liste de mots composant le n-gramme recherché (il est possible qu'il y ait plus d'un n-gramme au même rang)
        """
        counter = 0 #counter pour savoir quand on a atteint le n-ième gramme
        ngram = []
        # loop pour regrouper les grammes par nombre d'apparition
        # et non pas par nom
        for gram in self.orderedIdentity[auteur]:
            val = self.orderedIdentity[auteur][gram]
            tempList = gram.split()
            if val not in self.numberKey:
                self.numberKey[val] = [tempList]
            else:
                self.numberKey[val].append(tempList)

        # trouve le n-ième gramme
        for xgram in self.numberKey:
            counter += 1
            if counter == n:
                ngram = self.numberKey[xgram]
                break
        return ngram

    def analyze(self):
        """Fait l'analyse des textes fournis, en traitant chaque oeuvre de chaque auteur
        Args:
            void: toute l'information est contenue dans l'objet markov

        Returns:
            void : ne retourne rien, toute l'information extraite est conservée dans des strutures internes
        """

        # Ajouter votre code ici pour traiter l'ensemble des oeuvres de l'ensemble des auteurs
        # Pour l'analyse:  faire le calcul des fréquences de n-grammes pour l'ensemble des oeuvres
        #   d'un certain auteur, sans distinction des oeuvres individuelles,
        #       et recommencer ce calcul pour chacun des auteurs
        #   En procédant ainsi, les oeuvres comprenant plus de mots auront un impact plus grand sur
        #   les statistiques globales d'un auteur
        # Il serait possible de considérer chacune des oeuvres d'un auteur comme ayant un poids identique.
        #   Pour ce faire, il faudrait faire les calculs de fréquence pour chacune des oeuvres
        #       de façon indépendante, pour ensuite les normaliser (diviser chaque vecteur par sa norme),
        #       avant des les additionner pour obtenir le vecteur global d'un auteur
        #   De cette façon, les mots d'un court poème auraient une importance beaucoup plus grande que
        #   les mots d'une très longue oeuvre du même auteur. Ce n'est PAS ce qui vous est demandé ici.
        for authors in self.auteurs:
            self.wordCountAuthor[authors] = 0
            for oeuvrePath in self.get_aut_files(authors):
                currentText = open(oeuvrePath, 'r', encoding='utf-8').read()
                oeuvreData = {}
                currentText = currentText.lower()

                # retirer la ponctuation
                if not self.keep_ponc:
                    for separator in self.PONC:
                        currentText = currentText.replace(separator, ' ')

                # separation du string en list
                wordList = currentText.split()

                # analyse en bigrammes
                if self.ngram == 2:
                    tempString = ""
                    for x in range(1, len(wordList)):
                        tempString = wordList[x - 1] + " " + wordList[x]
                        if tempString not in oeuvreData:
                            oeuvreData[tempString] = 1

                        else:
                            oeuvreData[tempString] += 1
                        self.wordCountAuthor[authors] += 1

                # transformation de le list en dictionary
                if self.ngram == 1:
                    for word in wordList:
                        if word not in oeuvreData:
                            oeuvreData[word] = 1

                        else:
                            oeuvreData[word] += 1
                        self.wordCountAuthor[authors] += 1
                    # retirer les mots de 2 caracteres ou moins
                    for word in list(oeuvreData):
                        if len(word) <= 2:
                            oeuvreData.pop(word)
                self.DATA[authors] = oeuvreData

        # normalisation

        for authors in self.DATA:
            self.identity[authors] = {}
            totalword = sum(self.DATA[authors].values())

            for word in self.DATA[authors]:
                self.identity[authors][word] = self.DATA[authors][word] / totalword

            #creation d'un dictionaire ordonné pour simplifier les operations futures
            self.orderedIdentity[authors] = dict(
                sorted(self.identity[authors].items(), key=lambda item: item[1], reverse=True))

        return
