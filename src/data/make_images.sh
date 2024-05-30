#!/bin/bash

find . -maxdepth 1 -type f -name "images_*" -print0 | xargs -0 -I {} tar -xvf {}