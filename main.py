# import whatever you need here
import time
import sys
from hashmap import HashMap
cache = HashMap()
function_hits = 0
cache_hits = 0
# Part 1 -- Write weight_on_cacheless() method
def weight_on_cacheless(r,c):
    global function_hits
    function_hits += 1
    if r == 0:
        return 0
    elif c == 0:
        return (weight_on_cacheless(r - 1, c) + 200)/2
    elif c == r:
        return (weight_on_cacheless(r - 1, c - 1) + 200)/2
    else:
        return 200 + (weight_on_cacheless(r - 1, c - 1)/2) + (weight_on_cacheless(r - 1, c)/2)

# Part 3 -- Write weight_on_with_caching() method
def weight_on_with_caching(r,c):
    global function_hits
    global cache_hits
    function_hits += 1
    if (r,c) not in cache.table:
        if r == 0:
            return 0
        elif c == 0:
            weight = (weight_on_with_caching(r - 1, c) + 200)/2
        elif c == r:
            weight = (weight_on_with_caching(r - 1, c - 1) + 200)/2
        else:
            weight = 200 + (weight_on_with_caching(r - 1, c - 1)/2) + (weight_on_with_caching(r - 1, c)/2)
        cache.table[(r,c)] = weight
    else:
        cache_hits += 1
        weight = cache.table[(r,c)]
    return weight

def main():
    # Part 2 -- Use weight_on_cacheless() method
    # Cacheless
    global function_hits
    global cache_hits
    cache_hits = 0
    function_hits = 0
    print("Cacheless:")
    start = time.perf_counter()
    i = 0
    num = int(sys.argv[1])
    f = open("cacheless.txt","w")
    while i < num:
        j = 0
        row = ""
        while j <= i:
            row += '{:.2f}'.format((weight_on_cacheless(i,j))) + " "
            j+=1
        print(row)
        f.write(row + '\n')
        i+=1
    elapsed = time.perf_counter() - start
    print("Elapsed time: " + str(elapsed) + " seconds.")
    f.write("\nElapsed time: " + str(elapsed) + " seconds." + '\n')
    print(f"Number of function calls: {function_hits}\n")
    # f.write("Number of function calls: " + function_hits)
    f.close()
    
    #Part 3 -- Use weight_on_with_caching() method, with your HashMap ADT
    print("With caching:")
    start2 = time.perf_counter()
    f2 = open("with_caching.txt", "w")
    function_hits = 0
    i2 = 0
    while i2 < num:
        j2 = 0
        row2 = ""
        while j2 <= i2:
            row2 += '{:.2f}'.format((weight_on_with_caching(i2,j2))) + " "
            j2 += 1
        print(row2)
        f2.write(row2 + '\n')
        i2 += 1
    caching_elapsed = time.perf_counter() - start2
    print("Elapsed time: " + str(caching_elapsed) + " seconds.")
    f2.write("\nElapsed time: " + str(caching_elapsed) + " seconds." + '\n')
    print(f"Number of function calls: {function_hits}")
    print(f"Number of cache hits: {cache_hits}")
    f2.close()

if __name__=="__main__":
    main()