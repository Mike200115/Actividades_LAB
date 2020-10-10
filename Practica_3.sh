#!/bin/bash
#Miguel Alejadnro Juarez Gonzalez
#Script para revisar archivos en virus total y saber si alguno es malicioso de ser el caso moverlo a una carpeta
clear
Direccion_analizar=$1
Direccion_maliciosa=$2

echo 'Revisando archivos...'
for Archivo in $(ls $Direccion_analizar)
do
    echo "Revisando $Archivo"
    sleep 5
    curl -X POST https://www.virustotal.com/vtapi/v2/file/scan -F apikey=11e080dd9098c210fb2ed90cd2552f720ee50046103f99061816faba556a0a1b -F file=$Direccion_analizar/$Archivo >> json.txt 
    grep -i 'Scan request successfully queued, come back later for the report' json.txt > /dev/null 2>&1
    [ $? -eq 1 ] && {
        echo "Amenaza detectada $Archivo"
        Direccion_archivo=$Direccion_analizar/$Archivo
        mv $Direccion_archivo $Direccion_maliciosa
    }
    rm json.txt
done
