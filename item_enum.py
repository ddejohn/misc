from enum import Enum


class ItemSubtype(Enum):
    HELM = "helm"
    HELMET = "helmet"
    CUIRASS = "cuirass"
    CORSLET = "corslet"
    GAUNTLETS = "gauntlets"
    SABATONS = "sabatons"
    PAVISE_SHIELD = "pavise shield"
    KITE_SHIELD = "kite shield"
    HOOD = "hood"
    COIF = "coif"
    BRIGANDINE = "brigandine"
    GAMBESON = "gambeson"
    GLOVES = "gloves"
    BOOTS = "boots"
    BUCKLER = "buckler"
    TARGE_SHIELD = "targe shield"
    DAGGER = "dagger"
    HALADIE_DAGGER = "haladie dagger"
    CORVO = "corvo"
    STILETTO = "stiletto"
    SHORTSWORD = "shortsword"
    FALCHION = "falchion"
    SEAX = "seax"
    CUTLASS = "cutlass"
    RAPIER = "rapier"
    KODACHI = "kodachi"
    HOOK_SWORD = "hook sword"
    WILLOW_LEAF_SABRE = "willow leaf sabre"
    CHOKUTO = "chokuto"
    JIAN = "jian"
    XIPHOS = "xiphos"
    BASELARD = "baselard"
    GLADIUS = "gladius"
    MORNING_STAR = "morning star"
    MACE = "mace"
    CLUB = "club"
    FLAIL = "flail"
    LABRYS = "labrys"
    HATCHET = "hatchet"
    LONGSWORD = "longsword"
    CLAYMORE = "claymore"
    ODACHI = "odachi"
    DADAO = "dadao"
    ESTOC = "estoc"
    KATANA = "katana"
    FLAMBERGE = "flamberge"
    ZWEIHANDER = "zweihander"
    BROADSWORD = "broadsword"
    BASTARD_SWORD = "bastard sword"
    WAR_HAMMER = "war hammer"
    METEOR_HAMMER = "meteor hammer"
    DIRE_FLAIL = "dire flail"
    WAR_SCYTHE = "war scythe"
    BATTLE_AXE = "battle axe"
    HALBERD = "halberd"
    GLAIVE = "glaive"
    RECURVE_BOW = "recurve bow"
    SCYTHIAN_BOW = "scythian bow"
    CROSSBOW = "crossbow"
    LONGBOW = "longbow"


class ItemType(Enum):
    HEAD = "head"
    CHEST = "chest"
    HANDS = "hands"
    FEET = "feet"
    SHIELD = "shield"
    BLADE = "blade"
    BLUNT = "blunt"
    AXE = "axe"
    RANGED = "ranged"


class ItemSubclass(Enum):
    ONE_HANDED = "one-handed"
    TWO_HANDED = "two-handed"
    HEAVY = "heavy"
    LIGHT = "light"


class ItemClass(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"

    def __init__(self, item_class, item_subclass, item_type, item_subtype):
        self.item_class = item_class
        self.item_subclass = ItemClass(item_subclass)
        self.item_type = ItemType(item_type)
        self.item_subtype = ItemSubtype(item_subtype)
