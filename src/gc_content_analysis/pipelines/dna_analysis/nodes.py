import pandas as pd


def calculate_gc_content(dna_data: pd.DataFrame) -> pd.DataFrame:
    """Calculates GC content percentage for each DNA sequence."""
    def get_gc(seq):
        seq = seq.upper()
        return (seq.count('G') + seq.count('C')) / len(seq) * 100

    dna_data["gc_content"] = dna_data["sequence"].apply(get_gc)
    return dna_data
