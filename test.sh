#!/bin/sh


manual[0]="手順書0"
manual[1]="手順書1"
manual[2]="手順書2"
manual[3]="手順書3"
manual[4]="手順書4"

switch[0]="switch0"
switch[1]="switch1"
switch[2]="switch2"
switch[3]="switch3"
switch[4]="switch4"





# switch=$1
# manual=$2

function switch_auto_check(){
  echo ${manual[$1]}
  echo ${switch[$2]}
}

# switch_auto_check($1, $2)

# switch_auto_check $1 $2

echo "This is a test."