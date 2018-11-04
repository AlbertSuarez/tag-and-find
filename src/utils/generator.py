# Quick script for internal development

word1 = input()
while True:
    word2 = input()
    print("'{}': '{}',".format(word2.replace(" ", ""), word1))
