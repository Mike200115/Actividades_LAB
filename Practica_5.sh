#!/bin/bash
#Autor:Miguel Alejandro Juarez Gonzalez
#Script para decodificar y codificar archivos


function contiene() {
    local n=$#
    local value=${!n}
    for ((i=1;i < $#;i++)) {
        if [ "${!i}" == "${value}" ];
        then
            echo "y"
            return 0
        fi
    }
    echo "n"
    return 1
}

Direccion_analizar=$1
md5=(08b5e6f413402603ae48100110bac99b 40744679dff4bf36705c00f9cb815579 7264a79cccb5da23e0d37c504309af3d 0beac18480a527f29818d8c8b2964c74)
echo "Analizando..."
contador=0
declare -a arch_sin_editar
for Archivo in $(ls $Direccion_analizar)
do
    md5sum $Direccion_analizar/$Archivo  > temporal.txt
    for md5_posible in ${md5[@]}
    do
        grep -w $md5_posible temporal.txt > sin_valor.txt
        [ $? -eq 0 ] && {
            arch_sin_editar[$contador]=$Archivo
        }
       
        
        rm sin_valor.txt
    done
    ((contador ++))

    rm temporal.txt
done
mkdir "Carpeta_de_archivos"

for Archivo in $(ls $Direccion_analizar)
do
    if [ $(contiene "${arch_sin_editar[@]}" "$Archivo") == "y" ]; 
    then
        cat $Direccion_analizar/$Archivo | base64 > "Carpeta_de_archivos/$Archivo.txt"

    else
        cat $Direccion_analizar/$Archivo | base64 --decode > "Carpeta_de_archivos/$Archivo.png"
    fi
done









