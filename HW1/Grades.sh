#Liam Kolber

if [ $# = 0 ] 
then
	echo "Usage: Grades.sh filename"
	exit 1
fi

#Sort File based on last name, first name, then ID
sort -k3,3 -k2,2 -k1,1 $1 -o $1

#Read sorted file line by line and format output using expr. 
while read -a line;
do
	sum=`expr ${line[3]} + ${line[4]} + ${line[5]}`
	avg=`expr $sum / 3`
	echo "$avg [${line[0]}] ${line[2]}, ${line[1]}"
done < $1
