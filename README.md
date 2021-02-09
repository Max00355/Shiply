Overview
=====

![](https://img.shields.io/badge/version-1.3.2-brightgreen.svg) [![](https://img.shields.io/badge/irc-%23coffer-red.svg)](https://webchat.freenode.net/) [![](https://img.shields.io/badge/twitter-cofferproject-blue.svg)](http://twitter.com/cofferproject)

A lightweight platform for creating isolated and portable development environments.

Requirements
============

- Python 3
- Linux (Tested on Ubuntu 17.1.0)

Quick Start
===========

In Terminal

`python3 setup.py install`

`coffer create my_env`

`coffer enter my_env`

What is Coffer?
===============

Before I talk about what Coffer is, let me say what Coffer is *not*. Coffer is not a replacement for Docker. In fact, if you are looking for a completely isolated container
you're probably better off using Docker, or some other container software. Coffer is also not intended to be used as a secure means by which to isolate an application, and
it is recommended that Coffer not be used outside of a development setting. 

Coffer is a platform for creating isolated filesystem containers. It is intended to be used to create isolated development environments without having to worry about doing any network configuration.
Applications that are run in Coffer can be accessed outside of a Coffer environment through `localhost` without having to do anything more than `coffer create <name>`. 
This makes it easy to get environments up and running for those of us who do not need network isolation, and only wish to isolate an app and its dependencies.

Coffer makes it easy to create, enter, and share environments with others.

What are some features of Coffer?
=================================

- Create isolated file system containers
- Use Coffer templates to automatically install and configure a container
- Share containers and templates with a team to replicate an environment
- Does not isolate network, so there is no extra configuring that needs to be done
- Creating an environment is as easy as executing `coffer create <name of environment>`

How can I get started?
======================

1. Clone this repo
2. Run `setup.py`
3. In a terminal execute `coffer create first_env`
4. Then `coffer enter first_env`

Then like that you have created your first environment! For more extensive getting started docs, read our [Getting Started](https://github.com/Max00355/Coffer/blob/master/docs/GettingStarted.md) docs.

Current Status
==============

Coffer is under very heavy development, and receiving frequent updates. The code in the `master` branch is considered the most stable, and in it's current state Coffer is ready for actual use.
In fact, Coffer development is happening in a Coffer container as of right now. If there are any bugs, please create issues about them.

