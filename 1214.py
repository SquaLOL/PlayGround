geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]


# l=[]
#     for i in birds:
#         if i not in geese:
#             l.append(i)
#     return(l)


def sakura_fall(v):
    return 400 / v if v > 0 else 0
    if v <= 0:
        return 0
    return 400 / v
