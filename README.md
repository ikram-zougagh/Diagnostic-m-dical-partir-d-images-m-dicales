# Diagnostic Médical à Partir d'Images Médicales

Ce projet vise à appliquer des techniques de deep learning pour l'analyse et la classification des images IRM (Imagerie par Résonance Magnétique) du cerveau, en particulier pour détecter et classifier des tumeurs cérébrales. Le projet exploite des réseaux de neurones convolutifs (CNN) ainsi que des modèles préentraînés comme **VGG16** et **VGG19** pour améliorer la précision du diagnostic.

## Objectifs

L'objectif principal est de développer un modèle capable de :

- **Détecter des anomalies** dans les images IRM cérébrales.
- **Classer les tumeurs cérébrales** selon leur type (gliomes, méningiomes, etc.).
- Offrir une **interface utilisateur** via une application web pour permettre de soumettre des images IRM et obtenir un diagnostic automatique.

## Approche

Le projet utilise trois modèles principaux pour atteindre ses objectifs :

1. **Réseaux de Neurones Convolutifs (CNN)** pour entraîner un modèle à partir de zéro.
2. **VGG16** et **VGG19**, deux modèles préentraînés, pour tirer parti des architectures de réseaux de neurones profondes et optimisées.

### 1. CNN (Convolutional Neural Networks)

Le modèle CNN a été conçu spécifiquement pour ce projet en partant de zéro. Voici les étapes clés :

- **Convolution** : Extraction des caractéristiques importantes des images IRM.
- **MaxPooling** : Réduction de la dimension tout en conservant les informations pertinentes.
- **Fully Connected Layers** : Classification des tumeurs à partir des caractéristiques extraites.

### 2. Modèles Préentraînés : VGG16 et VGG19

Pour améliorer les performances et bénéficier de modèles déjà optimisés sur des millions d'images, nous avons utilisé les modèles **VGG16** et **VGG19** :

- **VGG16** : Un modèle de réseau de neurones profond comprenant 16 couches. Il est utilisé pour extraire des caractéristiques complexes des images IRM. Ce modèle a été affiné avec les données d'entraînement de ce projet.
- **VGG19** : Similaire au VGG16, mais avec 19 couches, offrant ainsi une architecture plus profonde et capable d'extraire des détails encore plus fins des images IRM.

#### Fine-tuning des modèles VGG

Nous avons appliqué le **transfert d'apprentissage** en réutilisant les couches convolutives préentraînées des modèles VGG16 et VGG19, et en ajustant uniquement les dernières couches pour s'adapter à notre tâche de classification des tumeurs. Cette technique permet d'accélérer l'entraînement tout en améliorant les résultats.

## Jeu de Données

Le projet utilise un jeu de données public constitué d'images IRM du cerveau, classées en plusieurs catégories en fonction du type de tumeur. Les images sont divisées en trois ensembles :

- **Entraînement** : Pour ajuster les paramètres des modèles.
- **Validation** : Pour ajuster les hyperparamètres et éviter le surapprentissage.
- **Test** : Pour évaluer la performance finale du modèle.

## Résultats

Les trois modèles ont été comparés sur la base de plusieurs métriques telles que la précision, le rappel et le F1-score :

- **CNN** : A donné une précision de base autour de **99.07%** après plusieurs itérations d'entraînement.
- **VGG16** : A montré une amélioration significative avec une précision de **98.13%** grâce à l'usage du transfert d'apprentissage.
- **VGG19** : A légèrement surpassé VGG16 avec une précision de **96.26%**, grâce à sa profondeur accrue qui lui permet de capturer plus de détails dans les images.

## Utilisation

Le projet inclut une **application web** développée en **Flask**, permettant de soumettre des images IRM et de recevoir des prédictions instantanées. L'utilisateur peut charger une image, et le modèle renvoie une prédiction sur le type de tumeur détectée, offrant une interface simple pour les médecins et les chercheurs.

## Conclusion

Ce projet démontre la puissance des modèles de deep learning, en particulier avec l'utilisation de **CNN**, **VGG16**, et **VGG19**, dans le diagnostic médical basé sur des images. L'utilisation de modèles préentraînés a permis d'améliorer la précision et de réduire le temps d'entraînement. Cette solution pourrait être un outil utile pour les professionnels de la santé afin de détecter rapidement les tumeurs cérébrales et d'améliorer la précision des diagnostics.

