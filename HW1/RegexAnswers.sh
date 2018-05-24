#Liam Kolber

#Usage message to ensure Regex.sh is called with a filename. 
if [ $# = 0 ]
then 
	echo "Usage: RegexAnswers.sh filename"
	exit 1
fi

#answers to questions coded below
#1. how many lines end with a number?
egrep [0-9]$ $1 |wc -l
#2. how many line do not start with a vowel?
egrep ^[^aeiouAEIOU] $1 |wc -l
#3. how any 12 letter (alphabet only) lines?
egrep "^[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]$" $1 |wc -l
#4. how many phone number are in the dataset?
egrep "[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]" $1 |wc -l
#5. how many city of Boulder phone numbers?
egrep "[3][0][3]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]" $1 |wc -l
#6. how many begin with vowel and end with number?
egrep "^[aeiouAEIOU].+[0-9]$" $1 |wc -l
#7. how many emails end in geocities.com?
egrep .+@geocities.com$ $1 |wc -l
#8. how many emails are in first.last name format?
egrep "^[a-lA-L][^[:blank:]]*\.[^[:blank:]]*@" $1 |wc -l
