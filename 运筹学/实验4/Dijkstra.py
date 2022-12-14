def Dijkstra(G):
    """
    Dijkstra算法，默认计算index为0的点与其他各点的距离
    :param G: 邻接矩阵，不存在的边以及距离为0的边请用99填充
    """
    n = len(G)  # 计算顶点数量

    # v:是否访问
    # dis:起始结点到相邻结点的距离
    v = [0]*n
    dis = G[0].copy()
    # 初始化
    v[0] = 1
    dis[0] = 99
    # 循环n次
    for _ in range(n):
        # 找出与集合相邻且距离起点最近的点
        k = 0
        for j in range(n):
            if v[j] == 0 and dis[j] < dis[k]:
                k = j
            # 该点被访问
        v[k] = 1  # 将该点加入集合

        # 用该点进行松弛(relax)
        for j in range(n):
            if v[j] == 0 and dis[k] + G[k][j] < dis[j]:
                dis[j] = dis[k] + G[k][j]
    return dis


G = [
    [99, 2, 99, 6, 99, 9, 99, 99],
    [99, 99, 30, 1, 99, 99, 99, 99],
    [99, 99, 99, 99, 99, 99, 99, 5],
    [99, 99, 99, 99, 2, 99, 99, 99],
    [99, 99, 8, 99, 99, 99, 7, 99],
    [99, 99, 99, 99, 3, 99, 24, 99],
    [99, 99, 99, 99, 99, 99, 99, 21],
    [99, 99, 99, 99, 99, 99, 99, 99]]
print(Dijkstra(G))
