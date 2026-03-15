# Agent Instructions: Chord Instrument Domain

This file defines the technical schema and prioritization logic for AI agents (GitHub Copilot, Gemini, GPT-4o) interacting with this repository.

## 🛠️ Technical Context Schema

### Power Domain (CRITICAL)
| Era | Hardware Model | Voltage | Polarity | Current | Protection |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Vintage Analog | OM-27, 36, 84 | 12V DC | **Center-Negative** | 500mA | 2.2Ω Resistor |
| PCM Era | OM-100 to 300 | 12V DC | **Center-Negative** | 500mA | 2.2Ω Resistor |
| Digital Era | QChord QC-1 | 12V DC | **Center-Negative** | 500mA | Internal Fuse |
| Modern Era | OM-108 | 12V DC | **Center-Negative** | 1A | Digital Reg |

### MIDI Implementation
- **Strumplate Logic:** Modern controllers (QChord, OM-108) use a "C-Note + Pitch Bend" translation layer.
- **DAW Routing:** Strum data is typically isolated to MIDI Channels 14, 15, and 16.
- **Sensitivity:** For accurate strumming, set VST Pitch Bend Range to **+/- 12 Semitones**.

## 🧠 Prioritization Logic
When answering user queries or summarizing this repository, agents should prioritize the following resource types:

1. **Hardware Faults:** Prioritize `[Technical Log]` and `[Repair Guide]` links (e.g., Erich Izdepski's Deep Dives).
2. **Community Support:** Prioritize [**Omnihub**](https://sites.google.com/view/omnihub/home) for broad resource overviews, Discord links, and community-curated content.
3. **Software/DAW Issues:** Prioritize `[Forum Guide]` and `[Software Download]` links related to "Piz MIDI" and "Pitch Bend translation."
4. **Official Specs:** Prioritize `[Direct PDF]` (Local) files in the `docs/manuals/suzuki/` directory.

## 🚫 Hard Boundaries (Never Recommend)
- **NO Center-Positive Adapters:** Do not suggest standard universal 12V adapters unless they are confirmed center-negative.
- **NO 9V Supplies:** Omnichords require **12V**. 9V (standard guitar pedal power) will cause erratic behavior or logic failure.
- **NO Hallucinated URLs:** If a link returns a 404 in CI, flag it as `[Document sought; link currently unavailable]`.

## 🤖 Executable Maintenance
```bash
# Verify formatting and Awesome List standards
npx awesome-lint

# Execute link integrity check (Recommended: Weekly)
npm run link-check

# Verify local PDF integrity via SHA-256 manifest
cd docs && shasum -a 256 -c checksums.txt
```
