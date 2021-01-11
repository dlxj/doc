//
//  EmojiMemoryGame.swift
//  Memorize
//
//  https://www.bilibili.com/video/BV1EV411C77B?p=2
// 【完结｜中英字幕】2020 斯坦福（Stanford）Swift 语言教程 SwiftUI 开发 苹果公司 iOS编程 CS193p
//  p2.57:47
//

import SwiftUI

struct EmojiMemoryGame {
    private(set) var model:MemoryGame<String> = createMemoryGame()
    
    static func factoryCardContent(index:Int)->String {
        let emojis = ["👻","🎃"]
        return emojis[index]
    }
    
    static func createMemoryGame()->MemoryGame<String> {
        return MemoryGame<String>(numberOfPairsCards: 2, cardContentFactory: factoryCardContent)
    }
    
    var cards:Array<MemoryGame<String>.Card> {
        return model.cards
    }
    
    func choose(card:MemoryGame<String>.Card) {
        model.choose(card: card)
    }
}
