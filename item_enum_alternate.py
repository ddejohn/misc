from enum import Enum


# class ItemSubtype(Enum):
#     HELM = "helm"
#     HELMET = "helmet"
#     CUIRASS = "cuirass"
#     CORSLET = "corslet"
#     GAUNTLETS = "gauntlets"
#     SABATONS = "sabatons"
#     PAVISE_SHIELD = "pavise shield"
#     KITE_SHIELD = "kite shield"

#     HOOD = "hood"
#     COIF = "coif"
#     BRIGANDINE = "brigandine"
#     GAMBESON = "gambeson"
#     GLOVES = "gloves"
#     BOOTS = "boots"
#     BUCKLER = "buckler"
#     TARGE_SHIELD = "targe shield"

#     DAGGER = "dagger"
#     HALADIE_DAGGER = "haladie dagger"
#     CORVO = "corvo"
#     STILETTO = "stiletto"
#     SHORTSWORD = "shortsword"
#     FALCHION = "falchion"
#     SEAX = "seax"
#     CUTLASS = "cutlass"
#     RAPIER = "rapier"
#     KODACHI = "kodachi"
#     HOOK_SWORD = "hook sword"
#     WILLOW_LEAF_SABRE = "willow leaf sabre"
#     CHOKUTO = "chokuto"
#     JIAN = "jian"
#     XIPHOS = "xiphos"
#     BASELARD = "baselard"
#     GLADIUS = "gladius"

#     MORNING_STAR = "morning star"
#     MACE = "mace"
#     CLUB = "club"
#     FLAIL = "flail"

#     LABRYS = "labrys"
#     HATCHET = "hatchet"

#     LONGSWORD = "longsword"
#     CLAYMORE = "claymore"
#     ODACHI = "odachi"
#     DADAO = "dadao"
#     ESTOC = "estoc"
#     KATANA = "katana"
#     FLAMBERGE = "flamberge"
#     ZWEIHANDER = "zweihander"
#     BROADSWORD = "broadsword"
#     BASTARD_SWORD = "bastard sword"

#     WAR_HAMMER = "war hammer"
#     METEOR_HAMMER = "meteor hammer"
#     DIRE_FLAIL = "dire flail"

#     WAR_SCYTHE = "war scythe"
#     BATTLE_AXE = "battle axe"
#     HALBERD = "halberd"
#     GLAIVE = "glaive"

#     RECURVE_BOW = "recurve bow"
#     SCYTHIAN_BOW = "scythian bow"
#     CROSSBOW = "crossbow"
#     LONGBOW = "longbow"


# class OneHandedBlade(Enum):
#     DAGGER = "dagger"
#     HALADIE_DAGGER = "haladie dagger"
#     CORVO = "corvo"
#     STILETTO = "stiletto"
#     SHORTSWORD = "shortsword"
#     FALCHION = "falchion"
#     SEAX = "seax"
#     CUTLASS = "cutlass"
#     RAPIER = "rapier"
#     KODACHI = "kodachi"
#     HOOK_SWORD = "hook sword"
#     WILLOW_LEAF_SABRE = "willow leaf sabre"
#     CHOKUTO = "chokuto"
#     JIAN = "jian"
#     XIPHOS = "xiphos"
#     BASELARD = "baselard"
#     GLADIUS = "gladius"


# class OneHandedBlunt(Enum):
#     MORNING_STAR = "morning star"
#     MACE = "mace"
#     CLUB = "club"
#     FLAIL = "flail"


# class OneHandedAxe(Enum):
#     LABRYS = "labrys"
#     HATCHET = "hatchet"


# class TwoHandedBlade(Enum):
#     LONGSWORD = "longsword"
#     CLAYMORE = "claymore"
#     ODACHI = "odachi"
#     DADAO = "dadao"
#     ESTOC = "estoc"
#     KATANA = "katana"
#     FLAMBERGE = "flamberge"
#     ZWEIHANDER = "zweihander"
#     BROADSWORD = "broadsword"
#     BASTARD_SWORD = "bastard sword"


# class TwoHandedBlunt(Enum):
#     WAR_HAMMER = "war hammer"
#     METEOR_HAMMER = "meteor hammer"
#     DIRE_FLAIL = "dire flail"


# class TwoHandedAxe(Enum):
#     WAR_SCYTHE = "war scythe"
#     BATTLE_AXE = "battle axe"
#     HALBERD = "halberd"
#     GLAIVE = "glaive"


# class TwoHandedRanged(Enum):
#     RECURVE_BOW = "recurve bow"
#     SCYTHIAN_BOW = "scythian bow"
#     CROSSBOW = "crossbow"
#     LONGBOW = "longbow"


class Item(Enum):
    HELM = ('armor', 'heavy', 'head', 'helm')
    HELMET = ('armor', 'heavy', 'head', 'helmet')
    CUIRASS = ('armor', 'heavy', 'chest', 'cuirass')
    CORSLET = ('armor', 'heavy', 'chest', 'corslet')
    GAUNTLETS = ('armor', 'heavy', 'hands', 'gauntlets')
    SABATONS = ('armor', 'heavy', 'feet', 'sabatons')
    PAVISE_SHIELD = ('armor', 'heavy', 'shield', 'pavise shield')
    KITE_SHIELD = ('armor', 'heavy', 'shield', 'kite shield')
    HOOD = ('armor', 'light', 'head', 'hood')
    COIF = ('armor', 'light', 'head', 'coif')
    BRIGANDINE = ('armor', 'light', 'chest', 'brigandine')
    GAMBESON = ('armor', 'light', 'chest', 'gambeson')
    GLOVES = ('armor', 'light', 'hands', 'gloves')
    BOOTS = ('armor', 'light', 'feet', 'boots')
    BUCKLER = ('armor', 'light', 'shield', 'buckler')
    TARGE_SHIELD = ('armor', 'light', 'shield', 'targe shield')
    DAGGER = ('weapon', 'one-handed', 'blade', 'dagger')
    HALADIE_DAGGER = ('weapon', 'one-handed', 'blade', 'haladie dagger')
    CORVO = ('weapon', 'one-handed', 'blade', 'corvo')
    STILETTO = ('weapon', 'one-handed', 'blade', 'stiletto')
    SHORTSWORD = ('weapon', 'one-handed', 'blade', 'shortsword')
    FALCHION = ('weapon', 'one-handed', 'blade', 'falchion')
    SEAX = ('weapon', 'one-handed', 'blade', 'seax')
    CUTLASS = ('weapon', 'one-handed', 'blade', 'cutlass')
    RAPIER = ('weapon', 'one-handed', 'blade', 'rapier')
    KODACHI = ('weapon', 'one-handed', 'blade', 'kodachi')
    HOOK_SWORD = ('weapon', 'one-handed', 'blade', 'hook sword')
    WILLOW_LEAF_SABRE = ('weapon', 'one-handed', 'blade', 'willow leaf sabre')
    CHOKUTO = ('weapon', 'one-handed', 'blade', 'chokuto')
    JIAN = ('weapon', 'one-handed', 'blade', 'jian')
    XIPHOS = ('weapon', 'one-handed', 'blade', 'xiphos')
    BASELARD = ('weapon', 'one-handed', 'blade', 'baselard')
    GLADIUS = ('weapon', 'one-handed', 'blade', 'gladius')
    MORNING_STAR = ('weapon', 'one-handed', 'blunt', 'morning star')
    MACE = ('weapon', 'one-handed', 'blunt', 'mace')
    CLUB = ('weapon', 'one-handed', 'blunt', 'club')
    FLAIL = ('weapon', 'one-handed', 'blunt', 'flail')
    LABRYS = ('weapon', 'one-handed', 'axe', 'labrys')
    HATCHET = ('weapon', 'one-handed', 'axe', 'hatchet')
    LONGSWORD = ('weapon', 'two-handed', 'blade', 'longsword')
    CLAYMORE = ('weapon', 'two-handed', 'blade', 'claymore')
    ODACHI = ('weapon', 'two-handed', 'blade', 'odachi')
    DADAO = ('weapon', 'two-handed', 'blade', 'dadao')
    ESTOC = ('weapon', 'two-handed', 'blade', 'estoc')
    KATANA = ('weapon', 'two-handed', 'blade', 'katana')
    FLAMBERGE = ('weapon', 'two-handed', 'blade', 'flamberge')
    ZWEIHANDER = ('weapon', 'two-handed', 'blade', 'zweihander')
    BROADSWORD = ('weapon', 'two-handed', 'blade', 'broadsword')
    BASTARD_SWORD = ('weapon', 'two-handed', 'blade', 'bastard sword')
    WAR_HAMMER = ('weapon', 'two-handed', 'blunt', 'war hammer')
    METEOR_HAMMER = ('weapon', 'two-handed', 'blunt', 'meteor hammer')
    DIRE_FLAIL = ('weapon', 'two-handed', 'blunt', 'dire flail')
    WAR_SCYTHE = ('weapon', 'two-handed', 'axe', 'war scythe')
    BATTLE_AXE = ('weapon', 'two-handed', 'axe', 'battle axe')
    HALBERD = ('weapon', 'two-handed', 'axe', 'halberd')
    GLAIVE = ('weapon', 'two-handed', 'axe', 'glaive')
    RECURVE_BOW = ('weapon', 'two-handed', 'ranged', 'recurve bow')
    SCYTHIAN_BOW = ('weapon', 'two-handed', 'ranged', 'scythian bow')
    CROSSBOW = ('weapon', 'two-handed', 'ranged', 'crossbow')
    LONGBOW = ('weapon', 'two-handed', 'ranged', 'longbow')

    def __init__(self, item_class, item_subclass, item_type, item_subtype):
        self.item_class = item_class
        self.item_subclass = item_subclass
        self.item_type = item_type
        self.item_subtype = item_subtype
