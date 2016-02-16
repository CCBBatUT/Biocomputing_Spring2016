"""
    SJS.
    This module contains functions for calculating various statistics for a DNA sequence, including:
        1. GC and AT content
        2. Percentage of a given nucleotide
        3. Purine vs. pyrimidine content
"""

known_nucleotides = ["A", "C", "G", "T"]

def calculate_gc(sequence):
    """
        This function computes the GC content for a given DNA sequence.
        
        Arguments:
            1. sequence, a string of a DNA sequence
        Returns:
            A decimal value representing the GC content of the provided sequence.
    """
    
    gc = 0.
    for nucleotide in sequence:
        if nucleotide == "G" or nucleotide == "C":
            gc += 1.
    
    gc_content = gc / len(sequence)
    
    return gc_content
    
    

def calculate_at(sequence):
    """
        This function computes the AT content for a given DNA sequence.
        
        Arguments:
            1. sequence, a string of a DNA sequence
        Returns:
            A decimal value representing the AT content of the provided sequence.
    """
    
    at = 0.
    for nucleotide in sequence:
        if nucleotide == "A" or nucleotide == "T":
            at += 1.
    
    at_content = at / len(sequence)
    
    return at_content
    

    
    
def calculate_nucleotide_percent(sequence, nuc):
    """
        This function computes the percent of a sequence comprised of a given nucleotide        
        Arguments:
            1. sequence, a string of a DNA sequence
            2. nucleotide, the nucleotide to count
        Returns:
            A decimal value representing the nucleotide content of the provided sequence.
    """
    
    n = 0.
    for nucleotide in sequence:
        if nucleotide == nuc:
            n += 1.
    
    at_content = at / len(sequence)
    
    return at_content