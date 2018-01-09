#!/usr/bin/env bash
# Initial configuration of Project


FOLDERNAME=${PWD##*/}
FOLDERNAME=echo ${FOLDERNAME}
# Rename all occurencies of mywebsite with the name of folder
find . -type f -exec sed -i 's/mywebsite/${FOLDERNAME}/g' {} +

mv mywebsite ${FOLDERNAME}
