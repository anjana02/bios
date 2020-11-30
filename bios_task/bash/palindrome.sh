read -p "Enter a string: " string
if [[ $string|rev == $string ]]; then
    echo "String is Palindrome"
 else
    echo"String is not palindrome"
fi  
