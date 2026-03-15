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

- [**Omnichord 101 - History & Technique**](https://theproaudiofiles.com/suzuki-omnichord/) ![status-stable](https://img.shields.io/badge/status-stable-green) `[Article]`
  Comprehensive breakdown of history, strumplate interface, and analog circuit translation.

---

## 🛠️ How-To Guides (Goal-Oriented)
*Goal-oriented resources for solving specific problems or implement features.*

- [**Mapping QChord Pitch Bend to VSTs**](https://www.kvraudio.com/forum/viewtopic.php?t=192282) ![status-stable](https://img.shields.io/badge/status-stable-green) `[Forum Guide]`
  Using Piz MIDI Plugins to translate aggressive strum pitch bends into standard MIDI notes.
- [**Using Q-Chord MIDI in a DAW**](https://www.reddit.com/r/Omnichord/comments/174m7d5/using_qchord_midi_in_a_daw_my_way/) ![status-stable](https://img.shields.io/badge/status-stable-green) `[Reddit Guide]`
  Detailed routing for isolating strumplate channels (14, 15, 16).
- [**Piz MIDI Utilities (midiPitchBendToNotes)**](https://www.paulcecchettimusic.com/piz-midi-utilities-archived-download-links/) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Software Download]`
  Essential VSTs for QChord DAW integration.
- [**Correcting Power Polarity (OM-100)**](https://www.keithrobertmurray.com/articles/omnichord-om-100-ps.html) ![status-critical](https://img.shields.io/badge/status-critical-red) `[Repair Guide]`
  Step-by-step on replacing the 2.2-ohm resistor after a polarity mismatch.
- [**Le Strum Open Source Repository**](https://github.com/hotchk155/Voici-Le-Strum) ![status-open-source](https://img.shields.io/badge/status-open--source-brightgreen) `[GitHub Repo]`
  Firmware and hardware files for DIY MIDI chord control.

---

## 📑 Reference (Information-Oriented)
*Information-oriented technical specs, genealogy, and archives.*

### Suzuki OM-Series Quick Reference
| Model | Year | Synthesis Type | Key Feature |
| :--- | :--- | :--- | :--- |
| **OM-27** | 1981 | Hybrid Analog | First Strumplate |
| **OM-36** | 1984 | Digital/Analog | 84 Chord Support |
| **OM-84** | 1984 | Digital/Analog | Chord Computer / Multi-Voice |
| **OM-100** | 1989 | PCM Wave | Transition to Samples |
| **OM-200M** | 1989 | PCM Wave | Native MIDI Implementation |
| **OM-300** | 1996 | PCM Wave | 100 Voices / Pro MIDI |
| **QChord** | 1999 | PCM Wave | QCard Expansion Slot |
| **OM-108** | 2024 | PCM/Analog Modeling | Modern MIDI / High Fidelity |

<details>
<summary><b>Suzuki OM-27 (1981)</b></summary>

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-27/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**Schematic (Primary)**](https://circuitbending.miraheze.org/wiki/File:OM27_Schematic.pdf) `[Direct PDF]`
- [**Schematic (Mirror)**](https://www.scribd.com/document/720477103/Suzuki-Omnichord-OM-27-schematics) `[Scribd]`
- [**Repair Deep Dive**](https://erichizdepski.wordpress.com/2020/03/28/omnichord-om-27-repair/) `[Technical Log]`
</details>

<details>
<summary><b>Suzuki OM-36 System One (1984)</b></summary>

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-36/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**Schematic Note**](https://www.reddit.com/r/Omnichord/comments/13wdvvf/om36_schematic/) `[Technical Note]`
</details>

<details>
<summary><b>Suzuki OM-84 System Two (1984)</b></summary>

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-84/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](https://www.popsmusic.com/uploads/3/0/6/8/30682235/om84_owners_manual.pdf) `[Direct PDF]`
- [**User Guide (Mirror)**](https://www.scribd.com/document/664559485/SUZUKI-OMNICHORD-om84-owners-manual) `[Scribd]`
- [**Schematic**](https://www.scribd.com/document/720477279/Suzuki-Omnichord-OM-84-schematics) `[Scribd]`
- [**Repair Documentation**](https://erichizdepski.wordpress.com/2017/11/11/suzuki-omnichord-om-84-repair/) `[Technical Log]`
</details>

<details>
<summary><b>Suzuki OM-100 / OM-200M (1989)</b></summary>

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-100-200m/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**Schematic**](https://circuitbending.miraheze.org/wiki/Suzuki_Omnichord) `[Wiki]`
</details>

<details>
<summary><b>Suzuki OM-150 / OM-250M (1993)</b></summary>

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-150-250m/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
</details>

<details>
<summary><b>Suzuki OM-300 (1996)</b></summary>

- [**User Guide (Primary)**](https://device.report/Omnichord/OM300) `[Web View]`
- [**User Guide (Mirror)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
</details>

<details>
<summary><b>Suzuki QChord QC-1 (1999)</b></summary>

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/qchord/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Primary)**](https://www.omnichord-heaven.com/downloads/manuals/qchord-manual.pdf) `[Direct PDF]`
- [**User Guide (Mirror)**](https://www.qchord.net/docs/qchord-manual.html) `[HTML]`
- [**Schematic**](https://www.scribd.com/document/720477201/Suzuki-Q-Chord-Schematic) `[Scribd]`
- [**Repair Documentation**](https://www.popsmusic.com/qchord-do-it-yourself-repair-help.html) `[Repair Guide]`
</details>

<details>
<summary><b>Suzuki OM-108 (2024)</b></summary>

- [**Official Manual (Local PDF)**](./docs/manuals/suzuki/om-108/owners-guide.pdf) `[Direct PDF]`
- [**Official Manual (Web)**](https://www.suzuki-music.co.jp/manual/om-108_en) `[Direct PDF]`
</details>

### Iconic Chord Keyboards & Pocket Stations
Quick-reference for the essential hardware that defined portable chord sequencing and sampling.

| Product | Years | Type | Key Chord Feature |
| :--- | :--- | :--- | :--- |
| **Casio VL-1** | 1979-1984 | Calculator Synth | One-Key Sequenced Chords |
| **Casio PT-30/50** | 1983-1987 | Compact Keyboard | Dedicated Accordion-style Chord Buttons |
| **Korg Poly-800** | 1983-1988 | Polyphonic Synth | Dedicated "Chord Memory" Button |
| **Casio SK-Series** | 1985-1992 | Lo-Fi Sampler | Polyphonic Sample-to-Chord Mapping |
| **Roland Alpha Juno**| 1985-1988 | Analog Poly | House-style "One-Finger" Chord Memory |
| **Yamaha VSS-Series**| 1987-1991 | Vocal Sampler | Harmonic Texture/Modulated Pads |
| **Yamaha QY-Series** | 1990-2014 | Walkstation | 8-Track Pocket Chord Sequencer |
| **Roland PMA-5** | 1995-1999 | Music PDA | Stylus-driven Touch Chord Interface |
| **Yamaha DJX-Series**| 1998-2002 | Dance Keyboard | Rhythmic Chord Manipulation / Loops |

<details>
<summary><b>Yamaha QY & QR series (Pocket Walkstations)</b></summary>

- [**Yamaha QY10** (1990-1995)](https://en.wikipedia.org/wiki/Yamaha_QY10) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  The first pocket "Walkstation" with an 8-track sequencer and chord patterns.
- [**Yamaha QY20** (1992-1997)](https://synthmania.com/yamaha-qy20/) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Web Archive]`
  Featured a larger graphic display and expanded General MIDI sound set.
- [**Yamaha QR10** (1993-1996)](https://en.wikipedia.org/wiki/Yamaha_QY10) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  Handheld unit with chord buttons and a strum-like interface for performance.
- [**Yamaha QY70** (1997-2001)](https://synthpedia.net/yamaha/qy70/) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Reference]`
  A professional-grade XG sound engine in a handheld chord-sequencing box.
- [**Yamaha QY100** (1998-2014)](https://synthpedia.net/yamaha/qy100/) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Reference]`
  Final evolution of the QY line; added guitar/mic inputs and SmartMedia storage.
</details>

<details>
<summary><b>Casio SK & PT series (Sampling & Portable)</b></summary>

- [**Casio SK-1** (1985-1988)](https://web.casio.com/emi/40th/history/sk-1.html) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Official History]`
  Low-cost sampler that could map any recorded sound to polyphonic chords.
- [**Casio SK-5** (1987-1990)](https://www.perfectcircuit.com/signal/casio-sk1-history) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Article]`
  Added rhythm pads for triggering samples as rhythmic chord stabs.
- [**Casio SK-8** (1987-1991)](https://www.casio.com/jp/electronic-musical-instruments/) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Web View]`
  Educational sampling model featuring ROM-pack slots for song learning.
- [**Casio SK-200** (1987-1992)](https://www.vintagesynth.com/casio/sk200.php) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  A mid-sized sampling keyboard with improved rhythm patterns and auto-chords.
- [**Casio PT-30** (1983-1986)](https://www.muzines.co.uk/articles/casio-pt-30/11981) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Article]`
  Compact keyboard with a dedicated "chord button" section similar to an accordion.
- [**Casio PT-50** (1983-1987)](https://www.casio.com/jp/electronic-musical-instruments/) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Web View]`
  Advanced PT model with an LCD screen for visual chord and melody sequencing.
- [**Casio VL-1** (1979-1984)](https://en.wikipedia.org/wiki/Casio_VL-1) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  The iconic calculator-synth that used simple button-sequencing for chords.
</details>

<details>
<summary><b>Yamaha VSS & DJX series (Performance & Dance)</b></summary>

- [**Yamaha VSS-30** (1987-1989)](https://www.vintagesynth.com/yamaha/vss30.php) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  Cult classic vocal sampler that turned single sounds into modulated chord pads.
- [**Yamaha VSS-200** (1988-1991)](https://synthmania.com/yamaha-vss-200/) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Web Archive]`
  Combined voice sampling with FM synthesis for complex harmonic textures.
- [**Yamaha DJX-1** (1998-2000)](https://www.vintagesynth.com/yamaha/djx.php) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  A "dance" keyboard with a ribbon controller for rhythmic chord manipulation.
- [**Yamaha DJX-II** (2000-2002)](https://synthmania.com/2005/02/22/yamaha-djx-iib/) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Web Archive]`
  Shifted to a loop-based interface for live chord and pattern "remixing."
</details>

<details>
<summary><b>Korg & Roland (Classic Synthesis & PDA)</b></summary>

- [**Korg Poly-800** (1983-1987)](https://en.wikipedia.org/wiki/Korg_Poly-800) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  The first affordable poly-synth with a dedicated "Chord Memory" button.
- [**Korg Poly-800 II** (1986-1988)](https://www.vintagesynth.com/korg/poly800.php) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  Updated version with digital delay and enhanced MIDI SysEx support.
- [**Roland Alpha Juno-1** (1985-1987)](https://www.vintagesynth.com/roland/ajuno1.php) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  Analog synth famous for "one-finger" chord memory stabs in house music.
- [**Roland Alpha Juno-2** (1985-1988)](https://www.vintagesynth.com/roland/ajuno2.php) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Wiki]`
  Expanded version of Juno-1 with velocity sensitivity and aftertouch.
- [**Roland PMA-5** (1995-1999)](https://southsideguitars.com.au/products/roland-pma-5) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Reference]`
  A stylus-driven "Music PDA" for touch-based chord and track arrangement.
</details>

### Modern Boutique Instruments
- [**Pocket Audio HiChord**](https://hichord.shop/) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`
- [**Minichord (Benjamin Poilvé)**](https://minichord.com/) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`
- [**Minichord GitHub Repository**](https://github.com/BenjaminPoilve/minichord) ![status-open-source](https://img.shields.io/badge/status-open--source-brightgreen) `[GitHub Repo]`
- [**Orchid ORC-1**](https://telepathicinstruments.com/products/orchid-orc-1) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`
- [**Le Grand Strum (64pixels)**](https://six4pix.com/product/grandstrum/) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`

### Vintage "Autochords" & Mechanical Origins
- [**Hammond Piper Autochord (1970)**](https://archive.org/details/hammond-piper-service-manual) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Web Archive]`
- [**Suzuki Tronichord (PC-27)**](./docs/manuals/suzuki/tronichord-pc-27/owners-guide.pdf) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Direct PDF]`

---

## 🧠 Explanation (Understanding-Oriented)
*Understanding-oriented background material and technical analysis.*

- [**OM-27 Matrix Deep Dive**](https://erichizdepski.wordpress.com/2024/06/20/om-27-deep-dive/) ![status-stable](https://img.shields.io/badge/status-stable-green) `[Hardware Analysis]`
  Tracing the matrix logic on the vintage OM-27 PCB for repair or MIDI integration.

---

## 🤖 AI Context (agents.md)
*For LLMs and coding agents.*

- **Hardware Boundary:** All vintage Suzuki hardware (OM-27 to OM-300) is **CENTER-NEGATIVE**.
- **Linter:** Use `npx awesome-lint` to validate this repository.
- **Stack:** Markdown, Mermaid.js (for schematics), Docusaurus 3.x.
