#!/usr/bin/env python
from __future__ import print_function
import sys
def reorder_dp (input_file, outfile):
    prog_name = "dp_reorderer"
    feature1 = "proximal_peak"
    feature2 = "distal_peak"
    dot = "."
    with open(outfile, 'w') as out_f:
        with open(input_file) as f:
            counter = 0
            for line in f:
                if counter != 0:
                    split_line = line.strip().split("\t")
                    chromosome = split_line[3].split(":")[0]
                    proximal_start = int(split_line[2])-2
                    proximal_end = int(split_line[2])+2
                    strand = split_line[0].split("|")[3]
                    if split_line[18] == "NA":
                        score = 0
                    else:
                        score = (1- float(split_line[18]))*500
                    split1 = split_line[3].split("-")
                    if strand == "-":
                         distal_peak = int(split1[0].split(":")[1])
                    else:
                        distal_peak = int(split1[1])
                    distal_end = distal_peak + 2
                    distal_start = distal_peak -2


                    info = "adjusted.P_val="+ split_line[20]+ ";" + "Pass_Filter=" + split_line[21]
                    prox_line = chromosome +"\t" +prog_name +"\t"+ feature1 + "\t"+ str(proximal_start)+ "\t"+ str(proximal_end)+ "\t"+str(score)+"\t"+strand+"\t"+ dot+"\t"+ info+"\n"
                    dist_line = chromosome +"\t" +prog_name +"\t"+ feature2 + "\t"+ str(distal_start)+ "\t"+ str(distal_end)+ "\t"+str(score)+"\t"+strand+"\t"+ dot+"\t"+ info+"\n"

                    out_f.write(prox_line)
                    out_f.write(dist_line)
                counter+=1

if __name__ == "__main__":

    in_file = sys.argv[1]

    out_fie= sys.argv[2]

    reorder_dp (in_file,out_fie )