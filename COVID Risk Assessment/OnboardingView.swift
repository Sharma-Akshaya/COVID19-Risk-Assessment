//
//  OnboardingView.swift
//  COVID Risk Assessment
//
//  Created by Swapnil Jangam on 6/14/20.
//  Copyright © 2020 Swapnil Jangam. All rights reserved.
//

import SwiftUI

struct OnboardingView: View {
    @EnvironmentObject var viewRouter: ViewRouter
    
    var subViews = [
        UIHostingController(rootView: Subview(imageString: "earlyDiagnosisWearable")),
        UIHostingController(rootView: Subview(imageString: "vitalsAnalysis")),
        UIHostingController(rootView: Subview(imageString: "socialDistancing"))
    ]
    
    var titles = ["Early diagnosis", "Continuous Analysis", "Contact Tracing"]
    var caption = ["Early Diagnosis of COVID-19 using wearables which won’t affect day-to-day chores.", "Continuous analysis of the vitals gathered like Heart rate, sleep analysis, body weight to diagnose the disease in early stages and alerting the primary care physician.", "Contact tracing using GPS to detect exposure for 14 days after being in contact with possibly infected person while maintaining user privacy on both sides."]
    var attributing = ["Vector image designed by rawpixel.com / Freepik","Vector image designed by pikisuperstar / Freepik","Vector image designed by pch.vector / Freepik"]
    @State var currentPageIndex = 0
    
    var body: some View {
        VStack {
            PageViewController(currentPageIndex: $currentPageIndex, viewControllers: subViews).frame(height: 550)
            
            Text(titles[currentPageIndex])
                .font(.title)
            Text(caption[currentPageIndex])
                .font(.subheadline)
                .foregroundColor(.gray)
                .frame(width: 300, height: 100, alignment: .leading)
                .lineLimit(nil)
            Button(action: {
                if self.currentPageIndex + 1 == self.subViews.count {
                    self.viewRouter.currentPage = "contentView"
                } else {
                    self.currentPageIndex += 1
                }
            }){
                ButtonContent()
            }
            Text(attributing[currentPageIndex])
            .font(.subheadline)
            .foregroundColor(.gray)
            .frame(width: 300, height: 40, alignment: .center)
            .lineLimit(nil)
        }
    }
}

struct OnboardingView_Previews: PreviewProvider {
    static var previews: some View {
        OnboardingView().environmentObject(ViewRouter())
    }
}

struct ButtonContent: View {
    var body: some View {
        
        Image(systemName: "arrow.right")
            .resizable()
            .foregroundColor(.white)
            .frame(width:30, height: 30)
            .padding()
            .background(Color.black)
            .cornerRadius(30)
    }
}
