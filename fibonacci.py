import datetime

def fibonacci(num):
    result = []
    for n in range(num):
        def sum(fib_list):
            length = len(fib_list)
            return fib_list[length-1] + fib_list[length-2]
        if len(result) == 0:
            result.append(0)
        elif len(result) == 1:
            result.append(1)
        else:
            result.append(sum(result))
    result_string = ""
    count = len(result)
    for n in result:
        count = count - 1
        if count != 0:
            result_string = result_string + str(n)+","
        else:
            result_string = result_string + str(n)
    return result_string

f = open("input.txt", "r")
input_text = f.readlines()
f.close()

f = open("output_fibonnacci.txt", "w")
request_id = 1

for n in input_text:
    if n != "":
        time = str(datetime.datetime.now())
        f.write(str(request_id)+"    "+time+"    "+str(int(n))+"    "+str(fibonacci(int(n)))+"\n")
        request_id = request_id + 1
f.close()
print("done")