---
layout: post
title:  "Analysis of Accountability Labels"
date:   2019-06-12 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---

This post will give an analysis of the labels accountability labels on the
excerpts from three news shootings datasets: Isla Vista, Marysville and Newton.

## Number of Excerpts

First, we can compare the total number of excerpts from each given dataset.
A large imbalance between these datasets can result in features more specific
to the larger datasets being given a higher importance when trained in a
classifier, for example a person's name specific to one of the shooting events.

![total_number_excerpts](/AnalyzeAccountability/assets/total_number_excerpts.png)

From the chart, we can see that the largest overall dataset is from the Newton
news articles. The Marysville is relatively much smaller, and so it is likely
to have the worst relative performance after training a classifier on this full
dataset.

## Proportions of Accountability labels

Next, we can compare each dataset of news excerpts based on the proportions of
the accountability labels. From the bar chart we can see that the largest
dataset, Newton has the lowest proportion of excerpts with the accountability
label. All three have accountability labels on much lower than half the
excerpts, and so this will result in a class imbalance situation for the
classifier.

![label_proportions](/AnalyzeAccountability/assets/label_proportions.png)

Some more observations can be made in comparing the sub-types of the
accountability label: 'other', 'individual', and 'cultural'. The biggest
issue with this, is that the label 'other' is very rare to occur, except in
the Marysville dataset. However, the Marysville dataset is quite small,
so overall the number of excerpts with the label of 'other' will be very low.
Aside from this, we can see that the proportions for 'individual' and 'cultural'
labels are very similar, so focussing on these two sub-classes as a second
classification task within the existing class of accountability could be
a promising approach to correctly identify the accountability sub-type label.

## Analysis of Multiclass Accountability Labels

It may be possible that an excerpt could be labelled as more than one sub-type
of accountability. This would result in a more complex classification task than
typical multiclass classification, called multi-label classification.

To clarify, the two possible types of classification for data with multiple
class labels are:

* [multiclass classification](https://en.wikipedia.org/wiki/Multiclass_classification): problem of categorizing instances into precisely
one of more than two classes
* [multi-label classification](https://en.wikipedia.org/wiki/Multi-label_classification): multiple labels are to be predicted for
each instance

To determine which approach should be used for this case, the overlap of the
sub-type of accountability labels was analyzed.

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
      <th>ACCOUNT_Cultural</th>
      <th>ACCOUNT_Individual</th>
      <th>ACCOUNT_Other</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ACCOUNT_Cultural</th>
      <td>1782</td>
      <td>204</td>
      <td>0</td>
    </tr>
    <tr>
      <th>ACCOUNT_Individual</th>
      <td>204</td>
      <td>1124</td>
      <td>7</td>
    </tr>
    <tr>
      <th>ACCOUNT_Other</th>
      <td>0</td>
      <td>7</td>
      <td>292</td>
    </tr>
  </tbody>
</table>
</div>

From this table we can see that the labels individual and cultural do have some
overlap, where some excerpts (204) will have the label of both individual and
cultural. Also note that there are only 7 excerpts that have an overlap with
the label other. It is possible that these may be due to some mis-classification
by the annotators, and are worth some inspection. The text of these 7 excerpts
is:

    Isla Vista_7635:
    In that manifesto, he described his life story, frustration over not being
    able to find a girlfriend and his hatred of women, racial minorities
    and interracial couples.

    Marysville_727:
    There seemed to be no clues that might have prevented the school shooting
    in Marysville, Washington. Members of the close­knit Tulalip Tribes  said to
    be one of the most successful Native American tribes in the US  are reeling.
    Retrospect always seems to provide tragic clues that might have prevented a
    school shooting. Bullying. Trouble at home. An unusual fascination with guns
     or violent video games. More than ones share of typical teen angst.

    None of that appears to have been the case in Marysville, Wash., Friday
    morning when 14 year-old high school freshman Jaylen Fryberg walked into the
     cafeteria at Marysville-Pilchuck High School and without a word shot five
     fellow students  killing one and then himself.

    Newtown_2359:
     Although suicide terrorists may share the same beliefs as the organizations
    whose propaganda they spout, they are primarily motivated by the desire to
    kill and be killed -- just like most rampage shooters.

    Newtown_2362:
    The key is that the aggrieved individual feels that he has been terribly
    mistreated and that violent vengeance is justified. In many cases, the target
    for revenge becomes broader and more symbolic than a single person, so that
    an entire type or category of people is deemed responsible for the
    attacker's pain and suffering.

    Newtown_3123:
    The gunman who massacred 26 people at Sandy Hook Elementary School in
    Newtown, Conn., was obsessed with mass murders and so mentally twisted that
    his mother planned to move him out of state so he could attend a special
    school, yet she had him living in a home with firearms and ammunition and
    gave him money to buy a gun for Christmas.

    Newtown_3129:
    Nancy Lanza, who was divorced from Adam's father, "took care of all the
    shooter's needs," according to the report, and indicated that she didn't
    work because of his condition. Nonetheless, she allowed Adam easy access to
    firearms, and one of the items found in their home was a check, written by
    Nancy Lanza to Adam and dated "Christmas Day," with a notation that it was
    for him to buy himself a CZ 83 pistol.

    Newtown_3799:
    Her son took the two handguns and the semiautomatic to the school. Lanza's
    developmental disorder had seen him drop out of high school. Some of his
    former classmates said they had been told he had Asperger's syndrome, a
    high-functioning form of autism. But what someone with his obvious mental
    issues was doing with access to a house full of high powered weapons is a
    question that his mother is no longer around to answer.

The question for the annotators about these 7 excerpts would be, do they truly
require both the annotation of 'individual' and 'other'? Or would it be possible
to consider these with a single label.

Another observation is that since 'individual' and 'cultural' labels overlap
in 204 excerpts, it might be possible to just create a new label called
'individual+cultural', resulting in four subtypes of accountability: 'individual',
'cultural', 'individual+cultural', and 'other'. This would be an option to
enable the use of multiclass classification approaches, instead of being
restricted to multi-label classification.

## Documents with no sub-type

Another observation was made during this analysis, that some excerpts have the
label of 'ACCOUNT' but was not assigned a sub-type of accountability label.
The question for the annotators about this is, was this intentional? Or should
these excerpts have actually been labelled with the 'other' subtype label.
The excerpts with no sub-type label are shown below:


    Marysville_1149:
    A detective investigating the Marysville high-school shootings that left
    five teens dead says in court papers that the young gunmans texts turned
    dark the week before he opened fire, with references to his funeral and the
     message: Bang bang Im dead. Moments before Jaylen Fryberg, 15, shot his
     fellow students Oct. 24 in the Marysville-Pilchuck High School cafeteria,
     he texted more than a dozen relatives, describing what he wanted to wear
     at his funeral and who should get his personal possessions, the detectives
     search ­warrant affidavit says. The boy asked relatives to apologize to the
     families of his friends who get caught up in the (expletive) tomorrow 
     referring to the day after the shooting. He also sent texts in the previous
      days to a female friend talking about his death and funeral.

    Marysville_1895:
    The shooter was a student at the school 30 miles north of Seattle, but
    Marysville Police Commander Robb Lamoureux said he could not provide more
    information on the gunman or his motive. Lamoureux said the gunman died of
    a self-inflicted wound.

    Marysville_1896:
    The shooter was a student at the school 30 miles north of Seattle, but
    Marysville Police Commander Robb Lamoureux said he could not provide more
    information on the gunman or his motive. Lamoureux said the gunman died of a
     self-inflicted wound.

    Newtown_6188:
    People who hadn't spoken to Adam Lanza in years are being asked to speculate
     about what led the young man to shoot his mother to death, mow down two
     classrooms of first-graders and kill a half-dozen school employees.

    Newtown_8597:
    Some of the recent mass shootings might have been prevented if their
    perpetrators had been diagnosed and treated for their apparent disorders

    Newtown_10504:
    The Sandy Hook case differs from the previous challenge to gunmaker's immunity,
    however, because it does not hinge upon the AR-15 rifle's sale to a particular
    buyer - in this case, the shooter's mother, whom he fatally shot before driving
    to the elementary school.

## Summary of Observations

Throughout the analysis there are several issues to note with the given labels.
They can be summarized as follows:

* class imbalance: as shown in the labels proportion graphs, the accountability
label is quite less than half in the full datasets for each new type. Also, the
'other' label class is relatively quite low compared to the other accountability
sub-type labels.
* size of datasets: the Marysville dataset is quite small, so features specific
to that dataset may not be picked up by a classifier trained on the full dataset
* missing sub-type labels: several documents of accountability have no sub-type
* sub-type label overlap: there is very low overlap with the 'other' label and
the other two accountability subtype labels
