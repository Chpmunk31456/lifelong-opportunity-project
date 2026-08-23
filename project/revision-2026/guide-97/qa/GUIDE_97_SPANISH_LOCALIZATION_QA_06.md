# Guide 97 — Spanish Localization QA

## Controlled source
- English frozen master: `project/revision-2026/guide-97/working-masters/GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_ENGLISH_v2.md`
- Frozen English blob: `f923ec4bbe08cd81d881091f204a4aa3d0c6c7cb`
- Spanish controlled master: `project/revision-2026/guide-97/working-masters/GUIDE_97_MECHANICAL_ENGINEERING_TECHNICIAN_SPANISH_es-419_v2.md`
- Spanish blob: `f851c168d366ee8ab551a63c842a7df830bcba91`
- Locale: neutral Latin American Spanish (`es-419`)

## Localization controls checked

- Occupation controls preserved: U.S. O*NET-SOC `17-3027.00`, Canada `NOC 22301`, Colombia `CUOC 31150`.
- Official U.S. 2025 wage benchmark preserved: `$35.82/hour` and `$74,510/year`; BLS May 2024 comparison preserved as `$68,730/year` with its date context.
- Canada wage controls preserved: `C$23.08 / C$35.00 / C$51.28` per hour and November 19, 2025 update context.
- Current private-market estimates remain explicitly labelled non-government estimates: ZipRecruiter `$75,124/year ($36.12/hour)`, Salary.com `$58,275/year ($28/hour)` with `$51,667–$65,216` interquartile context, and the broader Colombia Computrabajo `COP 1.4M–1.8M/month` reference with non-equivalence warning.
- SENA `Mantenimiento Mecánico Industrial` and `Mantenimiento Electromecánico Industrial` pathways preserve the `3,984 hours` duration and live-availability/admission caveats.
- WIOA/American Job Center, Canada training agreements, and OIT/Cinterfor pathways remain locators rather than promises of funding, admission, or placement.
- Engineering-authority boundaries remain explicit: technician work is not represented as licensed professional-engineering authority.
- Safety controls preserve hazardous-energy/LOTO, machine guarding, pressure/stored force, lifting/rigging, welding/hot-work, stop-work, authorization, and escalation boundaries.
- Cybersecurity controls preserve approved-account/device requirements, MFA, credentials, removable-media restrictions, firmware/software change verification, backups/change control, and reporting/escalation.
- Responsible-AI controls preserve the prohibition on treating AI as final authority for dimensions, tolerances, loads, stresses, material selection, pressure/temperature limits, torque, safety factors, lifting limits, maintenance intervals, acceptance criteria, guarding, LOTO, engineering changes, regulatory requirements, failure conclusions, or production release.
- Accessibility/job-fit guidance and the repaired six-step action plan are preserved with checkable milestones.
- Source and verification URLs are preserved as source destinations without translation or silent substitution.
- No claim of independent human translation certification, professional certification, accreditation, accessibility certification, legal review, or guaranteed outcome was introduced.

## Readability / locale check

The localization uses neutral Latin American terminology and avoids country-specific slang. Terms such as `plano`, `tolerancia`, `calibración`, `trazabilidad`, `bloqueo/etiquetado`, `guardas`, `izaje`, `metrología`, `mantenimiento`, `confiabilidad`, and `control de cambios` are used consistently. U.S./Canadian official classification titles are retained where needed for source fidelity.

## Gate result

**PASS — Spanish Localization (`es-419`)**

No blocker identified for Brazilian Portuguese localization.

## Post-freeze source-link correction revalidation — 2026-08-22

NIST moved the reader-verification page for *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. The obsolete URL ending in `-profile` returned HTTP 404 during Publication QA. The official NIST publication page was reverified on 2026-08-22 and the URL-only correction was applied in English, `es-419`, and `pt-BR` with no change to occupational claims, wage/training values, safety/professional-scope controls, cybersecurity/AI guidance, action-plan milestones, or assurance boundaries.

- Revalidated English blob: `f923ec4bbe08cd81d881091f204a4aa3d0c6c7cb`
- Revalidated Spanish blob: `f851c168d366ee8ab551a63c842a7df830bcba91`
- Revalidated Portuguese blob: `183a888d50148d4059c041b850548bef87e2cb09`
- Correct official NIST destination: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- Result: **PASS — affected gate revalidated after URL-only source correction.**
