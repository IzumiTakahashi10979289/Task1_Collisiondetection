own_position= list(map(int, input("＊自機の値入力＊左上X座標 左上Y座標 高さ 幅を半角スペース区切りで入力してください").split()))
print(own_position)
print("\n左上X座標：",own_position[0],"\n左上Y座標：",own_position[1],"\n高さ：",own_position[2],"\n幅：",own_position[3])

enemy_num = input("＊敵の数入力＊")
enemy_num = int(enemy_num)
print("\n敵の数：",enemy_num)

enemy_position = [list(map(int, input("＊敵機の値入力＊左上X座標 左上Y座標 高さ 幅＊").split())) for i in range(enemy_num)]
print(enemy_position)


ox = own_position[0]
oy = own_position[1]
oh = own_position[2]
ow = own_position[3]

for i in range(enemy_num):
      ex = enemy_position[i][0]
      ey = enemy_position[i][1]
      eh = enemy_position[i][2]
      ew = enemy_position[i][3]
      if ox+ow >= ex and ox<=ex+ew:
            print("敵機",i+1,"がアタリ")
            continue
            if  oy+oh >= ey and ey <= ey+ew:
                  print("敵機",i+1,"がアタリ")

print("やったぜ。")
