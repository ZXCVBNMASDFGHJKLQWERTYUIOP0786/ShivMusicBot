import random
from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle

import config
from AnonXMusic import app

# 🔥 PREMIUM EMOJIS LIST 🔥
# Yahan aap apne pasand ke Premium Emojis ke IDs daal sakte hain.
PREMIUM_EMOJIS = [
    "5422831825178206894", 
    "5368324170673489600",
    "5206607081334906820",
    "5206380668048496464"
]

def start_panel(_):
    # Har baar colors ko shuffle karenge
    styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
    random.shuffle(styles)
    style_map = {1: styles[0], 2: styles[1], 3: styles[2]}
    
    # Is row me 2 buttons hain, toh 2 button wala color milega
    row_2_btns_style = style_map.get(2) 
    
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], 
                url=f"https://t.me/{app.username}?startgroup=true",
                style=row_2_btns_style,
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_CHAT,
                style=row_2_btns_style,
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            ),
        ],
    ]
    return buttons


def private_panel(_):
    # Colors ko shuffle karke har line (row length) ke hisaab se assign karenge
    styles = [ButtonStyle.PRIMARY, ButtonStyle.SUCCESS, ButtonStyle.DANGER]
    random.shuffle(styles)
    style_map = {1: styles[0], 2: styles[1], 3: styles[2]}
    
    buttons = [
        [
            # Line me 1 button hai -> Color 1
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=style_map.get(1),
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            )
        ],
        [
            # Line me 1 button hai -> Color 1
            InlineKeyboardButton(
                text=_["S_B_4"], 
                callback_data="settings_back_helper",
                style=style_map.get(1),
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            )
        ],
        [
            # Line me 2 buttons hain -> Color 2
            InlineKeyboardButton(
                text=_["S_B_6"], 
                user_id=config.OWNER_ID,
                style=style_map.get(2),
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            ),
            InlineKeyboardButton(
                text=_["S_B_5"], 
                url=config.SUPPORT_CHANNEL,
                style=style_map.get(2),
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            ),
        ],
        [
            # Line me 1 button hai -> Color 1
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_CHAT,
                style=style_map.get(1),
                icon_custom_emoji_id=random.choice(PREMIUM_EMOJIS)
            ),
        ],
        # Source code wala button hata diya gaya hai ✅
    ]

    return buttons