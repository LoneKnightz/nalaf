# Goals:

1. Study significance of NL mentions in mutation mention recognition
  * ratio of standard vs NL in abstracts & full text
  * % of novel mutations not present in SwissProt (would require manual annotation of protein relations)
  * dataset of NLs (size depends on significance of NLs)
2. Method for mutation mention extraction grounded to their genes/proteins
  * Mutation mention recognizer better than tmVar for standard mentions
  * If NLs are relevant, prove good F1 performance (> 70-80)
  * Simple or optionally advanced normalization method
  * Easy to use program:
    * *Good documentation:*
      * code
      * end-user (biology researcher level, how to call from the command line, ...)
    * Accept inputs: programmatical call (string), text file, corpora' formats**
    * Accept outputs: ann.json (tagtog suitable)   
3. Paper
  * Full draft (1 or 2 papers?) by end of August submittable to Burkhard Rost
  * Submit by September-October




# Carsten's thesis

Bachelor thesis about named entity recognition for natural language mentions of mutation names in the biomedical domain.

## Title: Semi-supervised learning of natural language mutation mentions

## Abstract
Research and development in the biomedical domain is constantly growing. Millions of documents have been already published on various platforms including PubMed. But do people use the curated literature efficiently?
Looking at just a few papers that describe a particular protein can limit the understanding of occurring protein mutations. Through automating the process of identifying relevant protein mutations, research can be increased significantly.

> OLD The development of literature information extraction has already progressed to a certain degree: protein, mutation, gene names and similar following naming conventions can be parsed at a sufficient rate, though there are still cases of ambiguity. The current problematic is, that TODO.......
Text mining in the biomedical domain tends to be difficult, because the language used, including e.g. protein names, gene names, are very ambiguous and are thus difficult to parse. The natural language in combination with cryptic words is one big challenge for machine learning tasks. Finding those so called "named-entities" is the goal of my thesis.

With Conditional Random Fields (CRF), we want to incorporate many features and build a machine learning model, that is able to be used in a semi-supervised environment and does increase its dataset for prediction continuously with the help of annotation.

> OLD The difficulty lies within the description of entities that are consisting of multiple words and are defined through context and, thus can not be easily parsed.

> TODO argument: dataset extension with semi-supervised learning explanation, BECAUSE: small dataset because of difficult manual annotation

On top of that, there are no semi-supervised machine learning methods, that recognize named entities of natural language mutation mentions. In this thesis, I am aiming to create a named entity recognition conditional random field machine learning method, that is semi-supervised and targets natural language mentions of mutation names and descriptions to extract those entities.
> NOTE semi-supervised means:
> - combination of annotated data-points and novel data-points
> - confident (above a threshold) enough classified data-points are automatically defined as true (and used in further training?)
> - not-confident enough data-points can be manually declared true or false and incorporated in the training


Therefore a pipeline is developed, that aims to extract relevant protein mutations for genetic diseases, that can be used in drug-targeted pharmadevelopment.

## Timeframe

* Actual start: **@March-26th**
* Official start: **@June-15th**
* Method finished: **@August-15th**
* Official end: **@Octobre-15th**

# Alex's thesis 

## Title: Repre learning of natural language mutation mentions

> Old titles
* NER of natural language mentions of mutations in bio-medical texts
* Word representation features for NER of natural language mentions of mutations
* Unsupervised features learning for NER in the bio-medical domain

## Abstract
As the volume of published research in the biomedical domain increases, the need for effective information extraction systems grows with it. In this context, the task of named entity recognition (NER), defined as classifying chunks of text in natural language to a set of predefined categories such as genes, proteins or other entities, is essential.

The performance of named entity recognition (NER) models, in general, is intrinsically limited by the availability of quality annotated corpora. The construction of such corpora is usually costly and even more so when there is a need for expert annotators. In the biomedical domain, the difficulty of the task is even greater compared to other domains, due do the much higher number of possible named entities, which keeps increasing constantly.

To combat the lack of large annotated corpora, we turn to exploitation of large volumes of unlabeled text. Using techniques for unsupervised feature learning we aim to increase the performance of traditional NER models. More specifically, this thesis focuses on augmenting typical conditional random field (CRF) approaches with word representation features learned from large bodies of biomedical text. The goal is to evaluate the usefulness and effect on performance of different approaches such as word embeddings based on deep architectures, distributional representations or clustering based methods. 

[maybe a add a small paragraph about active learning and creating a larger corpus]


