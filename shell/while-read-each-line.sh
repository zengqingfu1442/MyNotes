#!/bin/bash
i=1
cat .gitignore | while read line;do echo "$line --- line number is $i";let i++;done

#------------
while read line; do echo $line;done < .gitignore
