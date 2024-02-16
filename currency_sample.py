def convert_to_indian_currency(number):
    #convert the integer to a string
    num_str = str(number)
    n = len(num_str)
    if n <= 3:
        return num_str
    else:
        comma_count = (n - 1) //2
        result = "" #empty string to store result
        for i in range(n):
            if (n - i) % 2 == 0 and i != 0:
                result += ","
            result += num_str[i]
        return result

#run the function
input_currency = 504678
output_str = convert_to_indian_currency(input_currency)
print("Number:", input_currency)
print("formatted_Indian_curreny:", output_str)





    
