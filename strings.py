#uppercase
#string = input("Enter a string: ")
#print(string.upper())


#capitalize
#string = input("Enter a string: ")
#print(string[0].upper()+string[1:])


#reverse
#string = input("Enter a string: ")
#print(string[::-1])


#LEETSPEAK
#array1 = ['A','E','G','I','O','S','T']
#array2 = [4,3,6,1,0,5,7]
#array3 = []
#string = (input("Enter a string: ")).upper()
#
#for i in range(len(string)):
#    array3.append(string[i])
#for j in range(len(array3)):
#    for k in range(len(array1)):
#        if array3[j] == array1[k]:
#           array3[j] = array2[k]
#        else:
#            array3[j] = array3[j]
#for i in range(len(array3)):
#    print(array3[i],end='')
#print()


#Long-Long Vowels
#vowels = ['a','e','i','o','u']
#string_array = []
#string = (input("Enter a string: ")).lower()
#for i in range(len(string)):
#    for j in range(len(vowels)):
#        if string[i] == vowels[j]:
#            print(string[0] + (string[i])*5 + string[-1])


#Caesar Cypher
string =  input("Enter a string: ").lower()
string_array = []
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
caesar = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','a','b','c','d','e']
for x in range(len(string)):
    string_array.append(string[x])
for i in range(len(string_array)):
    for j in range(len(alpha)):
        if string_array[i] == alpha[j]:
            string_array[i] = caesar[j]
print(string_array)




