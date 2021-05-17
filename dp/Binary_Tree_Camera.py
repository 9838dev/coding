# given a binary tree
# need to minimize the camera to be install
# if camera on some node then its parent, that particular node and immediate children is also monitor

# problem link: https://leetcode.com/problems/binary-tree-cameras/

# suppose we already created binary tree of value 0's 

'''
logic: 
    if left or right of node is not monitor then we require a camera in that particular node
    if left or right have camera then that particular node doesn't requires a camera and hence it is monitored
'''
total = 0
def minCamera(root): # root node of binary tree
    global total
    def find(root):
        global = total
        if root == None:
            # [monitor,camera]
            return [1,0]
        left = find(root.left)
        right = find(root.right)

        require_camera = monitor = 0
        if left[0] == 0 or right[0] == 0:
            require_camera+=1
            monitor+=1
            total+=1
        
        if left[1] == 1 or right[1] == 1:
            monitor+=1 
        return [monitor,require_camera]

    temp = find(root) 
    if temp[0] == 0:
        total+=1
    return total
