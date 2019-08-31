from time import sleep

def function():
    print("Hello")
    
def scheduler(f, n):
    f()
    sec_to_ms = n / 1000
    sleep(sec_to_ms)
    print("After 10 seconds")
    f()

scheduler(function, 10000)