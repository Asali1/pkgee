"""test"""
from s23p import Works


def testt():
    """
    to test
    """
    output = Works("https://doi.org/10.1021/acscatal.5b00538")
    w_repr = repr(output)
    citation_info = w_repr.split("cited by: ")[0].split()[0]

    assert citation_info == "John"
