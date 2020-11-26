'''
รับ input เป็น list คู่อันดับ(เช่น A B,B C = A ไปหา B ได้ และ B ไปหา C ได้) ให้สร้าง Directed Graph จากนั้นให้แสดงผล adjacency metrix ของ graph 
'''

if __name__ == "__main__":
    inp = input('Enter : ').split(',')

    node,graph = [],{}
    for d in inp:
        d = d.split()

        for i in range(2):
            node += d[i] if d[i] not in node else []
        graph[d[0]] = graph.get(d[0],[]) + [d[1]]

    node.sort()

    print('    ' + '  '.join(node))

    for n in node:
        s = []
        for edge in node:
            s.append('1' if edge in graph.get(n,[]) else '0')

        print(f'{n} : ' + ', '.join(s))