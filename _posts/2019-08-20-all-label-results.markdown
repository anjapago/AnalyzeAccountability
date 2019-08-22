---
layout: post
title:  "All Labels and Events"
date:   2019-08-20 00:39:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---

## Results from Each Event Individually

The following two links lead to interactive visualizations of the results for each event individually. The suggested use of the table is to drag "event" to the left column and "label" to the upper bar. Then select a viewing option, such as bar chart, and select to view "list unique values", and then select "fscore". The image below shows how to configure the options on the table to display the results.

![png](/AnalyzeAccountability/assets/barchartfscores.png)

Another view that is interesting is the heatmap, that shades cells of the table darker for better fscores, this can be configured as shown in the image below.

![png](/AnalyzeAccountability/assets/colheatmap.png)

Finally, there is also the option to filter by any event or label as desired, and this can be done as shown in the following two images.

![png](/AnalyzeAccountability/assets/selectevent.png)

![png](/AnalyzeAccountability/assets/selectlabels.png)

To use the interactive visualizations for the events, click the following two links.

<a class="post-link" href="/AnalyzeAccountability/results/2019/08/20/all-label-results-excerpts.html">
	Excerpt Based Results
</a>

<a class="post-link" href="/AnalyzeAccountability/results/2019/08/20/all-label-results-sentences.html">
	Sentence Based Results
</a>

## Results from Full Data

The results from all events together are shown in the following two sections, with the sentence based results, and the excerpt based results.

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
      <th>label</th>
      <th>recall</th>
      <th>precision</th>
      <th>fscore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ACCOUNT</td>
      <td>0.701298</td>
      <td>0.600271</td>
      <td>0.646427</td>
    </tr>
    <tr>
      <th>1</th>
      <td>EVENT</td>
      <td>0.855760</td>
      <td>0.760016</td>
      <td>0.804812</td>
    </tr>
    <tr>
      <th>2</th>
      <td>GRIEF</td>
      <td>0.691717</td>
      <td>0.730314</td>
      <td>0.710274</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HERO</td>
      <td>0.601905</td>
      <td>0.657407</td>
      <td>0.623459</td>
    </tr>
    <tr>
      <th>4</th>
      <td>INVESTIGATION</td>
      <td>0.700388</td>
      <td>0.600388</td>
      <td>0.646376</td>
    </tr>
    <tr>
      <th>5</th>
      <td>JOURNEY</td>
      <td>0.499084</td>
      <td>0.512640</td>
      <td>0.505202</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LEGAL</td>
      <td>0.684539</td>
      <td>0.545679</td>
      <td>0.607149</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MEDIA</td>
      <td>0.469642</td>
      <td>0.646586</td>
      <td>0.543683</td>
    </tr>
    <tr>
      <th>8</th>
      <td>MISCELLANEOUS</td>
      <td>0.097963</td>
      <td>0.358333</td>
      <td>0.153100</td>
    </tr>
    <tr>
      <th>9</th>
      <td>MOURNING</td>
      <td>0.745644</td>
      <td>0.729050</td>
      <td>0.737217</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PERPETRATOR</td>
      <td>0.666198</td>
      <td>0.607743</td>
      <td>0.635561</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PHOTO</td>
      <td>0.791482</td>
      <td>0.962235</td>
      <td>0.867822</td>
    </tr>
    <tr>
      <th>12</th>
      <td>POLICY</td>
      <td>0.809883</td>
      <td>0.719699</td>
      <td>0.761980</td>
    </tr>
    <tr>
      <th>13</th>
      <td>RACECULTURE</td>
      <td>0.577077</td>
      <td>0.485271</td>
      <td>0.526538</td>
    </tr>
    <tr>
      <th>14</th>
      <td>RESOURCES</td>
      <td>0.710595</td>
      <td>0.720465</td>
      <td>0.714699</td>
    </tr>
    <tr>
      <th>15</th>
      <td>SAFETY</td>
      <td>0.711840</td>
      <td>0.688813</td>
      <td>0.699861</td>
    </tr>
    <tr>
      <th>16</th>
      <td>SOCIALSUPPORT</td>
      <td>0.487058</td>
      <td>0.596018</td>
      <td>0.534268</td>
    </tr>
    <tr>
      <th>17</th>
      <td>THREAT</td>
      <td>0.366263</td>
      <td>0.478500</td>
      <td>0.412299</td>
    </tr>
    <tr>
      <th>18</th>
      <td>TRAUMA</td>
      <td>0.628757</td>
      <td>0.578450</td>
      <td>0.601620</td>
    </tr>
  </tbody>
</table>
</div>

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
      <th>label</th>
      <th>recall</th>
      <th>precision</th>
      <th>fscore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ACCOUNT</td>
      <td>0.689390</td>
      <td>0.520519</td>
      <td>0.593052</td>
    </tr>
    <tr>
      <th>1</th>
      <td>EVENT</td>
      <td>0.788855</td>
      <td>0.669544</td>
      <td>0.724264</td>
    </tr>
    <tr>
      <th>2</th>
      <td>GRIEF</td>
      <td>0.662380</td>
      <td>0.594215</td>
      <td>0.626353</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HERO</td>
      <td>0.390779</td>
      <td>0.458261</td>
      <td>0.421671</td>
    </tr>
    <tr>
      <th>4</th>
      <td>INVESTIGATION</td>
      <td>0.645075</td>
      <td>0.549435</td>
      <td>0.592606</td>
    </tr>
    <tr>
      <th>5</th>
      <td>JOURNEY</td>
      <td>0.527772</td>
      <td>0.552931</td>
      <td>0.538554</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LEGAL</td>
      <td>0.617024</td>
      <td>0.517006</td>
      <td>0.562588</td>
    </tr>
    <tr>
      <th>7</th>
      <td>MEDIA</td>
      <td>0.409108</td>
      <td>0.608507</td>
      <td>0.488292</td>
    </tr>
    <tr>
      <th>8</th>
      <td>MISCELLANEOUS</td>
      <td>0.111955</td>
      <td>0.316412</td>
      <td>0.163613</td>
    </tr>
    <tr>
      <th>9</th>
      <td>MOURNING</td>
      <td>0.694081</td>
      <td>0.618216</td>
      <td>0.653690</td>
    </tr>
    <tr>
      <th>10</th>
      <td>PERPETRATOR</td>
      <td>0.625522</td>
      <td>0.521118</td>
      <td>0.568497</td>
    </tr>
    <tr>
      <th>11</th>
      <td>PHOTO</td>
      <td>0.734191</td>
      <td>0.903715</td>
      <td>0.810145</td>
    </tr>
    <tr>
      <th>12</th>
      <td>POLICY</td>
      <td>0.768284</td>
      <td>0.624043</td>
      <td>0.688665</td>
    </tr>
    <tr>
      <th>13</th>
      <td>RACECULTURE</td>
      <td>0.555978</td>
      <td>0.411426</td>
      <td>0.472681</td>
    </tr>
    <tr>
      <th>14</th>
      <td>RESOURCES</td>
      <td>0.561214</td>
      <td>0.664053</td>
      <td>0.607568</td>
    </tr>
    <tr>
      <th>15</th>
      <td>SAFETY</td>
      <td>0.658571</td>
      <td>0.598168</td>
      <td>0.626388</td>
    </tr>
    <tr>
      <th>16</th>
      <td>SOCIALSUPPORT</td>
      <td>0.462509</td>
      <td>0.498682</td>
      <td>0.479476</td>
    </tr>
    <tr>
      <th>17</th>
      <td>THREAT</td>
      <td>0.378187</td>
      <td>0.509968</td>
      <td>0.433208</td>
    </tr>
    <tr>
      <th>18</th>
      <td>TRAUMA</td>
      <td>0.629151</td>
      <td>0.494055</td>
      <td>0.552743</td>
    </tr>
  </tbody>
</table>
</div>
