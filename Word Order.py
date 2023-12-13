if __name__ == '__main__':
    N = int(input())
    word_counts = {}

    for i in range(N):
        word = input().rstrip()  # Read a word and remove the trailing newline character

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    distinct_words = len(word_counts)

    print(distinct_words)
    print(*word_counts.values())
