---
layout: post
title:  "RedHen On-boarding"
date:   2019-06-08 00:00:30 -0400
categories: update
permalink: /:categories/:year/:month/:day/:title.html
---

This post will explain the onboarding procedure from RedHen. The objective is to
be able to work in the high performance computing environment provided by
RedHen. In order to get access to this, several steps were required.

## Main On-boarding Steps

1. Login for case western reserve university

  First, submit information to RedHen required to create an account, and then
  you will receive an email from case with information about how to log in
  and create an email address. The email address provided should be
  firstname.lastname@case.edu. This can be used to log in to email at
  http://webmail.case.edu.

2. Login for CWRU network

  Using links provided in the previous email, you can also set up the CWRU network
  login which will be a randomly assigned username in the format abc123. This
  username can be used to get into the vpn, and also to sign in here: login.case.edu

3. Logging in to vpn

  To log into the VPN, cisco AnyConnect can be used. The network to log into is
  vpn.case.edu. Once this is entered, you will need your CWRU network login,
  and the password you set for it. This log in will also show a field to fill
  in called second password. This second password comes from Duo.
  Duo can be set up for Case following [these instructions](https://case.edu/utech/departments/information-security/duo-security-two-factor-authentication). The main idea is
  download the app Duo, and connect it with the Case account. The second
  password to enter will be the numerical code shown in the app.

4. Ssh into the HPC

  In the terminal, ssh <caseID>@rider.case.edu, where caseID is the abc123 CWRU
  login. More guidelines can be [here](https://sites.google.com/a/case.edu/hpcc/).
  Once in the HPC, the home directory will be /home/abc123, and the path
  where you will have room to store data will be /mnt/rds/redhen/gallina/home/abc123.
  Next, follow steps to set up ssh keys, as will be explained in an email from RedHen.

5. Using Singularity

  In order to use Singularity, it must exist in the path. You can test Singularity
  by pulling from RedHen's singularity hub, and running the container:

    singularity pull --name deepspeech-temp.img shub://RedHenLab/singularity_containers:deepspeech2


## Summary

The hardest part of this process was figuring out which logins were for which,
and what to put as "password 2" in logging in to the vpn. Hopefully this summary
will fill in the blanks for some future students.

More information on this procedure can be found on the RedHen website:
[HPC orientation](https://sites.google.com/case.edu/techne-public-site/cwru-hpc-orientation)
[RedHen guidelines](https://sites.google.com/site/distributedlittleredhen/home/what-kind-of-red-hen-are-you/red-hen-developers)
[RedHen Singularity guide](https://sites.google.com/site/distributedlittleredhen/home/tutorials-and-educational-resources/using-singularity-to-create-portable-applications)
