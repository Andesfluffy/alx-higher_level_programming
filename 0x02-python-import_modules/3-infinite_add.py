#!/usr/bin/python3

if __name__ == "__main__":
    """Print the result of the addition of all arguments."""
    import sys
    cnt_tot=0
    for i in range(len(sys.argv) -1):
        cnt_tot = int(sys.argv[i+1])
    print("{}".format(cnt_tot))
