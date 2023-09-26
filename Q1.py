def brudite(N):
    if N % 3 == 0 and N % 5 == 0:
        print("Brudite - Python Training")
    
    elif N % 3 == 0:
        print("Brudite")
    elif N % 5 == 0:
        print("Python Training")
    
    # if N % 3 == 0 and N % 5 == 0:
    #     print("Brudite - Python Training")
if __name__ == "__main__":
    N = 3
    brudite(3)