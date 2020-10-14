#Autor: Miguel Alejandro Juarez Gonzalez
#Script para mandar mesajes a multiples correos a la vez
$outlook = New-Object -com Outlook.Application
$mail = $outlook.CreateItem(0)
$mail.importance = 2  # importancia del correo
$mail.subject = "holi" #titulo
$mail.body = "as cido aceado" #mensaje
$mail.To = " " # correos separados por un ;
$mail.Send()
$outlook.Quit()