#!/usr/bin/env python3
"""
PROFESSIONAL PLI ALPHA GENERATOR v2.0
Now with Expert-Validated Risk Factors & Institutional Stealth Tracking
"""

import json
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
import sys
import yfinance as yf
from pathlib import Path

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

# ============================================================
# CONFIGURATION
# ============================================================

NEWS_API_KEY = "e1a3eb1a81d849449f2bff0d4f301fc7"
NEWS_API_URL = "https://newsapi.org/v2/everything"

# ============================================================
# EXPERT INSIGHTS FROM GEMINI ANALYSIS (Feb 23, 2026)
# ============================================================

EXPERT_INSIGHTS = {
    'strategic_winners': {
        'DIXON': {
            'reason': 'IT Hardware division scaling from ₹1,500 Cr to ₹4,000 Cr+',
            'catalyst': 'Display and camera module JVs for backward integration',
            'warning': 'Mobile PLI allocation slashed from ₹9,000 Cr to ₹1,527 Cr',
            'geopolitical_risk': '49% Chinese ownership in Kunshan Q Tech JV - vulnerable to Press Note 3'
        },
        'SYRMA': {
            'reason': 'Golden Trio: Telecom (5G/6G), Med-Tech, Automotive',
            'catalyst': '₹40,000 Cr component PLI boost, 45% sales growth',
            'warning': 'Debt-to-Equity 0.35 vs industry avg 0.12 - capital intensive',
            'stealth': 'MF holdings jumped 4% → 10% in one year'
        },
        'AMBER': {
            'reason': 'Pivoted from AC assembler to EMS powerhouse',
            'catalyst': 'PCB/PCBA manufacturing targeting $1B revenue',
            'warning': 'P/E 166 - extremely high expectations priced in',
            'risk': 'Highly sensitive to quarterly misses'
        }
    },
    'stealth_ranking': {
        1: {'symbol': 'SYRMA', 'name': 'Syrma SGS', 'score': 'High Alpha', 
            'detail': 'MF holdings 4%→10%, retail cautious'},
        2: {'symbol': 'TCIEXP', 'name': 'TCI Express', 'score': 'Quiet Accumulation',
            'detail': 'B2B logistics proxy, under-the-radar buying'},
        3: {'symbol': 'BLUEDART', 'name': 'Blue Dart', 'score': 'Moderate',
            'detail': 'Stealth phase ending, hitting social media'},
        4: {'symbol': 'DIXON', 'name': 'Dixon Tech', 'score': 'Crowded/Testing',
            'detail': '27% price drop but consensus long, institutions trimming'},
        5: {'symbol': 'AMBER', 'name': 'Amber Ent', 'score': 'High Hype',
            'detail': 'P/E 166, retail/momentum priced in 3 years'}
    },
    'hidden_risks': {
        'DIXON': ['PLI allocation cut 9,000→1,527 Cr', '49% Chinese JV ownership'],
        'SYRMA': ['Debt-to-Equity 3x industry avg', 'High capital intensity'],
        'AMBER': ['P/E 166 extremely stretched', 'Momentum crowded']
    },
    'industry_metrics': {
        'avg_debt_equity': 0.12,
        'component_pli_size': 40000,  # ₹40,000 Cr
        'dixon_it_hardware_target': 4000,  # ₹4,000 Cr
        'amber_pcb_target': 1e9  # $1B
    }
}

# ============================================================
# ENHANCED COMPANY DISCOVERY WITH EXPERT VALIDATION
# ============================================================

def discover_companies_with_expert_insights() -> List[Dict[str, Any]]:
    """Fetch live data and overlay expert insights"""
    
    # Core companies from expert analysis
    target_symbols = ['DIXON.NS', 'SYRMA.NS', 'AMBER.NS', 'TCIEXP.NS', 'BLUEDART.NS']
    companies = []
    
    print(f"{Colors.BLUE}🔍 Mining companies with expert-validated factors...{Colors.END}")
    
    for symbol in target_symbols:
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            
            if info and 'longName' in info:
                # Get debt-to-equity from balance sheet
                balance_sheet = ticker.balance_sheet
                debt_to_equity = None
                if balance_sheet is not None and not balance_sheet.empty:
                    try:
                        total_debt = balance_sheet.loc['Total Debt'] if 'Total Debt' in balance_sheet.index else 0
                        total_equity = balance_sheet.loc['Total Equity Gross Minority Interest'] if 'Total Equity Gross Minority Interest' in balance_sheet.index else 1
                        if total_equity != 0:
                            debt_to_equity = total_debt.iloc[0] / total_equity.iloc[0]
                    except:
                        pass
                
                # Get institutional holdings
                institutional_holders = ticker.institutional_holders
                institutional_value = 0
                if institutional_holders is not None and not institutional_holders.empty:
                    institutional_value = institutional_holders['Value'].sum() if 'Value' in institutional_holders.columns else 0
                
                # Get mutual fund holdings
                mutual_fund_holders = ticker.mutualfund_holders
                mf_value = 0
                if mutual_fund_holders is not None and not mutual_fund_holders.empty:
                    mf_value = mutual_fund_holders['Value'].sum() if 'Value' in mutual_fund_holders.columns else 0
                
                # Calculate MF holding percentage (rough estimate)
                market_cap = info.get('marketCap', 1)
                mf_percentage = (mf_value / market_cap * 100) if market_cap > 0 else 0
                
                # Base company data
                company = {
                    'symbol': symbol.replace('.NS', ''),
                    'name': info.get('longName', 'Unknown'),
                    'current_price': info.get('currentPrice', info.get('regularMarketPrice', 0)),
                    'market_cap': market_cap,
                    'pe_ratio': info.get('trailingPE', 0),
                    'volume': info.get('volume', 0),
                    'avg_volume': info.get('averageVolume', 0),
                    'fifty_two_week_high': info.get('fiftyTwoWeekHigh', 0),
                    'fifty_two_week_low': info.get('fiftyTwoWeekLow', 0),
                    'debt_to_equity': debt_to_equity,
                    'institutional_value': institutional_value,
                    'mutual_fund_value': mf_value,
                    'mf_percentage': mf_percentage,
                    'beta': info.get('beta', 0),
                }
                
                # Add expert insights if available
                if company['symbol'] in EXPERT_INSIGHTS['strategic_winners']:
                    expert = EXPERT_INSIGHTS['strategic_winners'][company['symbol']]
                    company['expert_catalyst'] = expert.get('catalyst', '')
                    company['expert_warning'] = expert.get('warning', '')
                    company['geopolitical_risk'] = expert.get('geopolitical_risk', '')
                
                # Add stealth ranking
                for rank, data in EXPERT_INSIGHTS['stealth_ranking'].items():
                    if data['symbol'] == company['symbol']:
                        company['stealth_rank'] = rank
                        company['stealth_score'] = data['score']
                        company['stealth_detail'] = data['detail']
                
                # Add hidden risks
                if company['symbol'] in EXPERT_INSIGHTS['hidden_risks']:
                    company['hidden_risks'] = EXPERT_INSIGHTS['hidden_risks'][company['symbol']]
                
                # Get recent performance
                hist = ticker.history(period="3mo")
                if not hist.empty:
                    company['three_month_change'] = ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0] * 100)
                
                companies.append(company)
                print(f"{Colors.GREEN}  ✓ Analyzed: {company['name']} ({company['symbol']}){Colors.END}")
                
        except Exception as e:
            print(f"{Colors.YELLOW}  ⚠️ Could not fetch {symbol}: {e}{Colors.END}")
    
    return companies

# ============================================================
# ENHANCED ASYMMETRY WITH EXPERT WEIGHTS
# ============================================================

def analyze_expert_validated_asymmetry(companies: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Asymmetry analysis that incorporates expert insights
    """
    
    print(f"{Colors.CYAN}🔬 Running expert-validated asymmetry analysis...{Colors.END}")
    
    for company in companies:
        asymmetry_score = 0
        reasons = []
        risk_flags = []
        
        # Price-based factors
        if company['current_price'] < company['fifty_two_week_low'] * 1.1:
            asymmetry_score += 3
            reasons.append(f"Near 52-week low (₹{company['fifty_two_week_low']:.2f})")
        
        if company.get('three_month_change', 0) < -5:
            asymmetry_score += 2
            reasons.append(f"Down {company['three_month_change']:.1f}% in 3 months")
        
        # Expert catalyst check
        if 'expert_catalyst' in company:
            asymmetry_score += 4  # Big boost for expert-identified catalysts
            reasons.append(f"Expert catalyst: {company['expert_catalyst'][:50]}...")
        
        # Stealth factor (lower rank = higher stealth opportunity)
        stealth_rank = company.get('stealth_rank', 5)
        if stealth_rank <= 2:
            asymmetry_score += 5
            reasons.append(f"High stealth (Rank {stealth_rank}): {company.get('stealth_detail', '')}")
        elif stealth_rank <= 3:
            asymmetry_score += 2
            reasons.append(f"Moderate stealth (Rank {stealth_rank})")
        
        # Debt risk (expert identified)
        if company['symbol'] == 'SYRMA':
            d_e = company.get('debt_to_equity', 0)
            industry_avg = EXPERT_INSIGHTS['industry_metrics']['avg_debt_equity']
            if d_e and d_e > industry_avg * 2:
                risk_flags.append(f"⚠️ High debt: {d_e:.2f} vs industry {industry_avg:.2f}")
                asymmetry_score -= 2
        
        # Geopolitical risk (expert identified)
        if 'geopolitical_risk' in company:
            risk_flags.append(f"⚠️ Geopolitical: {company['geopolitical_risk']}")
            asymmetry_score -= 3
        
        # High P/E warning (expert identified)
        if company['symbol'] == 'AMBER' and company.get('pe_ratio', 0) > 150:
            risk_flags.append("⚠️ Extreme P/E: 166 (3 years growth priced in)")
            asymmetry_score -= 4
        
        company['asymmetry_score'] = asymmetry_score
        company['asymmetry_reasons'] = reasons
        company['risk_flags'] = risk_flags
    
    # Sort by asymmetry score
    sorted_companies = sorted(companies, key=lambda x: x.get('asymmetry_score', 0), reverse=True)
    
    return {
        'top_company': sorted_companies[0] if sorted_companies else None,
        'all_companies': sorted_companies
    }

# ============================================================
# GENERATE EXPERT-VALIDATED REPORT
# ============================================================

def generate_expert_report(companies: List[Dict[str, Any]], asymmetry: Dict[str, Any]) -> str:
    """Generate report blending live data with expert insights"""
    
    report = []
    report.append(f"\n{Colors.BOLD}{Colors.HEADER}{'='*100}{Colors.END}")
    report.append(f"{Colors.BOLD}{Colors.HEADER}🚀 AUTONOMOUS PLI ALPHA GENERATOR v2.0{Colors.END}")
    report.append(f"{Colors.BOLD}{Colors.HEADER}   Expert-Validated Supply Chain Intelligence{Colors.END}")
    report.append(f"{Colors.BOLD}{Colors.HEADER}{'='*100}{Colors.END}\n")
    report.append(f"{Colors.BLUE}Analysis Timestamp:{Colors.END} {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}")
    report.append(f"{Colors.BLUE}Expert Insights Date:{Colors.END} February 23, 2026 (Gemini Analysis)\n")
    
    # Expert Summary
    report.append(f"{Colors.BOLD}{Colors.YELLOW}📊 EXPERT MACRO VIEW{Colors.END}")
    report.append(f"• PLI disbursed: ₹28,748 crore (as of late 2025)")
    report.append(f"• Component PLI boost: ₹{EXPERT_INSIGHTS['industry_metrics']['component_pli_size']:,} Cr")
    report.append(f"• Shift: 'Screw-Driver Technology' → Core Component Manufacturing\n")
    
    # Strategic Winners (Expert identified)
    report.append(f"{Colors.BOLD}{Colors.CYAN}🏭 STRATEGIC CORRELATION: 20%+ Utilization Candidates{Colors.END}")
    for sym, data in EXPERT_INSIGHTS['strategic_winners'].items():
        # Find live price if available
        live_price = next((c['current_price'] for c in companies if c['symbol'] == sym), 'N/A')
        report.append(f"\n{Colors.BOLD}{sym}{Colors.END} - ₹{live_price if live_price != 'N/A' else 'N/A'}")
        report.append(f"  • {Colors.GREEN}Catalyst:{Colors.END} {data['catalyst']}")
        report.append(f"  • {Colors.YELLOW}Warning:{Colors.END} {data.get('warning', 'None')}")
        if 'geopolitical_risk' in data:
            report.append(f"  • {Colors.RED}Geo Risk:{Colors.END} {data['geopolitical_risk']}")
    
    # Stealth Ranking (Expert validated)
    report.append(f"\n{Colors.BOLD}{Colors.MAGENTA}🕵️ INSTITUTIONAL STEALTH RANKING{Colors.END}")
    report.append(f"{'Rank':<6} {'Company':<20} {'Score':<18} {'Live MF %':<10} {'Current':<10}")
    report.append("-" * 70)
    
    for rank in range(1, 6):
        data = EXPERT_INSIGHTS['stealth_ranking'][rank]
        company = next((c for c in companies if c['symbol'] == data['symbol']), None)
        if company:
            mf_pct = f"{company.get('mf_percentage', 0):.1f}%"
            price = f"₹{company['current_price']:.2f}"
            report.append(f"{rank:<6} {company['name'][:18]:<20} {data['score']:<18} {mf_pct:<10} {price:<10}")
    
    # Hidden Risks Matrix
    report.append(f"\n{Colors.BOLD}{Colors.RED}⚠️ HIDDEN RISKS MATRIX{Colors.END}")
    for company in companies:
        if 'hidden_risks' in company or 'risk_flags' in company:
            report.append(f"\n{Colors.BOLD}{company['symbol']}{Colors.END}")
            if 'hidden_risks' in company:
                for risk in company['hidden_risks']:
                    report.append(f"  • {risk}")
            if 'risk_flags' in company:
                for risk in company['risk_flags']:
                    report.append(f"  • {risk}")
    
    # Current Asymmetry Opportunity (Live data + Expert overlay)
    top = asymmetry['top_company']
    if top:
        report.append(f"\n{Colors.BOLD}{Colors.GREEN}🎯 CURRENT HIGHEST ASYMMETRY OPPORTUNITY{Colors.END}")
        report.append(f"{Colors.BOLD}{top['name']} ({top['symbol']}){Colors.END}")
        report.append(f"{Colors.BLUE}Asymmetry Score:{Colors.END} {top['asymmetry_score']}/10")
        report.append(f"{Colors.BLUE}Live Price:{Colors.END} ₹{top['current_price']:.2f}")
        report.append(f"{Colors.BLUE}52-Week Range:{Colors.END} ₹{top['fifty_two_week_low']:.2f} - ₹{top['fifty_two_week_high']:.2f}")
        
        if top['asymmetry_reasons']:
            report.append(f"{Colors.BLUE}Asymmetry Drivers:{Colors.END}")
            for reason in top['asymmetry_reasons']:
                report.append(f"  • {reason}")
        
        # Buy trigger calculation
        buy_trigger = top['fifty_two_week_low'] * 1.02
        report.append(f"\n{Colors.BOLD}{Colors.GREEN}💰 BUY TRIGGER (Live){Colors.END}")
        report.append(f"   Buy at: ₹{buy_trigger:.2f}")
        report.append(f"   Target: ₹{top['fifty_two_week_high']:.2f}")
        report.append(f"   Stop: ₹{top['fifty_two_week_low'] * 0.95:.2f}")
    
    report.append(f"\n{Colors.BOLD}{Colors.HEADER}{'='*100}{Colors.END}")
    report.append(f"{Colors.YELLOW}⚠️  DISCLAIMER: Expert insights from Feb 23, 2026. Prices are live.{Colors.END}")
    report.append(f"{Colors.YELLOW}   Always validate with current fundamentals.{Colors.END}")
    
    return "\n".join(report)

# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    """Run expert-validated analysis pipeline"""
    
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*100}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}🚀 AUTONOMOUS PLI ALPHA GENERATOR v2.0{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}   Expert-Validated Intelligence Engine{Colors.END}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*100}{Colors.END}\n")
    
    # Fetch live company data
    companies = discover_companies_with_expert_insights()
    if not companies:
        print(f"{Colors.RED}❌ No companies found.{Colors.END}")
        return
    
    # Run expert-validated asymmetry analysis
    asymmetry = analyze_expert_validated_asymmetry(companies)
    
    # Generate enhanced report
    report = generate_expert_report(companies, asymmetry)
    print(report)
    
    # Save results to JSON for README update
    reports_dir = Path(__file__).parent.parent / "reports"
    reports_dir.mkdir(exist_ok=True)
    
    report_file = reports_dir / f"analysis_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    
    # Prepare data for JSON
    json_data = {
        'timestamp': datetime.now().isoformat(),
        'top_company': {
            'name': asymmetry['top_company']['name'],
            'symbol': asymmetry['top_company']['symbol'],
            'current_price': asymmetry['top_company']['current_price'],
            'fifty_two_week_low': asymmetry['top_company']['fifty_two_week_low'],
            'fifty_two_week_high': asymmetry['top_company']['fifty_two_week_high'],
            'asymmetry_score': asymmetry['top_company']['asymmetry_score'],
            'asymmetry_reasons': asymmetry['top_company']['asymmetry_reasons'],
            'risk_flags': asymmetry['top_company'].get('risk_flags', [])
        },
        'all_companies': [
            {
                'symbol': c['symbol'],
                'name': c['name'],
                'price': c['current_price'],
                'score': c['asymmetry_score']
            }
            for c in asymmetry['all_companies']
        ]
    }
    
    with open(report_file, 'w') as f:
        json.dump(json_data, f, indent=2)
    
    print(f"{Colors.GREEN}✅ Analysis saved to {report_file}{Colors.END}")
    print(f"{Colors.GREEN}✅ File exists: {report_file.exists()}{Colors.END}")
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}✅ Analysis Complete!{Colors.END}")
    print(f"{Colors.YELLOW}📋 Next iteration: Feed latest news back to Gemini for updated insights{Colors.END}")

if __name__ == "__main__":
    main()
