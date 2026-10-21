#!/usr/bin/env python

from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqPart.dnaconvert import *

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    #gcContent
    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")

    #countBases
    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    #RNA
    transc_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transc_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transc_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    #protein
    transl_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    transl_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transl_command.add_argument("-r", "--revcomp", action="store_true", help="Convert DNA to reverse-complementary")

    #enzTargetsScan
    enz_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme sites')
    enz_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    enz_command.add_argument("-e", "--enz", type=str, default=None, help="Provide enzyme name")
    enz_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    return parser

def main():
    parser = argparserLocal()
    args = parser.parse_args()

    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent', '-h']))
        print("Input", args.seq, "\nGC content =", gcContent(seq))

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases', '-h']))
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input", args.seq, "\ncountBases =", countBasesDict(seq))

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription', '-h']))
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input", args.seq, "\nTranscription =", dna2rna(seq))

    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation', '-h']))
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input", args.seq, "\nTranslation =", dna2protein(seq))

    elif args.command == 'enzTargetsScan':
        if args.seq == None or args.enz == None:
            exit(parser.parse_args(['enzTargetsScan', '-h']))
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input", args.seq, f"\n{args.enz} sites =", enzTargetsScan(seq, args.enz))

if __name__ == "__main__":
    main()