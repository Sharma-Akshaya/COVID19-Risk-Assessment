//
//  ViewRouter.swift
//  COVID Risk Assessment
//
//  Created by Swapnil Jangam on 6/14/20.
//  Copyright © 2020 Swapnil Jangam. All rights reserved.
//

import Foundation
import SwiftUI

class ViewRouter: ObservableObject {
    @Published var currentPage: String 
    init() {
        if !UserDefaults.standard.bool(forKey: "didLaunchBefore") {
            UserDefaults.standard.set(true, forKey: "didLaunchBefore")
            currentPage = "onboardingView"
        } else {
            currentPage = "contentView"
        }
    }
}
