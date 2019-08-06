---
layout: post
title:  "Analysis of Performance by Event"
date:   2019-08-01 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---
The objective of this analysis is to compare the performance of classifier trained
to identify accountability specific to an event, vs a classifier trained to
identify accountability in general. If there are common features across all events
that indicate accountability, then the performance when trained on all the
news events should increase (typically more data improves performance).

However, if the performance decreases when the classifier is trained on multiple
datasets, this means that it is likely there are not a prominent features that capture the
meaning of accountability in general. This could indicate that the annotations of
accountability are event specific, or there is not enough data from a variety of
different events to capture the generalized representation of accountability.

The results shown in this post also compare sentence vs excerpt level classifiers,
and a comparison of different representation and classification algorithms.

## Summary of Findings

The main observation, is that there is a wide range of performance results,
with some events achieving performance in fscore above 0.8, while some are as low as
~0.5. Also, note that the inter-annotator agreement for the events ranges from 0.6-0.8.

The effect of transitioning from excerpt level to sentence level also decreases
performance, but not by as much as the effect of the event.

An additional finding is that the character based representation, and the SVM
classifier had the best performance out of the methods tested in this analysis,
the the difference between performance in the linear classifiers is almost
across all the variations tested is almost negligeable.

The are summarized in tables in the following sections. 

## Individual Events

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
      <th>event</th>
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
      <th>Charleston</th>
      <td>108.0</td>
      <td>0.232965</td>
      <td>0.141681</td>
      <td>0.000000</td>
      <td>0.120760</td>
      <td>0.245000</td>
      <td>0.357264</td>
      <td>0.462500</td>
    </tr>
    <tr>
      <th>Isla Vista</th>
      <td>108.0</td>
      <td>0.738317</td>
      <td>0.024722</td>
      <td>0.693498</td>
      <td>0.721297</td>
      <td>0.738237</td>
      <td>0.750443</td>
      <td>0.802410</td>
    </tr>
    <tr>
      <th>Marysville</th>
      <td>108.0</td>
      <td>0.710327</td>
      <td>0.028182</td>
      <td>0.654321</td>
      <td>0.687905</td>
      <td>0.710819</td>
      <td>0.733473</td>
      <td>0.761905</td>
    </tr>
    <tr>
      <th>Newtown</th>
      <td>108.0</td>
      <td>0.363988</td>
      <td>0.127713</td>
      <td>0.152091</td>
      <td>0.245902</td>
      <td>0.397473</td>
      <td>0.475519</td>
      <td>0.560870</td>
    </tr>
    <tr>
      <th>Orlando</th>
      <td>108.0</td>
      <td>0.270458</td>
      <td>0.157829</td>
      <td>0.000000</td>
      <td>0.138889</td>
      <td>0.278532</td>
      <td>0.418455</td>
      <td>0.476190</td>
    </tr>
    <tr>
      <th>San Bernardino</th>
      <td>108.0</td>
      <td>0.321567</td>
      <td>0.116414</td>
      <td>0.096386</td>
      <td>0.235294</td>
      <td>0.336304</td>
      <td>0.421232</td>
      <td>0.522293</td>
    </tr>
    <tr>
      <th>Vegas</th>
      <td>108.0</td>
      <td>0.141236</td>
      <td>0.115760</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.121212</td>
      <td>0.250880</td>
      <td>0.380952</td>
    </tr>
  </tbody>
</table>
</div>

### Excerpts

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
      <th>event</th>
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
      <th>Charleston</th>
      <td>108.0</td>
      <td>0.323976</td>
      <td>0.141580</td>
      <td>0.050000</td>
      <td>0.215686</td>
      <td>0.338462</td>
      <td>0.448497</td>
      <td>0.568182</td>
    </tr>
    <tr>
      <th>Isla Vista</th>
      <td>108.0</td>
      <td>0.757786</td>
      <td>0.022385</td>
      <td>0.722045</td>
      <td>0.740443</td>
      <td>0.754337</td>
      <td>0.777850</td>
      <td>0.813754</td>
    </tr>
    <tr>
      <th>Marysville</th>
      <td>108.0</td>
      <td>0.762653</td>
      <td>0.060974</td>
      <td>0.649351</td>
      <td>0.717634</td>
      <td>0.768177</td>
      <td>0.810127</td>
      <td>0.882353</td>
    </tr>
    <tr>
      <th>Newtown</th>
      <td>108.0</td>
      <td>0.413744</td>
      <td>0.164910</td>
      <td>0.067797</td>
      <td>0.337558</td>
      <td>0.476467</td>
      <td>0.522574</td>
      <td>0.599156</td>
    </tr>
    <tr>
      <th>Orlando</th>
      <td>108.0</td>
      <td>0.237244</td>
      <td>0.146436</td>
      <td>0.000000</td>
      <td>0.117647</td>
      <td>0.288018</td>
      <td>0.354430</td>
      <td>0.487805</td>
    </tr>
    <tr>
      <th>San Bernardino</th>
      <td>108.0</td>
      <td>0.412743</td>
      <td>0.130067</td>
      <td>0.121212</td>
      <td>0.333333</td>
      <td>0.448881</td>
      <td>0.500000</td>
      <td>0.615385</td>
    </tr>
    <tr>
      <th>Vegas</th>
      <td>108.0</td>
      <td>0.143728</td>
      <td>0.152868</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.080000</td>
      <td>0.285714</td>
      <td>0.518519</td>
    </tr>
  </tbody>
</table>
</div>

## Combined Datasets

### Sentences

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



### Excerpts


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
