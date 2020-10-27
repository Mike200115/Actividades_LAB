#Autor: Miguel Alejandro Juarez Gonzalez
#Script para el uso basico de nmap

rango_ip=$1
ip_scan=$2

nmap $rango_ip > reporte_de_rango_ip.txt
nmap $ip_scan > reporte_ip_publica.txt
nmap --script=vuln $ip_scan > vulneravilidades_ip_publica.txt