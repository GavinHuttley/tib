from cogent3 import make_aligned_seqs, make_table

seqs = {
    "seq-0": "ATTTATG",
    "seq-1": "ATATAAA",
    "seq-2": "TTATAAA",
    "seq-3": "TTAAAAG",
    "seq-4": "ATAAATG",
    "seq-5": "ATATATG",
    "seq-6": "ATATAGG",
    "seq-7": "ATAAAAA",
    "seq-8": "ATAAATC",
    "seq-9": "ATATTTA",
}

aln = make_aligned_seqs(data=seqs, moltype="dna")
aln.set_repr_policy(ref_name="seq-0")


def calc_pwm():
    c = aln.counts_per_pos()
    c = c.to_table()
    tr = c.transposed(
        r"Base \ Position",
        select_as_header="",
        index_name=r"Base \ Position",
        title="PWM",
        legend="position specific weights matrix",
    )
    tr.set_repr_policy(show_shape=False)
    return tr


def calc_ppm():
    attrs = dict(
        title="PPM --",
        legend="Position specific probability matrix",
        digits=1,
    )
    table = calc_pwm()
    table = table[:, :5]
    data = {}
    for n, column in table.columns.items():
        if len(n) == 1:
            column = column / column.sum()
        data[n] = column
    table = make_table(data=data, **attrs)
    table.set_repr_policy(show_shape=False)
    return table
