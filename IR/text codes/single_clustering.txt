import os
import math

def findDistancebetweenPoints(c1, c2):
        minimum = 1000 
        for i in c1:
                for j in c2:
                      dist =  float ( math.sqrt( pow((p[i-1][0]-p[j-1][0]), 2) + pow((p[i-1][1]-p[j-1][1]), 2) ) )
                      if minimum > dist:
                              minimum = dist
        return round(minimum,4)

def min_of_2D_array (dist):
        a = 0
        b = 0
        minimum = 100.0
        for i in range (len(dist)) :
                for j in range (i) :
                        if (dist[i][j] < minimum) :
                                minimum = dist[i][j]
                                a=i
                                b=j
        return [a,b]
        
        
p = []
p.append([0.40,0.53])
p.append([0.22,0.38])
p.append([0.35,0.32])
p.append([0.26,0.19])
p.append([0.08,0.41])
p.append([0.45,0.30])
''' p.append([0.19,0.40])
p.append([0.50,0.14])
p.append([0.30,0.25])
p.append([0.05,0.60]) '''
 
cluster = [[1],[2],[3],[4],[5],[6]]

while (len(cluster)>3):
        i =0
        dist = []

        for i in range(len(cluster)) :
                dist.append([])
                for j in range (0,i+1) :
                        if (i==j) :
                                dist[i].append(0)
                        else :
                                dist[i].append(findDistancebetweenPoints(cluster[i],cluster[j]))

        for i in range(len(cluster)) :
                print dist[i]

        closest_point = min_of_2D_array (dist)
#        print closest_point
        new_cluster = cluster[closest_point[0]] + cluster[closest_point[1]]
        cluster.append(new_cluster)
        print "New Cluster : ",new_cluster
#       new_point = centroid (p, new_cluster)
        cluster.remove(cluster[closest_point[0]])       
        cluster.remove(cluster[closest_point[1]])       
        print cluster   

        print "Iteration completed\n"     
                                


