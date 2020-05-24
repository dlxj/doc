//
//  TodoItem.swift
//  Todolist
//
//  Created by vvw on 2020/5/24.
//  Copyright © 2020 vvw. All rights reserved.
//

import SwiftUI

class Todo:NSObject, NSCoding, Identifiable {
    func encode(with coder: NSCoder) {
        UIApplication.shared.keyWindow?.endEditing(true)
        TextField()
    }
    
    required init?(coder: NSCoder) {
        
    }
    
    
}
