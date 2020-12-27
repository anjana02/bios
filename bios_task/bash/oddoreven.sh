echo -n "Enter numnber : "
read num
 
rem=$(( $num % 2 ))
 
if [ $rem -eq 0 ]
then
  echo "$num is even"
else
  echo "$num is odd"
fi
