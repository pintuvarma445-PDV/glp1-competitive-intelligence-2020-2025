# Source Registry — GLP-1 Sales Data (2020–2024)

This document ensures auditability and traceability of all revenue numbers used in CI analysis.

## Primary Data Sources

### Novo Nordisk
- Annual Reports 2020, 2021, 2022, 2023, 2024 (if available)
- Form 20-F filings (SEC)
- Quarterly Financial Reports
- Capital Markets Day presentations (obesity franchise)
- Press releases (product-specific updates)

### Eli Lilly
- Annual Report / Form 10-K (2020–2024)
- Quarterly earnings press releases
- Investor presentations
- Product-specific decks (tirzepatide franchise)

## Source Validation Rules
1. **Primary priority**: Audited financial statements (Annual Report, 10-K, 20-F).  
2. **Secondary**: Quarterly earnings releases.  
3. **Tertiary**: Investor deck numbers only if consistent with audited reports.  
4. Every number must include:
   - Exact **page number**  
   - **Table title**  
   - **Currency**  
   - **Period**  
   - **Direct quote** from report  
5. Screenshots or PDFs must be archived in `data/raw/reports/<company>/<year>/`.
6. Every number must be **double-verified** before approval.
