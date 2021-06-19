def SupportFunction(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def MainFunction(array_val,n,k,l):
    result = +2147483647 
    final_output.clear()
    array_val.sort() 
    for i in range(n-k+1): 
        result = int(min(result, array_val[i+k-1] - array_val[i])) 
    for j in range(0,l):
        for name,value in input_items.items():
            if(int(value)==array_val[k+j]):
                val = SupportFunction([name,value])
                final_output.update(val)
    return result



input_file = open("input.txt",'r')
global input_items, final_output 
input_items = {}
final_output = {}

for line in input_file:
    lines = line.split(":")
    val = SupportFunction(lines)
    input_items.update(val)

val = (input_items.values())
actual = []
for n in val:
    actual.append(int(n))

arr= actual 
n =len(arr) 
input_file.close()
while(True):
    f = open("output.txt", "a")
    k = int(input("Number of employees : ")) 
    f.write("Number of employees : "+str(k))
    f.write("\n")
    f.write("Here the input_items that are selected for distribution are:")
    f.write("\n")
    result = MainFunction(arr, n, k,k)
    for name,value in final_output.items():
        f.write(name+" : "+value)
    f.write("\n")
    print("Output File Written")
    f.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(result))
    f.write("\n")
    f.close()

