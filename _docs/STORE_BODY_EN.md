<!-- Modrinth/CurseForge description source of truth. Paste verbatim into Modrinth;
     paste into CurseForge in MARKDOWN mode. Title/summary below are the search-indexed fields. -->

<!-- TITLE (<=64 chars): Spectrum ProjectE EMC -->
<!-- SUMMARY (search-indexed, plain text): ProjectE EMC for Spectrum: values its gemstones, ores and key resources so you can transmute them. Foundational first pass. -->

# Spectrum ProjectE EMC

Play [Spectrum](https://modrinth.com/mod/spectrum) with [ProjectE](https://modrinth.com/mod/projecte) and find its gems and ores have no EMC value? This add-on adds foundational EMC coverage.

## What it does

A **data-only** add-on that seeds EMC for Spectrum's foundational resources:

- **Hand-tuned EMC** for Spectrum's gemstones (Topaz / Citrine / Onyx / Moonstone shards) and mined resources (Raw Azurite, Raw Malachite, Shimmerstone, Paltaeria, Stratine, Neolith, Shattered Bedrock, Quitoxic Powder).
- The things crafted from these via the mod's vanilla-style recipes **derive their EMC automatically**.

It adds **no items, blocks or recipes** — only EMC data.

## Compatibility

| | 1.21.1 |
|---|---|
| NeoForge | ✅ |

Requires **ProjectE** and **Spectrum** (NeoForge 1.21.1).

## Install

Drop the jar into your `mods` folder alongside ProjectE and Spectrum. EMC values apply on world load — open a Transmutation Table to see them.

## Dependencies

- **ProjectE** — required
- **Spectrum** — required

## Scope & limitations

- NeoForge 1.21.1 only.
- **Foundational coverage only.** Spectrum is a very large mod whose machine recipes (Pedestal, Fusion Shrine, Spirit Instiller, etc.) are not auto-derivable by ProjectE, so deep machine-only content does not have EMC in this first version. The gemstones, ores and their direct craftables do.
- Stateful gear and trinkets intentionally carry no EMC.
- EMC values are a considered first pass; balance and coverage feedback is welcome via the issue tracker.

## License & credits

MIT. Spectrum is by DaFuqs & contributors (LGPL-3.0); ProjectE by sinkillerj & contributors. This add-on is an independent integration and is not affiliated with either.
