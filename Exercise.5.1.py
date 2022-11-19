#Lab 5 Exercise.1 1630902656 Kanokporn Hudsree
class Node:
    def __init__ (self,Val):
        self.Val = Val
        self.Next = ""
        self.Prev = ""
    def append(self,Val):
        TempNode = self.Next
        while TempNode != "":
            if TempNode.Next =="":
                TempNode.Next = Node(Val)
                TempNode.Next.Prev = TempNode
                break
            else:
                TempNode = TempNode.Next
        if self.Next =="":
            self.Next = Node(Val)
            self.Next.Prev = self



header = Node(1)
header.append(2)
header.append(3)
header.append(4)
