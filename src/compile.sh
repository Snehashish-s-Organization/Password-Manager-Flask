#!/bin/bash

if [ $1 == 'api' ]
then 
    python3 api.py 
else
    python3 app.py
fi