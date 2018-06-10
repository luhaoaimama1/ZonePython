def my_callback(input):
    print("function my_callback was called with %s input" % (input,))


def caller(input, func):
    func(input)


for i in range(5):
    caller(i, my_callback)