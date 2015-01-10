"""
Implement a simple regex parser which, given a string and a pattern, returns a boolean indicating whether the input matches the pattern. By simple, we mean that the regex can only contain one special character: * (star). The star means what you'd expect, that there will be zero or more of any character in that place in the pattern. However, multiple consecutive stars are allowed. Some examples of valid input (and expected output):

    f(a*b, acb) => true
    f(abc*, abbc) => false
    f(**bc, bc) => true
"""
def match(pattern, text):
    if pattern == "" and text != "":
        return False
    if pattern != "" and text == "":
        return False
    if pattern == "" and text == "":
        return True

    # matches will be printed in reverse order
    # because recursion makes the last matches
    # print first.
    if pattern[0] == text[0]:
        result = match(pattern[1:], text[1:])
    #    if result:
    #        print "matched %s" % text[0]
        return result
    elif pattern[0] == "*":
        for i in range(len(text) + 1):
            result = match(pattern[1:], text[i:])
    #        if result:
    #            print "matched %s" % text[:i]
            if result:
                return True
    return False


def print_match_result(pattern, text):
    print "%s, %s = %s" % (pattern, text, match(pattern, text))

print_match_result("a*b", "acb")
print_match_result("abc*", "abbc")
print_match_result("**bc", "bc")
print_match_result("ba**", "badfg")
print_match_result("abc", "abcdef")
print_match_result("abcdef", "abc")
print_match_result("", "")
