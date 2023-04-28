from s23p import Works
import argparse
def main():
    def get_output(url, output_format):
        w = Works(url)
        if output_format == 'bib':
            return w.bib()
        elif output_format == 'ris':
            return print(w.ris)
        else:
            raise ValueError('bib or ris')
    parser = argparse.ArgumentParser(description='Get bib or ris for DOI')
    parser.add_argument('url', type=str, help='DOI')
    parser.add_argument('-f', '--format', type=str, choices=['bib', 'ris'], default='bib', help='format (default: bib)')
    args = parser.parse_args()
    output = get_output(args.url, args.format)


