from graph import Graph, graph_from_file


data_path = "input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(g)

ts= [1,2,3,4,5]
dic= {i : True for i in ts}
print(dic)

print (g.nodes)

dic[3]=False

for i in [1,2,3,4,5] :
    if dic[i]== True : 
        print("ca marche")
