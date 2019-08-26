---
layout: post
title:  "Setting up Singularity"
date:   2019-08-25 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---

This post will describe the process I used to run singularity in an HPC. The objective was to run an optimization for text classification using hyperopt and flair. The singularity recipe can be found in the [github](https://github.com/anjapago/AnalyzeAccountability/blob/master/singularity/Singularity).

## Creating the recipe and Singularity Hub
The created recipe can be found in the [github(https://github.com/anjapago/AnalyzeAccountability/blob/master/singularity/Singularity). The starting point for this recipe was from [Frederick Michaud](https://singularity-hub.org/collections/1851). Having a singularity file in my github results in automatic builds to be triggered in singularity hub. My singularity hub can be found [here](https://singularity-hub.org/collections/3129).

One challenge in this process was that 1) singularity will only build 10 builds per day, and 2) the build procedure is quite slow. The results in taking quite a long time to figure out and resolve errors in the singularity recipes. Looking through my commits, the types of errors that arose can be seen. Getting the flair installed properly required several iterations of recipes. One tricky error was fixing a utf-8 error that never showed up when running the code on my mac. This error was actually inside the flair library code, so I made some changes in my fork of flair to fix this, and so it is my fork of the flair library being used in this singularity container.

## Running in HPC
To run in the HPC, the procedure I followed is listed below:

1. connect to vpn with cisco and ssh into the hpc
2. change directory to gallina home
3. pull analyze accountability code from github to update
4. Transfer data files in with filezilla
5. pull from singularity hub
```sh
singularity pull shub://anjapago/AnalyzeAccountability
```
6. Run the singularity container and python code:
```sh
singularity run -e -H 'pwd' AnalyzeAccountability_latest.sif
```
or
```sh
singularity shell -e -H 'pwd' AnalyzeAccountability_latest.sif
python3 flair_opt.py
```
7. Run the python code in the background to prevent stopped when disconnect happens:
```sh
nohup python3 flair_opt.py &
```
Any print statements or logs will be output into a file 'nohup.out'. This file can get quite long, so to track the progress, one can run:
```sh
tail nohup.out
```
Which will show the most recent few lines of the logs. 

## Resources

The following are some resources used to create this set up, and also reseources that used alternative approaches.

- [Alternative approach for singularity with mac](https://yongzx.github.io/blog/2019/Singularity-Simple-Guide/)
- [Singularity desktop for mac](https://sylabs.io/singularity-desktop-macos/)
- [Reference recipe](https://singularity-hub.org/collections/1851)
- [RedHen reference](http://www.redhenlab.org/home/tutorials-and-educational-resources/using-singularity-to-create-portable-applications)
