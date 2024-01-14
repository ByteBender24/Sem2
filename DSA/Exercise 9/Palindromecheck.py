from WrapperQueue import AdapterQueue
from WrapperStack import AdapterStack


def Palindrome_check(num):
    q = AdapterQueue()
    s = AdapterStack()

    while num > 0:
        tmp = num % 10
        q.enqueue(tmp)
        s.push(tmp)
        num = num//10

    while (not s.is_empty()) and (not q.is_empty()):
        if q.peek() != s.top():
            return False
        q.dequeue()
        s.pop()
    return True


# Driver Code
if __name__ == "__main__":
    num1 = 123454321
    num2 = 1234564321
    print(Palindrome_check(num1))
    print(Palindrome_check(num2))
