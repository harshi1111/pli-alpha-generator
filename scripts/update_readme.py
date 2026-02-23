#!/usr/bin/env python3
"""
Auto-update README with latest analysis results
Run this after each analysis to keep README current
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import re

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

class ReadmeUpdater:
    def __init__(self):
        self.readme_path = Path(__file__).parent.parent / "README.md"
        self.reports_dir = Path(__file__).parent.parent / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        self.track_record = []
        
    def load_latest_analysis(self):
        """Find and load the most recent analysis report"""
        report_files = list(self.reports_dir.glob("analysis_*.json"))
        if not report_files:
            print("No analysis reports found")
            return None
        
        latest_report = max(report_files, key=lambda p: p.stat().st_mtime)
        with open(latest_report, 'r') as f:
            return json.load(f)
    
    def update_track_record(self, analysis):
        """Update track record with new analysis"""
        if not analysis or 'top_company' not in analysis:
            return
        
        top = analysis['top_company']
        new_entry = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'company': top['name'],
            'symbol': top['symbol'],
            'price': top['current_price'],
            'target': top['fifty_two_week_high'],
            'status': 'Active'
        }
        
        # Load existing track record
        track_file = Path(__file__).parent.parent / "data" / "track_record.json"
        if track_file.exists():
            with open(track_file, 'r') as f:
                self.track_record = json.load(f)
        
        # Add new entry (avoid duplicates)
        if not any(e['date'] == new_entry['date'] for e in self.track_record):
            self.track_record.append(new_entry)
        
        # Save updated track record
        with open(track_file, 'w') as f:
            json.dump(self.track_record, f, indent=2)
    
    def generate_track_record_table(self):
        """Generate markdown table from track record"""
        if not self.track_record:
            return "No track record yet. Run analysis first!"
        
        table = "| Date | Pick | Entry | Target | Status |\n"
        table += "|------|------|-------|--------|--------|\n"
        
        for entry in self.track_record[-10:]:  # Last 10 entries
            table += f"| {entry['date']} | {entry['symbol']} | ₹{entry['price']:.0f} | ₹{entry['target']:.0f} | {entry['status']} |\n"
        
        return table
    
    def update_readme(self):
        """Update README with latest data"""
        print(f"📝 Updating README at {self.readme_path}")
        
        # Load latest analysis
        analysis = self.load_latest_analysis()
        if analysis:
            self.update_track_record(analysis)
        
        # Read current README
        with open(self.readme_path, 'r') as f:
            content = f.read()
        
        # Update timestamp
        content = re.sub(
            r'Last Updated: .*',
            f'Last Updated: {datetime.now().strftime("%B %d, %Y at %H:%M IST")}',
            content
        )
        
        # Update track record section
        track_record_table = self.generate_track_record_table()
        content = re.sub(
            r'(## 📈 Track Record\n\n).*?(?=\n## |$)',
            f'\\1{track_record_table}\n\n',
            content,
            flags=re.DOTALL
        )
        
        # Update current top pick
        if analysis and 'top_company' in analysis:
            top = analysis['top_company']
            current_pick = f"""
## 🎯 Current Top Pick ({datetime.now().strftime('%B %d, %Y')})

**{top['name']} ({top['symbol']})**
- Price: ₹{top['current_price']:.2f}
- Buy Trigger: ₹{top['fifty_two_week_low'] * 1.02:.2f}
- Target: ₹{top['fifty_two_week_high']:.2f}
- Asymmetry Score: {top['asymmetry_score']}/10
"""
            content = re.sub(
                r'(## 🎯 Current Top Pick.*?)(?=\n## |$)',
                current_pick,
                content,
                flags=re.DOTALL
            )
        
        # Write updated README
        with open(self.readme_path, 'w') as f:
            f.write(content)
        
        print("✅ README updated successfully!")
        
        # Show preview
        print("\n📋 Track Record Updated:")
        print(self.generate_track_record_table())

if __name__ == "__main__":
    updater = ReadmeUpdater()
    updater.update_readme()
