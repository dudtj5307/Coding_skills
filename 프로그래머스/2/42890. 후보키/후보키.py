from itertools import combinations

def solution(relation):
    nrow, ncol = len(relation), len(relation[0])
    byRow = [[relation[i][j] for i in range(nrow)] for j in range(ncol)]
    
    unqCol = []
    answer = 0
    bFlag = False
    for n in range(1, nrow+1):
        for temp in combinations(range(0, ncol), n):
            bFlag = False
            for u in unqCol:
                if set(temp) & set(u) == set(u):
                    bFlag = True
            if bFlag: continue
            newRelation = [[relation[i][j] for j in temp] for i in range(nrow)]
            if len(newRelation) == len(set([tuple(r) for r in newRelation])):
                unqCol.append(temp)
    return len(unqCol)