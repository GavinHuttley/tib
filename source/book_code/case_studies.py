from cogent3 import load_seq, load_table
from cogent3.maths.stats.contingency import CategoryCounts
from cogent3.util.dict_array import DictArrayTemplate
from numpy import zeros


def get_seq(path):
    seq = load_seq(path, moltype="dna")
    return seq


def to_dinucs(seq, independent=True):
    return [seq[i : i + 2] for i in range(0, len(seq), 2)]


def to_4x4(dinucs):
    bases = "ACGT"
    data = zeros((4, 4), dtype=int)
    for b1, b2 in dinucs:
        data[bases.index(b1), bases.index(b2)] += 1
    return CategoryCounts(DictArrayTemplate(bases, bases).wrap(data))


def get_table(path):
    return load_table(path, index_name="ID")
