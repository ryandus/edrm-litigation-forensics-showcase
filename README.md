# High-Stakes Digital Forensics to E-Discovery & Litigation Support
### Executing the Full EDRM Lifecycle Under Strict Evidentiary & Defensibility Standards

**Author:** Ryan C. Hanks, Master of Forensic Sciences  
**Role:** Digital Forensics Investigator | Litigation Support & E-Discovery Analyst  
**Contact:** [Ryanchanks@gmail.com](mailto:Ryanchanks@gmail.com) | [LinkedIn](https://www.linkedin.com/in/ryan-c-hanks) | [GitHub Repository](https://github.com/Ryandus/edrm-litigation-forensics-showcase)  
**Key Certifications:** RelativityOne Review Pro | Cellebrite Certified Mobile Examiner (CCME) | Google Cybersecurity & AI Professional

[![Live Presentation](https://img.shields.io/badge/▶%20LAUNCH-Interactive%2013--Slide%20Deck-38bdf8?style=for-the-badge&logoColor=white)](https://ryandus.github.io/edrm-litigation-forensics-showcase/)
[![RelativityOne](https://img.shields.io/badge/Platform-RelativityOne%20Review%20Pro-0066CC?style=for-the-badge)](https://www.relativity.com/)
[![Forensics](https://img.shields.io/badge/Forensics-Cellebrite%20Inseyets%20%7C%20AXIOM-navy?style=for-the-badge)](https://cellebrite.com/)
[![Framework](https://img.shields.io/badge/Standard-EDRM%20%7C%20FRE%20702%20%7C%20Frye-success?style=for-the-badge)](https://edrm.net/)

> ### 🚀 **[Click Here to Launch the Live Interactive Presentation Deck ↗](https://ryandus.github.io/edrm-litigation-forensics-showcase/)**
> *An interactive 13-slide technical briefing mapping forensic defensibility, SQLite parsing, multi-source ingestion, and automated load-file validation directly into the civil EDRM lifecycle.*

---

## Executive Overview

This technical portfolio addresses the common industry misconception that **Criminal Digital Forensics** and **Civil E-Discovery / Litigation Support** are disjointed domains. 

Operating under the strict evidentiary burdens of the **Federal Rules of Evidence (FRE 702), the *Frye* standard, and Fourth Amendment constraints**, forensic investigations map directly to the **Electronic Discovery Reference Model (EDRM)**.

### Why Digital Forensics Experience Elevates Litigation Teams
* **Stricter Defensibility Standards:** Zero tolerance for spoliation, verified cryptographic hash chains of custody, and auditable intake environments.
* **Deep File System & Artifact Fluency:** Parsing SQLite databases, carving unallocated space, decoding proprietary DVR/NVR codecs, and resolving multi-source timestamp drift.
* **Transferable Relativity Skills:** Forensic discipline carries over to Relativity review work: dtSearch querying, structured analytics, Continuous Active Learning (CAL), and verified load-file productions (`.dat`/`.opt`).

---

## The Rosetta Stone: Forensics ⟷ E-Discovery Translation Matrix

| EDRM Stage | Criminal & Forensic Workflow | Civil Litigation & E-Discovery Parallel | Shared Technical Standard |
| :--- | :--- | :--- | :--- |
| **Information Governance** | Lab SOPs, Evidence Retention, CJIS, Read-Only Audits | Enterprise Information Governance, Defensible Deletion | Proactive data mapping, chain of custody, and integrity controls. |
| **Identification** | Exigent Warrants, Custodian Scoping, FLOCK ALPR | Custodian Interviews, Rule 26(f) Discovery Plans, RFPs | Pinpointing key players and multi-modal ESI repositories. |
| **Preservation** | 18 U.S.C. § 2703(f) Letters, Hardware Write-Blockers | Legal Holds, M365 Purview Silent Holds, Spoliation Defense | Securing data integrity prior to collection. |
| **Collection** | FFS Bitstream Extractions (Inseyets), Physical Images (`.E01`) | Targeted API Collections, Forensic Cloud/M365 Exports | Bitstream capture with SHA-256 cryptographic verification. |
| **Processing** | Magnet AXIOM, Cellebrite PA, Clock Drift Normalization | Relativity Processing, De-NISTing, MD5 De-duplication, OCR | Converting raw containers into structured, searchable records. |
| **Review** | Detective Timeline Tagging, Incident Coding Layouts | 1st/2nd Pass Review, Dynamic Coding, Privilege Logs | Evaluating ESI for responsiveness, relevance, and privilege. |
| **Analysis** | CSLI Tower Azimuth Triangulation, Dwell Anomaly Detection | Continuous Active Learning (CAL), dtSearch, Concept Clustering | Uncovering communication patterns and chronological timelines. |
| **Production** | Discovery Packets, PII Redaction, Statutory Disclosures | Concordance `.dat`, Opticon `.opt`, Bates Stamping, Slipsheets | Exporting formatted load files with audit-verified metadata. |
| **Presentation** | Courtroom Testimony, Evidentiary Demonstratives | Trial Director, Deposition Exhibits, Summary Judgment Evidence | Communicating complex technical findings clearly before triers of fact. |

---

## Featured Case Study

### [Operation Rapid Response: 48-Hour Multi-Source Timeline Reconstruction](docs/01_case_study_rapid_response.md)
> **Note:** This case study is a fictional scenario written for this portfolio. It is not based on any real investigation, and no real case data was used.

* **Scenario:** Emergency suspected homicide investigation involving an uncooperative subject and an unconfirmed 200-mile transit route crossing multiple jurisdictional boundaries.
* **Technical Breakthrough:** Ingested and normalized five disparate ESI streams (Cellebrite Inseyets FFS mobile extractions, carrier CSLI tower dumps, FLOCK ALPR reads, and commercial CCTV video). Correlated cell tower azimuth handoffs with ALPR speed vectors to isolate a 4-minute highway shoulder dwell anomaly, securing third-party video confirming evidence disposal within 48 hours.
* **Civil Equivalence:** Demonstrates full execution of emergency Ex Parte TRO workflows, high-velocity multi-custodian data exfiltration triage, and verified load-file delivery under strict court deadlines.

---

## Technical Tooling & Scripts

* **`scripts/loadfile_validator.py`:** Python production QC utility that verifies Concordance `.dat` delimiter counts, field headers, and validates matching `.opt` image page links.
* **`scripts/timestamp_normalizer.py`:** Python script that standardizes heterogeneous timestamp formats (UTC, GPS Epoch, local DVR drift) into a unified chronological data model.
* **`samples/sample_production.dat`:** Multi-source Concordance load file showcasing metadata mapping across mobile, cellular, ALPR, and CCTV sources.

---

## Data Notice

All scenarios and sample data in this repository are fictional or synthetic. No case, client, or law-enforcement data is included.

---

## License

This project is open-source and licensed under the MIT License.
