"""
Insurance Claims Analytics Platform
Advanced analytics for insurance claims processing and fraud detection
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from typing import Dict, List, Optional
import uuid

class InsuranceClaimsAnalyzer:
    """Analytics platform for insurance claims processing"""
    
    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        random.seed(seed)
        
        self.claim_types = ['Auto', 'Home', 'Health', 'Life', 'Travel', 'Business']
        self.claim_statuses = ['Submitted', 'Under Review', 'Approved', 'Denied', 'Paid']
        self.fraud_indicators = [
            'unusual_amount', 'multiple_claims', 'suspicious_timing',
            'inconsistent_story', 'previous_fraud', 'high_risk_area'
        ]
    
    def generate_claims_data(self, num_claims: int = 5000) -> pd.DataFrame:
        """Generate insurance claims data"""
        claims = []
        
        for i in range(num_claims):
            claim_type = np.random.choice(self.claim_types)
            
            # Amount based on claim type
            if claim_type == 'Auto':
                amount = np.random.lognormal(8, 1.2)
            elif claim_type == 'Home':
                amount = np.random.lognormal(9, 1.5)
            elif claim_type == 'Health':
                amount = np.random.lognormal(7, 1)
            elif claim_type == 'Life':
                amount = np.random.lognormal(11, 1.8)
            else:
                amount = np.random.lognormal(6, 1)
            
            # Fraud probability based on amount and type
            fraud_prob = min(0.15, amount / 100000 * 0.1)
            is_fraud = np.random.random() < fraud_prob
            
            claim = {
                'claim_id': f'CLM_{i+1:06d}',
                'policy_id': f'POL_{np.random.randint(1, 10000):06d}',
                'claim_type': claim_type,
                'amount': round(amount, 2),
                'claim_date': datetime.now() - timedelta(days=np.random.randint(0, 365)),
                'status': np.random.choice(self.claim_statuses),
                'is_fraud': is_fraud,
                'processing_days': np.random.randint(1, 60),
                'adjuster_id': f'ADJ_{np.random.randint(1, 100):03d}'
            }
            
            claims.append(claim)
        
        return pd.DataFrame(claims)
    
    def analyze_fraud_patterns(self, claims_df: pd.DataFrame) -> Dict:
        """Analyze fraud patterns in claims data"""
        fraud_analysis = {
            'total_claims': len(claims_df),
            'fraud_claims': len(claims_df[claims_df['is_fraud']]),
            'fraud_rate': claims_df['is_fraud'].mean(),
            'fraud_amount': claims_df[claims_df['is_fraud']]['amount'].sum(),
            'avg_fraud_amount': claims_df[claims_df['is_fraud']]['amount'].mean()
        }
        
        return fraud_analysis

if __name__ == "__main__":
    analyzer = InsuranceClaimsAnalyzer()
    claims_data = analyzer.generate_claims_data(2000)
    
    import os
    os.makedirs('../data', exist_ok=True)
    claims_data.to_csv('../data/insurance_claims.csv', index=False)
    
    print(f"Generated {len(claims_data)} insurance claims records")

