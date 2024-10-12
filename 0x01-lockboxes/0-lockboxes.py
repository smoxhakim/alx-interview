#!/usr/bin/python3
''' Locked box challenge '''


def canUnlockAll(boxes):
    ''' Locked box challenge '''
    boxes_length = len(boxes)
    opened_boxes = [False] * boxes_length
    opened_boxes[0] = True
    keys_queue = []

    keys_queue.extend(boxes[0])

    while keys_queue:
        key = keys_queue.pop(0)
        if 0 <= key < boxes_length and not opened_boxes[key]:
            opened_boxes[key] = True
            keys_queue.extend(boxes[key])

    return all(opened_boxes)
