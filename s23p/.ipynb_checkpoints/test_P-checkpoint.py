import os
import pytest
from s23p import Works

tst='''
@article{Kitchin2015,
 author = {['John R. Kitchin']},
 journal = {ACS Catalysis},
 pages = {3894-3899},
 title = {Examples of Effective Data Sharing in Scientific Publishing},
 volume = {5},
 year =	 {2015}
}'''
# bs = '''
# @article{kitchin-2018-machin-learn-catal,
#   author =	 {John R. Kitchin},
#   title =	 {Machine Learning in Catalysis},
#   journal =	 {Nature Catalysis},
#   volume =	 1,
#   number =	 4,
#   pages =	 {230-232},
#   year =	 2018,
#   doi =		 {10.1038/s41929-018-0056-y},
#   url =		 {https://doi.org/10.1038/s41929-018-0056-y},
#   DATE_ADDED =	 {Sun Mar 3 16:40:42 2019},
# }
# @article{kitchin-2015-examp-effec,
#   author =	 {John R. Kitchin},
#   title =	 {Examples of Effective Data Sharing in Scientific Publishing},
#   journal =	 {ACS Catalysis},
#   volume =	 5,
#   number =	 6,
#   pages =	 {3894-3899},
#   year =	 2015,
#   doi =		 {10.1021/acscatal.5b00538},
#   url =		 {https://doi.org/10.1021/acscatal.5b00538},
#   DATE_ADDED =	 {Fri Jan 18 09:54:51 2019},
# }'''

@pytest.fixture()
def setup():
    with open('test.bib', 'w') as f:
        f.write(tst)
    yield "setup"
    os.unlink('test.bib')
    
class TestSort:
    def test_sort(self, setup):
        entries = Works('test.bib')
        assert ['year'] == ['2015']    
        
# @pytest.fixture()
# def setup():
#     with open('test.bib', 'w') as f:
#         f.write(bs)
#     yield "setup"
#     os.unlink('test.bib')
    
# class TestSort:
#     def test_sort(self, setup):
#         entries = sort_bibtex('test.bib')
#         assert [e['year'] for e in entries] == ['2015', '2018']    

