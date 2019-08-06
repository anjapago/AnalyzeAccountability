---
layout: post
title:  "Feature Importances of Tfidf Representations Classifiers"
date:   2019-08-03 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---
This analysis will compare different text representations with simple sklearn linear and ensemble classifiers. The basis of all the text representations tested in this analysis is the sklearn vectorizer. The performance of these representations were tested in the [previous post](https://anjapago.github.io/AnalyzeAccountability/update/2019/08/01/vectorizer-comparison.html), and so the best performing methods from that analysis will be analyzed to determine which features (i.e. tokens or words) contribute to the decision to classify something as accountability. This will give further understanding into which method of text representation is most suitable for this task.


## Recap of Performance Results
The most notable effect on performance from the various representations was that character based consistently performed higher than other methods.

In the comparison of classifiers, it is clear overall the linear methods perform best, and the balanced linear classifiers was slightly better in most cases.

## Analysis of Features on performance

### Balanced vs Unbalanced

#### Balanced

|Weight? | Feature|
---------|---------
|+11.159	| hornaday|
|+10.813 | counsellor|
|+10.489	| bullied|
|+10.130	| rage|
|+9.911	| ugly|
|+9.760	| counselor|
|+9.615	| sprees|
|+8.979	| science|
… 2268 more positive …
… 3276 more negative …
|-8.918 |	massacred|
|-9.079	| camera|
|-9.144	| marquez|
|-9.147	| stringent|
|-9.266	| animals|
|-9.279	| proposed|
|-9.763	| bills|
|-9.897	| apple|
|-10.262 |	undergo|
|-10.303	| peace|
|-11.353	| proposals|
|-13.895	| caption|

#### Unbalanced

| Weight |	Feature |
|--------|----------|
| +5.122 | blame |
| +4.720 |	culture|
|+4.605	| blamed|
|+4.453	| shall|
|+4.126	| misogyny|
|+4.097	| counselor|
|+4.040	| rage|
|+3.882	| senselessness|
|+3.868	| isolated|
|+3.841	| hornaday|
|+3.795	| void|
|+3.795	| bullied|
|+3.788	| videos|
|+3.727	| none|
|+3.686	| illness|
|+3.664	| failure|
|+3.622	| counsellor|
… 2269 more positive …
… 3275 more negative …
|-3.843	| bmw|
|-3.935	| students|
|-4.184	| caption|

### Character Based vs Word Based tokens

|Weight	| Feature|
|-------|--------|
|+19.469	| e? |
|+19.191	| s? |
|+17.221	| n? |
|+16.696	| a? |
|+14.978	| fame|
|+13.483	| tered.|
|+13.476	| ak|
|+12.957	| ndw|
|+11.972	| be.|
|+11.777	|war,|
|+11.760	|var|
|+11.499	|u.|
|+11.329	| wild|
|+11.228	| se. |
|+11.153	|fame|
|+10.631	|od. |
… 45933 more positive …
… 59739 more negative …
|-11.270	| spa|
|-11.304	| 6 |
|-12.947	| work |
|-13.294	| ?" |

### Trigrams vs Unigrams

|Weight? | Feature|
|--------|--------|
|+10.839	| blame|
+8.991	in other
+8.746	know this
+8.640	knew he
+8.603	jaylen
+8.571	blamed
+8.456	motives
+8.343	culture
+8.291	believe the
+8.232	fame
+8.226	hornaday
+8.069	he doesn
+8.020	teens
+7.797	women
… 9930 more positive …
… 17166 more negative …
-7.655	marquez
-7.663	apple
-7.784	who was
-7.974	jaylen fryberg
-8.451	yes
-10.954	caption
