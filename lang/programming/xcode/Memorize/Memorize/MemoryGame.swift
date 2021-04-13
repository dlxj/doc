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
    
    mutating func choose(card:Card) {
        
        func index(card:Card)->Int{
            for i in 0..<cards.count {
                if cards[i].id == card.id {
                    return i
                }
            }
            return 0
        }
        
        let idx = index(card:card)
        cards[idx].isFaceUp = !cards[idx].isFaceUp
        
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
