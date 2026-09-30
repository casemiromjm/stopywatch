import time

def main():

    start = time.time()

    while True:

        now = time.time() - start

        hour = int(now // (3600))
        rem = now % (3600)
        
        minut = int(rem // (60))
        rem = rem % (60)
        
        seg = int(rem)

        print(f"{hour:02}:{minut:02}:{seg:02}", end='\r')

        # como parar? ctrl c normal
        # clean terminal at the start



if __name__ == "__main__":
    main()
