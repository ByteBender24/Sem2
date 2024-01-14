def word_histogram_maker(file):
    f = open(f"{file}", 'r', errors="ignore")

    words = []
    for word in f.read().split():
        if word.isalpha():              #reduces the runtime by 1 sec roughly
            words.append(word)      

    histogram = {}

    for word in words:
        if word in histogram:
            histogram[word] += 1
        elif word not in histogram:
            histogram[word] = 1

    uniq_words = histogram.keys()

    f.close()

    return uniq_words, histogram


def create_file():
    fw = open("words.txt", 'w' , errors = "ignore")
    fh = open("words-histogram.txt", 'w' , errors = "ignore")

    return fw, fh

def write_txt_file(uniq_words, histogram , fw, fh):

    fh.write(str(histogram))
    for word in uniq_words:
        fw.write(word)
        fw.write("\n")

if __name__ == "__main__":

    print(word_histogram_maker("file.txt"))

    uniq_words = word_histogram_maker("file.txt")[0]
    histogram = word_histogram_maker("file.txt")[1]

    write_txt_file(uniq_words, histogram)
