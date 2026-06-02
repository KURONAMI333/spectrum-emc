package com.kuronami.spectrumemc;

import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

/**
 * Spectrum ProjectE EMC — data-only integration (foundational coverage). EMC values
 * live in {@code data/spectrum/pe_custom_conversions/} (loaded by ProjectE via
 * datapack reload); this class only provides the {@code @Mod} entry point.
 */
@Mod(SpectrumEMC.MODID)
public final class SpectrumEMC {
    public static final String MODID = "spectrum_emc";
    public static final String VERSION = "0.1.0";
    private static final Logger LOGGER = LogUtils.getLogger();

    public SpectrumEMC(IEventBus modBus) {
        LOGGER.info("Spectrum ProjectE EMC v{} loading — EMC via data/spectrum/pe_custom_conversions", VERSION);
    }
}
