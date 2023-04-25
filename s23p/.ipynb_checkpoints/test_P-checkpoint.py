'''test'''
from s23p import Works
tst = 'https://doi.org/10.1021/acscatal.5b00538'
ww='John'
def testt():
    w = Works('https://doi.org/10.1021/acscatal.5b00538')
    w_repr = w.__repr__()
    citation_info = w_repr.split('cited by: ')[0].split()[0]
    
    assert citation_info == 'John'