App
===========


* Django REST API to create, update and edit surveys with different type of questions. This is perfect if you want to create custom surveys and let your users answer them easily.

Surveys Django REST API

### Requirements

* [Vagrant](https://www.vagrantup.com/downloads.html) 1.7.x or greater

### Set up development environment

* Run the following command to setup virtual environment
(it may take a while the first time)

```sh
vagrant up
```

* When the virtual environment is ready, establish a connection with the
following command

```sh
vagrant ssh
```

### Contributing

To ensure the project quality, you must run the following script before every
commit and make sure no problems were detected

```sh
sh tests.sh
```
