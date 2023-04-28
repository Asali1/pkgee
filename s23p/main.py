"""
commandline utility
"""
import argparse
from s23p import Works
def main():
    '''
    main
    '''
    def get_output(url, output_format):
        w_doi = Works(url)
        if output_format == "bib":
            return w_doi.bib()
        elif output_format == "ris":
            print(w_doi.ris)
        else:
            raise ValueError("bib or ris")
    parser = argparse.ArgumentParser(description="Get bib or ris for DOI")
    parser.add_argument("url", type=str, help="DOI")
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["bib", "ris"],
        default="bib",
        help="format (default: bib)",
    )
    args = parser.parse_args()

