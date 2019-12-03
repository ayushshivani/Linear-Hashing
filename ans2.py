import sys

p = 0		
total_rec = 0		
mod = 2		
mod_new = 4
bucket_count = 2
linHash = {}	
block_count = {}
output_buffer=[]

total_block_count = 2
block_count[0] = 1
block_count[1] = 1


def insert (num):
    global total_rec
    global total_block_count
    global output_buffer

    flag =0 
    hash_val = num % mod
    if hash_val < p:
        hash_val = num % mod_new
    if hash_val in linHash:
        flag=1
    if flag ==0:
        linHash[hash_val] = [[]]
    flag = 0
    no_of_blocks = block_count[hash_val]
    for i in range(no_of_blocks):
        if num in linHash[hash_val][i]:
            flag = 1

            
    if flag == 0:
        
        temp = block_count[hash_val] - 1
        if len(linHash[hash_val][block_count[hash_val] - 1]) >= (1):
            temp += 1
            total_block_count += 1
            linHash[hash_val].append([])
            block_count[hash_val] += 1
        total_rec += 1
        linHash[hash_val][block_count[hash_val] - 1].append(num)
        #print str(num)
        output_buffer.append(num)

    if hash_table_too_full(hash_val):
        create_new_bucket()


def hash_table_too_full(num):

    global b
    # print(block_counmat[num])
    if block_count[num] > 2:
        return 1
    return 0



def create_new_bucket():
    global bucket_count
    global p
    global mod
    global mod_new
    global total_block_count

    bucket_count += 1
    #rehash values
    replace_array = []
    total_block_count -= block_count[p]

    for i in range(block_count[p]):
        for value in linHash[p][i]:
            replace_array.append(value)


    linHash[p] = [[]]
    total_block_count += 1
    block_count[p] = 1

    linHash[bucket_count - 1] = [[]]
    total_block_count += 1
    block_count[bucket_count - 1] = 1

    for value in replace_array:
        hash_val = value % mod_new
        flag =0
        if hash_val in linHash:
            flag =1
            
        if flag==0:	
            block_count[hash_val] = 1
            linHash[hash_val] = [[]]
            total_block_count += 1

        flag = 0
        for j in range(block_count[hash_val]):
            if value in linHash[hash_val][j]:
                flag = 1

        if flag == 0:
            temp = block_count[hash_val] - 1
            if len(linHash[hash_val][temp]) >= 1:
                temp += 1
                total_block_count += 1

                block_count[hash_val] += 1
                linHash[hash_val].append([])
            linHash[hash_val][temp].append(value)
    p += 1

    if bucket_count == mod_new:
        mod= mod_new
        mod_new = 2 * mod_new
        p = 0

    return 1





def readfile(filename):
    file = open(filename)
    command = []
    for line in file:
        command.append(int(line.strip()))
    return command




if __name__ == '__main__':
    B = 2
    filename = sys.argv[1]
    commands = readfile(filename)

    for val in commands:
        insert(val)
    for i in output_buffer:
        print(i)
    # for i in linHash:
    #     print(block_count[i])
    #     print(linHash[i])