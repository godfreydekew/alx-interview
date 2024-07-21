#!/usr/bin/python3
'''
0. Lockboxes
'''


def canUnlockAll(boxes):
    '''
    determines if all the boxes can be opened.
    '''
    keys = boxes[0]
    for i in range(len(boxes)):
        if i in keys:
            for k in boxes[i]:
                if k not in keys:
                    keys.append(k)
    return len(keys) == (len(boxes) - 1)
