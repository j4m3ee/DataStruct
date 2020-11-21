'''
สร้างฟังก์ชันที่นำชุดข้อมูล(list)ของ football clubs ที่มีคุณสมบัติดังนี้ name, wins, loss, draws, scored, conceded 
และทำการ return list ของ team name โดยเรียงลำดับทีมที่มีคะแนน(total point)มากที่สุด โดยถ้าหากมีทีมที่คะแนนเท่ากัน 
ให้นำผลต่างของจำนวนประตูที่ทำได้(scored)กับจำนวนประตูที่เสีย(conceded) มาคิด

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

[ชนะได้ 3 คะแนน, เสมอได้ 1 คะแนน, แพ้ได้ 0 คะแนน]

code by : qiral
'''
def plScore(data):
    table = []
    for team in data:
        tmp = []
        team = team.split(',')
        point = int(team[1]) * 3 + int(team[3])
        gd = int(team[4]) - int(team[5])
        tmp += [team[0], point, gd]
        table.append(tmp)

    for i in range(1, len(table)):
        tmp = table[i]

        for k in range(i, -1, -1):
            if tmp[1] > table[k - 1][1] and k > 0:
                table[k] = table[k - 1]
            elif tmp[1] == table[k - 1][1] and k > 0:
                if tmp[2] > table[k - 1][2]:
                    table[k] = table[k - 1]
                else:
                    table[k] = tmp
                    break
            else:
                table[k] = tmp
                break
    return table

if __name__ == "__main__":
    inp = input('Enter Input : ').split('/')

    scr = plScore(inp)
    print('== results ==')
    for inf in scr:
        print(f"['{inf[0]}', " + "{'points': " + f"{inf[1]}" + "}, {" + f"'gd': {inf[2]}" + "}]")