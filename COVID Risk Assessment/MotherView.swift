//
//  MotherView.swift
//  COVID Risk Assessment
//
//  Created by Swapnil Jangam on 6/14/20.
//  Copyright © 2020 Swapnil Jangam. All rights reserved.
//

import SwiftUI

struct MotherView: View {
    @EnvironmentObject var viewRouter: ViewRouter
    var body: some View {
        VStack{
            if viewRouter.currentPage == "onboardingView" {
                OnboardingView()
            } else if viewRouter.currentPage == "contentView" {
                ContentView()
            } else if viewRouter.currentPage == "consentPage" {
                ConsentPage()
            } else if viewRouter.currentPage == "questionnairePage" {
                QuestionnairePage()
            }
        }
    }
}

struct MotherView_Previews: PreviewProvider {
    static var previews: some View {
        MotherView().environmentObject(ViewRouter())
    }
}
