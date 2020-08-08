//
//  ContentView.swift
//  COVID Risk Assessment
//
//  Created by Swapnil Jangam on 6/13/20.
//  Copyright © 2020 Swapnil Jangam. All rights reserved.
//

import SwiftUI

let lightGreyColor = Color(red: 239.0/255.0, green: 243.0/255.0, blue: 244.0/255.0)

struct ContentView: View {
    @State var username: String = ""
    @State var password: String = ""
    
    @State var authenticationDidFail: Bool = false
    var body: some View {
        VStack {
            HelloText()
            UserImage()
            UsernameTextField(username: $username)
            PasswordSecureField(password: $password)
            if authenticationDidFail {
                Text("Invalid credentials. Try again.")
                    .offset(y: -10)
                    .foregroundColor(.red)
            }
            Button(action: {
                print("Button tapped")
            }){
                LoginButtonContent()
            }
        }
        .padding()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

struct HelloText: View {
    var body: some View {
        Text("Welcome!")
            .font(.largeTitle)
            .fontWeight(.semibold)
            .padding(.bottom, 20)
    }
}

struct UserImage: View {
    var body: some View {
        Image("userImage").resizable().aspectRatio(contentMode: .fill)
            .frame(width: 100, height: 100)
            .cornerRadius(2)
            .padding(.bottom, 75)
    }
}

struct LoginButtonContent: View {
    var body: some View {
        Text("Login")
            .font(.headline)
            .foregroundColor(.white)
            .padding()
            .frame(width: 220, height: 60)
            .background(Color.black)
            .cornerRadius(35.0)
    }
}

struct UsernameTextField: View {
    
    @Binding var username: String
    
    var body: some View {
        TextField("Username", text: $username)
            .padding()
            .background(lightGreyColor)
            .cornerRadius(5.0)
            .padding(.bottom, 20)
    }
}

struct PasswordSecureField: View {
    @Binding var password: String
    var body: some View {
        SecureField("Password", text: $password)
            .padding()
            .background(lightGreyColor)
            .cornerRadius(5.0)
            .padding(.bottom, 20)
    }
}
