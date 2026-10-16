# Open-source / reusable components register

Discovery leads, not approved production dependencies. Independently verify security, versions, licenses, issue activity, API compatibility, hosting data exposure and maintenance before adoption.

| Candidate | Source | Candidate use | Key due diligence |
|---|---|---|---|
| Planfix/planfix-1c | https://github.com/planfix/planfix-1c | Historical Planfix-to-1C integration reference | Confirm actual scope; not full accounting |
| popstas/planfix-mcp-server | https://github.com/popstas/planfix-mcp-server | Experimental Planfix MCP bridge | Security, quotas, incomplete operations |
| theYahia/planfix-mcp | https://github.com/theYahia/planfix-mcp | Alternative MCP connector | Schema/tool coverage and authorization |
| demliz-org/planfix-api-php-client | https://github.com/demliz-org/planfix-api-php-client | PHP REST client reference | Generated version vs current API |
| boo1ean/planfix-api | https://github.com/boo1ean/planfix-api | Legacy XML API reference | Older protocol, maintenance |
| traccar/traccar | https://github.com/traccar/traccar | Dedicated GPS / geofences / events | Hosting/licensing/data consent, API |
| OCA/fleet | https://github.com/OCA/fleet | Odoo vehicle-management add-ons | Odoo-only; not Planfix plugin |
| frappe/erpnext | https://github.com/frappe/erpnext | ERP alternative or finance inspiration | Migration/licensing/localization |
| activepieces/activepieces | https://github.com/activepieces/activepieces | Event/process automation | Licensing/version/security/operations |
| n8n-io/n8n | https://github.com/n8n-io/n8n | Automation alternative | Fair-code licensing and embedding terms |
| ontaxi/taxiserver | https://github.com/ontaxi/taxiserver | Dispatch architecture research | Not recommended unreviewed for production |

Decision state: RESEARCH ONLY. None have passed an exact-version security, license or end-to-end acceptance gate; no plugin is installed by this scaffold.

## Reuse policy
Favor maintained official libraries and standards; wrap each integration behind an adapter. Never pull arbitrary repos into the build on trust; pin dependency versions, check licenses, review software bill of materials, test failure modes and rollback.

