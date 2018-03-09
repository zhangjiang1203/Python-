def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + " does not exist."
        print(msg)
    else:
        #计算文字大概包含多少个文字
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+" has about "+str(num_words)+" words")

file_name = "learningpython.txt"
count_words(file_name)