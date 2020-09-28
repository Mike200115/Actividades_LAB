#!/bin/bash
#11e080dd9098c210fb2ed90cd2552f720ee50046103f99061816faba556a0a1b
#@/home/mike/Documentos/1.txt
API=$1
#ARCH=$2
#LINK=$3
echo '\nPeticion 1'
#curl -X POST https://www.virustotal.com/vtapi/v2/file/scan -F apikey=$API -F file=$ARCH
echo '\nPeticion 2'
#curl -X POST https://www.virustotal.com/vtapi/v2/url/scan -F apikey=$API -F url=$LINK
echo '\nPeticion 3'
parte="&domain=google.com"
URL="https://www.virustotal.com/vtapi/v2/domain/report?apikey=$API"7878 
echo "$URL"
#curl --request GET --url ${URL}