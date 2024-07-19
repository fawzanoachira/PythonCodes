def getOneBits(n):
    # Write your code here
    binary = []
    while n // 2 != 1:
        rem = n % 2
        binary.append(rem)
        n = n // 2
    if n // 2 == 1:
        binary.append(0)
        binary.append(1)
    final_binary = []

    for i in range(len(binary)):
        final_binary.append(binary[len(binary) - +1 - i])

    indices = [i + 1 for i in range(len(final_binary)) if final_binary[i] == 1]
    length_of_indices = len(indices)
    indices.insert(0, length_of_indices)
    return indices


if __name__ == "__main__":

    n = int(input().strip())

    result = getOneBits(n)

    print(result)
