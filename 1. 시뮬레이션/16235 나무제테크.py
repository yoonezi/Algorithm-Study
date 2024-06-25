'''
가장 처음에 양분은 모든 칸에 5만큼 들어있다.

봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 
각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 

하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 
만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 
각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 
소수점 아래는 버린다.

가을에는 나무가 번식한다. 
번식하는 나무는 나이가 5의 배수이어야 하며, 
인접한 8개의 칸에 나이가 1인 나무가 생긴다. 
어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 
상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.


TIP:::::시뮬은 무조건 하라는대로 구현하기!!
'''

n, m, k = map(int, input().split())
nutrient = [[5] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

add_nut = []
for _ in range(n):
    add_nut.append(list(map(int, input().split())))
    
'''trees를 deque로??? 빠르고, 제거해야하니 ???'''
trees = [[[] for _ in range(n)] for _ in range(n)] 
for _ in range(m):
    tree_x, tree_y, old = map(int, input().split())
    trees[tree_x - 1][tree_y - 1].append(old)

def spring_summer():
    for i in range(n):
        for j in range(n):
            
            if trees[i][j]:
                '''new_trees = sorted(trees[i][j]) '''
                trees[i][j].sort() 
                die_tree_age = 0
                live_trees = []
                
                for tree in trees[i][j]:
                    
                    if nutrient[i][j] >= tree:
                        nutrient[i][j] -= tree
                        tree += 1
                        live_trees.append(tree)
                    else:
                        die_tree_age += tree // 2
            
                trees[i][j] = live_trees
                nutrient[i][j] += die_tree_age        
            

def fall():
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for tree in trees[i][j]:
                    if tree % 5 == 0:
                        for d in range(8):
                            nx = i + dx[d]
                            ny = j + dy[d]
                            '''함수로 빼보고 디거빙해보기!!!'''
                            if 0 <= nx < n and 0 <= ny < n:
                                trees[nx][ny].append(1)

def winter():
    for i in range(n):
        for j in range(n):
            nutrient[i][j] += add_nut[i][j]

for i in range(k):
    spring_summer()
    fall()
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)