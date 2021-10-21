import re

psd = "add \"King Street\" (1,2)(3,4)"
test_str = re.search(r'\(.*\)', psd)
if test_str:
    print(len(psd))
    print(psd[test_str.span()[0]:test_str.span()[1]])