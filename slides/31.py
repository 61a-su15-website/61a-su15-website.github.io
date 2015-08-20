d = {'dog':      {'dog':      0,
                  'bear':     32,
                  'raccoon':  48,
                  'weasel':   51,
                  'seal':     50,
                  'sea lion': 48,
                  'cat':      98,
                  'monkey':   148},
     'bear':     {'dog':      32,
                  'bear':     0,
                  'raccoon':  26,
                  'weasel':   34,
                  'seal':     29,
                  'sea lion': 33,
                  'cat':      84,
                  'monkey':   136},
     'raccoon':  {'dog':      48,
                  'bear':     26,
                  'raccoon':  0,
                  'weasel':   42,
                  'seal':     44,
                  'sea lion': 44,
                  'cat':      92,
                  'monkey':   152},
     'weasel':   {'dog':      51,
                  'bear':     34,
                  'raccoon':  42,
                  'weasel':   0,
                  'seal':     44,
                  'sea lion': 38,
                  'cat':      86,
                  'monkey':   142},
     'seal':     {'dog':      50,
                  'bear':     29,
                  'raccoon':  44,
                  'weasel':   44,
                  'seal':     0,
                  'sea lion': 24,
                  'cat':      89,
                  'monkey':   142},
     'sea lion': {'dog':      48,
                  'bear':     33,
                  'raccoon':  44,
                  'weasel':   38,
                  'seal':     24,
                  'sea lion': 0,
                  'cat':      90,
                  'monkey':   142},
     'cat':      {'dog':      98,
                  'bear':     84,
                  'raccoon':  92,
                  'weasel':   86,
                  'seal':     89,
                  'sea lion': 90,
                  'cat':      0,
                  'monkey':   148},
     'monkey':   {'dog':      148,
                  'bear':     136,
                  'raccoon':  152,
                  'weasel':   142,
                  'seal':     142,
                  'sea lion': 142,
                  'cat':      148,
                  'monkey':   0}}

def edit_distance(seq1, seq2):
    if len(seq1) == 0:
        return len(seq2)
    if len(seq2) == 0:
        return len(seq1)
    return min(
        1 + edit_distance(seq1, seq2[1:]),
        1 + edit_distance(seq1[1:], seq2),
        (0 if seq1[0] == seq2[0] else 1) + edit_distance(seq1[1:], seq2[1:])
    )

def edit_distance(seq1, seq2):
    costs = [[0 for j in range(len(seq2) + 1)]
             for i in range(len(seq1) + 1)]
    for i in range(len(seq1) + 1):
        costs[i][0] = i
    for j in range(len(seq2) + 1):
        costs[0][j] = j
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            costs[i][j] = min(
                1 + costs[i-1][j],
                1 + costs[i][j-1],
                (0 if seq1[i-1] == seq2[j-1] else 1) + costs[i-1][j-1])
    for row in costs:
        print(row)
    return costs[-1][-1]

class PhyloTree:
    def __init__(self, branches, height):
        self.branches = branches
        self.height = height

    @property
    def seqs(self):
        seqs = []
        for branch in self.branches:
            seqs.extend(branch.seqs)
        return seqs

    def __repr__(self):
        return 'PhyloTree({0}, {1})'.format(repr(self.branches),
                                            repr(self.height))

    @property
    def newick(self):
        return '({0})'.format(
            ','.join('{0}:{1}'.format(b.newick, self.height - b.height)
            for b in self.branches))

class PhyloLeaf:
    def __init__(self, seq):
        self.seq = seq

    @property
    def seqs(self):
        return [self.seq]

    @property
    def height(self):
        return 0

    def __repr__(self):
        return 'PhyloLeaf({0})'.format(repr(self.seq))

    @property
    def newick(self):
        return '({0}:0)'.format(self.seq)

def cluster_distance(c1, c2):
    return (sum(edit_distance(p, q) for p in c1.seqs for q in c2.seqs) /
            (len(c1.seqs) * len(c2.seqs)))

def UPGMA(seqs):
    clusters = {PhyloLeaf(seq) for seq in seqs}
    while len(clusters) > 1:
        closest_pair = pop_closest_pair(clusters)
        clusters.add(PhyloTree(closest_pair,
                     0.5*cluster_distance(*closest_pair)))
    for cluster in clusters:
        return cluster

def pop_closest_pair(clusters):
    pairs = ({c1, c2} for c1 in clusters for c2 in clusters if c1 is not c2)
    closest_pair = min(pairs,
                       key=lambda pair: cluster_distance(*pair))
    for cluster in closest_pair:
        clusters.remove(cluster)
    return closest_pair

def edit_distance(p, q):
    return d[p][q]

t = UPGMA(set(d))
print(t)
print(t.newick + ';')
