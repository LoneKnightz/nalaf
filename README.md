# Carsten's bthesis

Bachelor thesis about named entity recognition for natural language mentions of mutation names in the biomedical domain.

## title
> multiple versions

- [ ] Semi-supervised natural language NER of biomedical documents
- [ ] Protein mutation causing disease search through NER of biomedical texts
- [ ] Natural language NER of protein mutations in biomedical text domain
- [ ] Natural language NER within biomedical domain
- [ ] Natural language NER within biomedical domain drug-targeting


## abstract
Research and development in the biomedical domain is constantly growing. Millions of documents have been already published on various platforms including Pubmed.

The development of literature information extraction (NER important here) has already been done to a certain extend: protein, mutation, gene names and similar following naming conventions can be easily parsed. The difficulty lies within the naming or description of protein names that are consisting of multiple words, are based on the natural language and, thus are not easily being parsed.

On top of that, there are (almost?) no semi-supervised machine learning methods, that improve over time with more data. In this thesis, I am aiming to create a NER CRF machine learning method, that is semi-supervised and targets natural language mentions of protein mutation names and descriptions to extract those entities. (best case: self-improving machine that feeds on pubmed abstracts/articles)

Therefore a pipeline is developed, that aims to extract relevant protein mutations for genetic diseases, that can be used in drug-targeted pharma (is that the right way to say?) development.



## documentation CRF

### 1

Very deep tutorial. Contains lots of mathematics. But easy to understand, if to aim for full understanding of CRF.

[Tutorial by Charles Sutton and Andrew Cullom as PDF](http://people.cs.umass.edu/~mccallum/papers/crf-tutorial.pdf)

### 2

My presentation about CRF, which is very superficial, but lets you get an idea of CRF.

[CRF presenation at docs.google.com](https://docs.google.com/presentation/d/1Sq9a-y_2WW3I7gXBK-IUZx6eNG7vhJO1UfwX7MqWdgc/pub?start=false&loop=false&delayms=5000)


## Timeline

### Main timeframe

* Actual start: **@March-26th**
* Official start: **@May-15th**
* Method finished: **@August-15th**
* Official end: **@September-15th**


### Tasks and Planning

* [ ] Understand current guidelines in IDP4
* [ ] Try to annotate a few documents on tagtog (in `cuhlig` user)
* [ ] **@April-30th** Specify for myself my own guidelines of mutation mentions   
  *caring about distinction: standard vs NL mentions -- define exactly what a NL mention is (either follow Ankit's rule or your own)*


* [ ] Decide on final CRF framework (mallet vs CRF++ vs crfsuite vs ?)

* [ ] Develop own method
  * [ ] Create basic pipeline
    * [ ] Accept input
    * [ ] Data-structure the input
    * [ ] Output: do predictions
  * [ ] Bootstrapping, semi-supervised learning
  * [ ] Annotating (just sentences from abstracts)
  * [ ] Work on the CRF features
