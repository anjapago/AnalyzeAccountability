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

<div class="output_html rendered_html output_subarea output_execute_result">
<style  type="text/css" >
    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col0 {
            background-color:  #afcfae;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col1 {
            background-color:  #b8d5b7;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col2 {
            background-color:  #f4ced9;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col3 {
            background-color:  #f0baca;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col4 {
            background-color:  #88b786;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col5 {
            background-color:  #72a870;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col0 {
            background-color:  #5c9b5a;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col1 {
            background-color:  #6ea66c;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col2 {
            background-color:  #b8d5b7;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col3 {
            background-color:  #d1e5d0;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col4 {
            background-color:  #3c863a;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col5 {
            background-color:  #3c863a;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col0 {
            background-color:  #8eba8c;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col1 {
            background-color:  #a5c9a4;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col2 {
            background-color:  #cbe1ca;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col3 {
            background-color:  #fae9ee;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col4 {
            background-color:  #8cb98b;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col5 {
            background-color:  #80b27f;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col0 {
            background-color:  #bbd7ba;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col1 {
            background-color:  #f4ced9;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col2 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col3 {
            background-color:  #e794ad;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col4 {
            background-color:  #b8d5b7;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col5 {
            background-color:  #f5d3dd;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col0 {
            background-color:  #afcfae;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col1 {
            background-color:  #b9d6b8;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col2 {
            background-color:  #f4ced9;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col3 {
            background-color:  #f4ccd8;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col4 {
            background-color:  #88b786;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col5 {
            background-color:  #8bb889;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col0 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col1 {
            background-color:  #d8ead7;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col2 {
            background-color:  #e89ab1;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col3 {
            background-color:  #f4d0db;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col4 {
            background-color:  #ebf6ea;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col5 {
            background-color:  #cbe1ca;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col0 {
            background-color:  #c4ddc3;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col1 {
            background-color:  #cbe1ca;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col2 {
            background-color:  #edadc0;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col3 {
            background-color:  #efb9c9;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col4 {
            background-color:  #8fbb8d;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col5 {
            background-color:  #99c298;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col0 {
            background-color:  #e5f2e5;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col1 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col2 {
            background-color:  #faeaef;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col3 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col4 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col5 {
            background-color:  #f7dde4;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col0 {
            background-color:  #d43e6a;
            color:  #f1f1f1;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col1 {
            background-color:  #d43e6a;
            color:  #f1f1f1;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col2 {
            background-color:  #d43e6a;
            color:  #f1f1f1;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col3 {
            background-color:  #d43e6a;
            color:  #f1f1f1;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col4 {
            background-color:  #d43e6a;
            color:  #f1f1f1;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col5 {
            background-color:  #d43e6a;
            color:  #f1f1f1;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col0 {
            background-color:  #7fb17d;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col1 {
            background-color:  #95bf93;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col2 {
            background-color:  #cbe1ca;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col3 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col4 {
            background-color:  #72a870;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col5 {
            background-color:  #6fa76d;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col0 {
            background-color:  #b5d3b4;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col1 {
            background-color:  #c7dfc6;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col2 {
            background-color:  #f5d3dd;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col3 {
            background-color:  #f0bccb;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col4 {
            background-color:  #99c298;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col5 {
            background-color:  #95bf93;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col0 {
            background-color:  #3c863a;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col1 {
            background-color:  #3c863a;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col2 {
            background-color:  #3c863a;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col3 {
            background-color:  #3c863a;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col4 {
            background-color:  #5b9a59;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col5 {
            background-color:  #599956;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col0 {
            background-color:  #72a870;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col1 {
            background-color:  #82b380;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col2 {
            background-color:  #d1e5d0;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col3 {
            background-color:  #ecf6ec;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col4 {
            background-color:  #52944f;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col5 {
            background-color:  #468d43;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col0 {
            background-color:  #eef7ed;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col1 {
            background-color:  #faeaef;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col2 {
            background-color:  #e589a4;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col3 {
            background-color:  #e17897;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col4 {
            background-color:  #c5dec4;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col5 {
            background-color:  #bcd8bb;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col0 {
            background-color:  #8bb889;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col1 {
            background-color:  #b0d0af;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col2 {
            background-color:  #d1e5d0;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col3 {
            background-color:  #d4e7d3;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col4 {
            background-color:  #83b481;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col5 {
            background-color:  #b9d6b8;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col0 {
            background-color:  #93be92;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col1 {
            background-color:  #a5c9a4;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col2 {
            background-color:  #e4f1e3;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col3 {
            background-color:  #faeaef;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col4 {
            background-color:  #82b380;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col5 {
            background-color:  #83b481;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col0 {
            background-color:  #e9f5e9;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col1 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col2 {
            background-color:  #f3cbd7;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col3 {
            background-color:  #edadc0;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col4 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col5 {
            background-color:  #f2f2f2;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col0 {
            background-color:  #f1c0ce;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col1 {
            background-color:  #f5d4de;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col2 {
            background-color:  #e384a0;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col3 {
            background-color:  #eeb5c6;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col4 {
            background-color:  #f0bdcc;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col5 {
            background-color:  #f3cbd7;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col0 {
            background-color:  #c7dfc6;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col1 {
            background-color:  #cfe4ce;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col2 {
            background-color:  #f1c2d0;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col3 {
            background-color:  #ecabbe;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col4 {
            background-color:  #abcdaa;
            color:  #000000;
        }    #T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col5 {
            background-color:  #93be92;
            color:  #000000;
        }</style><table id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >fscore_excerpts</th>        <th class="col_heading level0 col1" >fscore_sentences</th>        <th class="col_heading level0 col2" >precision_excerpts</th>        <th class="col_heading level0 col3" >precision_sentences</th>        <th class="col_heading level0 col4" >recall_excerpts</th>        <th class="col_heading level0 col5" >recall_sentences</th>    </tr>    <tr>        <th class="index_name level0" >label</th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row0" class="row_heading level0 row0" >ACCOUNT</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col0" class="data row0 col0" >0.646427</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col1" class="data row0 col1" >0.593052</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col2" class="data row0 col2" >0.600271</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col3" class="data row0 col3" >0.520519</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col4" class="data row0 col4" >0.701298</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row0_col5" class="data row0 col5" >0.68939</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row1" class="row_heading level0 row1" >EVENT</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col0" class="data row1 col0" >0.804812</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col1" class="data row1 col1" >0.724264</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col2" class="data row1 col2" >0.760016</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col3" class="data row1 col3" >0.669544</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col4" class="data row1 col4" >0.85576</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row1_col5" class="data row1 col5" >0.788855</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row2" class="row_heading level0 row2" >GRIEF</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col0" class="data row2 col0" >0.710274</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col1" class="data row2 col1" >0.626353</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col2" class="data row2 col2" >0.730314</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col3" class="data row2 col3" >0.594215</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col4" class="data row2 col4" >0.691717</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row2_col5" class="data row2 col5" >0.66238</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row3" class="row_heading level0 row3" >HERO</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col0" class="data row3 col0" >0.623459</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col1" class="data row3 col1" >0.421671</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col2" class="data row3 col2" >0.657407</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col3" class="data row3 col3" >0.458261</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col4" class="data row3 col4" >0.601905</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row3_col5" class="data row3 col5" >0.390779</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row4" class="row_heading level0 row4" >INVESTIGATION</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col0" class="data row4 col0" >0.646376</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col1" class="data row4 col1" >0.592606</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col2" class="data row4 col2" >0.600388</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col3" class="data row4 col3" >0.549435</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col4" class="data row4 col4" >0.700388</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row4_col5" class="data row4 col5" >0.645075</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row5" class="row_heading level0 row5" >JOURNEY</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col0" class="data row5 col0" >0.505202</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col1" class="data row5 col1" >0.538554</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col2" class="data row5 col2" >0.51264</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col3" class="data row5 col3" >0.552931</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col4" class="data row5 col4" >0.499084</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row5_col5" class="data row5 col5" >0.527772</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row6" class="row_heading level0 row6" >LEGAL</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col0" class="data row6 col0" >0.607149</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col1" class="data row6 col1" >0.562588</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col2" class="data row6 col2" >0.545679</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col3" class="data row6 col3" >0.517006</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col4" class="data row6 col4" >0.684539</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row6_col5" class="data row6 col5" >0.617024</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row7" class="row_heading level0 row7" >MEDIA</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col0" class="data row7 col0" >0.543683</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col1" class="data row7 col1" >0.488292</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col2" class="data row7 col2" >0.646586</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col3" class="data row7 col3" >0.608507</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col4" class="data row7 col4" >0.469642</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row7_col5" class="data row7 col5" >0.409108</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row8" class="row_heading level0 row8" >MISCELLANEOUS</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col0" class="data row8 col0" >0.1531</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col1" class="data row8 col1" >0.163613</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col2" class="data row8 col2" >0.358333</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col3" class="data row8 col3" >0.316412</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col4" class="data row8 col4" >0.0979628</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row8_col5" class="data row8 col5" >0.111955</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row9" class="row_heading level0 row9" >MOURNING</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col0" class="data row9 col0" >0.737217</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col1" class="data row9 col1" >0.65369</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col2" class="data row9 col2" >0.72905</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col3" class="data row9 col3" >0.618216</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col4" class="data row9 col4" >0.745644</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row9_col5" class="data row9 col5" >0.694081</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row10" class="row_heading level0 row10" >PERPETRATOR</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col0" class="data row10 col0" >0.635561</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col1" class="data row10 col1" >0.568497</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col2" class="data row10 col2" >0.607743</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col3" class="data row10 col3" >0.521118</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col4" class="data row10 col4" >0.666198</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row10_col5" class="data row10 col5" >0.625522</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row11" class="row_heading level0 row11" >PHOTO</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col0" class="data row11 col0" >0.867822</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col1" class="data row11 col1" >0.810145</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col2" class="data row11 col2" >0.962235</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col3" class="data row11 col3" >0.903715</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col4" class="data row11 col4" >0.791482</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row11_col5" class="data row11 col5" >0.734191</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row12" class="row_heading level0 row12" >POLICY</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col0" class="data row12 col0" >0.76198</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col1" class="data row12 col1" >0.688665</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col2" class="data row12 col2" >0.719699</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col3" class="data row12 col3" >0.624043</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col4" class="data row12 col4" >0.809883</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row12_col5" class="data row12 col5" >0.768284</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row13" class="row_heading level0 row13" >RACECULTURE</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col0" class="data row13 col0" >0.526538</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col1" class="data row13 col1" >0.472681</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col2" class="data row13 col2" >0.485271</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col3" class="data row13 col3" >0.411426</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col4" class="data row13 col4" >0.577077</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row13_col5" class="data row13 col5" >0.555978</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row14" class="row_heading level0 row14" >RESOURCES</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col0" class="data row14 col0" >0.714699</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col1" class="data row14 col1" >0.607568</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col2" class="data row14 col2" >0.720465</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col3" class="data row14 col3" >0.664053</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col4" class="data row14 col4" >0.710595</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row14_col5" class="data row14 col5" >0.561214</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row15" class="row_heading level0 row15" >SAFETY</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col0" class="data row15 col0" >0.699861</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col1" class="data row15 col1" >0.626388</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col2" class="data row15 col2" >0.688813</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col3" class="data row15 col3" >0.598168</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col4" class="data row15 col4" >0.71184</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row15_col5" class="data row15 col5" >0.658571</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row16" class="row_heading level0 row16" >SOCIALSUPPORT</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col0" class="data row16 col0" >0.534268</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col1" class="data row16 col1" >0.479476</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col2" class="data row16 col2" >0.596018</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col3" class="data row16 col3" >0.498682</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col4" class="data row16 col4" >0.487058</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row16_col5" class="data row16 col5" >0.462509</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row17" class="row_heading level0 row17" >THREAT</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col0" class="data row17 col0" >0.412299</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col1" class="data row17 col1" >0.433208</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col2" class="data row17 col2" >0.4785</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col3" class="data row17 col3" >0.509968</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col4" class="data row17 col4" >0.366263</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row17_col5" class="data row17 col5" >0.378187</td>
            </tr>
            <tr>
                        <th id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70level0_row18" class="row_heading level0 row18" >TRAUMA</th>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col0" class="data row18 col0" >0.60162</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col1" class="data row18 col1" >0.552743</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col2" class="data row18 col2" >0.57845</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col3" class="data row18 col3" >0.494055</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col4" class="data row18 col4" >0.628757</td>
                        <td id="T_691d6106_c4a0_11e9_95d5_d4619d2e8c70row18_col5" class="data row18 col5" >0.629151</td>
            </tr>
    </tbody></table>
</div>

This table identifies which f-scores, precision and recall values were the best, and compares the sentence based and excerpt based results. The colour green indicates good performance and red indicates poor performance. It is nice to see that by far MISCELLANEOUS label had the worst performance. Another thing to note, is that these results show that overall recall does fairly well. This means that the classifiers are performing well at identifying the excerpts as having the correct label. The lower precision indicates that it is returning too many results (i.e. too many false positives). This could be a good thing in this application, since the false positives may actually be true positives due to errors or inconsistencies in the annotations. Also, in this application it may be better to bring to attention more of the results rather than less, since it may be better to identify more cases relevant to the label, as opposed to missing too many of them. 
