import itertools

def rotate(m):
    while m:
        yield m[0]
        m = list(reversed(zip(*m[1:])))

def main():
    m = [[1,2,3],
         [8,9,4],
         [7,6,5]]

    print list(itertools.chain(*rotate(m)))

if __name__ == "__main__":
    main()
