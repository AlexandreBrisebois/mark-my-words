# Readability Standard (Flesch-Kincaid Mental Model)

This document provides a shared mental model for auditing and improving the readability of content. All auditing skills (mark, devil, echo) and drafting skills (caret) must use this standard for calibration.

## The Goal
- **Grade Level**: Smart Grade 8 (Age 13-14).
- **Readability Score**: > 60 (Standard English).

---

## Core Rules

### 1. Sentence Architecture
- **Length**: Aim for < 20 words per sentence.
- **Structure**: Use Subject-Verb-Object (SVO). Avoid passive voice.
- **Rhythm**: Break long, complex sentences into two short, punchy ones.

### 2. Diction & Precision
- **No Weasel Words**: Eliminate *nearly, significantly, probably, very, extremely*.
- **Directness**: If a metric exists, use it. If not, describe the observation.
- **Syllable Control**: Prefer shorter, common words over multi-syllabic jargon.

---

## Readability Self-Audit Formula (Mental Model)

When a skill or user requests a readability check (`--grade`), evaluate the text using these prompts:

1.  **Word Count / Sentence**: Is the average over 20? If so, REVISE.
2.  **Syllable Count**: Are there more than 3 multi-syllabic words in this paragraph? If so, simplify.
3.  **Active Voice**: Is the subject doing the action?
4.  **Clarity Score**: 
    - **90-100**: (Grade 5) Too simple.
    - **60-70**: (Grade 8-9) **Optimal Target.**
    - **30-50**: (College) Too complex.
    - **0-30**: (Graduate) Incomprehensible for the target audience.

---

## Calibration Examples

### ❌ Grade 12+ (Bad)
> "In order to facilitate a more robust architectural orientation, we are leveraging serverless paradigms to significantly mitigate the operational overhead typically associated with infrastructure management."

### ✅ Grade 8 (Standard)
> "We use serverless code to cut operational costs. This lets us focus on building features instead of managing servers."
