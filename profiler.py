#!/usr/bin/env python
import argparse


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        description='Author Profiler for PAN 2016')
    argparser.add_argument('-l', '--log-level', dest='log_level', type=str, default='INFO',
                           help='Set log level (DEBUG, INFO, ERROR)')

    argparser.add_argument('-i', '--input', dest='tira_input', type=str, required=True,
                           help='Path to the corpus for which the gender and age of the authors have to be predicted')

    argparser.add_argument('-r', '--RUN', dest='input_run', type=str, required=False,
                           help='Input run')

    argparser.add_argument('-o', '--output', dest='tira_output', type=str, required=True,
                           help='Output directory')

    args = argparser.parse_args()
    LOGFMT = '%(asctime)s %(name)s %(levelname)s %(message)s'
    logging.basicConfig(level=getattr(logging, args.log_level), format=LOGFMT)
    print(tira_input)
    print(inptu_run)
    print(tira_output)