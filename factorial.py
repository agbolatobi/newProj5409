import datetime
def factorial(num):
    result = 1
    for n in range(num):
        result = result * (n+1)
    return result

f = open("input.txt", "r")
input_text = f.readlines()
f.close()

f = open("output_factorial.txt", "w")
request_id = 1
for n in input_text:
    if n != "":
        time = str(datetime.datetime.now())
        f.write(str(request_id)+"    "+time+"    "+str(int(n))+"    "+str(factorial(int(n)))+"\n")
        request_id = request_id + 1
f.close()
print("done")