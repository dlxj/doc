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
    
    struct Card {
        var isFaceUp: Bool
        var isMatch: Bool
        var conten: CardContent
        
    }
}
