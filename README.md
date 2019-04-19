変数を分かりやすくしたいのでそれぞれ代入していく(ownのoとx座標でoxみたいな)

    ox = own_position[0]
    oy = own_position[1]
    oh = own_position[2]
    ow = own_position[3]


敵機数回ループ、変数を分かりやすくしたいので同時に代入する。

    for i in range(enemy_num):
      ex = enemy_position[i][0]
      ey = enemy_position[i][1]
      eh = enemy_position[i][2]
      ew = enemy_position[i][3]
      
判定部分、x軸に注目してまずx軸の判定を行っていく。
      
      if ox+ow >= ex and ox<=ex+ew:
         
自機の角が敵機の角よりも大きければ重なっていることになるのでアタリになる        
Y軸に関してもおなじ
      
       print("敵機",i+1,"がアタリ")
       continue 
ここでcoutinueすればおんなじ結果が二回出ることはない
            
            
       if  oy+oh >= ey and ey <= ey+ew:
                print("敵機",i+1,"がアタリ")
               
               
正直、プログラミングよりGitの使い方のほうが難しくて困惑したん
                  
