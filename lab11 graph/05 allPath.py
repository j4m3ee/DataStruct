'''
ให้น้องสร้างกราฟจาก input ที่รับเข้าไป  จากนั้นให้ทำการหาเส้นทางที่เป็นไปได้ทั้งหมดที่สามารถไปยังโหนดปลายทางได้ ถ้าหาก node ไหนเคยผ่านแล้วจะไม่สามารถผ่านได้อีก  
โดยการแสดงผลลัพธ์ให้เรียงลำดับจากน้อยไปมาก ถ้าหากไม่สามารถไปยังปลายทางได้ให้แสดงว่า (source)  can't go to (destination)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง การสร้างเส้นทางระหว่าง node a และ node b เช่น 1 2,3 4 หมายความว่า node 1 จะเชื่อมกับ node 2 และ node 3 จะเชื่อมกับ node 4
    -   ด้านขวาหมายถึง ให้หาว่าเส้นทางจากต้นทางไปยังปลายทาง เช่น 1 6 คือให้หาเส้นทางที่เป็นไปได้ทั้งหมดจาก node 1 ไปยัง node 6

อธิบาย Test Case #1

เส้นทางจาก node 1 ไปยัง node 3 มี 3 เส้นทางได้แก่ 1->2->3  ,  1->5->3  ,  1->5->4->3  จากการแสดงผลจะเห็นได้ว่า 1->2->3 แสดงก่อน 1->5->3  
เนื่องจาก 2 มีค่าน้อยกว่า 5  จึงแสดงผล 1->2->3 ก่อน 1->5->3
'''

def possiblePath(graph,start,stop,path,allPath):
    if start == stop:
        for index, data in enumerate(allPath):
            if len(path) < len(data):
                allPath.insert(index, path)
                return
        allPath.append(path)
        return

    for i in graph.get(start,[]):
        if i not in path:
            possiblePath(graph,i,stop,path + [i],allPath)

if __name__ == "__main__":
    inp,path = input('Enter Input : ').split('/')

    graph,allPath = {},[]
    for i in inp.split(','):
        i = list(map(int,i.split()))
        graph[i[0]] = graph.get(i[0],[]) + [i[1]]
        graph[i[1]] = graph.get(i[1],[]) + [i[0]]
        
    src,dest = map(int,path.split())
    possiblePath(graph,src,dest,[src],allPath)

    if allPath == []:
        print('{} can\'t go to {}'.format(src,dest))
    else:
        print('All possible path from {} to {} :'.format(src,dest))
        for data in allPath:
            print(' -> '.join(str(a) for a in data))

'''
Enter Input : 1 2,1 4,1 5,2 3,2 4,3 5,4 5,4 6/1 6
All possible path from 1 to 6 :
1 -> 4 -> 6
1 -> 2 -> 4 -> 6
1 -> 5 -> 4 -> 6
1 -> 2 -> 3 -> 5 -> 4 -> 6
1 -> 5 -> 3 -> 2 -> 4 -> 6
'''