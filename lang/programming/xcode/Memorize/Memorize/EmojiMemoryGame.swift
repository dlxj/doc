//
//  EmojiMemoryGame.swift
//  Memorize
//
//  https://www.bilibili.com/video/BV1EV411C77B?p=2
// 【完结｜中英字幕】2020 斯坦福（Stanford）Swift 语言教程 SwiftUI 开发 苹果公司 iOS编程 CS193p
//  p2.57:47
//

import SwiftUI

class EmojiMemoryGame :ObservableObject {
    @Published private(set) var model:MemoryGame<String> = createMemoryGame() // @Published 会在每次数据改变时都发通知
    
    static func createMemoryGame()->MemoryGame<String> {
        let emojis = ["👻","🎃", "🕷"]
        return MemoryGame<String>(numberOfPairsCards: emojis.count,
                                  cardContentFactory: {
                                    (index:Int)->String in return emojis[index]
                                  }
        )
    }
    
    var cards:Array<MemoryGame<String>.Card> {
        return model.cards
    }
    
    func choose(card:MemoryGame<String>.Card) {
        model.choose(card: card)
    }
}

