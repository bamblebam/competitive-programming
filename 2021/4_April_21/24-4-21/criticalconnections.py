import collections


class Solution:
    def criticalConnections(self, n: int, connections):
        adjacency_matrix = collections.defaultdict(list)
        for a, b in connections:
            adjacency_matrix[a].append(b)
            adjacency_matrix[b].append(a)
        low, disc, self.time, answer = [0]*n, [0]*n, 1, list()

        def tarjans(curr, prev):
            low[curr] = disc[curr] = self.time
            self.time += 1
            for next in adjacency_matrix[curr]:
                if not disc[next]:
                    tarjans(next, curr)
                    low[curr] = min(low[curr], low[next])
                elif next != prev:
                    low[curr] = min(low[curr], disc[next])
                if low[next] > disc[curr]:
                    answer.append([curr, next])
        tarjans(0, -1)
        return answer
