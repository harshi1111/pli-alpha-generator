"""Unit tests for PLI Alpha Generator"""

import sys
import pytest
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from dynamic_pli_analyzer import (
    analyze_expert_validated_asymmetry,
    EXPERT_INSIGHTS
)

def test_asymmetry_scoring():
    """Test that asymmetry scoring works"""
    
    # Mock company data
    companies = [{
        'symbol': 'TEST',
        'name': 'Test Company',
        'current_price': 100,
        'fifty_two_week_low': 95,
        'fifty_two_week_high': 150,
        'three_month_change': -10,
        'stealth_rank': 1,
        'mf_percentage': 5.0,
        'debt_to_equity': 0.1
    }]
    
    result = analyze_expert_validated_asymmetry(companies)
    assert result['top_company'] is not None
    assert result['top_company']['symbol'] == 'TEST'

def test_expert_insights_loaded():
    """Test that expert insights are properly loaded"""
    
    assert 'strategic_winners' in EXPERT_INSIGHTS
    assert 'DIXON' in EXPERT_INSIGHTS['strategic_winners']
    assert EXPERT_INSIGHTS['strategic_winners']['DIXON']['catalyst'] is not None

def test_buy_trigger_calculation():
    """Test buy trigger calculation"""
    
    from dynamic_pli_analyzer import calculate_buy_trigger
    
    company = {
        'symbol': 'TEST',
        'current_price': 100,
        'fifty_two_week_low': 90,
        'fifty_two_week_high': 150
    }
    
    result = calculate_buy_trigger(company)
    assert result['buy_trigger'] > company['fifty_two_week_low']
    assert result['target'] == company['fifty_two_week_high']

if __name__ == "__main__":
    pytest.main([__file__])