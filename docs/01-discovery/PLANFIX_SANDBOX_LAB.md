# Planfix synthetic development lab — exact first steps

**Important:** Planfix itself is cloud-hosted; we create a **separate Planfix account**, not a locally deployed copy. Our code in D:\Repo\Taxi can run on Windows or a dev server with sandbox credentials. Production remains the operator's untouched account.

## Choosing a lab account
- Start with a separate 14-day trial if immediate testing is needed.
- For continuous experimental use, certified partners can request a special partner account (Plan X capabilities, up to five partner employees; not permitted for daily company work). A partner demo account can be used for customer demonstrations with its own role/access limits.
- Normal free accounts do not grant the Planfix REST API. A partner status is not assumed until actually confirmed.

Official references: https://planfix.com/help/Partner_account ; https://planfix.com/help/Demo_account ; https://planfix.com/help/REST_API ; https://planfix.com/help/Partner_program .

## A safe, no-API first exercise
1. Create a separately named lab Planfix account under the technology provider's control. Confirm it is **not** the customer's existing production account. Do not share administrator credentials in issues or chat.
2. Add a directory for vehicles and a contact template for drivers (or use object types if more appropriate for actual UX). Add only simulated fields and restrict who can view finance data.
3. Run `python scripts/generate_sandbox_data.py --vehicles 500 --seed 42 --output artifacts/sandbox` from repo root. Output is **invented data** in three UTF-8 CSV files and a JSON manifest.
4. Import `drivers.csv` from Planfix Contacts -> Import, after selecting a matching contact template and mapping columns.
5. Import `vehicles.csv` from the Vehicles directory -> Import after mapping its fields. Use an external synthetic identifier for safe reimport and avoid duplicate matches.
6. Import `exceptions.csv` as tasks (Tasks -> Import) **only after** configuring a task object/template for settlement exceptions. Map the date and custom fields explicitly. Import is optional for the first manual walkthrough.
7. Set up process statuses for exceptions and a limited automation: "missing driver statement" assigns one finance specialist and schedules a reminder. Verify script conditions in Planfix's testing mode.
8. Compare the test Planfix task state against the source CSV and standalone financial forecast. Do not attempt real bank or accounting synchronization yet.

Official import guidance: https://planfix.com/help/Importing_contacts ; https://planfix.com/help/Import_of_directory_entries ; https://planfix.com/help/Importing_tasks ; https://planfix.com/help/Object_scripts ; https://planfix.com/help/Testing_mode .

Planfix task-import files accept CSV/XLS/XLSX, but currently cap at 1,000 rows per file. The generator deliberately produces at most 500 exception rows by default. Planfix automation scripts are asynchronous; do not interpret accepted API writes as final completed actions until verified.

## Required guardrails
- Simulated driver entries are contacts, **not 500 employee login licenses**. Do not add real names, phone numbers, tax IDs, license plates or bank accounts.
- Task/csv column names require one-time mapping to the custom fields actually configured in the lab.
- Planfix's REST API docs execute against the selected account; they do not create a separate simulated account implicitly.
- Never run generator/import against live operator Planfix or use company data to create the simulated 500 records.
- This repository does not create a Planfix cloud account or configure OAuth; access is a separate, human-approved setup step.
- Use only fake invoices/financial totals, clearly stamped SYNTHETIC, and never submit them as statutory reporting.

## Definition of done for lab bootstrap
Separate tenant established; generator repeatable; 500 contacts and 500 vehicles visible in lab with unique synthetic IDs; one exception workflow manually tested; one case triggers a source-missing/shortfall alert; all operations reversible in that separate lab. Evidence/screenshots must contain no credentials.
