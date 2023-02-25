class BinaryTree:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        
data = BinaryTree(
    val="Are you smart?",
    left=BinaryTree(
        val="Cool"
    ),
    right=BinaryTree(
        val="Not cool"
    )
)

def traverse(tree):
    if not tree:
        print("You reached the end")
    else:
        if tree.left is not None or tree.right is not None:
            print(tree.val)
            userInput = input(print(tree.val + " (yes/no) \n"))
            if userInput.lower() == "yes" or userInput == "1" and tree.left is not None:
                traverse(tree.left)
            elif userInput.lower() == "no" or userInput == "0" and tree.right is not None:
                traverse(tree.right)
            else:
                print(tree.val)
                
traverse(data)