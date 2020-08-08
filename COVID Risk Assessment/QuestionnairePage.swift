//
//  QuestionnairePage.swift
//  COVID Risk Assessment
//
//  Created by Swapnil Jangam on 6/14/20.
//  Copyright © 2020 Swapnil Jangam. All rights reserved.
//
import Combine
import SwiftUI

enum Symptoms: Int, CaseIterable, Identifiable {
    case fever = 0
    case cough
    case shortnessOfBreath
    case lossOfAppettiteOrSmell
    case chills
    case repeatedShakingWithChills
    case musclePain
    case chestPain
    case headache
    case soreThroat
    case congestedRunnyNose
    case vomitingOrDiarrhea
    case rashes
    case none
    
    var id: Symptoms {
        self
    }
    
    var literal: String {
        switch self {
        case .fever: return "Fever"
        case .cough: return "Cough"
        case .shortnessOfBreath: return "Shortness of breath"
        case .lossOfAppettiteOrSmell: return "Loss of appetite or smell"
        case .chills: return "Chills"
        case .repeatedShakingWithChills: return "Repeated Shaking with chills"
        case .musclePain: return "Muscle pain"
        case .chestPain: return "Chest Pain"
        case .headache: return "Headache"
        case .soreThroat: return "Sore Throat"
        case .congestedRunnyNose: return "Congested / Runny Nose"
        case .vomitingOrDiarrhea: return "Vomiting / Diarrhea"
        case .rashes: return "Rashes"
        case .none: return "None"
            
        }
    }
}

class SymptomsExperienced: ObservableObject {
    @Published var symptoms = [Symptoms]()
    
}

struct QuestionnairePage: View {
    @State private var showSymptomSheet = false
    
    @State private var highRiskTravel = "No"
    
    @State private var infectedContact = "No"
    
    @State private var bpHeartLungKidney = "No"
    
    @State private var hivCancer = "No"
    
    @ObservedObject var symptomsExperienced = SymptomsExperienced()
    
    var body: some View {
        NavigationView {
            VStack {
                Form {
                    Section(header: Text("Self Assessment").font(.caption)) {
                        Button(action: {
                            self.showSymptomSheet.toggle()
                        }) {
                            HStack {
                                Text("Symptoms").foregroundColor(Color.black)
                                Spacer()
                                Text("\(symptomsExperienced.symptoms.count)")
                                    .foregroundColor(Color(UIColor.systemGray))
                                    .font(.body)
                                Image(systemName: "chevron.right")
                                    .foregroundColor(Color(UIColor.systemGray4))
                                    .font(Font.body.weight(.medium))
                                
                            }
                        }
                        .sheet(isPresented: $showSymptomSheet) {
                            SettingsLanguagePickerView(self.symptomsExperienced)
                        }
                        
                        Picker(selection: $highRiskTravel, label: Text("High Risk area travel?")) {
                            Text("Yes")
                            Text("No")
                        }
                        Picker(selection: $infectedContact, label: Text("Contact with someone infected?")) {
                            Text("Yes")
                            Text("No")
                            Text("Maybe")
                        }
                        Picker(selection: $bpHeartLungKidney, label: Text("High BP, heart, lung or kidney disease?")) {
                            Text("Yes")
                            Text("No")
                        }
                        
                        Picker(selection: $hivCancer, label: Text("HIV or Cancer")) {
                            Text("Yes")
                            Text("No")
                        }
                        
                        Button(action: {
                            func getPoints(sympt: Symptoms) -> NSInteger {
                                if self.symptomsExperienced.symptoms.contains(where: { item in
                                    if case sympt = item {
                                        return true
                                    }
                                    return false
                                }) {
                                    return 8
                                } else {
                                    return 0
                                }
                                
                            }
                            func getOtherPoints(mypoint: String) -> Bool {
                                if !mypoint.isEmpty {
                                    return true
                                } else {
                                    return false
                                }
                            }
                            
                            
                            
                                
                            do {
                            var jsonObject: [String: Any]  = [
                                "userid": "SJ12467",
                                "firstname":"John",
                                "lastname":"Doe",
                                "dob": try DataStore.shared().healthStore.dateOfBirthComponents(),
                                "gender": try DataStore.shared().healthStore.biologicalSex(),
                                "bloodtype":try DataStore.shared().healthStore.bloodType(),
                                "lung_issues": getOtherPoints(mypoint: self.bpHeartLungKidney),
                                "hypertension":"False",
                                "heartdisease": getOtherPoints(mypoint: self.bpHeartLungKidney),
                                "hiv":getOtherPoints(mypoint: self.hivCancer),
                                "diabetes":"False",
                                "cancer":"False",
                                "Age": 25,
                                "fever": 98.2,
                                "drycough":7,
                                "fatigue":0,
                                "trouble_breathing":8,
                                "muscle_pain":5,
                                "sore_throat":0,
                                "heart_rate":[
                                    "heartrate": 100, "timestamp": "2019-08-24 22:05:09",
                                    "heartrate": 100, "timestamp": "2019-08-24 22:05:09",
                                    "heartrate": 100, "timestamp": "2019-08-24 22:05:09",
                                    "heartrate": 100, "timestamp": "2019-08-24 22:05:09"],
                                "headache": getPoints(sympt: Symptoms.headache),
                                "runnynose": getPoints(sympt: Symptoms.congestedRunnyNose),
                                "diarrhea": getPoints(sympt: Symptoms.vomitingOrDiarrhea),
                                "zipcode":76204,
                                "latitude":-6.7594317,
                                "longitude":111.4484559
                            ]
                            } catch {
                            }
                        }
                            ){
                            Text("Get report")
                                .font(.headline)
                                .foregroundColor(.white)
                                .padding()
                                .frame(width: 220, height: 60)
                                .background(Color.black)
                                .cornerRadius(35.0)
                        }.padding(.all, 50)
                        }
                    }
                }
            }
            .navigationBarTitle("Content")
    }
}

struct SettingsLanguagePickerView: View {
    @State private var selections = [Symptoms]()
    
    @ObservedObject var preferedLanguages: SymptomsExperienced
    
    init(_ preferedLanguages: SymptomsExperienced) {
        self.preferedLanguages = preferedLanguages
    }
    
    @Environment(\.presentationMode) var presentationMode
    
    var body: some View {
        NavigationView {
            List {
                Section(header: Text("Choose prefered languages")) {
                    ForEach(Symptoms.allCases) { item in
                        MultipleSelectionRow(title: item.literal, isSelected: self.selections.contains(item)) {
                            if self.selections.contains(item) {
                                self.selections.removeAll(where: { $0 == item })
                            }
                            else {
                                self.selections.append(item)
                            }
                        }
                    }
                    
                }
            }
            .onAppear(perform: { self.selections = self.preferedLanguages.symptoms })
            .listStyle(GroupedListStyle())
            .navigationBarTitle("Languages", displayMode: .inline)
            .navigationBarItems(trailing:
                Button(action: {
                    self.preferedLanguages.symptoms = self.selections
                    self.presentationMode.wrappedValue.dismiss()
                }) {
                    Text("OK")
                }
            )
        }
    }
}

struct MultipleSelectionRow: View {
    var title: String
    var isSelected: Bool
    var action: () -> Void
    
    var body: some View {
        Button(action: self.action) {
            HStack {
                Text(self.title)
                if self.isSelected {
                    Spacer()
                    Image(systemName: "checkmark").foregroundColor(.blue)
                }
            }
        }.foregroundColor(Color.black)
    }
}

