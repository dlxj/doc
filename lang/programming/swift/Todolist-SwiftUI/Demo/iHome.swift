//
//  iHome.swift
//  Demo
//
//  Adding a navigation bar
//  https://www.hackingwithswift.com/books/ios-swiftui/adding-a-navigation-bar
//

import SwiftUI


struct iHome: View {
    var body: some View {
        VStack {
            Section {
                Text("Hello World")
            }
        }
    }
}

#if DEBUG
struct iHome_Previews: PreviewProvider {
    static var previews: some View {
        iHome()
    }
}
#endif
