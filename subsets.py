def subsets(some_set, chosen):
    if len(some_set) == 0:
        print chosen
        return

    subsets(some_set[1:], chosen + [some_set[0]])
    subsets(some_set[1:], chosen)

subsets(['a', 'b','c','d'], [])
