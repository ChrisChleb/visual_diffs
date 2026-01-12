# source: https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
def progressBar(iterable, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    
    printProgressBar(0)
    
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
        
    # print new line on complete
    print()