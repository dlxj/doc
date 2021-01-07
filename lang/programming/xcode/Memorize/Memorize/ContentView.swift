//
//  ContentView.swift
//  Memorize
//
//  Created by v on 12/30/20.
//  Copyright © 2020 v. All rights reserved.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        ZStack(content: {
            RoundedRectangle(cornerRadius: 10.0).fill(Color.white)
            RoundedRectangle(cornerRadius: 10.0).stroke(lineWidth: 3)
            Text("👻").font(.largeTitle)
        }).padding().foregroundColor(Color.orange)

    }
}

struct mainView: View {
    var body: some View {
        HStack(){
            ForEach(0..<4) { index in
                ZStack(content: {
                    RoundedRectangle(cornerRadius: 10.0).fill(Color.white)
                    RoundedRectangle(cornerRadius: 10.0).stroke(lineWidth: 3)
                    Text("👻").font(.largeTitle)
                })
            }
            
        }.padding().foregroundColor(Color.orange)
            .font(.largeTitle)
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
//        ContentView()
        mainView()
    }
}
