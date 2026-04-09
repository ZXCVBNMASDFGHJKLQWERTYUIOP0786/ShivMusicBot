import random
from typing import Union

from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonXMusic import app

# 🔥 PREMIUM EMOJIS LIST 🔥
# Yahan aap apne pasand ke Premium Emojis ke IDs daal sakte hain. (Aap jitne chahein utne IDs add kar sakte hain)
PREMIUM_EMOJIS = [
    "5422831825178206894", # Example 1
    "5368324170673489600", # Example 2
    "5206607081334906820", # Aap apna naya ID yahan add karein
    "5206380668048496464", # Ek aur naya ID
]

def help_pannel(_, is_sudo, START: Union[bool, int] = None):
    # 1️⃣ Har baar colors ko shuffle karenge taaki hamesha Random Colors aayein
    styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
    random.shuffle(styles)
    
    # 2️⃣ Smart Logic: Line (Row) me kitne buttons hain, us hisaab se color assign hoga
    style_map = {
        1: styles[0], 
        2: styles[1], 
        3: styles[2]  
    }

    # Buttons ka Raw Data (Text, Callback)
    raw_layout = [
        [(_["H_B_1"], "help_callback hb1"), (_["H_B_2"], "help_callback hb2"), (_["H_B_3"], "help_callback hb3")],
        [(_["H_B_4"], "help_callback hb4"), (_["H_B_5"], "help_callback hb5"), (_["H_B_6"], "help_callback hb6")],
        [(_["H_B_7"], "help_callback hb7"), (_["H_B_8"], "help_callback hb8"), (_["H_B_9"], "help_callback hb9")],
        [(_["H_B_10"], "help_callback hb10"), (_["H_B_11"], "help_callback hb11"), (_["H_B_12"], "help_callback hb12")],
        [(_["H_B_13"], "help_callback hb13"), (_["H_B_14"], "help_callback hb14"), (_["H_B_15"], "help_callback hb15")],
    ]

    # Sudo Users ke liye 1 button wali line
    if is_sudo:
        raw_layout.append([("Ai/TTS/IMAGE Settings", "help_callback hb16")])

    # Back / Close ke liye 1 button wali line
    if START:
        raw_layout.append([(_["BACK_BUTTON"], "settingsback_helper")])
    else:
        raw_layout.append([(_["CLOSE_BUTTON"], "close")])

    # 3️⃣ Dynamically Buttons Create Karna (Colors aur Emojis ke sath)
    upl = []
    for row in raw_layout:
        row_length = len(row) 
        row_style = style_map.get(row_length, ButtonStyle.PRIMARY) 
        
        button_row = []
        for text, cb in row:
            button_row.append(
                InlineKeyboardButton(
                    text=text,
                    callback_data=cb,
                    style=row_style, 
                    icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS) # 🔥 Ye code automatically list me se Premium emoji utha lega
                )
            )
        upl.append(button_row)

    return InlineKeyboardMarkup(upl)


def help_back_markup(_):
    styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                    style=random.choice(styles),
                    icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
                ),
            ]
        ]
    )


def private_help_panel(_):
    styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
    return [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                style=random.choice(styles),
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            ),
        ],
    ]