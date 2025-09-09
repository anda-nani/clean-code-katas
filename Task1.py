def multiples(num : int) -> str :

    sum_of_multiples = 0

    for i in range(1, num):         #each int from 1 up to the provided argument

        if i % 3 == 0 or i % 5 == 0 :
            
            sum_of_multiples += i

    return print(sum_of_multiples)

multiples(10)
multiples(11)