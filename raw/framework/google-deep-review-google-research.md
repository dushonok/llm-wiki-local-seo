---
title: "Google Deep Review"
source: "https://research.google/deepreview/"
also:
  - "https://research.google/blog/analyzing-technical-documents-with-deep-review/"
  - "https://developers.google.com/deep-review/docs"
author: "Google Research (Rajesh Jayaram, Vincent Cohen-Addad et al.)"
published: 2026-10-14
created: 2026-11-25
description: "Agentic AI for rigorous verification of complex technical documents; public release after PAT pilots at major CS conferences."
tags:
  - "google-research"
  - "tool-reference"
---

# Capture notes (wiki ingest source)

Public release announced in Google Research blog, 2026-10-14. Product landing: https://research.google/deepreview/

**Summary:** Deep Review is an agentic system for rigorous feedback on complex documents—logical consistency, mathematical statements, improvements, fact grounding, comparison to existing work. Origin: Paper Assistant Tool (PAT); optional pre-submission pilots at STOC 2026, ICML 2026, NeurIPS 2026, ICLR 2027 (16,000+ opt-in manuscripts). Expanded beyond CS papers to design docs, presentations, legal/finance (per Google).

**Access:** 2 complimentary document reviews per week; higher volume via Gemini API key and Deep Review API (alpha, no SLA).

**Inputs:** PDF and plain text initially; multi-file support announced as coming soon.

**Privacy (Google-stated):** Uploads not used to train/fine-tune Google models; stored one year for UI display.

**Pipeline (four stages):** (1) document segmentation into logical segments; (2) adaptive compute budgeting by section density; (3) parallel section verification agents with full-document context; (4) global synthesis, consistency checks, external grounding/tool calls.

**Related:** Antigravity Teamwork Deep Document Review pattern (`/teamwork-preview`); research preprint linked from blog (*Towards Automating Scientific Review with Google’s Paper Assistant Tool*).

Full narrative and diagrams: use blog URL above as primary long-form source for wiki distillation.