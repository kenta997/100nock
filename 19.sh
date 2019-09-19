#!/bin/bash

cut -f 1 hightemp.txt | sort | uniq -c | sort -n -r -k 1

