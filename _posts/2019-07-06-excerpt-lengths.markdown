---
layout: post
title:  "Analysis of Excerpts For Sentence Classifier"
date:   2019-07-06 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---


This notebook will analyze how many sentences are in each excerpt, and transform the labelled excerpts into a dataset of labelled sentences.

## Import Data and Libraries


```python
import numpy as np
import matplotlib.pyplot as plt

from itertools import compress
from classifiers.binary_classifier import *
from nltk import sent_tokenize
```


```python
data_df = load_data()
```


```python
data_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ACCOUNT</th>
      <th>Excerpts</th>
      <th>StoryID</th>
      <th>file</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Are guns the problem, video\ngames, the increa...</td>
      <td>NI2599</td>
      <td>data/Isla Vista - All Excerpts - 1_2_2019.xlsx</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>May 23, 2014, in Isla Vista, California. 22-ye...</td>
      <td>NI2599</td>
      <td>data/Isla Vista - All Excerpts - 1_2_2019.xlsx</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>A 22-year-old student last Friday killed six p...</td>
      <td>NI2951</td>
      <td>data/Isla Vista - All Excerpts - 1_2_2019.xlsx</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>A 22-year-old student last Friday killed six p...</td>
      <td>NI2951</td>
      <td>data/Isla Vista - All Excerpts - 1_2_2019.xlsx</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Elliot Rodger was not a typical man � few of u...</td>
      <td>NI2951</td>
      <td>data/Isla Vista - All Excerpts - 1_2_2019.xlsx</td>
    </tr>
  </tbody>
</table>
</div>



## Process Data Into Sentences


```python
sentences = []
account_labels = []
original_file = []
docid = []
excerpt_lengths = []
excerpt_len_sent_df = []

for index, row in data_df.iterrows():
    excerpt = row['Excerpts']
    excerpt_sentences = sent_tokenize(excerpt)
    labels = [row['ACCOUNT']]*len(excerpt_sentences) # add same label for each sentence
    StoryIDs = [row['StoryID']]*len(excerpt_sentences) # add same label for each sentence
    files = [row['file']]*len(excerpt_sentences) # add same label for each sentence
    excerpt_lengths.append(len(excerpt_sentences))
    excerpt_len_sent_df.extend([len(excerpt_sentences)]*len(excerpt_sentences))

    sentences.extend(excerpt_sentences)

    account_labels.extend(labels)
    original_file.extend(files)
    docid.extend(StoryIDs)
    if index%1000 ==0:
        print("Index: "+str(index))

sentences_dict = {'file':original_file, 'StoryID': docid,
                  'Sentences': sentences, 'ACCOUNT': account_labels,
                 'excerpt_length':excerpt_len_sent_df}

sentences_df = pd.DataFrame(sentences_dict)
```

    Index: 0
    Index: 1000
    Index: 2000
    Index: 3000
    Index: 4000
    Index: 5000
    Index: 6000
    Index: 7000
    Index: 8000
    Index: 9000
    Index: 10000
    Index: 11000
    Index: 12000
    Index: 13000
    Index: 14000
    Index: 15000
    Index: 16000
    Index: 17000
    Index: 18000
    Index: 19000
    Index: 20000
    Index: 21000



```python
# save the sentences data frame to csv for further use
sentences_df.to_csv("data/sentences_df.csv")
```

## Analyze Lengths of Sentences

### Overall Excerpt Length Distribution


```python
plt.hist(excerpt_lengths, bins=60)
plt.title("Histogram of Number of Sentences")
plt.xlabel("Number of Sentences in Excerpt")
plt.ylabel("Number of Excerpts")
plt.savefig('sentence_counts.png')
plt.show()
```


![png](output_8_0.png)



```python
data_df['excerpt_lengths']=excerpt_lengths
```


```python
fig = plt.figure(figsize = (15,10))
ax = fig.gca()
data_df['excerpt_lengths'].hist(by=data_df['file'], bins = 60, ax=ax)
plt.show()
```

    /anaconda3/lib/python3.6/site-packages/pandas/plotting/_core.py:2214: UserWarning: To output multiple subplots, the figure containing the passed axes is being cleared
      ylabelsize=ylabelsize, yrot=yrot, **kwds)



![png](output_10_1.png)



```python
sentence_counts_df = pd.DataFrame(data_df.excerpt_lengths.value_counts())
sentence_counts_df.columns = ['Number of Excerpts']
sentence_counts_df.index.name = 'Number of Sentences in Excerpt'
sentence_counts_df.sort_index()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Excerpts</th>
    </tr>
    <tr>
      <th>Number of Sentences in Excerpt</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>5730</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4650</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3384</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2273</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1564</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1180</td>
    </tr>
    <tr>
      <th>7</th>
      <td>785</td>
    </tr>
    <tr>
      <th>8</th>
      <td>591</td>
    </tr>
    <tr>
      <th>9</th>
      <td>448</td>
    </tr>
    <tr>
      <th>10</th>
      <td>286</td>
    </tr>
    <tr>
      <th>11</th>
      <td>231</td>
    </tr>
    <tr>
      <th>12</th>
      <td>146</td>
    </tr>
    <tr>
      <th>13</th>
      <td>125</td>
    </tr>
    <tr>
      <th>14</th>
      <td>125</td>
    </tr>
    <tr>
      <th>15</th>
      <td>73</td>
    </tr>
    <tr>
      <th>16</th>
      <td>60</td>
    </tr>
    <tr>
      <th>17</th>
      <td>69</td>
    </tr>
    <tr>
      <th>18</th>
      <td>26</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11</td>
    </tr>
    <tr>
      <th>21</th>
      <td>10</td>
    </tr>
    <tr>
      <th>22</th>
      <td>14</td>
    </tr>
    <tr>
      <th>23</th>
      <td>10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>17</td>
    </tr>
    <tr>
      <th>25</th>
      <td>8</td>
    </tr>
    <tr>
      <th>26</th>
      <td>6</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2</td>
    </tr>
    <tr>
      <th>28</th>
      <td>4</td>
    </tr>
    <tr>
      <th>29</th>
      <td>5</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2</td>
    </tr>
    <tr>
      <th>31</th>
      <td>3</td>
    </tr>
    <tr>
      <th>34</th>
      <td>3</td>
    </tr>
    <tr>
      <th>35</th>
      <td>6</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1</td>
    </tr>
    <tr>
      <th>44</th>
      <td>1</td>
    </tr>
    <tr>
      <th>47</th>
      <td>1</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2</td>
    </tr>
    <tr>
      <th>60</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### Analysis by Article


```python
data_df.groupby('file').excerpt_lengths.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
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
      <th>file</th>
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
      <th>data/Isla Vista - All Excerpts - 1_2_2019.xlsx</th>
      <td>8127.0</td>
      <td>4.106189</td>
      <td>3.876340</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>data/Marysville - All Excerpts - Final - 1_2_2019.xlsx</th>
      <td>2978.0</td>
      <td>3.345198</td>
      <td>2.666752</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>data/Newtown - All Excerpts - 1-2-2019.xlsx</th>
      <td>10767.0</td>
      <td>3.480821</td>
      <td>3.190377</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>44.0</td>
    </tr>
  </tbody>
</table>
</div>



## Analysis of Single Sentence Excerpts

From these results we can see that most of the excerpts have only one sentence. This is good news, and if needed, this dataset of one sentence labels could be used to train a classifier, or use it as the test set to test the classifier on single sentences.


```python
# extract and save a df of single sentences
single_sents = [num_sent ==1  for num_sent in excerpt_lengths]
single_sent_ids = list(compress(data_df.index, single_sents))
single_sents_df = data_df.iloc[single_sent_ids, :]
```


```python
# make sure there is a decent class distribution
print(single_sents_df['ACCOUNT'].value_counts())
# check if there is some representation from each file
print(single_sents_df['file'].value_counts())
```

    0    5284
    1     446
    Name: ACCOUNT, dtype: int64
    data/Newtown - All Excerpts - 1-2-2019.xlsx               3085
    data/Isla Vista - All Excerpts - 1_2_2019.xlsx            1864
    data/Marysville - All Excerpts - Final - 1_2_2019.xlsx     781
    Name: file, dtype: int64



```python
# save the sentences data frame to csv for further use
single_sents_df.to_csv("data/single_sents_df.csv")
```

## Analysis of Long Excerpts

There are several exceedingly long excerpts of over 25 sentences. This may be due to errors in the sentence tokenization, and so will be inspected manually. There are only about 20 total excerpts that are quite long, so it will not be too difficult to inspect them and decide if there are errors or if they should be kept in the dataset as is.


```python
# extract and save a df of single sentences
long_excerpts = [num_sent > 25  for num_sent in excerpt_lengths]
long_excerpt_ids = list(compress(data_df.index, long_excerpts))
long_excerpt_df = data_df.iloc[long_excerpt_ids, :]
```


```python
# check the labels )it would be a good idea to remove non-account documents that are too long)
print(long_excerpt_df['ACCOUNT'].value_counts())
# check if there is some representation from each file
print(long_excerpt_df['file'].value_counts())
```

    0    32
    1     5
    Name: ACCOUNT, dtype: int64
    data/Isla Vista - All Excerpts - 1_2_2019.xlsx    19
    data/Newtown - All Excerpts - 1-2-2019.xlsx       18
    Name: file, dtype: int64



```python
long_excerpt_df.groupby('ACCOUNT').describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">excerpt_lengths</th>
    </tr>
    <tr>
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
      <th>ACCOUNT</th>
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
      <th>0</th>
      <td>32.0</td>
      <td>32.09375</td>
      <td>6.060764</td>
      <td>26.0</td>
      <td>28.0</td>
      <td>30.5</td>
      <td>35.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.0</td>
      <td>38.80000</td>
      <td>14.549914</td>
      <td>27.0</td>
      <td>29.0</td>
      <td>30.0</td>
      <td>48.0</td>
      <td>60.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
for excerpt in long_excerpt_df.loc[long_excerpt_df['ACCOUNT'] == 1].Excerpts:
    print("********************************************")
    print(excerpt)
    print("********************************************")
```

    ********************************************
    Elliot Rodger here.

    This is my last video . It all has to come to this. Tomorrow is the day of
    retribution; the day in which I will have my revenge against humanity. Against
    all of you.

    For the last eight years of my life , ever since I hit puberty, I have been
    forced to endure an existence of loneliness, rejection and unfulfilled desires.
    All because girls have never been attracted to me. Girls gave their affection
    and sex and love to other men but never to me. I am 22, and I am still a virgin.
    I have never even kissed a girl. I have been through college for 21 / 2 years,
    more than that actually, and I am still a virgin. It has been very torturous. .
    . .

    College is the time when everyone experiences those things such as sex and fun
    and pleasure. In those years, I have had to rot in loneliness. It is not fair.
    You girls have never been attracted to me. I don't know why you girls aren't
    attracted me. But I will punish you all for it. It is an injustice, a crime. I
    don't know what you don't see in me. I am the perfect guy, and yet you throw
    yourselves at all these obnoxious men instead of me - the supreme gentleman. I
    will punish all of you for it.

    On the day of retribution , I am going to enter the hottest sorority house of
    UCSB, and I will slaughter every single spoiled, stuck-up blond slut I see
    inside there. . . .

    All those girls that I have desired so much, they all rejected me and looked
    down on me as an inferior man . . . while they throw themselves at these
    obnoxious brutes. I will take great pleasure in slaughtering all of you. You
    will finally see that I am, in truth, the superior one. The true alpha male.

    After I have annihilated every single girl in the sorority house , I will take
    to the streets of Isle Vista and slay every single person I see there. All those
    popular kids who live such lives of hedonistic pleasure while I have had to rot
    in loneliness all these years . . . now, I will be a god compared to you. You
    will all be animals. You are animals, and I will slaughter you like animals. I
    will be a god, exacting my retribution on all those who deserve it. And you do
    deserve it, just for the crime of living a better life than me. All you popular
    kids, you never accepted me, and now you will all pay for it."

    Girls, all I have ever wanted was to love you and to be loved by you. I wanted a
    girlfriend, I wanted sex, I wanted love, affection, adoration. You think I am
    unworthy of it. That is a crime that can never be forgiven. If I can't have you,
    girls, I will destroy you. You denied me a happy life, and in turn I will deny
    all of you life. It is only fair. I hate all of you. Humanity is a disgusting,
    wretched, depraved species. If I had it in my power, I would stop at nothing to
    reduce every single one of you to mountains of skulls, rivers of blood. You
    deserve to be annihilated. I will give that to you. You never showed me any
    mercy, so I will show you none. You forced me to suffer all my life, now I will
    make all of you suf...
    ********************************************
    ********************************************
    Hi. Elliot Rodger here. Well, this is my last video. It all has to come to this.
    Tomorrow is the day of retribution. The day in which I will have my revenge
    against humanity, against all of you.

    For the last eight years of my life, ever since I've hit puberty, I've been
    forced to endure an existence of loneliness, rejection and unfulfilled desires
    all because girls have never been attracted to me. Girls gave their affection
    and sex and love to other men, but never to me. I'm 22 years old and still a
    virgin. I've never even kissed a girl. I've been through college for 2½ years,
    more than that actually, and I'm still a virgin.

    It has been very torturous. College is the time when everyone experiences those
    things such as sex and fun and pleasure. In those years, I've had to rot in
    loneliness.

    It's not fair. You girls have never been attracted to me. I don't know why you
    girls aren't attracted to me, but I will punish you all for it.

    It's an injustice, a crime, because I don't know what you don't see in me. I'm
    the perfect guy, and yet you throw yourselves at all these obnoxious men instead
    of me - the supreme gentleman. I will punish all of you for it (creepy laugh).

    On the day of retribution, I am going to enter the hottest sorority house of
    UCSB and I will slaughter every single spoiled stuckup blond slut I see inside
    there.

    All those girls that I've desired so much. They would have all rejected me and
    looked down upon me as an inferior man if I ever made a sexual advance towards
    them, while they throw themselves at these obnoxious brutes. I'll take great
    pleasure in slaughtering all of you. You will finally see that I am in truth the
    superior one. The true alpha man (creepy laugh). Yes.

    After I've annihilated every single girl in the sorority house, I'll take to the
    streets of Isla Vista and slay every single person I see there - all those
    popular kids who live such lives of hedonistic pleasure while I've had to rot in
    loneliness for all these years.

    They've all looked down upon me every time I tried to go and join them. They've
    all treated me like a mouse. Well, now I will be a god compared to you. You will
    all be animals. You are animals, and I will slaughter you like animals. And I'll
    be a god exacting my retribution on all those who deserve it. And you do deserve
    it, just for the crime of living a better life than me. All you popular kids.
    You've never accepted me, and now you'll all pay for it.

    And girls. All I've ever wanted was to love you and to be loved by you. I've
    wanted a girlfriend, I've wanted sex, I've wanted love, affection, adoration.
    You think I'm unworthy of it. That's a crime that can never be forgiven. If I
    can't have you, girls, I will destroy you. (creepy laugh)

    You denied me a happy life, and in turn I will deny all of you life. (laughs)
    It's only fair. I hate all of you. Humanity is a disgusting, wretched, depraved
    species. If I had it in my power I would stop at nothing to reduce every single
    one of you to m...
    ********************************************
    ********************************************
    Some of Elliot Rodger's online posts leading up to Friday's shooting:
    One year ago: Rodger begins revealing his views on women, dating and his own life in comments on several YouTube videos. One video
    shows students partying in Isla Vista, Calif., during Deltopia, a notorious all-day party in Isla Vista. "It angers me so much to see these
    people having so much fun here. I've lived here for over a year now, and it's been such a miserable experience. I haven't been invited to a
    single party, and all the girls ignore me when I walk around at night."
    Dec. 2, 2013: Rodger posts a photo to Facebook and Google Plus, sitting with sunglasses inside a black BMW with a license plate that
    eventually would match the car involved in the shooting.
    Jan. 1, 2014: Rodger begins considering his plot, according to a 141-page manifesto, setting April 26 to carry out his plan.
    Feb. 10: Rodger uploads the first of at least 22 videos to YouTube, titled "Enjoying the sunset in Santa Barbara." Rodger doesn't speak
    during the nearly two-minute video filmed from a car.
    April 20: Rodger tweets a link to a video later taken down from his YouTube channel titled "Why do girls hate me so much?" A video with
    the same title is re-uploaded Friday, May 23, the day of the killings. "I don't know why you girls are so repulsed by me. It doesn't make
    sense," he said. "I do everything I can to appear attractive to you. I dress nice, I'm sophisticated. I'm magnificent. I have a nice car, a
    BMW. Well, it's nicer than 90 percent of the people in my college."
    April 24: Rodger wakes up with a cold and decides to postpone his plan to May 24.

April 30: Authorities do a well-being check on Rodger after his family calls police about his YouTube videos. Rodger says in his manifesto
    that he tactfully tells them the videos were a misunderstanding. "If they had demanded to search my room ... that would have ended
    everything. For a few horrible seconds, I thought it was all over."
    May 20: Rodger posts a 59-second video that shows his face as he drives around wearing sunglasses and a collared shirt, playing
    George Michael's 1988 hit "Father Figure." Rodger does not speak, but the description of the video says: "I'm awesome. Yeah, you better
    believe it. (Expletive) you haters."
    May 23: Rodger posts several more videos to YouTube, including his detailed plan titled "Elliot Rodger's Retribution." "All you popular
    kids, you've never accepted me; now you'll all pay for it," he said.
    ********************************************
    ********************************************
    Rodger saw every female as a "tall, hot blonde" -- and, this being California, that's at a campus that's only 50 percent white. He viewed all
    couples as his sworn enemies causing his suffering.

    Although Rodger loved driving his car, he "soon learned the hard way" not to drive on Friday and Saturday nights, where he "frequently
    saw bands of teenagers roaming the streets." They "had pretty girls beside them," probably on their way to "get drunk and have sex and
    do all sorts of fun pleasurable things that I've never had the chance to do. Damn them all!"

    At Santa Barbara City College, he dropped his sociology class on the first day of school "because there was this extremely hot blonde girl
    in the class with her brute of a boyfriend." Rodger couldn't even sit through the whole first class with them, merely for being a couple.

    Santa Monica Pier was out for him, too: "I saw young couples everywhere. ... Life was too unfair to me." On a trip to England, he refused
    to leave his hotel room so he wouldn't have to see men walking with their girlfriends.

    The "cruelty" of women apparently consisted of the failure of any "tall, hot blondes" to approach Rodger and ask for sex. He would walk
    around for hours "in the desperate hope that I might possibly cross paths with some pretty girl who would be attracted to me."

    But only once, in the entire 141-page manifesto, does Rodger attempt to speak to a girl himself. She's a total stranger walking past him on
    a bridge, and he musters up the courage to say "hi." He claims she "kept on walking" and said nothing. She probably didn't hear him. But
    he called her a "foul bitch" and went to a bathroom to cry for an hour.

    Although Rodger repeatedly denounces the world and everyone in it for "cruelty and injustice," he was the bully more often than the


    bullied, especially as time went on, and his rage increased.

    He hectors his mother to marry "any wealthy man" because it would "be a way out of my miserable and insignificant life." He tells her "she
    should sacrifice her well-being for the sake of my happiness."
    When flying first class, he says, "I took great satisfaction as I passed by all of the other people who flew economy, giving all of the

    younger passengers a cocky little smirk whenever they looked at me."
    Meanwhile, in 141 pages, the worst thing anyone ever did to him was not say "hi" back.
    But the story that sounds the most like Gogol's Poprishchin hearing two dogs talking in Russian is Rodger's claim that his stepmother


    bragged to him that his stepbrother, Jazz -- her own 6-year-old son! -- "would be a success with girls and probably lose his virginity early."
    I know Moroccan cultural mores are different, but I'm calling "auditory hallucination" on that one.
    A family friend, Simon Astaire, described Rodger's flat affect, common to schizophrenics, saying he "couldn't look at you straight in the


    eye and looked at your feet. It was unbearable."
    ********************************************
    ********************************************
    If only it was as simple as one madman. Only as infrequent as one grim Friday.


    But it's not. You wonder if we have created too fertile a breeding ground for violence. You wonder why the predominant emotion among
    so many of us so often is rage.
    And then you look around, and the way we communicate with one another.
    You look at our talk shows that once fostered thoughtful discussion and meaningful debate. Now they value one word only. Attack. Attack.


    Attack. The more vicious the better, because it sells.
    You look at our Internet, and its vast promise of an interchange of ideas. And then see how that promise has been perverted, to where


    assault is made all the easier by anonymity, and even the media no longer has use for beauty or perspective, because scandal and
    conflict and heated rhetoric get so many more computer hits.
    You look at our entertainment, and note the high body count, where we are numb to bloodshed and blind to its consequences. Where the


    winner is often the one who kills best.


    I look at my own pitifully trivial world of sport. Where proposals for safer football rules are hooted down, because the game might be less
    violent, and the crowds might stay away.
    I look at some of the mail I get. Abusive, brutal language from those furious about a Heisman vote or top 20 pick. If college football


    provokes such fury, one can only imagine what the real world must do.


    If rage and rancor are so much a part of our daily lives, it should not be a shock that gunfire breaks out. It has happened so often, that
    now when the first reports come, we ask the same questions, dulled as we are by mayhem.
    Where? How many? How young?
    What terrible questions for a society to have to keep asking itself.
    No, our violence-rich culture does not make murderers of us all. But cigarettes don't give everyone lung cancer. That does not make them


    non-lethal.
    ********************************************


It seems like these passages are way to long to be of use in training for sentence classification. Breaking passages this long up into sentences to use for training would add a lot of noise to the training data, and this would be better to avoid. Given the data set is quite large, with thousands of existing excerpts, removing only around 40 will not hurt the training, and given that these particular excerpts would be contributing quite a lot of noise, it would be best to remove them.

Given this result, the charts were inspected again, to consider removing even more excerpts that are too long. Since 75% of the data has excerpts of less than 5 sentences, if there is enough accountability labels present in this subset of the dataset, it might be best to restrict the new dataset for training sentence classifiers to only use the excerpts with less than 5 sentences.


```python
long_excerpts = [num_sent > 5  for num_sent in excerpt_lengths]
long_excerpt_ids = list(compress(data_df.index, long_excerpts))
long_excerpt_df = data_df.iloc[long_excerpt_ids, :]
```


```python
# check the labels )it would be a good idea to remove non-account documents that are too long)
print(long_excerpt_df['ACCOUNT'].value_counts())
# check if there is some representation from each file
print(long_excerpt_df['file'].value_counts())
```

    0    3468
    1     803
    Name: ACCOUNT, dtype: int64
    data/Newtown - All Excerpts - 1-2-2019.xlsx               1908
    data/Isla Vista - All Excerpts - 1_2_2019.xlsx            1891
    data/Marysville - All Excerpts - Final - 1_2_2019.xlsx     472
    Name: file, dtype: int64



```python
long_excerpt_df.groupby('ACCOUNT').describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="8" halign="left">excerpt_lengths</th>
    </tr>
    <tr>
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
      <th>ACCOUNT</th>
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
      <th>0</th>
      <td>3468.0</td>
      <td>9.051038</td>
      <td>4.07154</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>803.0</td>
      <td>9.125778</td>
      <td>4.31842</td>
      <td>6.0</td>
      <td>6.5</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>60.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
### save the sentences_df containing only excerpts with less than 5 sentences
short_excerpts_df = sentences_df.loc[sentences_df['excerpt_length']<5]
short_excerpts_df.shape
short_excerpts_df.groupby(['file', 'ACCOUNT', 'excerpt_length']).count()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>Sentences</th>
      <th>StoryID</th>
    </tr>
    <tr>
      <th>file</th>
      <th>ACCOUNT</th>
      <th>excerpt_length</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">data/Isla Vista - All Excerpts - 1_2_2019.xlsx</th>
      <th rowspan="4" valign="top">0</th>
      <th>1</th>
      <td>1638</td>
      <td>1638</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2740</td>
      <td>2740</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2655</td>
      <td>2655</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2524</td>
      <td>2524</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">1</th>
      <th>1</th>
      <td>226</td>
      <td>226</td>
    </tr>
    <tr>
      <th>2</th>
      <td>646</td>
      <td>646</td>
    </tr>
    <tr>
      <th>3</th>
      <td>969</td>
      <td>969</td>
    </tr>
    <tr>
      <th>4</th>
      <td>840</td>
      <td>840</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">data/Marysville - All Excerpts - Final - 1_2_2019.xlsx</th>
      <th rowspan="4" valign="top">0</th>
      <th>1</th>
      <td>743</td>
      <td>743</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1170</td>
      <td>1170</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1386</td>
      <td>1386</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1172</td>
      <td>1172</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">1</th>
      <th>1</th>
      <td>38</td>
      <td>38</td>
    </tr>
    <tr>
      <th>2</th>
      <td>102</td>
      <td>102</td>
    </tr>
    <tr>
      <th>3</th>
      <td>231</td>
      <td>231</td>
    </tr>
    <tr>
      <th>4</th>
      <td>176</td>
      <td>176</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">data/Newtown - All Excerpts - 1-2-2019.xlsx</th>
      <th rowspan="4" valign="top">0</th>
      <th>1</th>
      <td>2903</td>
      <td>2903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4260</td>
      <td>4260</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4473</td>
      <td>4473</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3976</td>
      <td>3976</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">1</th>
      <th>1</th>
      <td>182</td>
      <td>182</td>
    </tr>
    <tr>
      <th>2</th>
      <td>382</td>
      <td>382</td>
    </tr>
    <tr>
      <th>3</th>
      <td>438</td>
      <td>438</td>
    </tr>
    <tr>
      <th>4</th>
      <td>404</td>
      <td>404</td>
    </tr>
  </tbody>
</table>
</div>




```python
short_excerpts_df.to_csv("data/short_excerpts_df.csv")
```

These results show that many more non-accountability labels would be removed than accountability labels, so it seems this will not hurt the class imbalance too greatly if all these excerpts with length longer than 5 sentences are removed for training the sentence classifier.

This new dataframe containing only sentences from excerpts of length less than 5 will be created and saved to csv for future use.

### Compare Class and File Balance in Short Sentences Only


```python
short_excerpts_df.groupby(['file', 'ACCOUNT']).count()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Sentences</th>
      <th>StoryID</th>
      <th>excerpt_length</th>
    </tr>
    <tr>
      <th>file</th>
      <th>ACCOUNT</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">data/Isla Vista - All Excerpts - 1_2_2019.xlsx</th>
      <th>0</th>
      <td>9557</td>
      <td>9557</td>
      <td>9557</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2681</td>
      <td>2681</td>
      <td>2681</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">data/Marysville - All Excerpts - Final - 1_2_2019.xlsx</th>
      <th>0</th>
      <td>4471</td>
      <td>4471</td>
      <td>4471</td>
    </tr>
    <tr>
      <th>1</th>
      <td>547</td>
      <td>547</td>
      <td>547</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">data/Newtown - All Excerpts - 1-2-2019.xlsx</th>
      <th>0</th>
      <td>15612</td>
      <td>15612</td>
      <td>15612</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1406</td>
      <td>1406</td>
      <td>1406</td>
    </tr>
  </tbody>
</table>
</div>




```python
sentences_df.groupby(['file', 'ACCOUNT']).count()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Sentences</th>
      <th>StoryID</th>
      <th>excerpt_length</th>
    </tr>
    <tr>
      <th>file</th>
      <th>ACCOUNT</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">data/Isla Vista - All Excerpts - 1_2_2019.xlsx</th>
      <th>0</th>
      <td>24695</td>
      <td>24695</td>
      <td>24695</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8676</td>
      <td>8676</td>
      <td>8676</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">data/Marysville - All Excerpts - Final - 1_2_2019.xlsx</th>
      <th>0</th>
      <td>8389</td>
      <td>8389</td>
      <td>8389</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1573</td>
      <td>1573</td>
      <td>1573</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">data/Newtown - All Excerpts - 1-2-2019.xlsx</th>
      <th>0</th>
      <td>34400</td>
      <td>34400</td>
      <td>34400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3078</td>
      <td>3078</td>
      <td>3078</td>
    </tr>
  </tbody>
</table>
</div>



## Using this Data for Sentence Classifier

One issue to consider, is that in using this transformation, additional noise is possible being introduced into the labels. For example, in an excerpt of four labels, it is possible that only one out of the four sentences actually makes a statement about accountability, that means there are three new sentences added to the training set that are incorrectly labelled. Incorrectly labelled training data is a problem known as "label noise". The specific type of label noise being introduced in this case is asymetric binary, random label noise, known as NAR label noise (noisy at random). The assumption made is that the noise introduced is independant of the features of the data, but not independant of the true class label.

Only false postiive labels are being introduced, since all the sentences in an excerpt labelled as accountability are now being given the label accountability. It is a lot less likely there are many sentences in the excerpts that were labelled as not accountability, that should actually be labelled as accountability, resulting in the asymentric introduction of label noise being introduced. These considerations are important, since with correct assumptions about label noise introduced, label noise filters can be used.

Label noise in the test set could also be an issue, but luckily we have a dataset of single sentences of sufficient size, that this could be used to make up the test data.

To assess the overall possible amount of noise being introduced by this approach, lets assume each excerpt actually only contained one sentence about accountability. In this case, we can calculate how many sentences we now have in the short excerpts and full excerpts dataframes that are inccorectly labelled.


```python
sentences_account_df = sentences_df.loc[sentences_df['ACCOUNT']==1]
num_incorrect_full = 0
num_incorrect_short = 0
tot_full = 0
tot_short = 0

for index, row in sentences_account_df.iterrows():
    num_sents = row['excerpt_length']
    num_incorrect_full = num_incorrect_full + (num_sents -1) # assuming only one sentence is correct per excerpt
    tot_full = tot_full +num_sents
    if num_sents <5:
        num_incorrect_short = num_incorrect_short + (num_sents -1)
        tot_short = tot_short + num_sents
```


```python
print("Percent incorrect sentences out of short excerpts sentences dataset: "+str(100*num_incorrect_short/tot_short))
print("Percent incorrect sentences out of full excerpts sentences dataset: "+str(100*num_incorrect_full/tot_full))
```

    Percent incorrect sentences out of short excerpts sentences dataset: 65.15789473684211
    Percent incorrect sentences out of full excerpts sentences dataset: 86.92854690794958


## Approaches to Use Excerpts to Train Sentence Classifier

There are two factors to consider in converting the existing labelled excerpts into labelled sentences.

* How to train the classifier
* How to test the classifier

### How to Test

The ultimate objective in the end would be to use the classifier on an article sentence by sentence and identify which sentences are talking about accountability. To evaluate the performance of operating in this manner, the testing data used would have have to be passed in as single sentences. Therefore, it would be important to use a test set of only single sentences. The two approaches for this are:

* only evaluate with the excerpts that already exist as single sentences
* use the excerpts converted to labelled sentences

There are some issues with both of these approaches.

#### Evaluate on only single sentence excerpts

The main issue with this, is that the distribution of features may different in the single sentence excerpts than the rest of the data set. For example, the fact that these single sentences were able to fully capture a statement about accountability, indicate that perhaps they have some unigue sentence structure and terms that would not be present throughout the rest of the training data of excerpts that were more than one sentence. There are many issues that can arise from having a test set with a different distribution of features from the training set.

If the data is trained as well only on single sentences, then this would likely lead to the best possible performance in this situation, since it is learning the features relevant to single sentences and evaluating based on sentences with those features as well. The main issue with this approach is that this greatly restricts the size of the dataset, and likely misses out on many examples of discussing accountability that is not present in these few excerpts. However the size of this data of single sentences alone, would actually be sufficient to train a simple classifier.

#### Evaluate on sentences from multi-sentence excerpts

Another approach that would increase the size of the usable data, and also likely make the classifier able to generalize to more ways of discussing accountability, would be to evaluate based on the excerpts that were transformed into single labelled sentences.

The main issue with this approach, is that it is possible this would be introducing too much label noise into the evaluation. The amount of label noise, could be as much as 65% of the labels from the short excerpts dataset, in which case the evaluation of results would have a high variance. The fact that the label noise introduced by this method is assymetric will also pose additional issues with the evaluation.  


### How to Train

The next issue to consider is how to train. This method is more straightforward to deal with, since it can be determined by experimentation, and the evaluation of the results with each approach can be used to determine which training method was most appropriate.

#### Using Only Single Sentence Excerpts

The issue with this method as mentioned before, is that the excerpts with onyl single sentences may contain unique features, and have a very different distribution of features from the rest of the dataset. Also the size of data available for training is reduced, however certain model will still be ok with this size of data.

#### Converting Excerpts into Labelled Sentences

The next approach, to convert more of the dataset into labelled sentences will increase the size of the data, but result in training in the presenve of label noise. Asymetric label noise can be tricky to deal with in training, however there are existing approaches such as noise filters and noise robust models that can be used to accommodate this.

#### Using Original Length Excerpts

Using the original full excerpts for training would reduce the amount of label noise, but once again it would have the issue of making the features and representation of the training set differ from the test set, which will likely hurt the performance. Instead of dealing with the noise in the labels, the noise will exist in the feature space, and dilute the representations to become less meaningful. A classifier trained on this may have issues applied to documents that have a significant difference in length and representation of features.

## Proposed Approach

Based on this analysis the proposed approach to assess the options is as follows:

1) Evaluation with single sentence excerpts: use clear cut evaluation with minimal noise to evaluate training approaches
* train with singles sentences
* train with full excerpts
* train with excerpts converted to labelled sentences

2) Evaluation with excerpts converted to labelled single sentences: compare the same training methods as previous, this comparison will indicate the effectiveness of evaluating with the larger dataset.

3) Evaluate on full excerpts: this is the method that was used previously, and can be used to compare to the new sentence based approach to determine if there is a drop in performance.

The simplest, quickest and most trustworthy method is to use only the dataset of single sentences for both training and evaluation. This method should be used for testing and experimentation with models, and then the proposed approach for extending the included dataset will be tested on only the higher performing classification methods based on the results from single sentences.
