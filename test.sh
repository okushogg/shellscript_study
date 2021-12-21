#!/bin/sh


manual[0]="MarioCart/MarioCart_matchmake.py"
switch[0]="00:00:00:00"





# switch=$1
# manual=$2

function switch_auto_check(){
  echo ${manual[$1]}
  echo ${switch[$2]}
  echo $'\a\a\a'
}

# switch_auto_check($1, $2)

switch_auto_check $1 $2