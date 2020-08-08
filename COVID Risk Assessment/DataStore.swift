//
//  DataStore.swift
//  COVID Risk Assessment
//
//  Created by Swapnil Jangam on 6/14/20.
//  Copyright © 2020 Swapnil Jangam. All rights reserved.
//

import Foundation
import HealthKit
public class DataStore {
    
    // MARK: - Properties
    
    private static var sharedDataStore: DataStore = {
        let dataStore = DataStore(healthStore: HKHealthStore())
        
        // Configuration
        // ...
        
        return dataStore
    }()
    
    // MARK: -
    
    let healthStore: HKHealthStore
    
    // Initialization
    
    private init(healthStore: HKHealthStore) {
        self.healthStore = healthStore
    }
    
    
    
    // MARK: - Accessors
    
    class func shared() -> DataStore {
        return sharedDataStore
    }
    
}
