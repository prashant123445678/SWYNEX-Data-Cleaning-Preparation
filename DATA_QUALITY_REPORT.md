# Data Quality Report

## Dataset
**Mauna Loa Weekly Atmospheric CO2 Data** — public dataset distributed by `statsmodels`.

- Raw rows: **2,284**
- Columns: **2** (`date`, `co2`)
- Period in this snapshot: **1958-03-29 to 2001-12-29**
- Measurement: CO2 concentration in ppmv

## Checks performed

| Issue | Result | Action |
|---|---:|---|
| Missing CO2 values | 59 | Filled by time-based interpolation |
| Exact duplicate records | 0 | Checked; none removed |
| Duplicate dates | 0 | Checked; none found |
| Invalid dates | 0 | Checked; none found |
| Non-numeric CO2 values | 0 | Converted/validated as numeric |
| Inconsistent ordering | Checked | Sorted chronologically |
| Incorrect/ambiguous data types | Standardized | `date` → datetime, `co2` → float |

## Missing-value treatment
Missing weekly CO2 observations were filled using **time interpolation**, which uses surrounding dated observations rather than replacing all gaps with one constant.

## Final validation
- Final rows: **2,284**
- Missing CO2 after cleaning: **0**
- Final date type: **datetime64**
- Final CO2 type: **float64**
- Dataset is chronologically sorted.

## Important note
Repeated CO2 *values* are not automatically duplicate records because each observation has its own date. Duplicate checking was therefore performed on the complete record (`date` + `co2`), not on the CO2 value alone.
