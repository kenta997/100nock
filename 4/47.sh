# /bin/bash

cut -f 1 47.txt | uniq -c | sort -n -r | head
echo --------------------------
cut -f 1,2 47.txt | uniq -c | sort -n -r | head

