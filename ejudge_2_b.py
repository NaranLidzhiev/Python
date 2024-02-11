
import re
from sys import stdin
from collections import deque
def print_deck(list):
    if len(list) == 0:
        print("empty")
    else:
        print(" ".join(map(str, list)))

def pushb(list, el):
    if len(list) == set_size:
        print("overflow")
        return 
    list.append(el)

def pushf(list, el):
    if len(list) == set_size:
        print("overflow")
        return
    list.appendleft(el)


def popf(list):
    if len(list) == 0:
        print("underflow")
        return
    print(list[0])
    list.popleft()

def popb(list):
    if len(list) == 0:
        print("underflow")
        return
    print(list[len(list)-1])
    list.pop()
#добавил вместо обычного списка двустороннюю очередь a = deque([]). В ней операции выполняются за O(1), а не за O(n) как в обычном списке
a = deque([])
set_size_check = False
for line in stdin:
    space_count = line.count(' ')
    line = line.strip()  
    if not line.strip(): 
        continue
    set_size_match = re.match(r'^\s*set_size\s+(\d+)\s*$', line)
    if set_size_match:
        if set_size_check == True:
            print("error")
            continue
        set_size = int(set_size_match.group(1))
        set_size_check = True
    elif not 'set_size' in globals():
        print("error")
        continue
    elif line == "print" and space_count == 0:
        print_deck(a)
    elif line.startswith("pushb") and space_count == 1:
        pushb_match = re.match(r'^\s*pushb\s+(\S+)\s*$', line)
        if pushb_match:
            pushb(a, pushb_match.group(1))
        else:
            print("error")
    elif line.startswith("pushf") and space_count == 1:
        pushf_match = re.match(r'^\s*pushf\s+(\S+)\s*$', line)
        if pushf_match:
            pushf(a, pushf_match.group(1))
        else:
            print("error")
    elif line == "popf" and space_count == 0:
        popf(a)
    elif line == "popb" and space_count == 0:
        popb(a)
    else:
        print("error")