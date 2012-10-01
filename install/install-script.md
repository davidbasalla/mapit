---
layout: default
title: Install script
---

# MapIt Install Script

If you have a new installation of Debian squeeze or Ubuntu precise,
you can use an install script to set up a basic installation of
MapIt on your server.

*Warning: only use this script on a newly installed server - it will
make significant changes to your server's setup, including modifying
your nginx setup, creating a user account, creating a database,
installing new packages etc.*

The script to run is `pre-install-as-root`, whose usage is as follows:

    Usage: ./pre-install-as-root [--default] <UNIX-USER> [HOST]
    HOST is only optional if you are running this on an EC2 instance.
    --default means to install as the default site for this server,
    rather than a virtualhost for HOST.

The `<UNIX-USER>` parameter is the name of the Unix user that you want
to own and run the code.  (This user will be created by the script.)

The `HOST` parameter is a hostname for the server that will be usable
externally - a virtualhost for this name will be created by the
script, unless you specified the `--default` option..  This parameter
is optional if you are on an EC2 instance, in which case the hostname
of that instance will be used.

For example, if you wish to use a new user called `mapit` and the
hostname `mapit.example.org`, creating a virtualhost just for that
hostname, you could download and run the script with:

    curl https://raw.github.com/mysociety/mapit/master/bin/pre-install-as-root | \
        sudo sh -s mapit mapit.example.org

Or, if you want to set this up as the default site on an EC2 instance,
you could download the script and then invoke it with:

    sudo pre-install-as-root --default mapit

When the script has finished, you should have a working copy of the
website, accessible via the hostname you supplied to the script.

You should take a look at the configuration file in
`mapit/conf/general.yml`.  In particular, you should set `BUGS_EMAIL`
to your email address.  You should also consider the `SRID` and
`COUNTRY` settings, as described in the [manual installation
instructions](/install/).

Then you should then restart the MapIt Django server with:

    mapit@ip-10-58-191-98:~/mapit$ logout
    ubuntu@ip-10-58-191-98:~$ sudo /etc/init.d/mapit restart

Now you will probably want to carry on to [import some data](import).