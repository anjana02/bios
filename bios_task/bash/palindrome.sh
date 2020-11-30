palindromeStirng="SOS"

rav=$(echo $palindromeStirng | rev)

if [[ $rav == $palindromeStirng ]];then
    echo "String is palindrome"
else
    echo "String is not palindrome"
fi