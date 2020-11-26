'''
รับ input เป็น list คู่อันดับ เพื่อนำไปสร้าง Directed Graph แบบมี weight จากนั้นให้แสดงผล shortest path โดยใช้ Dijkstra’s Shortest Path Algorithm

เช่น A 3 B,B 1 C/A B,A C = สร้างกราฟที่ A ไปหา B ได้โดยมีweight=3 และ B ไปหา C ได้โดยมีweight=1 / แสดง shortest path จากA>BและA>C) 

'''

def shortestPath(graph,start,stop,path,dis,min):
    if start == stop and (min == None or (dis <= min[1] and len(path) <= len(min[0]))):
        min = [path,dis]
        return min

    for a in graph.get(start,[]):
        if a[0] not in path:
            tmp = shortestPath(graph, a[0], stop, path + [a[0]], dis + a[1], min)
            if tmp is not None:
                min = tmp
    return min

if __name__ == "__main__":
    inp,case = input('Enter : ').split('/')
    graph = {}
    for a in inp.split(','):
        a = a.split()
        graph[a[0]] = graph.get(a[0],[]) + [[a[2], int(a[1])]]

    for b in case.split(','):
        b = b.split()
        path = shortestPath(graph,b[0],b[1],[b[0]],0,None)
        if path is None:
            print(f'Not have path : {b[0]} to {b[1]}')
            continue
        print(f'{b[0]} to {b[1]} : ' + '->'.join(path[0]))
        
''' 
Enter : v0 1 v1,v1 1 v2,v2 1 v3,v0 1 v3/v0 v1,v0 v2,v0 v3
v0 to v1 : v0->v1
v0 to v2 : v0->v1->v2
v0 to v3 : v0->v3
'''