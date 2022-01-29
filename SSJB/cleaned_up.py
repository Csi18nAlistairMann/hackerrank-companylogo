from collections import Counter

TOP_N_TO_SHOW = 3
CHARACTER = 0
FREQUENCY = 1


class top:
    def __init__(self, n_to_show):
        self.n_to_show = n_to_show
        topN = []
        for n in range(self.n_to_show):
            topN.append([' ', 0])
        self.topN = topN

    def swap(self, x, to_comp):
        if x + 1 < self.n_to_show:
            for idx in range(self.n_to_show - 1, x + 1, -1):
                self.topN[idx] = self.topN[idx - 1]
            self.topN[x + 1] = self.topN[x]
        self.topN[x] = to_comp

    def compare(self, to_comp):
        for x in range(self.n_to_show):
            # Check frequency
            if to_comp[FREQUENCY] > self.topN[x][FREQUENCY]:
                self.swap(x, to_comp)
                break

            # If frequencies identical check alphabetic
            elif to_comp[FREQUENCY] == self.topN[x][FREQUENCY]:
                if to_comp[CHARACTER] < self.topN[x][CHARACTER]:
                    self.swap(x, to_comp)
                    break
        return

    def print_result(self):
        for x in range(self.n_to_show):
            print(self.topN[x][CHARACTER], self.topN[x][FREQUENCY])

if __name__ == '__main__':
    s = input()
    c = Counter(s)
    topN = top(TOP_N_TO_SHOW)
    for item in c.items():
        topN.compare(item)
    topN.print_result()
