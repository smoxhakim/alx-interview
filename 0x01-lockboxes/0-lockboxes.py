def canUnlockAll(boxes):
    # Initial setup: length of boxes and a list to track opened boxes
    boxes_length = len(boxes)
    opened_boxes = [False] * boxes_length  # Track opened boxes
    opened_boxes[0] = True  # The first box is unlocked
    keys_queue = []  # This will keep track of which keys we can use

    # We begin with the keys in the first box
    keys_queue.extend(boxes[0])  # Start with keys from the first box

    while keys_queue:  # While there are keys to check
        key = keys_queue.pop(0)  # Get the next key
        if 0 <= key < boxes_length and not opened_boxes[key]:  # Check key validity
            opened_boxes[key] = True  # Mark the box as opened
            keys_queue.extend(boxes[key])  # Add the new keys from this box

    # All boxes have been opened if all elements in opened_boxes are True
    return all(opened_boxes)