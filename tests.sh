#!/bin/bash

success_status_code=0
failure_status_code=1

red_color='\033[0;31m'
green_color='\033[0;32m'
no_color='\033[0m'

NAME_PROJECT=surveys_rest_api

echo 'Deleting .pyc files...'
find $NAME_PROJECT/ -name '*.pyc' -exec rm {} \;

echo 'Deleting backup files...'
find ./ -name '*~' -exec rm {} \;

echo 'Running source code analyzers...'
flake8 $NAME_PROJECT/

if [ $? -eq $success_status_code ]
    then
        echo "${green_color}No source code problems found${no_color}"
    else
        echo "${red_color}Source code problems found, please fix them to continue${no_color}"
        exit $failure_status_code
fi

echo 'Running unit tests'
python $NAME_PROJECT/manage.py test $NAME_PROJECT/

if [ $? -eq $success_status_code ]
    then
        echo "${green_color}The tests ran successfully${no_color}"
    else
        echo "${red_color}The tests failed, please fix them to continue${no_color}"
        exit $failure_status_code
fi

echo "${green_color}All tests ran successfully, now you can make a commit${red_color}"
exit $success_status_code
