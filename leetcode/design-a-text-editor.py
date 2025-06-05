from itertools import islice

class TextEditor:

    def __init__(self):
        self.left = collections.deque()
        self.right = collections.deque()
        
    # append text to where cursor left
    def addText(self, text: str) -> None:
        for c in text: # add text to the left deque
            self.left.append(c)
        
    # Delete k char to the left of cursor
    # return no. of char deleted
    def deleteText(self, k: int) -> int:
        if k < 0:
            return -1
        
        count = 0
        while self.left and count < k:
            self.left.pop()
            count += 1

        return count


    # return at most 10
    def cursorLeft(self, k: int) -> str:
        if k < 0:
            return ""

        for _ in range(min(k, len(self.left))):
            self.right.appendleft(self.left.pop())

        return ''.join(list(self.left)[-10:])

    def cursorRight(self, k: int) -> str:
        if k < 0:
            return ""

        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.popleft())

        return ''.join(list(self.left)[-10:])

    def getLast10(self) -> str:
        n = len(self.left)
        start = max(n - 10, 0)
        return ''.join(islice(self.left, start, n))

# left: [leetcode]
# right: []
# output:[null, ]

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

'''
question: Create a text editor that can add/delete text, move cursor

Use a double deque to push word from left or right 


'''