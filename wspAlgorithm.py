#!/usr/bin/python2.7


import yaml
import random

def distance(point1, point2):
    dist = 0
    for (k1,v1),(k2,v2) in zip(point1.items(),point2.items()):
        dist += abs(v1-v2)
    return dist

def wsp(design_space,dmin):
    rmarray = list()
    processed = list()
    lowest = 0
    lowest_index = 0
    print len(processed)
    print len(design_space)-len(rmarray)
    while len(processed)<(len(design_space)-len(rmarray)) :
        initial = design_space[lowest_index]
        processed.append(lowest_index)
        for i in range(0,len(design_space)):
            if not(i in processed) and not (design_space[i] in rmarray):
                dist = distance(initial,design_space[i])
                if dist<dmin:
                    rmarray.append(design_space[i])
                else:
                    if lowest>dist:
                        lowest_index = i
    for i in rmarray:
        try:
            design_space.remove(i)
        except ValueError:
            print "Value not found", i

    print design_space
    print len(design_space)

def main():
    design_space = list()
    ref = open("conf.yaml", "r")
    sample = yaml.load(ref)
    for i in range(20):
        #print sample
        
        result = dict(sample)
        for k in sample:
            vrange = sample[k]
            start = int(vrange.split(",")[0])
            end = int(vrange.split(",")[1])
            result[k] = random.randint(start,end)
            #print k,result[k]
        #print result
        design_space.append(dict(result))
    print design_space

    wsp(design_space,6)

if __name__ == '__main__':
    main()