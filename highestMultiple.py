#10/02/2022 Computing Challenge - www.101computing.net/10-02-22-computing-challenge

# Let’s consider a string consisting of 10 characters “2”: string = “2222222222”

# This computing challenge consists of writing an algorithm to work out the largest number we can create by inserting 2 multiplication operators (*) anywhere within this string.

# For instance:

# 2 * 2 * 22222222 = 88,888,888
# 2 * 22 * 2222222 = 97,777,768
# 2222 * 2222 * 22 = 108,620,248
# 222 * 222 * 2222 = 109,509,048
# etc.

def largestMultiple(string):
    maximum = 0
    # Adding the first multiplication sign
    for i in range(1, len(string)):
        leftNumber = int(string[0:i])
        
        # Second multiplication
        for j in range(i+1, len(string)):
            midNumber = int(string[i:j])
            rightNumber = int(string[j:len(string)])

            result = leftNumber * midNumber * rightNumber
            
            if (result > maximum):
                maximum = result
                print(maximum)

            print(str(leftNumber) + " * " + str(midNumber) + " * " + str(rightNumber) + " = " + str(result))

    print("max multiple = " + str(maximum))

largestMultiple("2222222222")