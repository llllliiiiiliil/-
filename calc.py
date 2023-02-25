class calc:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        self.result = 0

    def sum(self):
        self.result = self.left + self.right

    def sub(self):
        self.result = (self.left - self.right)
    def mul(self):
        self.result = (self.left * self.right)
    def div(self):
        self.result = (self.left / self.right)

