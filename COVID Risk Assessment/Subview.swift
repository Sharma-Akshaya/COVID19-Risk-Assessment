//
//  Subview.swift
//  COVID Risk Assessment
//
//  Created by Swapnil Jangam on 6/14/20.
//  Copyright © 2020 Swapnil Jangam. All rights reserved.
//

import SwiftUI

struct Subview: View {
    var imageString: String
    
    var body: some View {
        Image(imageString).resizable().aspectRatio(contentMode: .fill).clipped().shadow(color: Color.gray, radius: 50, x: 50, y: 50)
    }
}

struct Subview_Previews: PreviewProvider {
    static var previews: some View {
        Subview(imageString: "earlyDiagnosisWearable")
    }
}
