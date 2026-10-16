# Commercial model != access tier != product ownership

One product/one codebase; no customer forks.

Per tenant configuration:
- commercial_model: subscription | partnership | per_vehicle | commission | license | franchise | hybrid | custom_rule.
- access_tier: starter | full_access, plus feature entitlements.
- billing_frequency / currency / price components / effective_from / effective_to.
- distribution rules: technology-product revenue only; never automatically allocate taxi-operator receipts or investor funds.
- legal agreement version + approver; changing the setting does not transfer IP rights.
- audit trail with prior/new config, identity, timestamp and reason.

## Safe switching
Prepare -> simulate future invoice and distribution -> dual approval for high-impact changes -> schedule effective date -> publish config -> reconcile invoice. Existing documents remain bound to prior effective configuration.

## MVP
Starter at minimal subscription; Business Plans & Real Reporting and safe Planfix workflows MUST remain included. A configured 'Full Access' may enable advanced modules, but entitlements never rewrite historical operational records, safety controls or finance truth.

## Model extensions
Use a registered calculation strategy with typed inputs/outputs and a compatibility test suite. 'Custom' is not permission to execute untrusted user-provided Python or arbitrary formulas in the billing runtime. New calculation families can require developer work even when existing variants are configurable.

