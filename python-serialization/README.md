# Python – Serialization & Marshaling

## 📌 Introduction

Ce document explique simplement les notions de **serialization**, **désérialisation**, **marshaling**, **pickle**, **JSON**, ainsi que les différences entre `dump / dumps` et `load / loads`.

**Ces concepts sont fondamentaux pour :**

* sauvegarder des données
* transmettre des données sur un réseau
* reconstruire des objets plus tard ou sur un autre système

---

## 🔹 Qu’est-ce que la sérialisation ?

**Sérialiser** signifie :

> Transformer un objet (ex: dictionnaire, liste, objet de classe) en une suite de données (chaîne ou binaire) afin de pouvoir le **stocker** ou le **transmettre**.

Exemples de formats de sérialisation :

* JSON (texte, lisible)
* XML
* Binaire (pickle)

### Exemple (JSON)

Un dictionnaire Python est transformé en une chaîne JSON.

---

## 🔹 Qu’est-ce que la désérialisation ?

**Désérialiser** signifie :

> Reprendre les données sérialisées et **reconstruire l’objet original**.

C’est l’opération inverse de la sérialisation.

---

## 🔁 Sérialisation vs Désérialisation

| Action          | Description              |
| --------------- | ------------------------ |
| Sérialisation   | Objet → chaîne / binaire |
| Désérialisation | Chaîne / binaire → objet |

---

## 🔹 Qu’est-ce que le marshaling ?

Le **marshaling** est très proche de la sérialisation.

Il désigne surtout :

> Le fait de préparer des objets pour être **envoyés sur un réseau**, souvent entre deux machines ou deux systèmes différents.

📌 Le marshaling est très utilisé dans :

* RPC (Remote Procedure Call)
* systèmes distribués
* communications client / serveur

💡 Astuce :

* **Marshaling = voyage**
* **Serialization = sauvegarde / reconstruction**

En pratique, en Python, les deux notions se recouvrent souvent.

---

## 🔹 RPC (Remote Procedure Call)

Un **RPC** permet d’appeler une fonction située sur une autre machine comme si elle était locale.

**Fonctionnement simplifié :**

1. Le client sérialise les données
2. Les données sont envoyées sur le réseau
3. Le serveur désérialise, exécute la fonction
4. Le résultat est renvoyé (sérialisé)

---

## 🔹 Pickle

`pickle` est un module Python qui permet de :

* sérialiser des objets Python complexes
* désérialiser ces objets plus tard

Caractéristiques :

* format **binaire**
* spécifique à Python
* capable de gérer des objets de classes
* ⚠️ dangereux avec des données non fiables (sécurité)

**📌 Utilisation typique :**

* sauvegarde interne
* transmission Python ↔ Python

---

## 🔹 JSON

JSON est un format de sérialisation :

* lisible par l’humain
* compatible avec presque tous les langages
* très utilisé dans les APIs et le web

Limitation :

* ne gère pas directement les objets Python complexes

---

## 🔹 Différence entre dump / dumps

| Fonction | Rôle                                           |
| -------- | ---------------------------------------------- |
| `dump`   | Sérialise et écrit directement dans un fichier |
| `dumps`  | Sérialise et retourne une chaîne ou des bytes  |

💡 Astuce :

* **s** dans `dumps` = *string* / mémoire

---

## 🔹 Différence entre load / loads

| Fonction | Rôle                                       |
| -------- | ------------------------------------------ |
| `load`   | Désérialise depuis un fichier              |
| `loads`  | Désérialise depuis une chaîne ou des bytes |

---

## 🧠 Résumé ultra simple

* Sérialiser → transformer pour stocker ou envoyer
* Désérialiser → reconstruire l’objet
* Marshaling → préparer pour le réseau
* Pickle → binaire, Python only
* JSON → texte, universel
* dump/load → fichiers
* dumps/loads → mémoire

---

## ✅ Conclusion

La sérialisation est au cœur des applications modernes :

* APIs
* bases de données
* réseaux
* systèmes distribués

Comprendre ces notions permet d’écrire des programmes plus robustes, plus flexibles et capables de communiquer efficacement.
