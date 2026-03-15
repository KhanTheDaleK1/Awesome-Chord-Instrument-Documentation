# Awesome Chord Instruments 🎹✨

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Stability: Stable](https://img.shields.io/badge/stability-stable-green.svg)
![AI-Ready: Optimized](https://img.shields.io/badge/AI--Ready-Optimized-blue.svg)

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
- [**The Failed Instrument That Became an Ambient Legend**](https://youtu.be/R2GSSyd4liw) ![status-stable](https://img.shields.io/badge/status-stable-green) `[Documentary]`
  Hainbach explores the history and unique sound of the Omnichord.
- [**Omnichord Content Hub (Omnihub)**](https://sites.google.com/view/omnihub/home) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Community Hub]`
  The central directory for the Omnichord community, linking to Discord, Reddit, and specialized technical resources.

---

## ⚠️ Power & Polarity Safety (CRITICAL)
*Most vintage chord instruments use non-standard power polarities. Using the wrong adapter will cause permanent hardware failure.*

> [!CAUTION]
> **POLARITY MISMATCH:** Most modern 9V/12V adapters (like guitar pedal supplies) are **Center-Negative**. However, many vintage Yamaha units are **Center-Positive**, while Suzuki and Casio units are **Center-Negative**. Always verify the symbol on the chassis before plugging in.

### Quick Reference Polarity Table
| Brand | Series / Model | Voltage | Polarity | Recommended Tip |
| :--- | :--- | :--- | :--- | :--- |
| **Suzuki** | All Omnichords / QChord | 12V DC | **Center-Negative** | 2.1mm |
| **Casio** | VL-1, SK-Series, PT-Series| 6V-7.5V DC | **Center-Negative** | 2.1mm |
| **Yamaha** | QY-Series, QR-Series | 9V-12V DC | **Center-Positive** | 2.1mm |
| **Korg** | Poly-800 | 9V DC | **Center-Negative** | 2.1mm |
| **Roland** | Alpha Juno, PMA-5 | 9V DC | **Center-Negative** | 2.1mm |

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
- [**Modified Omnichord by Folktek**](https://youtu.be/R7FUiJN9Ehw) ![status-stable](https://img.shields.io/badge/status-stable-green) `[Demo]`
  A showcase of high-end circuit bending and modifications by Ben Houston.

---

## 📑 Reference (Information-Oriented)
*Information-oriented technical specs, genealogy, and archives.*

### Suzuki OM-Series Quick Reference
| Model | Year | Synthesis Type | Polarity | Key Feature |
| :--- | :--- | :--- | :--- | :--- |
| **OM-27** | 1981 | Hybrid Analog | **Center-Negative** | First Strumplate |
| **OM-36** | 1984 | Digital/Analog | **Center-Negative** | 84 Chord Support |
| **OM-84** | 1984 | Digital/Analog | **Center-Negative** | Chord Computer / Multi-Voice |
| **OM-100** | 1989 | PCM Wave | **Center-Negative** | Transition to Samples |
| **OM-200M** | 1989 | PCM Wave | **Center-Negative** | Native MIDI Implementation |
| **OM-300** | 1996 | PCM Wave | **Center-Negative** | 100 Voices / Pro MIDI |
| **QChord** | 1999 | PCM Wave | **Center-Negative** | QCard expansion Slot |
| **OM-108** | 2024 | PCM/Analog Modeling | **Center-Negative** | Modern MIDI / High Fidelity |

<details>
<summary><b>Suzuki OM-27 (1981)</b></summary>

- **Production:** 1981 – 1984 (Discontinued)
- **MSRP:** $200 – $300 (Launch) | **Current Market:** <!-- PRICE_OM-27_START -->TBD<!-- PRICE_OM-27_END -->
- **Notable Fact:** The first true Omnichord; Suzuki produced 40,000 units in the first year alone.

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-27/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**OM-27 Mk 1 Demo**](https://youtu.be/h1WIo7vhr1I) `[Demo]` (keyboard resource)
- [**OM-27 Mk II Demo**](https://youtu.be/Ihkwl6G9E5k) `[Demo]` (keyboard resource)
- [**Dabchick vs. Omnichord**](https://youtu.be/jfuSEdOdNz0) `[Demo]` (Barnaby Dixon)
- [**OM-27 Tutorial**](https://youtu.be/C8fHvffnfiY) `[Tutorial]` (Tiger Arcade)
- [**OM-27 Demo & Review**](https://youtu.be/zB9PtHTF2fE) `[Demo]` (Tiger Arcade)
- [**Schematic (Primary)**](https://circuitbending.miraheze.org/wiki/File:OM27_Schematic.pdf) `[Direct PDF]`
- [**Schematic (Mirror)**](https://www.scribd.com/document/720477103/Suzuki-Omnichord-OM-27-schematics) `[Scribd]`
- [**Repair Deep Dive**](https://erichizdepski.wordpress.com/2020/03/28/omnichord-om-27-repair/) `[Technical Log]`
</details>

<details>
<summary><b>Suzuki OM-36 System One (1984)</b></summary>

- **Production:** 1984 – 1989 (Discontinued)
- **MSRP:** £99 (Launch)
- **Notable Fact:** Known as "System One," it updated the original design with 36 chords (later expandable to 84).

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-36/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**Schematic Note**](https://www.reddit.com/r/Omnichord/comments/13wdvvf/om36_schematic/) `[Technical Note]`
</details>

<details>
<summary><b>Suzuki OM-84 System Two (1984)</b></summary>

- **Production:** 1984 – 1989 (Discontinued)
- **MSRP:** £99 (Launch) | **Current Market:** <!-- PRICE_OM-84_START -->TBD<!-- PRICE_OM-84_END -->
- **Notable Fact:** "System Two" introduced dual strumplate voices and the first integrated chord memory sequencer.

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-84/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](https://www.popsmusic.com/uploads/3/0/6/8/30682235/om84_owners_manual.pdf) `[Direct PDF]`
- [**OM-84 System Two Demo**](https://youtu.be/Oiz2m0AmgIQ) `[Demo]` (keyboard resource)
- [**Modified OM-84 by Folktek**](https://youtu.be/VOqLSI2w_Ak) `[Demo]` (Folktek)
- [**User Guide (Mirror)**](https://www.scribd.com/document/664559485/SUZUKI-OMNICHORD-om84-owners-manual) `[Scribd]`
- [**Schematic**](https://www.scribd.com/document/720477279/Suzuki-Omnichord-OM-84-schematics) `[Scribd]`
- [**Repair Documentation**](https://erichizdepski.wordpress.com/2017/11/11/suzuki-omnichord-om-84-repair/) `[Technical Log]`
</details>

<details>
<summary><b>Suzuki OM-100 / OM-200M (1989)</b></summary>

- **Production:** 1989 – 1993 (Discontinued)
- **MSRP:** $229 (OM-100) / $299 (OM-200M)
- **Notable Fact:** The OM-200M was the first model to feature native MIDI Out, enabling control of external synths.

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-100-200m/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**OM-100 Demo**](https://youtu.be/ZEW6ff9TJ4c) `[Demo]` (keyboard resource)
- [**OM-200M Demo**](https://youtu.be/1UKz0euYX5U) `[Demo]` (keyboard resource)
- [**Circuit Bent OM-200m**](https://youtu.be/FOVBIwl1WH0) `[Demo]` (Notch Audio)
- [**Schematic**](https://circuitbending.miraheze.org/wiki/Suzuki_Omnichord) `[Wiki]`
</details>

<details>
<summary><b>Suzuki OM-150 / OM-250M (1993)</b></summary>

- **Production:** 1993 – 1996 (Discontinued)
- **MSRP:** ~$250 - $300
- **Notable Fact:** These models refined the PCM sounds and ergonomics before the transition to the OM-300.

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/om-150-250m/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Web)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**OM-150 All Sounds**](https://youtu.be/U-xYnzPi2ng) `[Demo]` (General Jams)
- [**OM-150 Chill Bubbles**](https://youtu.be/5CxUwLbMw_0) `[Demo]` (General Jams)
- [**OM-250M Demo**](https://youtu.be/5axBQ83S348) `[Demo]` (keyboard resource)
</details>

<details>
<summary><b>Suzuki OM-300 (1996)</b></summary>

- **Production:** 1996 (Discontinued 1996)
- **MSRP:** $300+ (Launch)
- **Notable Fact:** Extremely rare final original model; its drum preset is the foundation of the Gorillaz hit "Clint Eastwood."

- [**User Guide (Primary)**](https://device.report/Omnichord/OM300) `[Web View]`
- [**User Guide (Mirror)**](http://www.omnichord-heaven.com/owners_guides.html) `[Web Archive]`
- [**OM-300 Demo**](https://youtu.be/KdtR_TREAyQ) `[Demo]` (keyboard resource)
</details>

<details>
<summary><b>Suzuki QChord QC-1 (1999)</b></summary>

- **Production:** 1999 – 2020 (Discontinued)
- **MSRP:** $250 (Launch) | **Current Market:** <!-- PRICE_QCHORD_START -->TBD<!-- PRICE_QCHORD_END -->
- **Notable Fact:** A digital reimagining with 100 voices and a QCard expansion slot for proprietary song cartridges.

- [**User Guide (Local PDF)**](./docs/manuals/suzuki/qchord/owners-guide.pdf) `[Direct PDF]`
- [**User Guide (Primary)**](https://www.omnichord-heaven.com/downloads/manuals/qchord-manual.pdf) `[Direct PDF]`
- [**User Guide (Mirror)**](https://www.qchord.net/docs/qchord-manual.html) `[HTML]`
- [**Qchord QC-1 Demo**](https://youtu.be/eBE4HK-Q5sk) `[Demo]` (keyboard resource)
- [**Schematic**](https://www.scribd.com/document/720477201/Suzuki-Q-Chord-Schematic) `[Scribd]`
- [**Repair Documentation**](https://www.popsmusic.com/qchord-do-it-yourself-repair-help.html) `[Repair Guide]`
</details>

<details>
<summary><b>Suzuki OM-108 (2024)</b></summary>

- **Production:** 2024 – Present (Active)
- **MSRP:** $800+ (Launch)
- **Notable Fact:** A 70th-anniversary tribute that returns to analog-voiced synthesis while expanding to 108 chords.

- [**Official Manual (Local PDF)**](./docs/manuals/suzuki/om-108/owners-guide.pdf) `[Direct PDF]`
- [**Official Manual (Web)**](https://www.suzuki-music.co.jp/manual/om-108_en) `[Direct PDF]`
</details>

### Iconic Chord Keyboards & Pocket Stations
Quick-reference for the essential hardware that defined portable chord sequencing and sampling. For community-driven resources on these and similar instruments, see [**Omnihub**](https://sites.google.com/view/omnihub/home).

| Product | Years | Type | Polarity | Key Chord Feature |
| :--- | :--- | :--- | :--- | :--- |
| **Casio VL-1** | 1979-1984 | Calculator Synth | **Center-Negative** | One-Key Sequenced Chords |
| **Casio PT-30/50** | 1983-1987 | Compact Keyboard | **Center-Negative** | Dedicated Accordion-style Chord Buttons |
| **Korg Poly-800** | 1983-1988 | Polyphonic Synth | **Center-Negative** | Dedicated "Chord Memory" Button |
| **Casio SK-Series** | 1985-1992 | Lo-Fi Sampler | **Center-Negative** | Polyphonic Sample-to-Chord Mapping |
| **Roland Alpha Juno**| 1985-1988 | Analog Poly | **Internal (AC)** | House-style "One-Finger" Chord Memory |
| **Yamaha VSS-Series**| 1987-1991 | Vocal Sampler | **Center-Positive** | Harmonic Texture/Modulated Pads |
| **Yamaha QY-Series** | 1990-2014 | Walkstation | **Center-Positive** | 8-Track Pocket Chord Sequencer |
| **Roland PMA-5** | 1995-1999 | Music PDA | **Center-Negative** | Stylus-driven Touch Chord Interface |
| **Yamaha DJX-Series**| 1998-2002 | Dance Keyboard | **Center-Positive** | Rhythmic Chord Manipulation / Loops |

<details>
<summary><b>Yamaha QY & QR series (Pocket Walkstations)</b></summary>

> [!IMPORTANT]
> **Power Specs:** 12V DC, **Center-Positive** (Yamaha PA-3B/PA-130 Standard).

#### **Yamaha QY10** (1990-1995)
- **Production:** 1990 – 1995 (Discontinued)
- **MSRP:** $399 (Launch)
- **Notable Fact:** The first "Walkstation," designed to be roughly the size of a VHS tape for mobile composing.
- [**Historical Overview**](https://en.wikipedia.org/wiki/Yamaha_QY10) `[Wiki]`
- [**Operating Manual**](https://usa.yamaha.com/files/download/other_assets/5/317585/QY10E.PDF) `[Direct PDF]`
- [**Service Manual**](https://archive.org/details/yamaha-qy10-service-manual) `[Web Archive]`

#### **Yamaha QY20** (1992-1997)
- **Production:** 1992 – 1997 (Discontinued)
- **MSRP:** ~$450 (Launch)
- **Notable Fact:** Introduced a much larger graphic display and a 2-octave micro-keyboard for easier data entry.
- [**Historical Overview**](https://synthmania.com/yamaha-qy20/) `[Web Archive]`
- [**Operating Manual**](https://usa.yamaha.com/files/download/other_assets/7/318357/QY20E.PDF) `[Direct PDF]`
- [**Battery Replacement Guide**](https://www.ifixit.com/Guide/Yamaha+QY20+Internal+Battery+Replacement/100000) `[How-To]`

#### **Yamaha QR10** (1993-1996)
- **Production:** 1993 – 1996 (Discontinued)
- **MSRP:** ~$350 (Launch)
- **Notable Fact:** Marketed as a "Music Accompaniment Player" with a built-in 8-bit sampler for capturing quick ideas.
- [**Historical Overview**](https://en.wikipedia.org/wiki/Yamaha_QY10) `[Wiki]`
- [**Operating Manual**](https://usa.yamaha.com/files/download/other_assets/4/317584/QR10E.PDF) `[Direct PDF]`

#### **Yamaha QY70** (1997-2001)
- **Production:** 1997 – 2001 (Discontinued)
- **MSRP:** ~$599 (Launch)
- **Notable Fact:** The first portable QY with full Yamaha XG support, featuring over 500 high-quality voices.
- [**Historical Overview**](https://synthpedia.net/yamaha/qy70/) `[Reference]`
- [**Service Manual**](https://archive.org/details/yamaha-qy70-service-manual) `[Web Archive]`

#### **Yamaha QY100** (1998-2014)
- **Production:** 2001 – 2014 (Discontinued)
- **MSRP:** ~$649 (Launch)
- **Notable Fact:** The peak of the series; added a guitar/mic input with amp simulation and SmartMedia storage.
- [**Historical Overview**](https://synthpedia.net/yamaha/qy100/) `[Reference]`
- [**Operating Manual**](https://usa.yamaha.com/files/download/other_assets/3/319683/QY100E.pdf) `[Direct PDF]`
</details>

<details>
<summary><b>Casio SK & PT series (Sampling & Portable)</b></summary>

> [!IMPORTANT]
> **Power Specs:** 6V to 7.5V DC, **Center-Negative** (Casio AD-1/AD-4160 Standard).

#### **Casio SK-1** (1985-1988)
- **Production:** 1985 – 1988 (Discontinued)
- **MSRP:** $139 (Launch)
- **Notable Fact:** Democratized sampling technology; its 8-bit lo-fi sound became a staple of early hip-hop and indie.
- [**Historical Overview**](https://web.casio.com/emi/40th/history/sk-1.html) `[Official]`
- [**Service Manual**](https://warningwillrobinson.com.au/manuals/Casio%20SK-1%20Service%20manual.pdf) `[Direct PDF]`
- [**Modification (Circuit Bending)**](https://www.anti-theory.com/soundart/circuitbend/cb04.html) `[Technical Guide]`

#### **Casio SK-5** (1987-1990)
- **Production:** 1987 – 1990 (Discontinued)
- **MSRP:** ~$100 (Launch)
- **Notable Fact:** Added four dedicated sample pads for "preset" samples like a barking dog and surf noises.
- [**Historical Overview**](https://www.perfectcircuit.com/signal/casio-sk1-history) `[Article]`
- [**Service Manual**](https://archive.org/details/casio-sk-5-service-manual) `[Web Archive]`

#### **Casio SK-8** (1987-1991)
- **Production:** 1987 – 1991 (Discontinued)
- **MSRP:** ~$150 (Launch)
- **Notable Fact:** A "Melody Guide" variant with light-up keys and a ROM pack slot for song expansion.
- [**Historical Overview**](https://www.casio.com/jp/electronic-musical-instruments/) `[Official]`
- [**Operating Manual**](https://www.manualslib.com/manual/1218084/Casio-Sk-8.html) `[Web View]`

#### **Casio SK-200** (1987-1992)
- **Production:** 1987 – 1992 (Discontinued)
- **MSRP:** ~$200 (Launch)
- **Notable Fact:** A more professional SK variant with larger keys and improved synthesis features.
- [**Historical Overview**](https://www.vintagesynth.com/casio/sk200.php) `[Wiki]`

#### **Casio PT-30** (1983-1986)
- **Production:** 1983 – 1986 (Discontinued)
- **MSRP:** ~$120 (Launch)
- **Notable Fact:** Features a "Harmony Arranger" that automatically creates chord accompaniments for melodies.
- [**Historical Overview**](https://www.muzines.co.uk/articles/casio-pt-30/11981) `[Article]`
- [**Service Manual**](https://archive.org/details/casio-pt-30-service-manual) `[Web Archive]`

#### **Casio PT-50** (1983-1987)
- **Production:** 1983 – 1987 (Discontinued)
- **MSRP:** ~$150 (Launch)
- **Notable Fact:** Famously appeared as a background prop in the 1984 movie *Gremlins*.
- [**Historical Overview**](https://www.casio.com/jp/electronic-musical-instruments/) `[Official]`

#### **Casio VL-1** (1979-1984)
- **Production:** 1979 – 1984 (Discontinued)
- **MSRP:** $69.95 (Launch)
- **Notable Fact:** The first commercial digital synth; features a calculator and the "Da Da Da" rhythm preset.
- [**Historical Overview**](https://en.wikipedia.org/wiki/Casio_VL-1) `[Wiki]`
- [**Service Manual**](https://archive.org/details/casio-vl-1-service-manual) `[Web Archive]`
</details>

<details>
<summary><b>Yamaha VSS & DJX series (Performance & Dance)</b></summary>

#### **Yamaha VSS-30** (1987-1989)
- **Production:** 1987 – 1989 (Discontinued)
- **MSRP:** ~$100 (Launch)
- **Notable Fact:** A cult-classic 8-bit sampler used extensively by Sigur Rós for its unique "U-Turn" loop mode.
- [**Historical Overview**](https://www.vintagesynth.com/yamaha/vss30.php) `[Wiki]`
- [**Service Manual**](https://archive.org/details/yamaha-vss-30-service-manual) `[Web Archive]`

#### **Yamaha VSS-200** (1988-1991)
- **Production:** 1988 – 1991 (Discontinued)
- **MSRP:** ~$180 (Launch)
- **Notable Fact:** Features 9 DSP effects (Fuzz, Echo, FM modulation) for creative sample manipulation.
- [**Historical Overview**](https://synthmania.com/yamaha-vss-200/) `[Web Archive]`
- [**Operating Manual**](https://usa.yamaha.com/files/download/other_assets/2/322302/VSS200E.pdf) `[Direct PDF]`

#### **Yamaha DJX-1** (1998-2000)
- **Production:** 1998 – 2000 (Discontinued)
- **MSRP:** $500 (Launch)
- **Notable Fact:** Features a ribbon controller and assignable knobs tailored for late-90s dance music production.
- [**Historical Overview**](https://www.vintagesynth.com/yamaha/djx.php) `[Wiki]`
- [**Service Manual**](https://archive.org/details/yamaha-djx-psr-d1-service-manual) `[Web Archive]`

#### **Yamaha DJX-II** (2000-2002)
- **Production:** 2000 – 2002 (Discontinued)
- **MSRP:** ~$450 (Launch)
- **Notable Fact:** Notable for lacking standard MIDI note transmission; it only transmits system clock and data.
- [**Historical Overview**](https://synthmania.com/2005/02/22/yamaha-djx-iib/) `[Web Archive]`
- [**Operating Manual**](https://usa.yamaha.com/files/download/other_assets/2/319592/DJXIIE.pdf) `[Direct PDF]`
</details>

<details>
<summary><b>Korg & Roland (Classic Synthesis & PDA)</b></summary>

#### **Korg Poly-800** (1983-1987)
- **Production:** 1983 – 1987 (Discontinued)
- **MSRP:** $795 (Launch) | **Current Market:** <!-- PRICE_POLY800_START -->TBD<!-- PRICE_POLY800_END -->
- **Notable Fact:** The first programmable poly-synth under $1k; features pegs for use with a guitar strap as a keytar.
- [**Historical Overview**](https://en.wikipedia.org/wiki/Korg_Poly-800) `[Wiki]`
- [**Service Manual**](http://www.synfo.nl/servicemanuals/Korg/POLY-800_SERVICE_MANUAL.pdf) `[Direct PDF]`
- [**Modification (Moog Slayer)**](https://www.synthtopia.com/content/2008/01/29/korg-poly-800-moog-slayer-mod/) `[How-To]`

#### **Korg Poly-800 II** (1986-1988)
- **Production:** 1986 – 1988 (Discontinued)
- **MSRP:** ~$850 (Launch)
- **Notable Fact:** Updated the original with a digital delay and an improved filter, often preferred by modern collectors.
- [**Historical Overview**](https://www.vintagesynth.com/korg/poly800.php) `[Wiki]`
- [**Battery Leak Repair Guide**](https://www.youtube.com/watch?v=korg-poly-800-battery-fix) `[Video Guide]`

#### **Roland Alpha Juno-1** (1985-1987)
- **Production:** 1985 – 1987 (Discontinued)
- **MSRP:** $895 (Launch)
- **Notable Fact:** Famous for the "Hoover" sound (Preset 86) which became a foundational element of rave and techno.
- [**Historical Overview**](https://www.vintagesynth.com/roland/ajuno1.php) `[Wiki]`
- [**Service Manual**](http://www.synfo.nl/servicemanuals/Roland/JU-1_SERVICE_NOTES.pdf) `[Direct PDF]`

#### **Roland Alpha Juno-2** (1985-1988)
- **Production:** 1985 – 1988 (Discontinued)
- **MSRP:** $1,295 (Launch)
- **Notable Fact:** Adds a 61-note keyboard with velocity and aftertouch, plus a cartridge slot for additional patches.
- [**Historical Overview**](https://www.vintagesynth.com/roland/ajuno2.php) `[Wiki]`
- [**Service Manual**](http://www.synfo.nl/servicemanuals/Roland/JU-2_SERVICE_NOTES.pdf) `[Direct PDF]`

#### **Roland PMA-5** (1995-1999)
- **Production:** 1996 – 2001 (Discontinued)
- **MSRP:** $595 (Launch)
- **Notable Fact:** A handheld music workstation with a stylus-driven touchscreen interface, unique for its time.
- [**Historical Overview**](https://southsideguitars.com.au/products/roland-pma-5) `[Reference]`
- [**Operating Manual**](https://cdn.roland.com/assets/media/pdf/PMA-5_OM.pdf) `[Direct PDF]`
</details>

### Modern Boutique Instruments
- [**Pocket Audio HiChord**](https://hichord.shop/) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`
- [**Minichord (Benjamin Poilvé)**](https://minichord.com/) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`
- [**Minichord GitHub Repository**](https://github.com/BenjaminPoilve/minichord) ![status-open-source](https://img.shields.io/badge/status-open--source-brightgreen) `[GitHub Repo]`
- [**Orchid ORC-1**](https://telepathicinstruments.com/products/orchid-orc-1) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`
- [**Le Grand Strum (64pixels)**](https://six4pix.com/product/grandstrum/) ![status-maintained](https://img.shields.io/badge/status-maintained-blue) `[Hardware]`

### Vintage "Autochords" & Mechanical Origins
- [**Hammond Piper Autochord (1970)**](https://archive.org/details/hammond-piper-service-manual) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Web Archive]`
  - **Production:** 1970 – 1979 (Discontinued)
  - **MSRP:** <$1,000 (Launch)
  - **Notable Fact:** The first instrument to feature "automatic chording," famously endorsed by Duke Ellington.
- [**Suzuki Tronichord (PC-27)**](./docs/manuals/suzuki/tronichord-pc-27/owners-guide.pdf) ![status-legacy](https://img.shields.io/badge/status-legacy-yellow) `[Direct PDF]`
  - **Production:** 1980 – 1981 (Discontinued)
  - **MSRP:** ~$150 (Launch)
  - **Notable Fact:** The direct precursor to the Omnichord; extremely rare and marketed as the "Portachord."

---

## 🧠 Explanation (Understanding-Oriented)
*Understanding-oriented background material and technical analysis.*

- [**OM-27 Matrix Deep Dive**](https://erichizdepski.wordpress.com/2024/06/20/om-27-deep-dive/) ![status-stable](https://img.shields.io/badge/status-stable-green) `[Hardware Analysis]`
  Tracing the matrix logic on the vintage OM-27 PCB for repair or MIDI integration.

---

## 🙏 Special Thanks
*Acknowledging the pioneers of chord instrument preservation.*

- [**Omnichord Heaven**](https://www.omnichord-heaven.com/) - The ultimate Suzuki Omnichord and Qchord resource library. This repository owes a massive debt to their decades of archiving, repair documentation, and community building.
- [**Omnihub (OmniHoard)**](https://sites.google.com/view/omnihub/home) - A community-driven central repository that aggregates creators, documentation, and technical advice for Suzuki instruments.
- [**Yamaha Corporation**](https://usa.yamaha.com/) - For providing exhaustive and accessible PDF archives of their heritage products (QY, VSS, and DJX series).
- [**Internet Archive (Archive.org)**](https://archive.org/) - For preserving critical, out-of-print service manuals and technical documentation for legacy hardware.
- [**Vintage Synth Explorer**](https://www.vintagesynth.com/) - For maintaining the premier historical database and specifications for classic synthesizers and samplers.
- [**Erich Izdepski**](https://erichizdepski.wordpress.com/) - For providing high-fidelity hardware deep-dives and technical repair logs that enable modern preservation.
- [**Synfo.nl**](http://www.synfo.nl/) - For hosting essential technical service notes and schematics for Roland and Korg hardware.
- [**Synthmania**](https://synthmania.com/) - For their high-quality technical overviews and audio references for vintage gear.
- [**Circuit Bending Wiki**](https://circuitbending.miraheze.org/) - For detailed community-driven technical schematics and modification data.
- [**Scribd**](https://www.scribd.com/) - For serving as a critical mirror host for redundant technical documentation.

---

## 🤖 AI Context (agents.md)
*For LLMs and coding agents.*

- **Hardware Boundary:** All vintage Suzuki hardware (OM-27 to OM-300) is **CENTER-NEGATIVE**.
- **Linter:** Use `npx awesome-lint` to validate this repository.
- **Stack:** Markdown, Mermaid.js (for schematics), Docusaurus 3.x.
