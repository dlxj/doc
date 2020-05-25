//
//  ContentView.swift
//  Todolist
//
//  Created by vvw on 2020/5/13.
//  Copyright © 2020 vvw. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Hello, World!")
            Button(action:{
                
            }){
                Text("屠龙宝刀点击就送！")
                .padding() // 文本外围胖一圈
                    .background(Color.blue)
                    .foregroundColor(.white)
            }
            .cornerRadius(10) // 按钮加圆角效果
            .shadow(radius: 10) // 按钮加外围阴影
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
