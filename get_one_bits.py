def getOneBits(n):
    # Write your code here
    binary = []
    final_binary = []

    if n == 0:
        binary.append(0)
    elif n == 1:
        binary.append(1)
    else:
        while n // 2 != 1:
            rem = n % 2
            binary.append(rem)
            n = n // 2

        if n // 2 == 1:
            binary.append(0)
            binary.append(1)

    for i in range(len(binary)):
        final_binary.append(binary[len(binary) - +1 - i])

    indices = [i + 1 for i in range(len(final_binary)) if final_binary[i] == 1]
    length_of_indices = len(indices)
    indices.insert(0, length_of_indices)

    return indices, final_binary


if __name__ == "__main__":

    n = int(input().strip())

    result, binary = getOneBits(n)

    print(f"Total count of 1 bit and positions of 1 bit {result}")
    print(binary)
