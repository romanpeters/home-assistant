"""
"""

channel_dict =  {"animal_planet": [],
                 "apple_back": [],
                 "apple_down": [],
                 "apple_left": [],
                 "apple_ok": [],
                 "apple_playpause": [],
                 "apple_right": [],
                 "apple_up": [],
                 "ard": [],
                 "bbc_first": [],
                 "bbc_one": [],
                 "bbc_two": [],
                 "bbc_world_news": [],
                 "canvas": [],
                 "cnn": [],
                 "comedy_central": [],
                 "discovery_channel": [],
                 "disney_channel": [],
                 "een": [],
                 "entone_back": [],
                 "entone_channel_down": [],
                 "entone_channel_up": [],
                 "entone_down": [],
                 "entone_guide": [],
                 "entone_left": [],
                 "entone_menu": [],
                 "entone_ok": [],
                 "entone_right": [],
                 "entone_toggle": [],
                 "entone_up": [],
                 "euro_news": [],
                 "eurosport": [],
                 "fox": [],
                 "mtv": [],
                 "national_geographic": [],
                 "net_5": [],
                 "nickelodeon": [],
                 "npo_1": [],
                 "npo_1_extra": [],
                 "npo_2": [],
                 "npo_3": [],
                 "rtl_4": [],
                 "rtl_5": [],
                 "rtl_7": [],
                 "rtl_8": [],
                 "rtl_z": [],
                 "rtv_utrecht": [],
                 "sbs_6": [],
                 "sbs_9": [],
                 "sony_back": [],
                 "sony_down": [],
                 "sony_left": [],
                 "sony_menu": [],
                 "sony_mute": [],
                 "sony_ok": [],
                 "sony_right": [],
                 "sony_theatre": [],
                 "sony_up": [],
                 "sony_volume_higher": [],
                 "sony_volume_lower": [],
                 "sony_toggle": [],
                 "trt_turk": [],
                 "veronica_disney_xd": [],
                 "xite": [],
                 "zdf": [],
                 "ziggo_sport": [],
}

for k, v in channel_dict.items():



if packet:
    hass.services.call("switch", "broadlink_send_packet_10_10_10_203", 
                       service_data={"packet": packet})
else:
    logger.warning("IR packet lookup for {} failed.".format(button))
