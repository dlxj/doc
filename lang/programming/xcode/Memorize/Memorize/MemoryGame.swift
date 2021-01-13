//
//  MemoryGame.swift
//  Memorize
//
//  Created by v on 1/9/21.
//  Copyright © 2021 v. All rights reserved.
//

import Foundation

struct MemoryGame<CardContent> {
    var cards:Array<Card>
    
    func choose(card:Card) {
        print("card choose:\(card)")
    }
    
    init(numberOfPairsCards:Int, cardContentFactory:(Int)->CardContent) {
        cards = Array<Card>()
        
        for pairIndex in 0..<numberOfPairsCards {
            let content = cardContentFactory(pairIndex)
            cards.append(Card(content: content, id:pairIndex*2))
            cards.append(Card(content: content, id:pairIndex*2+1))
        }
    }
    
    struct Card:Identifiable {
        var isFaceUp: Bool = false
        var isMatch: Bool = false
        var content: CardContent
        var id:Int
    }
}
