---
layout: post
title:  "Comparison of Text Tfidf Representations"
date:   2019-08-02 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---
This analysis will compare different text representations with simple sklearn linear and ensemble classifiers. The basis of all the text representations tested in this analysis is the sklearn vectorizer. Another, more common approach to represent text is based on word embeddings, but that is out of the scope of this post, and will be explained in a subsequent post.

The sklearn basic vectorizers are the focus of this analysis, because they have shown that their baseline performance [previously tested](https://anjapago.github.io/AnalyzeAccountability/update/2019/06/05/binary-classifier.html) was comparable in performance to state of the art text representation using [BERT embeddings](https://anjapago.github.io/AnalyzeAccountability/update/2019/07/11/sentence-classifier-BERT.html). Since previously no experimentation was done on the input representation to these basic linear classifiers and the classifier performance was still comparable with state of the art methods, these simple sklearn classifiers will be re-visited and tested again with different variations of the input text representation to see if any substantial improvements can be obtained.

## Text Pre-Processing and Vectorization

There were several variations of each phase of the text processing pipeline tested in this experiment, as will be explained in the following sections.

The main phases are:
* Text Cleaning
* Text Analyzer
* N-grams
* Text vectorizer

### Text Cleaning
There are numerous variations of what can be done during the text cleaning phase, such as removing certain terms, numbers, punctuation, lemmatizing words, lower casing words, etc. The first step applied in all cases is lower-casing all words, this is to reduce the vocabulary size and noisiness. There were several variations of subsequents steps to the text cleaning applied next:

* None: input text remains as is
* Removing numbers: often numeric values do not provide significant meaning and only add noise, e.g. the numbers 1, 5000, 35, etc. ... if these numbers are mentioned in the text, each one would be a new term in the vocabulary.
* Removing numbers and punctuation: in this variation the only characters remaining are letters, and so the vocabulary will be much cleaner, made up only of words. However this is possible that it could also lose some of the meaning connected to numbers and punctuation that was used.

### Text Tokenization

The variations of text cleaning previously explained were all used with the bert tokenization method described below. Other variants of tokenization were also used, including the most simple word based approach built in to sklearn vectorizer, and also the character-based analyzer option built into the sklearn vectorizer.

* **Bert-based method**: This method is a custom tokenization procedure, that is used for input to the BERT classifiers. Bert uses SentencePiece, an unsupervised text tokenizer that implements subword units (e.g., byte-pair-encoding). The steps followed in this procedure are:
    * Word tokenize it (i.e. "susie is calling" -> ["susie", "is", "calling"])
    * Break words into WordPieces (i.e. "calling" -> ["call", "##ing"])
    * Add special "CLS" and "SEP" tokens
    * Append "index" and "segment" tokens to each input
* **Word Tokenization**: basic tokenization based on white spaces between words
* **Character based tokenization**: each character is considered an individual unit, and tokens are made up of character n-grams, as will be described in the following section

### N-grams

N-grams determine the number of tokens to include as an individual unit to count in the document. For example, character-based 3-grams for "good morning" would be: "goo", "ood", "od ", "d m", " mo", "mor" ... etc., with each combination of 3 adjacent characters. For sequences of words, the 3-grams for a the phrase "the dog ran up the hill" are "# the dog", "the dog ran", "dog ran up", ... etc.. Any  number of n can be chosen as the the number of n-grams to consider. The numbers chosen for this experiments were:
* bert based tokens: unigrams only, unigrams bigrams and trigrams
* word tokens: unigram, unigrams bigrams and trigrams
* character based: n-grams from three to ten characters

 Note, increasing the number of n-grams to include will greatly increase the size of the vocabulary, and so there must be methods to mitigate this great increase in vocabulary size, such as setting a maximum vocabulary size, and excluding vocabulary terms that are too rare (most terms will be rare due to [zipf's law](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4176592/)).

### Text Vectorizers
There are multiple versions of the vectorizers that can be used from sklearn including:

* Count vectors: each text is translated into a vector directly based on the counts of each term in the vocabulary. For example, with a vocabulary vector of [dog, runs, the, up, hill, good], the text "The dog runs up the hill. The dog is good." would be transformed into the vector: [dog:2, runs:1, the:3, up:1, hill:1, good:1].
* term-frequency inverse-document-frequency (tfidf): is the product of two statistics, term frequency and inverse document frequency, which has the effect of weighting terms by importance. Note how the word "the" had a high weight in the previous example, even though that term had low impact on the meaning of the content. This can be factored in by taking into account the word "the" will occur at a high frequency across all documents, and the weight will be adjusted proportional to that to decrease the weight of this term.

Additional settings set in the vectorizer include:
* minimum frequency: minimum frequency of words or ngrams. as mentioned, there will be a large number of tokens and ngrams that occur only once or a few times across the whole corpus . This will greatly expand the size of the vocabulary, especially when considering a large number of ngrams, and so a way to limit this is to set a restriction in the vectorizer, than only allows terms that appear a minimum number of times to exist in the vocabulary. For this set of experiments this value was set at 10.
* maximum frequency: Maximum frequency is a way of limiting the vocabulary to reduce the number of stop words. Instead of using a built in stopwords library, we can simply set a restriction on the maximum allowable frequency of terms. This means, that terms that appear in every document will be excluded because those terms will not have a big impact on the classifier anyways, especially given the tfidf weighting, and these term weights will likely just contribute noise and increase the dimensionality unnecessarily.




## Analysis by Classifier and Representations

The results from testing all the representation previously described is summarized in the folloing tables. The vectorizers are named according to the number of ngrams, whether it was character based "char", and the type of custom tokenization (the bert method)  and pre-processing (all characters included, no numbers, and only letter characters included).

Two linear classifiers were tested: logistic regression and support vector machines (SVM), as well as an ensemble method for comparison. A balanced cost functions was used, and a normal cost function was also used for SVM.

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>classifier</th>
      <th>vectorizer</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="9" valign="top">logregcv</th>
      <th>1gram</th>
      <td>21.0</td>
      <td>0.387130</td>
      <td>0.291712</td>
      <td>0.000000</td>
      <td>0.216216</td>
      <td>0.341463</td>
      <td>0.714286</td>
      <td>0.835821</td>
    </tr>
    <tr>
      <th>3gram</th>
      <td>21.0</td>
      <td>0.404456</td>
      <td>0.291235</td>
      <td>0.000000</td>
      <td>0.117647</td>
      <td>0.418605</td>
      <td>0.690909</td>
      <td>0.823529</td>
    </tr>
    <tr>
      <th>char</th>
      <td>21.0</td>
      <td>0.415545</td>
      <td>0.289436</td>
      <td>0.000000</td>
      <td>0.227273</td>
      <td>0.419753</td>
      <td>0.690909</td>
      <td>0.869565</td>
    </tr>
    <tr>
      <th>cust_all-1gram</th>
      <td>21.0</td>
      <td>0.376788</td>
      <td>0.316743</td>
      <td>0.000000</td>
      <td>0.050000</td>
      <td>0.341463</td>
      <td>0.742515</td>
      <td>0.865672</td>
    </tr>
    <tr>
      <th>cust_all-3gram</th>
      <td>21.0</td>
      <td>0.379196</td>
      <td>0.301674</td>
      <td>0.000000</td>
      <td>0.121212</td>
      <td>0.305085</td>
      <td>0.750000</td>
      <td>0.882353</td>
    </tr>
    <tr>
      <th>cust_no_nums-1gram</th>
      <td>21.0</td>
      <td>0.375641</td>
      <td>0.316426</td>
      <td>0.000000</td>
      <td>0.050000</td>
      <td>0.341463</td>
      <td>0.750751</td>
      <td>0.865672</td>
    </tr>
    <tr>
      <th>cust_no_nums-3gram</th>
      <td>21.0</td>
      <td>0.393199</td>
      <td>0.302940</td>
      <td>0.000000</td>
      <td>0.121212</td>
      <td>0.392157</td>
      <td>0.750000</td>
      <td>0.882353</td>
    </tr>
    <tr>
      <th>cust_only_alpha-1gram</th>
      <td>21.0</td>
      <td>0.377285</td>
      <td>0.308369</td>
      <td>0.000000</td>
      <td>0.171429</td>
      <td>0.333333</td>
      <td>0.750000</td>
      <td>0.852941</td>
    </tr>
    <tr>
      <th>cust_only_alpha-3gram</th>
      <td>21.0</td>
      <td>0.401743</td>
      <td>0.295126</td>
      <td>0.000000</td>
      <td>0.121212</td>
      <td>0.435294</td>
      <td>0.727273</td>
      <td>0.848485</td>
    </tr>
    <tr>
      <th rowspan="9" valign="top">logregcv_balanced</th>
      <th>1gram</th>
      <td>21.0</td>
      <td>0.495358</td>
      <td>0.210163</td>
      <td>0.062500</td>
      <td>0.380952</td>
      <td>0.488889</td>
      <td>0.695652</td>
      <td>0.821918</td>
    </tr>
    <tr>
      <th>3gram</th>
      <td>21.0</td>
      <td>0.508967</td>
      <td>0.212936</td>
      <td>0.074074</td>
      <td>0.380952</td>
      <td>0.483871</td>
      <td>0.718750</td>
      <td>0.810811</td>
    </tr>
    <tr>
      <th>char</th>
      <td>21.0</td>
      <td>0.521330</td>
      <td>0.182913</td>
      <td>0.190476</td>
      <td>0.379310</td>
      <td>0.502415</td>
      <td>0.666667</td>
      <td>0.857143</td>
    </tr>
    <tr>
      <th>cust_all-1gram</th>
      <td>21.0</td>
      <td>0.491233</td>
      <td>0.214054</td>
      <td>0.064516</td>
      <td>0.352941</td>
      <td>0.497653</td>
      <td>0.707692</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>cust_all-3gram</th>
      <td>21.0</td>
      <td>0.499426</td>
      <td>0.209599</td>
      <td>0.083333</td>
      <td>0.333333</td>
      <td>0.481132</td>
      <td>0.709677</td>
      <td>0.837838</td>
    </tr>
    <tr>
      <th>cust_no_nums-1gram</th>
      <td>21.0</td>
      <td>0.497385</td>
      <td>0.212544</td>
      <td>0.066667</td>
      <td>0.366197</td>
      <td>0.461538</td>
      <td>0.730159</td>
      <td>0.861111</td>
    </tr>
    <tr>
      <th>cust_no_nums-3gram</th>
      <td>21.0</td>
      <td>0.499315</td>
      <td>0.208580</td>
      <td>0.086957</td>
      <td>0.347826</td>
      <td>0.479592</td>
      <td>0.700000</td>
      <td>0.873239</td>
    </tr>
    <tr>
      <th>cust_only_alpha-1gram</th>
      <td>21.0</td>
      <td>0.492733</td>
      <td>0.217237</td>
      <td>0.076923</td>
      <td>0.322581</td>
      <td>0.478873</td>
      <td>0.730159</td>
      <td>0.849315</td>
    </tr>
    <tr>
      <th>cust_only_alpha-3gram</th>
      <td>21.0</td>
      <td>0.510576</td>
      <td>0.208496</td>
      <td>0.074074</td>
      <td>0.416667</td>
      <td>0.480392</td>
      <td>0.730159</td>
      <td>0.837838</td>
    </tr>
    <tr>
      <th rowspan="9" valign="top">random_forest_balanced</th>
      <th>1gram</th>
      <td>21.0</td>
      <td>0.311567</td>
      <td>0.293623</td>
      <td>0.000000</td>
      <td>0.090909</td>
      <td>0.187500</td>
      <td>0.701754</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th>3gram</th>
      <td>21.0</td>
      <td>0.340907</td>
      <td>0.266239</td>
      <td>0.000000</td>
      <td>0.146341</td>
      <td>0.227273</td>
      <td>0.666667</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th>char</th>
      <td>21.0</td>
      <td>0.365583</td>
      <td>0.263516</td>
      <td>0.000000</td>
      <td>0.181818</td>
      <td>0.251852</td>
      <td>0.689655</td>
      <td>0.800000</td>
    </tr>
    <tr>
      <th>cust_all-1gram</th>
      <td>21.0</td>
      <td>0.312634</td>
      <td>0.283756</td>
      <td>0.000000</td>
      <td>0.125000</td>
      <td>0.174603</td>
      <td>0.689655</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th>cust_all-3gram</th>
      <td>21.0</td>
      <td>0.331651</td>
      <td>0.272659</td>
      <td>0.000000</td>
      <td>0.111111</td>
      <td>0.229008</td>
      <td>0.654545</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th>cust_no_nums-1gram</th>
      <td>21.0</td>
      <td>0.302543</td>
      <td>0.291940</td>
      <td>0.000000</td>
      <td>0.097561</td>
      <td>0.160000</td>
      <td>0.701754</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th>cust_no_nums-3gram</th>
      <td>21.0</td>
      <td>0.332594</td>
      <td>0.269699</td>
      <td>0.000000</td>
      <td>0.115702</td>
      <td>0.227273</td>
      <td>0.654545</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th>cust_only_alpha-1gram</th>
      <td>21.0</td>
      <td>0.311563</td>
      <td>0.293241</td>
      <td>0.000000</td>
      <td>0.090909</td>
      <td>0.181818</td>
      <td>0.701754</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th>cust_only_alpha-3gram</th>
      <td>21.0</td>
      <td>0.331593</td>
      <td>0.282147</td>
      <td>0.000000</td>
      <td>0.121212</td>
      <td>0.227273</td>
      <td>0.666667</td>
      <td>0.779661</td>
    </tr>
    <tr>
      <th rowspan="9" valign="top">svm_balanced</th>
      <th>1gram</th>
      <td>21.0</td>
      <td>0.528486</td>
      <td>0.191674</td>
      <td>0.000000</td>
      <td>0.454545</td>
      <td>0.522727</td>
      <td>0.702703</td>
      <td>0.842105</td>
    </tr>
    <tr>
      <th>3gram</th>
      <td>21.0</td>
      <td>0.527106</td>
      <td>0.190601</td>
      <td>0.062500</td>
      <td>0.428571</td>
      <td>0.500000</td>
      <td>0.687500</td>
      <td>0.853333</td>
    </tr>
    <tr>
      <th>char</th>
      <td>21.0</td>
      <td>0.537184</td>
      <td>0.193380</td>
      <td>0.000000</td>
      <td>0.444444</td>
      <td>0.523364</td>
      <td>0.718750</td>
      <td>0.833333</td>
    </tr>
    <tr>
      <th>cust_all-1gram</th>
      <td>21.0</td>
      <td>0.517229</td>
      <td>0.186578</td>
      <td>0.060606</td>
      <td>0.413793</td>
      <td>0.526718</td>
      <td>0.649351</td>
      <td>0.820513</td>
    </tr>
    <tr>
      <th>cust_all-3gram</th>
      <td>21.0</td>
      <td>0.527482</td>
      <td>0.183058</td>
      <td>0.080000</td>
      <td>0.444444</td>
      <td>0.513274</td>
      <td>0.696970</td>
      <td>0.794872</td>
    </tr>
    <tr>
      <th>cust_no_nums-1gram</th>
      <td>21.0</td>
      <td>0.517215</td>
      <td>0.184749</td>
      <td>0.064516</td>
      <td>0.413793</td>
      <td>0.514286</td>
      <td>0.649351</td>
      <td>0.810127</td>
    </tr>
    <tr>
      <th>cust_no_nums-3gram</th>
      <td>21.0</td>
      <td>0.521650</td>
      <td>0.188471</td>
      <td>0.080000</td>
      <td>0.454545</td>
      <td>0.500000</td>
      <td>0.686567</td>
      <td>0.810127</td>
    </tr>
    <tr>
      <th>cust_only_alpha-1gram</th>
      <td>21.0</td>
      <td>0.523520</td>
      <td>0.181054</td>
      <td>0.066667</td>
      <td>0.423529</td>
      <td>0.529412</td>
      <td>0.657895</td>
      <td>0.810127</td>
    </tr>
    <tr>
      <th>cust_only_alpha-3gram</th>
      <td>21.0</td>
      <td>0.527546</td>
      <td>0.190969</td>
      <td>0.071429</td>
      <td>0.437500</td>
      <td>0.512821</td>
      <td>0.707692</td>
      <td>0.810127</td>
    </tr>
  </tbody>
</table>
</div>


## Analysis of Classifier on Full Datasets

### Sentence Based

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>classifier</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>logregcv</th>
      <td>27.0</td>
      <td>0.538240</td>
      <td>0.026181</td>
      <td>0.502447</td>
      <td>0.521963</td>
      <td>0.528771</td>
      <td>0.563489</td>
      <td>0.583333</td>
    </tr>
    <tr>
      <th>logregcv_balanced</th>
      <td>27.0</td>
      <td>0.560509</td>
      <td>0.032042</td>
      <td>0.504496</td>
      <td>0.532829</td>
      <td>0.565003</td>
      <td>0.591144</td>
      <td>0.606166</td>
    </tr>
    <tr>
      <th>random_forest_balanced</th>
      <td>27.0</td>
      <td>0.506861</td>
      <td>0.008723</td>
      <td>0.489726</td>
      <td>0.502209</td>
      <td>0.505082</td>
      <td>0.509686</td>
      <td>0.532418</td>
    </tr>
    <tr>
      <th>svm_balanced</th>
      <td>27.0</td>
      <td>0.552539</td>
      <td>0.026245</td>
      <td>0.511447</td>
      <td>0.536557</td>
      <td>0.550852</td>
      <td>0.573312</td>
      <td>0.607453</td>
    </tr>
  </tbody>
</table>
</div>

### Excerpt Based

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>classifier</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>logregcv</th>
      <td>27.0</td>
      <td>0.606388</td>
      <td>0.029977</td>
      <td>0.548485</td>
      <td>0.592954</td>
      <td>0.600801</td>
      <td>0.624813</td>
      <td>0.658854</td>
    </tr>
    <tr>
      <th>logregcv_balanced</th>
      <td>27.0</td>
      <td>0.616874</td>
      <td>0.023957</td>
      <td>0.576471</td>
      <td>0.600716</td>
      <td>0.612943</td>
      <td>0.629839</td>
      <td>0.661818</td>
    </tr>
    <tr>
      <th>random_forest_balanced</th>
      <td>27.0</td>
      <td>0.470446</td>
      <td>0.021622</td>
      <td>0.440141</td>
      <td>0.454623</td>
      <td>0.464883</td>
      <td>0.489271</td>
      <td>0.507993</td>
    </tr>
    <tr>
      <th>svm_balanced</th>
      <td>27.0</td>
      <td>0.614373</td>
      <td>0.028834</td>
      <td>0.566914</td>
      <td>0.590567</td>
      <td>0.618690</td>
      <td>0.629487</td>
      <td>0.670190</td>
    </tr>
  </tbody>
</table>
</div>


## Analysis of Representation on Full datasets

### Sentence Based

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>vectorizer</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1gram</th>
      <td>12.0</td>
      <td>0.523218</td>
      <td>0.014292</td>
      <td>0.502758</td>
      <td>0.512716</td>
      <td>0.524475</td>
      <td>0.531200</td>
      <td>0.546624</td>
    </tr>
    <tr>
      <th>3gram</th>
      <td>12.0</td>
      <td>0.551585</td>
      <td>0.032038</td>
      <td>0.504334</td>
      <td>0.528432</td>
      <td>0.556689</td>
      <td>0.574398</td>
      <td>0.593997</td>
    </tr>
    <tr>
      <th>char</th>
      <td>12.0</td>
      <td>0.570441</td>
      <td>0.031584</td>
      <td>0.518699</td>
      <td>0.548608</td>
      <td>0.579456</td>
      <td>0.590890</td>
      <td>0.607453</td>
    </tr>
    <tr>
      <th>cust_all-1gram</th>
      <td>12.0</td>
      <td>0.517531</td>
      <td>0.016412</td>
      <td>0.496622</td>
      <td>0.502655</td>
      <td>0.517321</td>
      <td>0.532072</td>
      <td>0.542048</td>
    </tr>
    <tr>
      <th>cust_all-3gram</th>
      <td>12.0</td>
      <td>0.548571</td>
      <td>0.034563</td>
      <td>0.498834</td>
      <td>0.518188</td>
      <td>0.558592</td>
      <td>0.578283</td>
      <td>0.590374</td>
    </tr>
    <tr>
      <th>cust_no_nums-1gram</th>
      <td>12.0</td>
      <td>0.519189</td>
      <td>0.017042</td>
      <td>0.489726</td>
      <td>0.505752</td>
      <td>0.520005</td>
      <td>0.534048</td>
      <td>0.540292</td>
    </tr>
    <tr>
      <th>cust_no_nums-3gram</th>
      <td>12.0</td>
      <td>0.550599</td>
      <td>0.033735</td>
      <td>0.505082</td>
      <td>0.518338</td>
      <td>0.557842</td>
      <td>0.578534</td>
      <td>0.593817</td>
    </tr>
    <tr>
      <th>cust_only_alpha-1gram</th>
      <td>12.0</td>
      <td>0.518241</td>
      <td>0.013186</td>
      <td>0.501186</td>
      <td>0.507472</td>
      <td>0.517567</td>
      <td>0.526971</td>
      <td>0.537879</td>
    </tr>
    <tr>
      <th>cust_only_alpha-3gram</th>
      <td>12.0</td>
      <td>0.556459</td>
      <td>0.034341</td>
      <td>0.506245</td>
      <td>0.526145</td>
      <td>0.568348</td>
      <td>0.578001</td>
      <td>0.602856</td>
    </tr>
  </tbody>
</table>
</div>

### Excerpt Based

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
    <tr>
      <th>vectorizer</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1gram</th>
      <td>12.0</td>
      <td>0.556811</td>
      <td>0.060908</td>
      <td>0.440141</td>
      <td>0.540708</td>
      <td>0.577642</td>
      <td>0.601289</td>
      <td>0.606838</td>
    </tr>
    <tr>
      <th>3gram</th>
      <td>12.0</td>
      <td>0.587291</td>
      <td>0.075564</td>
      <td>0.451049</td>
      <td>0.563028</td>
      <td>0.620402</td>
      <td>0.637051</td>
      <td>0.658854</td>
    </tr>
    <tr>
      <th>char</th>
      <td>12.0</td>
      <td>0.600079</td>
      <td>0.070327</td>
      <td>0.469178</td>
      <td>0.579143</td>
      <td>0.620645</td>
      <td>0.648738</td>
      <td>0.670190</td>
    </tr>
    <tr>
      <th>cust_all-1gram</th>
      <td>12.0</td>
      <td>0.560850</td>
      <td>0.062405</td>
      <td>0.440141</td>
      <td>0.547690</td>
      <td>0.587992</td>
      <td>0.597148</td>
      <td>0.623542</td>
    </tr>
    <tr>
      <th>cust_all-3gram</th>
      <td>12.0</td>
      <td>0.589742</td>
      <td>0.072032</td>
      <td>0.457539</td>
      <td>0.576271</td>
      <td>0.618028</td>
      <td>0.633470</td>
      <td>0.653504</td>
    </tr>
    <tr>
      <th>cust_no_nums-1gram</th>
      <td>12.0</td>
      <td>0.555949</td>
      <td>0.060072</td>
      <td>0.445614</td>
      <td>0.536471</td>
      <td>0.584496</td>
      <td>0.596083</td>
      <td>0.604692</td>
    </tr>
    <tr>
      <th>cust_no_nums-3gram</th>
      <td>12.0</td>
      <td>0.589490</td>
      <td>0.070813</td>
      <td>0.457539</td>
      <td>0.577209</td>
      <td>0.620488</td>
      <td>0.632463</td>
      <td>0.648438</td>
    </tr>
    <tr>
      <th>cust_only_alpha-1gram</th>
      <td>12.0</td>
      <td>0.557290</td>
      <td>0.060581</td>
      <td>0.440141</td>
      <td>0.535464</td>
      <td>0.579711</td>
      <td>0.595053</td>
      <td>0.622642</td>
    </tr>
    <tr>
      <th>cust_only_alpha-3gram</th>
      <td>12.0</td>
      <td>0.595678</td>
      <td>0.071185</td>
      <td>0.459413</td>
      <td>0.578810</td>
      <td>0.623086</td>
      <td>0.639356</td>
      <td>0.661433</td>
    </tr>
  </tbody>
</table>
</div>

## Summary of Performance Results
The most notable effect on performance from the various representations was that character based consistently performed higher than other methods. However, the difference between representation methods was almost negligeable, considering the amount of variation between folds in the 3-cross validation.

In the comparison of classifiers, it is clear overall the linear methods perform best, and the balanced SVM was slightly better in most cases.
