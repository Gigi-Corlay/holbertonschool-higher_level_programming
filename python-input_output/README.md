# Python - Input/Output (I/O)

Ce document explore les mécanismes fondamentaux pour lire des entrées utilisateur, afficher des résultats et manipuler des fichiers en Python.

## 1. Entrées et Sorties Standards

L'interaction la plus basique se fait via la console.

- `input()` : Permet de récupérer une saisie utilisateur (toujours renvoyée sous forme de chaîne de caractères).
- `print()` : Affiche des données à l'écran.

```python
name = input("Comment t'appelles-tu ? ")
print(f"Bonjour {name} !")```


### 2. Formatage de texte

Pour rendre les sorties plus lisibles, on utilise principalement les **f-strings** (introduites en Python 3.6).

| Méthode      | Exemple                          |
|--------------|----------------------------------|
| f-strings    | `f"Valeur : {val:.2f}"`          |
| `format()`   | `"{} est {}".format(a, b)`       |
| `%` operator | `"%s a %d ans" % (nom, age)`     |

---

## 3. Manipulation de Fichiers

La gestion des fichiers repose sur la fonction :

```python
open(file, mode)```

Modes d'ouverture courants :

- 'r' : Lecture seule (par défaut)
- 'w' : Écriture (écrase le contenu existant)
- 'a' : Ajout (append) à la fin du fichier
- 'b' : Mode binaire (ex : pour des images)

Utilisation de with (Context Manager)

Il est fortement recommandé d'utiliser le mot-clé with.
Il garantit que le fichier est fermé automatiquement, même si une erreur survient.

# Écrire dans un fichier
with open("exemple.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python!")

# Lire un fichier
```python
with open("exemple.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
    print(contenu)
    ```
