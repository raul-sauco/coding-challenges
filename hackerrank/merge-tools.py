# Merge the tools
# 🟠 Medium
# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# tags : String

def merge_the_tools(string, k):
    l = []
    out = []
    for i in range (0, len(string), k):
        c = ""
        for j in range(k):
            c += string[i + j]
        l.append(c)
    
    for elm in l:
        c= ""
        for j in range(k):
            if elm[j] not in c:
                c += elm[j]
        out.append(c)
        
    for res in out:
        print(res)
