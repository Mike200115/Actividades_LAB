#!/bin/bash
#Autor: Miguel Alejandro Juarez Gonzalez
#Script para hacer 3 peticiones a virustotal con curl
API=$1
ARCH=$2
LINK=$3
COMMENT=$4
echo -e "\n\n"
echo -e "\nPeticion 1"
curl -X POST https://www.virustotal.com/vtapi/v2/file/scan -F apikey=$API -F file=$ARCH #Example of file: @/home/mike/Doc/1.txt 
echo -e "\nPeticion 2"
curl -X POST https://www.virustotal.com/vtapi/v2/url/scan -F apikey=$API -F url=$LINK #Example of link: https://www.youtube.com/watch?v=S0tltAWkfLA&list=RDMM4dOT1BoJFko&index=8
echo -e "\nPeticion 3"
curl -v --request POST https://www.virustotal.com/vtapi/v2/comments/put -F apikey=$API -F comment=$COMMENT -F resource=8ebc97e05c8e1073bda2efb6f4d00ad7e789260afa2c276f0c72740b838a0a93 #Example of comment: Hello
echo -e "\n"