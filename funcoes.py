import random
import sys

# -- KanapSack ---


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]


def mudarValoresKnapSack(W, wt, val, n):
    wt.clear()
    val.clear()
    for i in range(0, 5):
        wt.append(random.randint(1, 32))
        val.append(random.randint(1, 32))
    wt.sort()
    val.sort()
    W = random.randint(15, 30)
    n = len(val)
    return W, wt, val, n


# --- Grafos 2 - PRIM ---
vetorPontosTuristicos = ["PhiLen", "Zanzicave", "Doong", "Kavera", "Mycape",
                         "Maiorc", "Vatnajok", "Snowpe", "Banhall", "Algrep"
                         ]


class Graphico():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        totalMap = 0
        new_line = "\n"
        resultMap = ""
        for i in range(1, self.V):
            resultMap += '{} -  {}  R$ {},00 . '.format(
                vetorPontosTuristicos[parent[i]], vetorPontosTuristicos[i], self.graph[i][parent[i]], new_line)
            resultMap += "\n"
            totalMap += self.graph[i][parent[i]]

        return resultMap

    def printMST1(self, parent):
        totalMap = 0
        for i in range(1, self.V):
            totalMap += self.graph[i][parent[i]]

        return totalMap

    def minKey(self, key, mstSet):

        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return(self.printMST(parent))

    def primMST1(self):

        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        return(self.printMST1(parent))


def mudarValoresArestas():
    aresta1 = random.randint(1, 52)
    aresta2 = random.randint(1, 52)
    aresta3 = random.randint(1, 52)
    aresta4 = random.randint(1, 52)
    aresta5 = random.randint(1, 52)
    aresta6 = random.randint(1, 52)
    aresta7 = random.randint(1, 52)
    aresta8 = random.randint(1, 52)
    aresta9 = random.randint(1, 52)
    aresta10 = random.randint(1, 52)
    aresta11 = random.randint(1, 52)
    aresta12 = random.randint(1, 52)
    aresta13 = random.randint(1, 52)
    aresta14 = random.randint(1, 52)
    aresta15 = random.randint(1, 52)
    aresta16 = random.randint(1, 52)
    aresta17 = random.randint(1, 52)
    aresta18 = random.randint(1, 52)
    aresta19 = random.randint(1, 52)
    return aresta1, aresta2, aresta3, aresta4, aresta5, aresta6, aresta7, aresta8, aresta9, aresta10, aresta11, aresta12, aresta13, aresta14, aresta15, aresta16, aresta17, aresta18, aresta19


# --- GREED ----
def minimize_lateness(ttimes, dtimes):
    """Return minimum max lateness and the schedule to obtain it.

    (min_lateness, schedule) is returned.

    Lateness of a request i is L(i) = finish time of i - deadline of if
    request i finishes after its deadline.
    The maximum lateness is the maximum value of L(i) over all i.
    min_lateness is the minimum value of the maximum lateness that can be
    achieved by optimally scheduling the requests.

    schedule is a list that contains the indexes of the requests ordered such
    that minimum maximum lateness is achieved.

    ttime[i] is the time taken to complete request i.
    dtime[i] is the deadline of request i.
    """
    # index = [0, 1, 2, ..., n - 1] for n requests
    index = list(range(len(dtimes)))
    # sort according to deadlines
    index.sort(key=lambda i: dtimes[i])

    min_lateness = 0
    start_time = 0
    for i in index:
        min_lateness = max(min_lateness,
                           (ttimes[i] + start_time) - dtimes[i])
        start_time += ttimes[i]

    return min_lateness, index
