---
type: concept
title: Settlement Email Template and Contact Governance
created: 2026-08-23
updated: 2026-08-23
tags: [email-template, client-contact, maker-checker, settlement-affirmation]
related: [cdups, fmrp, murex, affirmation-email-scope-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Derivative Settlement Affirmation - Email Automation.md"]
---
# Settlement Email Template and Contact Governance

Settlement email template and contact governance covers CDUPS maintenance of templates, recipient contacts, copies, and approval controls.

Templates must support Gross, Bilateral Netting, and BIC Netting settlements, with variation by country, product, client, location, strategy, and other parameters. Contacts are maintained separately from Confirmation and FX-netting contacts, with maker-checker approval and FMID/BIC-level support.

Recipient routing must support one address across products, separate messages to one address for different products, and different addresses by product. Copies to SCB contacts are configurable by Booking Entity and Product.