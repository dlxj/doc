//
//  ContentView.swift
//  Memorize
//
//  Created by v on 12/30/20.
//  Copyright © 2020 v. All rights reserved.
//

import SwiftUI

struct EmojiGameView: View {
    
    var model = EmojiMemoryGame()

    
    var body: some View {
        HStack(){
            ForEach(model.cards) { card in
                ZStack(content: {
                    RoundedRectangle(cornerRadius: 10.0).fill(Color.white)
                    RoundedRectangle(cornerRadius: 10.0).stroke(lineWidth: 3)
                    Text(card.content).font(.largeTitle)
                }).onTapGesture {
                    self.model.choose(card: card)
                }
            }
            
        }.padding().foregroundColor(Color.orange)
            .font(.largeTitle)
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        EmojiGameView()
    }
}
