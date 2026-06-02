"""Generate data/spectrum/pe_custom_conversions/spectrum_emc.json.

Spectrum is very large and its machine recipes (pedestal/anvil_crushing/fusion_shrine/
spirit_instiller/...) extend the Recipe INTERFACE, not vanilla recipe classes, so ProjectE
cannot auto-derive their outputs. Full coverage would mean transcribing ~2000 custom recipes
across many schemas — out of scope for v0.1. This first pass seeds Spectrum's foundational
resources (gemstones, ores, key materials); the vanilla-recipe subset (shaped/stonecutting/
smelting/blasting) cascades from them. Deep machine-only content is intentionally not covered
yet, and stateful gear/trinkets have no EMC.

All item IDs below were verified present in the 1.11.8 jar's lang.
ProjectE NSS schema (1.21.1): values.before = list of {type,emc_value,id}.
"""

import json
import os

OUT = os.path.join(
    os.path.dirname(__file__),
    "..",
    "src",
    "main",
    "resources",
    "data",
    "spectrum",
    "pe_custom_conversions",
    "spectrum_emc.json",
)

# Foundational primitives (P2; ProjectE anchor: amethyst_shard 32). Gem tier per
# Spectrum progression: topaz < citrine < onyx < moonstone.
BEFORE = {
    "topaz_shard": 32,  # geode drop (amethyst-tier)
    "citrine_shard": 48,
    "onyx_shard": 64,
    "moonstone_shard": 128,  # capstone gem
    "raw_azurite": 64,  # mid-tier ore drop
    "raw_malachite": 96,
    "shimmerstone_gem": 128,
    "paltaeria_fragments": 256,  # late ore
    "stratine_fragments": 256,
    "bedrock_dust": 512,  # special "Shattered Bedrock"
    "neolith": 384,  # late spirit-instiller resource
    "quitoxic_powder": 64,
}


def main() -> None:
    doc = {
        "replace": False,
        "comment": (
            "Spectrum EMC integration for ProjectE (KURONAMI) — foundational coverage. "
            "Seeds gemstones/ores/key resources; vanilla recipes cascade. Spectrum's "
            "custom machine recipes are not auto-derivable, so deep machine-only content "
            "is not covered in v0.1. Stateful gear/trinkets have no EMC."
        ),
        "values": {
            "before": [
                {"type": "projecte:item", "emc_value": v, "id": f"spectrum:{k}"}
                for k, v in BEFORE.items()
            ]
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(doc, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"primitives={len(BEFORE)} -> {os.path.normpath(OUT)}")


if __name__ == "__main__":
    main()
