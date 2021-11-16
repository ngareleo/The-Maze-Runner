## maze-solve-py
A simple python script to solve 1-bit mazes

#### Run
`python3 appv2.py -image='Maze name' --save='Save file'`

#### app.py 
- Implements recursion to solve the mazes
- It encounters problem in large mazes that invlove loops/ rings
- It uses a **single node** that forks into child nodes in split ends 
  - Whenever the child-node encouters a dead-end or the end-point, it traces back through the hierachy tree to the parent node
  - Reaches very deep recursion depths

#### appv2.py
- Uses a long iterative a list to keep track of position and data
