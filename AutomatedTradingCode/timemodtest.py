import time
import numpy as np

def fibonacci(n):
    # recursive function to print fibonacci
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
    
def main():
    num = np.random.randint(1,23)
    print("%dth fibonacci number is : %d"%(num, fibonacci(num)))
    
start_time = time.time()
timeout = time.time() + 60*2

while time.time() <= timeout:
    try:
        main()
        time.sleep(5 - ((time.time() - start_time)%5))
    except KeyboardInterrupt:
        print('\n\nKeyboard Exception Received.. Exiting...')
        exit()

     