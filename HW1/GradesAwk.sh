#Liam Kolber

if [ $# = 0 ] 
then
	echo "Usage: GradesAwk.sh filename"
	exit 1
fi

#Sort File based on last name, first name, ID. 
sort -k3,3 -k2,2 -k1,1 $1 -o $1

#Format output using awk: cast output to int to match bash
awk '{print int(($4+$5+$6)/3) " [" $1 "] " $3 ", "  $2}' $1
