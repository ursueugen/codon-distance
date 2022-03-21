import Bio.Data.CodonTable



def get_start_codons() -> list:
    return Bio.Data.CodonTable.standard_dna_table.start_codons

def get_stop_codons() -> list:
    return Bio.Data.CodonTable.standard_dna_table.stop_codons

def get_alphabets() -> tuple:
    return (
        Bio.Data.CodonTable.standard_dna_table.nucleotide_alphabet,
        Bio.Data.CodonTable.standard_dna_table.protein_alphabet
    )

def get_codon_dict() -> dict:
    fwd_table = Bio.Data.CodonTable.standard_dna_table.forward_table
    codon_dict = {
        **fwd_table,
        **{k: "STOP" for k in get_stop_codons()},
        # **{k: "START" for k in get_start_codons()},
    }
    return codon_dict

def get_codons() -> list:
    codons = sorted(get_codon_dict().keys())
    assert len(codons) == 64
    return codons

def get_code_values() -> list:
    _, protein_alphabet = get_alphabets()
    code_values = sorted(protein_alphabet)
    code_values += ["STOP"]
    return code_values