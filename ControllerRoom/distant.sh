echo "waiting for command"

read x

password="raspberry"
username="pi"
Ip="192.168.0.52"

if [ "$x" = "login" ]; then
  sshpass -p "$password" ssh $username@$Ip 'bash ~/Desktop/ControllerRoom/run.sh'
  echo "exited room contoller"
fi



if [ "$x" = "getData" ]; then
  sshpass -p "$password" scp $username@$Ip:~/Desktop/Implementation/DATA/temp.csv ~/Desktop/temp.csv
  sshpass -p "$password" scp $username@$Ip:~/Desktop/Implementation/DATA/hum.csv ~/Desktop/hum.csv
  sshpass -p "$password" scp $username@$Ip:~/Desktop/Implementation/DATA/light.csv ~/Desktop/light.csv
  sshpass -p "$password" scp $username@$Ip:~/Desktop/Implementation/DATA/ir_data.csv ~/Desktop/ir_data.csv
fi