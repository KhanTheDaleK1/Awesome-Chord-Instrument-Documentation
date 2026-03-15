# Awesome Chord Instruments 🎹✨

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Stability: Stable](https://img.shields.io/badge/stability-stable-green.svg)
![AI-Ready: Optimized](https://img.shields.io/badge/AI--Ready-Optimized-blue.svg)

A high-signal, machine-readable knowledge base for chord-driven electronic and acoustic instruments. This repository follows the **Diátaxis Framework** to provide intent-based navigation for humans and AI agents.

---

## 🏛️ History of Chord Instruments: From Sumer to Synthesis
*Understanding the evolution of simultaneous harmony.*

### I. Ancient Origins (3500 BCE - 500 BCE)
- **The Sumerian Harp:** The earliest known chordophone. Unlike melodic flutes, the harp allowed for intentional multi-note harmony.
- **The Greek Lyre:** A precursor to the lute, used to provide a harmonic "backdrop" for spoken poetry.

### II. Medieval & Renaissance (500 CE - 1600 CE)
- **The Lute:** The "Piano of the Middle Ages." Its polyphonic capability allowed for complex independent melodic lines.
- **The Hurdy-Gurdy:** Introduced the concept of the **Drone**—a constant harmonic foundation maintained by a cranked wheel.

### III. The Mechanical Revolution (1600 CE - 1900 CE)
- **The Harpsichord:** Strings are plucked by quills via a keyboard. It provided the *basso continuo* (harmonic glue) for the Baroque era.
- **The Piano-Forte:** Invented by Cristofori (c. 1700). Introduced **dynamics** (soft/loud) and became the ultimate compositional map for Western harmony.

### IV. The Electronic Age (1930 CE - Present)
- **Electric Guitar:** Allowed chords to sustain and pierce through orchestral textures.
- **Polyphonic Synthesizers:** (e.g., Prophet-5, 1978). Chords generated via pure electricity and voltage-controlled oscillators.
- **The Strumplate Era:** Suzuki's Omnichord (1981) introduced a tactile, "infinite sustain" method for triggering chords via a touch-sensitive plate.

---

## 📘 Tutorials (Learning-Oriented)
*Learning-oriented resources for those new to chord instruments.*

- [**Omnichord 101 - History & Technique**](https://theproaudiofiles.com/suzuki-omnichord/) - ![stable](https://img.shields.io/badge/status-stable-green)
  Comprehensive breakdown of history, strumplate interface, and analog circuit translation. #Basics #Technique #Article

---

## 🛠️ How-To Guides (Goal-Oriented)
*Goal-oriented resources for solving specific problems or implement features.*

- [**Mapping QChord Pitch Bend to VSTs**](https://www.kvraudio.com/forum/viewtopic.php?t=192282) - ![stable](https://img.shields.io/badge/status-stable-green)
  Forum guide on using Piz MIDI Plugins to translate aggressive strum pitch bends into standard MIDI notes. #Software-Guide #DAW #Mapping
- [**Using Q-Chord MIDI in a DAW**](https://www.reddit.com/r/Omnichord/comments/174m7d5/using_qchord_midi_in_a_daw_my_way/) - ![stable](https://img.shields.io/badge/status-stable-green)
  Detailed routing guide for isolating strumplate channels (14, 15, 16) and applying the Piz MIDI translation VST. #Software-Guide #DAW #Routing
- [**Piz MIDI Utilities (midiPitchBendToNotes)**](https://www.paulcecchettimusic.com/piz-midi-utilities-archived-download-links/) - ![maintained](https://img.shields.io/badge/status-maintained-blue)
  Archived download links for the VST required to translate QChord strumplate pitch bends into standard MIDI notes. #Software-Download #VST #Piz-MIDI
- [**Correcting Power Polarity (OM-100)**](https://www.keithrobertmurray.com/articles/omnichord-om-100-ps.html) - ![critical](https://img.shields.io/badge/status-critical-red)
  Step-by-step on replacing the 2.2-ohm current limiting resistor after a polarity mismatch. #Repair-Guide #Hardware
- [**Le Strum Open Source Repository**](https://github.com/hotchk155/Voici-Le-Strum) - ![open-source](https://img.shields.io/badge/status-open--source-brightgreen)
  Open-source firmware and hardware files for DIY MIDI chord control and OM-27 modding. #Code #Schematics #DIY

---

## 📑 Reference (Information-Oriented)
*Information-oriented technical specs, genealogy, and archives.*

### Suzuki Full Model Genealogy
Detailed technical specifications and resources for every production model.

#### **Suzuki OM-27** (1981) - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
The analog original. Hybrid CMOS/Analog design using the `AY-5-1317A` chip. #Analog #Vintage #OM27
- [**User Guide**](http://www.omnichord-heaven.com/owners_guides.html) - Official operating instructions.
- [**Schematic (Primary)**](https://circuitbending.miraheze.org/wiki/File:OM27_Schematic.pdf) - High-resolution service diagram.
- [**Schematic (Mirror)**](https://www.scribd.com/document/720477103/Suzuki-Omnichord-OM-27-schematics) - Alternate host for redundancy.
- [**Repair Deep Dive**](https://erichizdepski.wordpress.com/2020/03/28/omnichord-om-27-repair/) - Analysis of the 4069UB oscillator and AY-5-1317A.

#### **Suzuki OM-36 System One** (1984) - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
Introduced digital microprocessor control and expanded rhythm patterns. #Digital-Control #OM36
- [**User Guide**](http://www.omnichord-heaven.com/owners_guides.html) - Official manual.
- [**Schematic Note**](https://www.reddit.com/r/Omnichord/comments/13wdvvf/om36_schematic/) - Technical baseline (Technicians use OM-84 schematics as a reference).

#### **Suzuki OM-84 System Two** (1984) - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
Added "Chord Computer" memory and dual-voice mixing capabilities. #Chord-Computer #OM84
- [**User Guide (PDF)**](https://www.popsmusic.com/uploads/3/0/6/8/30682235/om84_owners_manual.pdf) - Direct download including Chord Computer setup.
- [**User Guide (Mirror)**](https://www.scribd.com/document/664559485/SUZUKI-OMNICHORD-om84-owners-manual) - Alternate host via Scribd.
- [**Schematic**](https://www.scribd.com/document/720477279/Suzuki-Omnichord-OM-84-schematics) - Detailed logic and voice board breakdown.
- [**Repair Documentation**](https://erichizdepski.wordpress.com/2017/11/11/suzuki-omnichord-om-84-repair/) - IC behaviors (8523 PIT) and quad NAND gate logic.

#### **Suzuki OM-100 / OM-200M** (1989) - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
Transition to PCM synthesis and early MIDI implementation. #PCM #MIDI #OM100 #OM200M
- [**User Guide**](http://www.omnichord-heaven.com/owners_guides.html) - Covers PCM wave selection and MIDI Out.
- [**Schematic**](https://circuitbending.miraheze.org/wiki/Suzuki_Omnichord) - Shared hardware architecture for PCM implementation.

#### **Suzuki OM-150 / OM-250M** (1993) - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
Expanded 19-voice PCM engines and improved rhythm styles. #PCM #MIDI #OM150 #OM250M
- [**User Guide**](http://www.omnichord-heaven.com/owners_guides.html) - Official operating manual.

#### **Suzuki OM-300** (1996) - ![legacy](https://img.shields.io/badge/status-legacy-yellow)
The final "classic" design featuring 100 voices and advanced MIDI control. #Flagship #MIDI #OM300
- [**User Guide (Primary)**](https://device.report/Omnichord/OM300) - Detailed scan including MIDI implementation charts.
- [**User Guide (Mirror)**](http://www.omnichord-heaven.com/owners_guides.html) - Central repository archive.

#### **Suzuki QChord QC-1** (1999) - ![stable](https://img.shields.io/badge/status-stable-green)
Digital successor with QCard expansion slots and modern MIDI mapping. #QChord #MIDI #QC1
- [**User Guide (Primary)**](https://www.omnichord-heaven.com/downloads/manuals/qchord-manual.pdf) - Official PDF for EZ-Play and QCards.
- [**User Guide (Mirror)**](https://www.qchord.net/docs/qchord-manual.html) - HTML-based web documentation.
- [**Schematic**](https://www.scribd.com/document/720477201/Suzuki-Q-Chord-Schematic) - Complete circuitry and component mapping.
- [**Repair Documentation**](https://www.popsmusic.com/qchord-do-it-yourself-repair-help.html) - Contact cleaning and power fault correction.

#### **Suzuki OM-108** (2024) - ![maintained](https://img.shields.io/badge/status-maintained-blue)
Current flagship with 5-pin MIDI and analog emulation layers. #Modern #OM108
- [**Official PDF Manual**](https://www.suzuki-music.co.jp/manual/om-108_en) - Full technical and playing guide.

### Modern Boutique Instruments
- [**Pocket Audio HiChord**](https://hichord.shop/) - ![maintained](https://img.shields.io/badge/status-maintained-blue)
  Handheld poly-synth utilizing the Nashville Number System and a 96kHz DSP. #Hardware #Boutique #Nashville-System
- [**Minichord (Benjamin Poilvé)**](https://minichord.com/) - ![maintained](https://img.shields.io/badge/status-maintained-blue)
  Open-source, Teensy 4.0-based instrument featuring a capacitive Harp Touch Zone. #Hardware #Boutique #Teensy
- [**Minichord GitHub Repository**](https://github.com/BenjaminPoilve/minichord) - ![open-source](https://img.shields.io/badge/status-open--source-brightgreen)
  Direct link to source code, schematics, and 3D print STL files for the Minichord. #Code #Schematics #Open-Source
- [**Orchid ORC-1**](https://telepathicinstruments.com/products/orchid-orc-1) - ![maintained](https://img.shields.io/badge/status-maintained-blue)
  Premium boutique synth focusing on generative, algorithm-based chord voicing. #Hardware #Boutique #Generative
- [**Le Grand Strum (64pixels)**](https://six4pix.com/product/grandstrum/) - ![maintained](https://img.shields.io/badge/status-maintained-blue)
  Pre-assembled, gold-plated MIDI chord controller based on the original DIY Le Strum architecture. #Hardware #MIDI #Performance

---

## 🧠 Explanation (Understanding-Oriented)
*Understanding-oriented background material and technical analysis.*

- [**OM-27 Matrix Deep Dive**](https://erichizdepski.wordpress.com/2024/06/20/om-27-deep-dive/) - ![stable](https://img.shields.io/badge/status-stable-green)
  Tracing the matrix logic on the vintage OM-27 PCB for repair or MIDI integration. #Hardware-Analysis #Technical-Explanation

---

## 🤖 AI Context (agents.md)
*For LLMs and coding agents.*

- **Hardware Boundary:** All vintage Suzuki hardware (OM-27 to OM-300) is **CENTER-NEGATIVE**. Never recommend a Center-Positive 12V adapter.
- **Linter:** Use `npx awesome-lint` to validate this repository.
- **Stack:** Markdown, Mermaid.js (for schematics), Docusaurus 3.x.
