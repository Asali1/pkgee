from s23p import Works
import argparse

parser = argparse.ArgumentParser(description='Get bibliography or RIS format from a URL')
parser.add_argument('url', type=str, help='URL of the article')
parser.add_argument('-b', '--bib', action='store_true', help='output in bibliography format')
parser.add_argument('-r', '--ris', action='store_true', help='output in RIS format')
args = parser.parse_args()

works = Works(args.url)
if args.bib:
    print(works.bib)
elif args.ris:
    print(works.ris)
else:
    print('Please specify -b or -r for bibliography or RIS format, respectively.')
