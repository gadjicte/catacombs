class materials:
   def __init__ (self, name:str, type:str) ->None:
    self.name= name
    self.type=type

#Basic crafting materials
iron_shards = materials("iron shards", "common")
bone_fragments = materials("bone fragments", "common")
ancient_leather = materials("ancient leather", "common")
cursed_wood = materials("cursed wood", "common")
ember_dust = materials("ember dust", "common")

#Weapon upgrade materials
blacksteel_ingot = materials("blacksteel ingot", "uncommon")
molten_core = materials("molten core", "rare")
obsidian_edge = materials("obsidian edge", "rare")
phantom_essence = materials("phantom essence", "epic")
echo_shard = materials("echo shard", "legendary") 

#Armor upgrade materials
spider_silk_cloth = materials("spider silk cloth", "uncommon")
stoneplate = materials("stoneplate", "rare")
soulthread = materials("soulthread", "epic")
voidscale = materials("voidscale", "legendary")

#Magical Enchantment materials
rune_dust = materials("rune dust", "common")
glowing_marrow = materials("glowing marrow", "uncommon")
mana_crystal = materials("mana crystal", "rare")
eldritch_eye = materials("eldritch eye", "epic")
catacomb_heart = materials("catacomb heart", "legendary")

#Common Herbs 
mossleaf = materials("mossleaf", "common")               # Mild healing herb
cave_mint = materials("cave mint", "common")             # Slight stamina regen
embergrass = materials("embergrass", "common")           # Boosts fire resistance temporarily
gravedust_root = materials("gravedust root", "common")   # Used in minor antidotes

#Uncommon Herbs
shadebloom = materials("shadebloom", "uncommon")         # Grants stealth for a short time
ghostberry = materials("ghostberry", "uncommon")         # Minor invisibility or spirit vision
moonpetal = materials("moonpetal", "uncommon")           # Regenerates health over time
ashen_thistle = materials("ashen thistle", "uncommon")   # Improves resistance to curses

#Rare and mythical Herbs
nightshade_lily = materials("nightshade lily", "rare")       # Used in powerful poisons
soulbloom = materials("soulbloom", "rare")                   # Restores both health and mana
cryptorchid = materials("cryptorchid", "rare")               # Boosts attack power temporarily
eldergloom = materials("eldergloom", "epic")                 # Used in resurrection or revive potions
bloodvine = materials("bloodvine", "legendary")              # Required for ultimate healing elixirs
