import sqlite3

con = sqlite3.connect('run_report_db.db')
cur = con.cursor()

cur.executescript(
    '''
    CREATE TABLE Run_Meta_Data (
        Run_ID TEXT NOT NULL,
        Game_Mode TEXT NOT NULL,
        Difficulty TEXT NOT NULL,
        Ending TEXT NOT NULL,
        Run_Date TEXT NOT NULL,
        PRIMARY KEY (Run_ID)
    );
    
    CREATE TABLE Player_Info (
        Run_ID TEXT NOT NULL,
        Player_Name TEXT NOT NULL,
        Survivor TEXT NOT NULL,
        Total_Time_Alive REAL NOT NULL,
        Total_Distance_Traveled REAL NOT NULL,
        Died TEXT NOT NULL,
        Killer TEXT NOT NULL,
        Highest_Level INTEGER NOT NULL,
        Total_Deaths INTEGER NOT NULL,
        PRIMARY KEY (Run_ID, Player_Name),
        FOREIGN KEY (Run_ID) REFERENCES Run_Meta_Data(Run_ID)
    );

    CREATE TABLE Damage_Stats (
        Run_ID TEXT NOT NULL,
        Total_Minion_Damage_Dealt INTEGER DEFAULT 0,
        Total_Damage_Dealt INTEGER DEFAULT 0,
        Total_Damage_Taken INTEGER DEFAULT 0,
        Total_Health_Healed INTEGER DEFAULT 0,
        Highest_Damage_Dealt INTEGER DEFAULT 0,
        Damage_Dealt_To_BEETLE INTEGER DEFAULT 0,
        Damage_Dealt_To_BEETLEGUARD INTEGER DEFAULT 0,
        Damage_Dealt_To_BISON INTEGER DEFAULT 0,
        Damage_Dealt_To_GOLEM INTEGER DEFAULT 0,
        Damage_Dealt_To_WISP INTEGER DEFAULT 0,
        Damage_Dealt_To_GREATERWISP INTEGER DEFAULT 0,
        Damage_Dealt_To_LEMURIAN INTEGER DEFAULT 0,
        Damage_Dealt_To_LEMURIANBRUISER INTEGER DEFAULT 0,
        Damage_Dealt_To_IMP INTEGER DEFAULT 0,
        Damage_Dealt_To_JELLYFISH INTEGER DEFAULT 0,
        Damage_Dealt_To_CLAY INTEGER DEFAULT 0,
        Damage_Dealt_To_HERMIT_CRAB INTEGER DEFAULT 0,
        Damage_Dealt_To_BELL INTEGER DEFAULT 0,
        Damage_Dealt_To_CLAYBRUISER INTEGER DEFAULT 0,
        Damage_Dealt_To_VULTURE INTEGER DEFAULT 0,
        Damage_Dealt_To_ROBOBALLMINI INTEGER DEFAULT 0,
        Damage_Dealt_To_NULLIFIER INTEGER DEFAULT 0,
        Damage_Dealt_To_PARENT INTEGER DEFAULT 0,
        Damage_Dealt_To_MINIMUSHROOM INTEGER DEFAULT 0,
        Damage_Dealt_To_POD INTEGER DEFAULT 0,
        Damage_Dealt_To_LUNARWISP INTEGER DEFAULT 0,
        Damage_Dealt_To_LUNARGOLEM INTEGER DEFAULT 0,
        Damage_Dealt_To_LUNAREXPLODER INTEGER DEFAULT 0,
        Damage_Dealt_To_BEETLEQUEEN INTEGER DEFAULT 0,
        Damage_Dealt_To_CLAYBOSS INTEGER DEFAULT 0,
        Damage_Dealt_To_TITAN INTEGER DEFAULT 0,
        Damage_Dealt_To_TITANGOLD INTEGER DEFAULT 0,
        Damage_Dealt_To_VAGRANT INTEGER DEFAULT 0,
        Damage_Dealt_To_MAGMAWORM INTEGER DEFAULT 0,
        Damage_Dealt_To_ELECTRICWORM INTEGER DEFAULT 0,
        Damage_Dealt_To_IMPBOSS INTEGER DEFAULT 0,
        Damage_Dealt_To_GRAVEKEEPER INTEGER DEFAULT 0,
        Damage_Dealt_To_ROBOBALLBOSS INTEGER DEFAULT 0,
        Damage_Dealt_To_SUPERROBOBALLBOSS INTEGER DEFAULT 0,
        Damage_Dealt_To_SCAV INTEGER DEFAULT 0,
        Damage_Dealt_To_SCAVLUNAR1 INTEGER DEFAULT 0,
        Damage_Dealt_To_SCAVLUNAR2 INTEGER DEFAULT 0,
        Damage_Dealt_To_SCAVLUNAR3 INTEGER DEFAULT 0,
        Damage_Dealt_To_SCAVLUNAR4 INTEGER DEFAULT 0,
        Damage_Dealt_To_GRANDPARENT INTEGER DEFAULT 0,
        Damage_Dealt_To_ARTIFACTSHELL INTEGER DEFAULT 0,
        Damage_Dealt_To_BROTHER INTEGER DEFAULT 0,
        Damage_Dealt_To_VERMIN INTEGER DEFAULT 0,
        Damage_Dealt_To_FLYINGVERMIN INTEGER DEFAULT 0,
        Damage_Dealt_To_CLAYGRENADIER INTEGER DEFAULT 0,
        Damage_Dealt_To_GUP INTEGER DEFAULT 0,
        Damage_Dealt_To_GEEP INTEGER DEFAULT 0,
        Damage_Dealt_To_GIP INTEGER DEFAULT 0,
        Damage_Dealt_To_SULFURPOD INTEGER DEFAULT 0,
        Damage_Dealt_To_ACIDLARVA INTEGER DEFAULT 0,
        Damage_Dealt_To_MINORCONSTRUCT INTEGER DEFAULT 0,
        Damage_Dealt_To_MEGACONSTRUCT INTEGER DEFAULT 0,
        Damage_Dealt_To_VOIDMEGACRAB INTEGER DEFAULT 0,
        Damage_Dealt_To_VOIDRAIDCRAB INTEGER DEFAULT 0,
        Damage_Dealt_To_VOIDBARNACLE INTEGER DEFAULT 0,
        Damage_Dealt_To_VOIDJAILER INTEGER DEFAULT 0,
        Damage_Dealt_To_ASSASSIN2 INTEGER DEFAULT 0,
        Damage_Dealt_To_VOIDINFESTOR INTEGER DEFAULT 0,
        Damage_Taken_From_BEETLE INTEGER DEFAULT 0,
        Damage_Taken_From_BEETLEGUARD INTEGER DEFAULT 0,
        Damage_Taken_From_BISON INTEGER DEFAULT 0,
        Damage_Taken_From_GOLEM INTEGER DEFAULT 0,
        Damage_Taken_From_WISP INTEGER DEFAULT 0,
        Damage_Taken_From_GREATERWISP INTEGER DEFAULT 0,
        Damage_Taken_From_LEMURIAN INTEGER DEFAULT 0,
        Damage_Taken_From_LEMURIANBRUISER INTEGER DEFAULT 0,
        Damage_Taken_From_IMP INTEGER DEFAULT 0,
        Damage_Taken_From_JELLYFISH INTEGER DEFAULT 0,
        Damage_Taken_From_CLAY INTEGER DEFAULT 0,
        Damage_Taken_From_HERMIT_CRAB INTEGER DEFAULT 0,
        Damage_Taken_From_BELL INTEGER DEFAULT 0,
        Damage_Taken_From_CLAYBRUISER INTEGER DEFAULT 0,
        Damage_Taken_From_VULTURE INTEGER DEFAULT 0,
        Damage_Taken_From_ROBOBALLMINI INTEGER DEFAULT 0,
        Damage_Taken_From_NULLIFIER INTEGER DEFAULT 0,
        Damage_Taken_From_PARENT INTEGER DEFAULT 0,
        Damage_Taken_From_MINIMUSHROOM INTEGER DEFAULT 0,
        Damage_Taken_From_POD INTEGER DEFAULT 0,
        Damage_Taken_From_LUNARWISP INTEGER DEFAULT 0,
        Damage_Taken_From_LUNARGOLEM INTEGER DEFAULT 0,
        Damage_Taken_From_LUNAREXPLODER INTEGER DEFAULT 0,
        Damage_Taken_From_BEETLEQUEEN INTEGER DEFAULT 0,
        Damage_Taken_From_CLAYBOSS INTEGER DEFAULT 0,
        Damage_Taken_From_TITAN INTEGER DEFAULT 0,
        Damage_Taken_From_TITANGOLD INTEGER DEFAULT 0,
        Damage_Taken_From_VAGRANT INTEGER DEFAULT 0,
        Damage_Taken_From_MAGMAWORM INTEGER DEFAULT 0,
        Damage_Taken_From_ELECTRICWORM INTEGER DEFAULT 0,
        Damage_Taken_From_IMPBOSS INTEGER DEFAULT 0,
        Damage_Taken_From_GRAVEKEEPER INTEGER DEFAULT 0,
        Damage_Taken_From_ROBOBALLBOSS INTEGER DEFAULT 0,
        Damage_Taken_From_SUPERROBOBALLBOSS INTEGER DEFAULT 0,
        Damage_Taken_From_SCAV INTEGER DEFAULT 0,
        Damage_Taken_From_SCAVLUNAR1 INTEGER DEFAULT 0,
        Damage_Taken_From_SCAVLUNAR2 INTEGER DEFAULT 0,
        Damage_Taken_From_SCAVLUNAR3 INTEGER DEFAULT 0,
        Damage_Taken_From_SCAVLUNAR4 INTEGER DEFAULT 0,
        Damage_Taken_From_GRANDPARENT INTEGER DEFAULT 0,
        Damage_Taken_From_ARTIFACTSHELL INTEGER DEFAULT 0,
        Damage_Taken_From_BROTHER INTEGER DEFAULT 0,
        Damage_Taken_From_VERMIN INTEGER DEFAULT 0,
        Damage_Taken_From_FLYINGVERMIN INTEGER DEFAULT 0,
        Damage_Taken_From_CLAYGRENADIER INTEGER DEFAULT 0,
        Damage_Taken_From_GUP INTEGER DEFAULT 0,
        Damage_Taken_From_GEEP INTEGER DEFAULT 0,
        Damage_Taken_From_GIP INTEGER DEFAULT 0,
        Damage_Taken_From_SULFURPOD INTEGER DEFAULT 0,
        Damage_Taken_From_ACIDLARVA INTEGER DEFAULT 0,
        Damage_Taken_From_MINORCONSTRUCT INTEGER DEFAULT 0,
        Damage_Taken_From_MEGACONSTRUCT INTEGER DEFAULT 0,
        Damage_Taken_From_VOIDMEGACRAB INTEGER DEFAULT 0,
        Damage_Taken_From_VOIDRAIDCRAB INTEGER DEFAULT 0,
        Damage_Taken_From_VOIDBARNACLE INTEGER DEFAULT 0,
        Damage_Taken_From_VOIDJAILER INTEGER DEFAULT 0,
        Damage_Taken_From_ASSASSIN2 INTEGER DEFAULT 0,
        Damage_Taken_From_VOIDINFESTOR INTEGER DEFAULT 0,
        FOREIGN KEY (Run_ID) REFERENCES Run_Meta_Data(Run_ID)
    );

    CREATE TABLE Kill_Stats (
        Run_ID TEXT NOT NULL,
        Total_Minion_Kills INTEGER DEFAULT 0,
        Total_Kills INTEGER DEFAULT 0,
        Total_Elite_Kills INTEGER DEFAULT 0,
        Total_Teleporter_Boss_Kills INTEGER DEFAULT 0,
        Kills_Against_BEETLE INTEGER DEFAULT 0,
        Kills_Against_BEETLEGUARD INTEGER DEFAULT 0,
        Kills_Against_BISON INTEGER DEFAULT 0,
        Kills_Against_GOLEM INTEGER DEFAULT 0,
        Kills_Against_WISP INTEGER DEFAULT 0,
        Kills_Against_GREATERWISP INTEGER DEFAULT 0,
        Kills_Against_LEMURIAN INTEGER DEFAULT 0,
        Kills_Against_LEMURIANBRUISER INTEGER DEFAULT 0,
        Kills_Against_IMP INTEGER DEFAULT 0,
        Kills_Against_JELLYFISH INTEGER DEFAULT 0,
        Kills_Against_CLAY INTEGER DEFAULT 0,
        Kills_Against_HERMIT_CRAB INTEGER DEFAULT 0,
        Kills_Against_BELL INTEGER DEFAULT 0,
        Kills_Against_CLAYBRUISER INTEGER DEFAULT 0,
        Kills_Against_VULTURE INTEGER DEFAULT 0,
        Kills_Against_ROBOBALLMINI INTEGER DEFAULT 0,
        Kills_Against_NULLIFIER INTEGER DEFAULT 0,
        Kills_Against_PARENT INTEGER DEFAULT 0,
        Kills_Against_MINIMUSHROOM INTEGER DEFAULT 0,
        Kills_Against_POD INTEGER DEFAULT 0,
        Kills_Against_LUNARWISP INTEGER DEFAULT 0,
        Kills_Against_LUNARGOLEM INTEGER DEFAULT 0,
        Kills_Against_LUNAREXPLODER INTEGER DEFAULT 0,
        Kills_Against_BEETLEQUEEN INTEGER DEFAULT 0,
        Kills_Against_CLAYBOSS INTEGER DEFAULT 0,
        Kills_Against_TITAN INTEGER DEFAULT 0,
        Kills_Against_TITANGOLD INTEGER DEFAULT 0,
        Kills_Against_VAGRANT INTEGER DEFAULT 0,
        Kills_Against_MAGMAWORM INTEGER DEFAULT 0,
        Kills_Against_ELECTRICWORM INTEGER DEFAULT 0,
        Kills_Against_IMPBOSS INTEGER DEFAULT 0,
        Kills_Against_GRAVEKEEPER INTEGER DEFAULT 0,
        Kills_Against_ROBOBALLBOSS INTEGER DEFAULT 0,
        Kills_Against_SUPERROBOBALLBOSS INTEGER DEFAULT 0,
        Kills_Against_SCAV INTEGER DEFAULT 0,
        Kills_Against_SCAVLUNAR1 INTEGER DEFAULT 0,
        Kills_Against_SCAVLUNAR2 INTEGER DEFAULT 0,
        Kills_Against_SCAVLUNAR3 INTEGER DEFAULT 0,
        Kills_Against_SCAVLUNAR4 INTEGER DEFAULT 0,
        Kills_Against_GRANDPARENT INTEGER DEFAULT 0,
        Kills_Against_ARTIFACTSHELL INTEGER DEFAULT 0,
        Kills_Against_BROTHER INTEGER DEFAULT 0,
        Kills_Against_VERMIN INTEGER DEFAULT 0,
        Kills_Against_FLYINGVERMIN INTEGER DEFAULT 0,
        Kills_Against_CLAYGRENADIER INTEGER DEFAULT 0,
        Kills_Against_GUP INTEGER DEFAULT 0,
        Kills_Against_GEEP INTEGER DEFAULT 0,
        Kills_Against_GIP INTEGER DEFAULT 0,
        Kills_Against_SULFURPOD INTEGER DEFAULT 0,
        Kills_Against_ACIDLARVA INTEGER DEFAULT 0,
        Kills_Against_MINORCONSTRUCT INTEGER DEFAULT 0,
        Kills_Against_MEGACONSTRUCT INTEGER DEFAULT 0,
        Kills_Against_VOIDMEGACRAB INTEGER DEFAULT 0,
        Kills_Against_VOIDRAIDCRAB INTEGER DEFAULT 0,
        Kills_Against_VOIDBARNACLE INTEGER DEFAULT 0,
        Kills_Against_VOIDJAILER INTEGER DEFAULT 0,
        Kills_Against_ASSASSIN2 INTEGER DEFAULT 0,
        Kills_Against_VOIDINFESTOR INTEGER DEFAULT 0,
        Kills_Against_Elite_BEETLE INTEGER DEFAULT 0,
        Kills_Against_Elite_BEETLEGUARD INTEGER DEFAULT 0,
        Kills_Against_Elite_BISON INTEGER DEFAULT 0,
        Kills_Against_Elite_GOLEM INTEGER DEFAULT 0,
        Kills_Against_Elite_WISP INTEGER DEFAULT 0,
        Kills_Against_Elite_GREATERWISP INTEGER DEFAULT 0,
        Kills_Against_Elite_LEMURIAN INTEGER DEFAULT 0,
        Kills_Against_Elite_LEMURIANBRUISER INTEGER DEFAULT 0,
        Kills_Against_Elite_IMP INTEGER DEFAULT 0,
        Kills_Against_Elite_JELLYFISH INTEGER DEFAULT 0,
        Kills_Against_Elite_CLAY INTEGER DEFAULT 0,
        Kills_Against_Elite_HERMIT_CRAB INTEGER DEFAULT 0,
        Kills_Against_Elite_BELL INTEGER DEFAULT 0,
        Kills_Against_Elite_CLAYBRUISER INTEGER DEFAULT 0,
        Kills_Against_Elite_VULTURE INTEGER DEFAULT 0,
        Kills_Against_Elite_ROBOBALLMINI INTEGER DEFAULT 0,
        Kills_Against_Elite_NULLIFIER INTEGER DEFAULT 0,
        Kills_Against_Elite_PARENT INTEGER DEFAULT 0,
        Kills_Against_Elite_MINIMUSHROOM INTEGER DEFAULT 0,
        Kills_Against_Elite_POD INTEGER DEFAULT 0,
        Kills_Against_Elite_LUNARWISP INTEGER DEFAULT 0,
        Kills_Against_Elite_LUNARGOLEM INTEGER DEFAULT 0,
        Kills_Against_Elite_LUNAREXPLODER INTEGER DEFAULT 0,
        Kills_Against_Elite_BEETLEQUEEN INTEGER DEFAULT 0,
        Kills_Against_Elite_CLAYBOSS INTEGER DEFAULT 0,
        Kills_Against_Elite_TITAN INTEGER DEFAULT 0,
        Kills_Against_Elite_TITANGOLD INTEGER DEFAULT 0,
        Kills_Against_Elite_VAGRANT INTEGER DEFAULT 0,
        Kills_Against_Elite_IMPBOSS INTEGER DEFAULT 0,
        Kills_Against_Elite_GRAVEKEEPER INTEGER DEFAULT 0,
        Kills_Against_Elite_ROBOBALLBOSS INTEGER DEFAULT 0,
        Kills_Against_Elite_SUPERROBOBALLBOSS INTEGER DEFAULT 0,
        Kills_Against_Elite_SCAV INTEGER DEFAULT 0,
        Kills_Against_Elite_GRANDPARENT INTEGER DEFAULT 0,
        Kills_Against_Elite_ARTIFACTSHELL INTEGER DEFAULT 0,
        Kills_Against_Elite_BROTHER INTEGER DEFAULT 0,
        Kills_Against_Elite_VERMIN INTEGER DEFAULT 0,
        Kills_Against_Elite_FLYINGVERMIN INTEGER DEFAULT 0,
        Kills_Against_Elite_CLAYGRENADIER INTEGER DEFAULT 0,
        Kills_Against_Elite_GUP INTEGER DEFAULT 0,
        Kills_Against_Elite_GEEP INTEGER DEFAULT 0,
        Kills_Against_Elite_GIP INTEGER DEFAULT 0,
        Kills_Against_Elite_SULFURPOD INTEGER DEFAULT 0,
        Kills_Against_Elite_ACIDLARVA INTEGER DEFAULT 0,
        Kills_Against_Elite_MINORCONSTRUCT INTEGER DEFAULT 0,
        Kills_Against_Elite_MEGACONSTRUCT INTEGER DEFAULT 0,
        Kills_Against_Elite_VOIDMEGACRAB INTEGER DEFAULT 0,
        Kills_Against_Elite_VOIDRAIDCRAB INTEGER DEFAULT 0,
        Kills_Against_Elite_VOIDBARNACLE INTEGER DEFAULT 0,
        Kills_Against_Elite_VOIDJAILER INTEGER DEFAULT 0,
        Kills_Against_Elite_ASSASSIN2 INTEGER DEFAULT 0,
        FOREIGN KEY (Run_ID) REFERENCES Run_Meta_Data(Run_ID)
    );

    CREATE TABLE Purchases (
        Run_ID TEXT NOT NULL,
        Total_Gold_Collected INTEGER DEFAULT 0,
        Max_Gold_Collected INTEGER DEFAULT 0,
        Total_Purchases INTEGER DEFAULT 0,
        Highest_Purchases INTEGER DEFAULT 0,
        Total_Gold_Purchases INTEGER DEFAULT 0,
        Highest_Gold_Purchases INTEGER DEFAULT 0,
        Total_Blood_Purchases INTEGER DEFAULT 0,
        Highest_Blood_Purchases INTEGER DEFAULT 0,
        Total_Lunar_Purchases INTEGER DEFAULT 0,
        Highest_Lunar_Purchases INTEGER DEFAULT 0,
        Total_Drones_Purchased INTEGER DEFAULT 0,
        Total_Turrets_Purchased INTEGER DEFAULT 0,
        FOREIGN KEY (Run_ID) REFERENCES Run_Meta_Data(Run_ID)
    );

    CREATE TABLE Item_Info (
        Run_ID TEXT NOT NULL,
        Total_Items_Collected INTEGER DEFAULT 0,
        Highest_Items_Collected INTEGER DEFAULT 0,
        Total_Collected_ARMORPLATE INTEGER DEFAULT 0,
        Total_Collected_ATTACKSPEEDANDMOVESPEED INTEGER DEFAULT 0,
        Total_Collected_BARRIERONKILL INTEGER DEFAULT 0,
        Total_Collected_BEAR INTEGER DEFAULT 0,
        Total_Collected_BLEEDONHIT INTEGER DEFAULT 0,
        Total_Collected_BOSSDAMAGEBONUS INTEGER DEFAULT 0,
        Total_Collected_CRITGLASSES INTEGER DEFAULT 0,
        Total_Collected_CROWBAR INTEGER DEFAULT 0,
        Total_Collected_FIREWORK INTEGER DEFAULT 0,
        Total_Collected_FLATHEALTH INTEGER DEFAULT 0,
        Total_Collected_FRAGILEDAMAGEBONUS INTEGER DEFAULT 0,
        Total_Collected_GOLDONHURT INTEGER DEFAULT 0,
        Total_Collected_HEALWHILESAFE INTEGER DEFAULT 0,
        Total_Collected_HEALINGPOTION INTEGER DEFAULT 0,
        Total_Collected_HOOF INTEGER DEFAULT 0,
        Total_Collected_IGNITEONKILL INTEGER DEFAULT 0,
        Total_Collected_MEDKIT INTEGER DEFAULT 0,
        Total_Collected_MUSHROOM INTEGER DEFAULT 0,
        Total_Collected_NEARBYDAMAGEBONUS INTEGER DEFAULT 0,
        Total_Collected_OUTOFCOMBATARMOR INTEGER DEFAULT 0,
        Total_Collected_PERSONALSHIELD INTEGER DEFAULT 0,
        Total_Collected_SCRAPWHITE INTEGER DEFAULT 0,
        Total_Collected_SECONDARYSKILLMAGAZINE INTEGER DEFAULT 0,
        Total_Collected_SPRINTBONUS INTEGER DEFAULT 0,
        Total_Collected_STICKYBOMB INTEGER DEFAULT 0,
        Total_Collected_STUNCHANCEONHIT INTEGER DEFAULT 0,
        Total_Collected_SYRINGE INTEGER DEFAULT 0,
        Total_Collected_TOOTH INTEGER DEFAULT 0,
        Total_Collected_TREASURECACHE INTEGER DEFAULT 0,
        Total_Collected_WARDONLEVEL INTEGER DEFAULT 0,
        Total_Collected_ATTACKSPEEDONCRIT INTEGER DEFAULT 0,
        Total_Collected_BANDOLIER INTEGER DEFAULT 0,
        Total_Collected_BONUSGOLDPACKONKILL INTEGER DEFAULT 0,
        Total_Collected_CHAINLIGHTNING INTEGER DEFAULT 0,
        Total_Collected_DEATHMARK INTEGER DEFAULT 0,
        Total_Collected_ENERGIZEDONEQUIPMENTUSE INTEGER DEFAULT 0,
        Total_Collected_EQUIPMENTMAGAZINE INTEGER DEFAULT 0,
        Total_Collected_EXECUTELOWHEALTHELITE INTEGER DEFAULT 0,
        Total_Collected_EXPLODEONDEATH INTEGER DEFAULT 0,
        Total_Collected_FEATHER INTEGER DEFAULT 0,
        Total_Collected_FIRERING INTEGER DEFAULT 0,
        Total_Collected_FREECHEST INTEGER DEFAULT 0,
        Total_Collected_HEALONCRIT INTEGER DEFAULT 0,
        Total_Collected_ICERING INTEGER DEFAULT 0,
        Total_Collected_INFUSION INTEGER DEFAULT 0,
        Total_Collected_JUMPBOOST INTEGER DEFAULT 0,
        Total_Collected_MISSILE INTEGER DEFAULT 0,
        Total_Collected_MOVESPEEDONKILL INTEGER DEFAULT 0,
        Total_Collected_PHASING INTEGER DEFAULT 0,
        Total_Collected_PRIMARYSKILLSHURIKEN INTEGER DEFAULT 0,
        Total_Collected_REGENERATINGSCRAP INTEGER DEFAULT 0,
        Total_Collected_SCRAPGREEN INTEGER DEFAULT 0,
        Total_Collected_SEED INTEGER DEFAULT 0,
        Total_Collected_SLOWONHIT INTEGER DEFAULT 0,
        Total_Collected_SPRINTARMOR INTEGER DEFAULT 0,
        Total_Collected_SPRINTOUTOFCOMBAT INTEGER DEFAULT 0,
        Total_Collected_SQUID INTEGER DEFAULT 0,
        Total_Collected_STRENGTHENBURN INTEGER DEFAULT 0,
        Total_Collected_TPHEALINGNOVA INTEGER DEFAULT 0,
        Total_Collected_THORNS INTEGER DEFAULT 0,
        Total_Collected_WARCRYONMULTIKILL INTEGER DEFAULT 0,
        Total_Collected_ALIENHEAD INTEGER DEFAULT 0,
        Total_Collected_ARMORREDUCTIONONHIT INTEGER DEFAULT 0,
        Total_Collected_BARRIERONOVERHEAL INTEGER DEFAULT 0,
        Total_Collected_BEHEMOTH INTEGER DEFAULT 0,
        Total_Collected_BOUNCENEARBY INTEGER DEFAULT 0,
        Total_Collected_CAPTAINDEFENSEMATRIX INTEGER DEFAULT 0,
        Total_Collected_CLOVER INTEGER DEFAULT 0,
        Total_Collected_CRITDAMAGE INTEGER DEFAULT 0,
        Total_Collected_DAGGER INTEGER DEFAULT 0,
        Total_Collected_DRONEWEAPONS INTEGER DEFAULT 0,
        Total_Collected_EXTRALIFE INTEGER DEFAULT 0,
        Total_Collected_FALLBOOTS INTEGER DEFAULT 0,
        Total_Collected_GHOSTONKILL INTEGER DEFAULT 0,
        Total_Collected_HEADHUNTER INTEGER DEFAULT 0,
        Total_Collected_ICICLE INTEGER DEFAULT 0,
        Total_Collected_IMMUNETODEBUFF INTEGER DEFAULT 0,
        Total_Collected_INCREASEHEALING INTEGER DEFAULT 0,
        Total_Collected_KILLELITEFRENZY INTEGER DEFAULT 0,
        Total_Collected_LASERTURBINE INTEGER DEFAULT 0,
        Total_Collected_MOREMISSILE INTEGER DEFAULT 0,
        Total_Collected_NOVAONHEAL INTEGER DEFAULT 0,
        Total_Collected_PERMANENTDEBUFFONHIT INTEGER DEFAULT 0,
        Total_Collected_PLANT INTEGER DEFAULT 0,
        Total_Collected_RANDOMEQUIPMENTTRIGGER INTEGER DEFAULT 0,
        Total_Collected_SCRAPRED INTEGER DEFAULT 0,
        Total_Collected_SHOCKNEARBY INTEGER DEFAULT 0,
        Total_Collected_TALISMAN INTEGER DEFAULT 0,
        Total_Collected_UTILITYSKILLMAGAZINE INTEGER DEFAULT 0,
        Total_Collected_AUTOCASTEQUIPMENT INTEGER DEFAULT 0,
        Total_Collected_FOCUSCONVERGENCE INTEGER DEFAULT 0,
        Total_Collected_GOLDONHIT INTEGER DEFAULT 0,
        Total_Collected_HALFATTACKSPEEDHALFCOOLDOWNS INTEGER DEFAULT 0,
        Total_Collected_HALFSPEEDDOUBLEHEALTH INTEGER DEFAULT 0,
        Total_Collected_LUNARBADLUCK INTEGER DEFAULT 0,
        Total_Collected_LUNARDAGGER INTEGER DEFAULT 0,
        Total_Collected_LUNARPRIMARYREPLACEMENT INTEGER DEFAULT 0,
        Total_Collected_LUNARSECONDARYREPLACEMENT INTEGER DEFAULT 0,
        Total_Collected_LUNARSPECIALREPLACEMENT INTEGER DEFAULT 0,
        Total_Collected_LUNARSUN INTEGER DEFAULT 0,
        Total_Collected_LUNARTRINKET INTEGER DEFAULT 0,
        Total_Collected_LUNARUTILITYREPLACEMENT INTEGER DEFAULT 0,
        Total_Collected_MONSTERSONSHRINEUSE INTEGER DEFAULT 0,
        Total_Collected_RANDOMDAMAGEZONE INTEGER DEFAULT 0,
        Total_Collected_RANDOMLYLUNAR INTEGER DEFAULT 0,
        Total_Collected_REPEATHEAL INTEGER DEFAULT 0,
        Total_Collected_SHIELDONLY INTEGER DEFAULT 0,
        Total_Collected_ARTIFACTKEY INTEGER DEFAULT 0,
        Total_Collected_BEETLEGLAND INTEGER DEFAULT 0,
        Total_Collected_BLEEDONHITANDEXPLODE INTEGER DEFAULT 0,
        Total_Collected_FIREBALLSONHIT INTEGER DEFAULT 0,
        Total_Collected_KNURL INTEGER DEFAULT 0,
        Total_Collected_LIGHTNINGSTRIKEONHIT INTEGER DEFAULT 0,
        Total_Collected_MINORCONSTRUCTONKILL INTEGER DEFAULT 0,
        Total_Collected_NOVAONLOWHEALTH INTEGER DEFAULT 0,
        Total_Collected_PARENTEGG INTEGER DEFAULT 0,
        Total_Collected_PEARL INTEGER DEFAULT 0,
        Total_Collected_ROBOBALLBUDDY INTEGER DEFAULT 0,
        Total_Collected_SCRAPYELLOW INTEGER DEFAULT 0,
        Total_Collected_SHINYPEARL INTEGER DEFAULT 0,
        Total_Collected_SIPHONONLOWHEALTH INTEGER DEFAULT 0,
        Total_Collected_SPRINTWISP INTEGER DEFAULT 0,
        Total_Collected_TITANGOLDDURINGTP INTEGER DEFAULT 0,
        Total_Collected_BEARVOID INTEGER DEFAULT 0,
        Total_Collected_BLEEDONHITVOID INTEGER DEFAULT 0,
        Total_Collected_CRITGLASSESVOID INTEGER DEFAULT 0,
        Total_Collected_MUSHROOMVOID INTEGER DEFAULT 0,
        Total_Collected_TREASURECACHEVOID INTEGER DEFAULT 0,
        Total_Collected_CHAINLIGHTNINGVOID INTEGER DEFAULT 0,
        Total_Collected_ELEMENTALRINGVOID INTEGER DEFAULT 0,
        Total_Collected_EQUIPMENTMAGAZINEVOID INTEGER DEFAULT 0,
        Total_Collected_EXPLODEONDEATHVOID INTEGER DEFAULT 0,
        Total_Collected_MISSILEVOID INTEGER DEFAULT 0,
        Total_Collected_SLOWONHITVOID INTEGER DEFAULT 0,
        Total_Collected_CLOVERVOID INTEGER DEFAULT 0,
        Total_Collected_EXTRALIFEVOID INTEGER DEFAULT 0,
        Total_Collected_VOIDMEGACRABITEM INTEGER DEFAULT 0,
        Highest_Collected_ARMORPLATE INTEGER DEFAULT 0,
        Highest_Collected_ATTACKSPEEDANDMOVESPEED INTEGER DEFAULT 0,
        Highest_Collected_BARRIERONKILL INTEGER DEFAULT 0,
        Highest_Collected_BEAR INTEGER DEFAULT 0,
        Highest_Collected_BLEEDONHIT INTEGER DEFAULT 0,
        Highest_Collected_BOSSDAMAGEBONUS INTEGER DEFAULT 0,
        Highest_Collected_CRITGLASSES INTEGER DEFAULT 0,
        Highest_Collected_CROWBAR INTEGER DEFAULT 0,
        Highest_Collected_FIREWORK INTEGER DEFAULT 0,
        Highest_Collected_FLATHEALTH INTEGER DEFAULT 0,
        Highest_Collected_FRAGILEDAMAGEBONUS INTEGER DEFAULT 0,
        Highest_Collected_GOLDONHURT INTEGER DEFAULT 0,
        Highest_Collected_HEALWHILESAFE INTEGER DEFAULT 0,
        Highest_Collected_HEALINGPOTION INTEGER DEFAULT 0,
        Highest_Collected_HOOF INTEGER DEFAULT 0,
        Highest_Collected_IGNITEONKILL INTEGER DEFAULT 0,
        Highest_Collected_MEDKIT INTEGER DEFAULT 0,
        Highest_Collected_MUSHROOM INTEGER DEFAULT 0,
        Highest_Collected_NEARBYDAMAGEBONUS INTEGER DEFAULT 0,
        Highest_Collected_OUTOFCOMBATARMOR INTEGER DEFAULT 0,
        Highest_Collected_PERSONALSHIELD INTEGER DEFAULT 0,
        Highest_Collected_SCRAPWHITE INTEGER DEFAULT 0,
        Highest_Collected_SECONDARYSKILLMAGAZINE INTEGER DEFAULT 0,
        Highest_Collected_SPRINTBONUS INTEGER DEFAULT 0,
        Highest_Collected_STICKYBOMB INTEGER DEFAULT 0,
        Highest_Collected_STUNCHANCEONHIT INTEGER DEFAULT 0,
        Highest_Collected_SYRINGE INTEGER DEFAULT 0,
        Highest_Collected_TOOTH INTEGER DEFAULT 0,
        Highest_Collected_TREASURECACHE INTEGER DEFAULT 0,
        Highest_Collected_WARDONLEVEL INTEGER DEFAULT 0,
        Highest_Collected_ATTACKSPEEDONCRIT INTEGER DEFAULT 0,
        Highest_Collected_BANDOLIER INTEGER DEFAULT 0,
        Highest_Collected_BONUSGOLDPACKONKILL INTEGER DEFAULT 0,
        Highest_Collected_CHAINLIGHTNING INTEGER DEFAULT 0,
        Highest_Collected_DEATHMARK INTEGER DEFAULT 0,
        Highest_Collected_ENERGIZEDONEQUIPMENTUSE INTEGER DEFAULT 0,
        Highest_Collected_EQUIPMENTMAGAZINE INTEGER DEFAULT 0,
        Highest_Collected_EXECUTELOWHEALTHELITE INTEGER DEFAULT 0,
        Highest_Collected_EXPLODEONDEATH INTEGER DEFAULT 0,
        Highest_Collected_FEATHER INTEGER DEFAULT 0,
        Highest_Collected_FIRERING INTEGER DEFAULT 0,
        Highest_Collected_FREECHEST INTEGER DEFAULT 0,
        Highest_Collected_HEALONCRIT INTEGER DEFAULT 0,
        Highest_Collected_ICERING INTEGER DEFAULT 0,
        Highest_Collected_INFUSION INTEGER DEFAULT 0,
        Highest_Collected_JUMPBOOST INTEGER DEFAULT 0,
        Highest_Collected_MISSILE INTEGER DEFAULT 0,
        Highest_Collected_MOVESPEEDONKILL INTEGER DEFAULT 0,
        Highest_Collected_PHASING INTEGER DEFAULT 0,
        Highest_Collected_PRIMARYSKILLSHURIKEN INTEGER DEFAULT 0,
        Highest_Collected_REGENERATINGSCRAP INTEGER DEFAULT 0,
        Highest_Collected_SCRAPGREEN INTEGER DEFAULT 0,
        Highest_Collected_SEED INTEGER DEFAULT 0,
        Highest_Collected_SLOWONHIT INTEGER DEFAULT 0,
        Highest_Collected_SPRINTARMOR INTEGER DEFAULT 0,
        Highest_Collected_SPRINTOUTOFCOMBAT INTEGER DEFAULT 0,
        Highest_Collected_SQUID INTEGER DEFAULT 0,
        Highest_Collected_STRENGTHENBURN INTEGER DEFAULT 0,
        Highest_Collected_TPHEALINGNOVA INTEGER DEFAULT 0,
        Highest_Collected_THORNS INTEGER DEFAULT 0,
        Highest_Collected_WARCRYONMULTIKILL INTEGER DEFAULT 0,
        Highest_Collected_ALIENHEAD INTEGER DEFAULT 0,
        Highest_Collected_ARMORREDUCTIONONHIT INTEGER DEFAULT 0,
        Highest_Collected_BARRIERONOVERHEAL INTEGER DEFAULT 0,
        Highest_Collected_BEHEMOTH INTEGER DEFAULT 0,
        Highest_Collected_BOUNCENEARBY INTEGER DEFAULT 0,
        Highest_Collected_CAPTAINDEFENSEMATRIX INTEGER DEFAULT 0,
        Highest_Collected_CLOVER INTEGER DEFAULT 0,
        Highest_Collected_CRITDAMAGE INTEGER DEFAULT 0,
        Highest_Collected_DAGGER INTEGER DEFAULT 0,
        Highest_Collected_DRONEWEAPONS INTEGER DEFAULT 0,
        Highest_Collected_EXTRALIFE INTEGER DEFAULT 0,
        Highest_Collected_FALLBOOTS INTEGER DEFAULT 0,
        Highest_Collected_GHOSTONKILL INTEGER DEFAULT 0,
        Highest_Collected_HEADHUNTER INTEGER DEFAULT 0,
        Highest_Collected_ICICLE INTEGER DEFAULT 0,
        Highest_Collected_IMMUNETODEBUFF INTEGER DEFAULT 0,
        Highest_Collected_INCREASEHEALING INTEGER DEFAULT 0,
        Highest_Collected_KILLELITEFRENZY INTEGER DEFAULT 0,
        Highest_Collected_LASERTURBINE INTEGER DEFAULT 0,
        Highest_Collected_MOREMISSILE INTEGER DEFAULT 0,
        Highest_Collected_NOVAONHEAL INTEGER DEFAULT 0,
        Highest_Collected_PERMANENTDEBUFFONHIT INTEGER DEFAULT 0,
        Highest_Collected_PLANT INTEGER DEFAULT 0,
        Highest_Collected_RANDOMEQUIPMENTTRIGGER INTEGER DEFAULT 0,
        Highest_Collected_SCRAPRED INTEGER DEFAULT 0,
        Highest_Collected_SHOCKNEARBY INTEGER DEFAULT 0,
        Highest_Collected_TALISMAN INTEGER DEFAULT 0,
        Highest_Collected_UTILITYSKILLMAGAZINE INTEGER DEFAULT 0,
        Highest_Collected_AUTOCASTEQUIPMENT INTEGER DEFAULT 0,
        Highest_Collected_FOCUSCONVERGENCE INTEGER DEFAULT 0,
        Highest_Collected_GOLDONHIT INTEGER DEFAULT 0,
        Highest_Collected_HALFATTACKSPEEDHALFCOOLDOWNS INTEGER DEFAULT 0,
        Highest_Collected_HALFSPEEDDOUBLEHEALTH INTEGER DEFAULT 0,
        Highest_Collected_LUNARBADLUCK INTEGER DEFAULT 0,
        Highest_Collected_LUNARDAGGER INTEGER DEFAULT 0,
        Highest_Collected_LUNARPRIMARYREPLACEMENT INTEGER DEFAULT 0,
        Highest_Collected_LUNARSECONDARYREPLACEMENT INTEGER DEFAULT 0,
        Highest_Collected_LUNARSPECIALREPLACEMENT INTEGER DEFAULT 0,
        Highest_Collected_LUNARSUN INTEGER DEFAULT 0,
        Highest_Collected_LUNARTRINKET INTEGER DEFAULT 0,
        Highest_Collected_LUNARUTILITYREPLACEMENT INTEGER DEFAULT 0,
        Highest_Collected_MONSTERSONSHRINEUSE INTEGER DEFAULT 0,
        Highest_Collected_RANDOMDAMAGEZONE INTEGER DEFAULT 0,
        Highest_Collected_RANDOMLYLUNAR INTEGER DEFAULT 0,
        Highest_Collected_REPEATHEAL INTEGER DEFAULT 0,
        Highest_Collected_SHIELDONLY INTEGER DEFAULT 0,
        Highest_Collected_ARTIFACTKEY INTEGER DEFAULT 0,
        Highest_Collected_BEETLEGLAND INTEGER DEFAULT 0,
        Highest_Collected_BLEEDONHITANDEXPLODE INTEGER DEFAULT 0,
        Highest_Collected_FIREBALLSONHIT INTEGER DEFAULT 0,
        Highest_Collected_KNURL INTEGER DEFAULT 0,
        Highest_Collected_LIGHTNINGSTRIKEONHIT INTEGER DEFAULT 0,
        Highest_Collected_MINORCONSTRUCTONKILL INTEGER DEFAULT 0,
        Highest_Collected_NOVAONLOWHEALTH INTEGER DEFAULT 0,
        Highest_Collected_PARENTEGG INTEGER DEFAULT 0,
        Highest_Collected_PEARL INTEGER DEFAULT 0,
        Highest_Collected_ROBOBALLBUDDY INTEGER DEFAULT 0,
        Highest_Collected_SCRAPYELLOW INTEGER DEFAULT 0,
        Highest_Collected_SHINYPEARL INTEGER DEFAULT 0,
        Highest_Collected_SIPHONONLOWHEALTH INTEGER DEFAULT 0,
        Highest_Collected_SPRINTWISP INTEGER DEFAULT 0,
        Highest_Collected_TITANGOLDDURINGTP INTEGER DEFAULT 0,
        Highest_Collected_BEARVOID INTEGER DEFAULT 0,
        Highest_Collected_BLEEDONHITVOID INTEGER DEFAULT 0,
        Highest_Collected_CRITGLASSESVOID INTEGER DEFAULT 0,
        Highest_Collected_MUSHROOMVOID INTEGER DEFAULT 0,
        Highest_Collected_TREASURECACHEVOID INTEGER DEFAULT 0,
        Highest_Collected_CHAINLIGHTNINGVOID INTEGER DEFAULT 0,
        Highest_Collected_ELEMENTALRINGVOID INTEGER DEFAULT 0,
        Highest_Collected_EQUIPMENTMAGAZINEVOID INTEGER DEFAULT 0,
        Highest_Collected_EXPLODEONDEATHVOID INTEGER DEFAULT 0,
        Highest_Collected_MISSILEVOID INTEGER DEFAULT 0,
        Highest_Collected_SLOWONHITVOID INTEGER DEFAULT 0,
        Highest_Collected_CLOVERVOID INTEGER DEFAULT 0,
        Highest_Collected_EXTRALIFEVOID INTEGER DEFAULT 0,
        Highest_Collected_VOIDMEGACRABITEM INTEGER DEFAULT 0,
        FOREIGN KEY (Run_ID) REFERENCES Run_Meta_Data(Run_ID)
    );

    CREATE TABLE Equipment_Info (
        Run_ID TEXT NOT NULL,
        Total_Time_Held_BFG INTEGER DEFAULT 0,
        Total_Time_Held_BLACKHOLE INTEGER DEFAULT 0,
        Total_Time_Held_BOSSHUNTER INTEGER DEFAULT 0,
        Total_Time_Held_BURNNEARBY INTEGER DEFAULT 0,
        Total_Time_Held_CLEANSE INTEGER DEFAULT 0,
        Total_Time_Held_COMMANDMISSILE INTEGER DEFAULT 0,
        Total_Time_Held_CRIPPLEWARD INTEGER DEFAULT 0,
        Total_Time_Held_CRITONUSE INTEGER DEFAULT 0,
        Total_Time_Held_DEATHPROJECTILE INTEGER DEFAULT 0,
        Total_Time_Held_DRONEBACKUP INTEGER DEFAULT 0,
        Total_Time_Held_FIREBALLDASH INTEGER DEFAULT 0,
        Total_Time_Held_FRUIT INTEGER DEFAULT 0,
        Total_Time_Held_GAINARMOR INTEGER DEFAULT 0,
        Total_Time_Held_GATEWAY INTEGER DEFAULT 0,
        Total_Time_Held_GOLDGAT INTEGER DEFAULT 0,
        Total_Time_Held_GUMMYCLONE INTEGER DEFAULT 0,
        Total_Time_Held_JETPACK INTEGER DEFAULT 0,
        Total_Time_Held_LIFESTEALONHIT INTEGER DEFAULT 0,
        Total_Time_Held_LIGHTNING INTEGER DEFAULT 0,
        Total_Time_Held_METEOR INTEGER DEFAULT 0,
        Total_Time_Held_MOLOTOV INTEGER DEFAULT 0,
        Total_Time_Held_MULTISHOPCARD INTEGER DEFAULT 0,
        Total_Time_Held_PASSIVEHEALING INTEGER DEFAULT 0,
        Total_Time_Held_RECYCLE INTEGER DEFAULT 0,
        Total_Time_Held_SAW INTEGER DEFAULT 0,
        Total_Time_Held_SCANNER INTEGER DEFAULT 0,
        Total_Time_Held_TEAMWARCRY INTEGER DEFAULT 0,
        Total_Time_Held_TONIC INTEGER DEFAULT 0,
        Total_Time_Held_VENDINGMACHINE INTEGER DEFAULT 0,
        Total_Times_Fired_BFG INTEGER DEFAULT 0,
        Total_Times_Fired_BLACKHOLE INTEGER DEFAULT 0,
        Total_Times_Fired_BOSSHUNTER INTEGER DEFAULT 0,
        Total_Times_Fired_BURNNEARBY INTEGER DEFAULT 0,
        Total_Times_Fired_CLEANSE INTEGER DEFAULT 0,
        Total_Times_Fired_COMMANDMISSILE INTEGER DEFAULT 0,
        Total_Times_Fired_CRIPPLEWARD INTEGER DEFAULT 0,
        Total_Times_Fired_CRITONUSE INTEGER DEFAULT 0,
        Total_Times_Fired_DEATHPROJECTILE INTEGER DEFAULT 0,
        Total_Times_Fired_DRONEBACKUP INTEGER DEFAULT 0,
        Total_Times_Fired_FIREBALLDASH INTEGER DEFAULT 0,
        Total_Times_Fired_FRUIT INTEGER DEFAULT 0,
        Total_Times_Fired_GAINARMOR INTEGER DEFAULT 0,
        Total_Times_Fired_GATEWAY INTEGER DEFAULT 0,
        Total_Times_Fired_GOLDGAT INTEGER DEFAULT 0,
        Total_Times_Fired_GUMMYCLONE INTEGER DEFAULT 0,
        Total_Times_Fired_JETPACK INTEGER DEFAULT 0,
        Total_Times_Fired_LIFESTEALONHIT INTEGER DEFAULT 0,
        Total_Times_Fired_LIGHTNING INTEGER DEFAULT 0,
        Total_Times_Fired_METEOR INTEGER DEFAULT 0,
        Total_Times_Fired_MOLOTOV INTEGER DEFAULT 0,
        Total_Times_Fired_MULTISHOPCARD INTEGER DEFAULT 0,
        Total_Times_Fired_PASSIVEHEALING INTEGER DEFAULT 0,
        Total_Times_Fired_RECYCLE INTEGER DEFAULT 0,
        Total_Times_Fired_SAW INTEGER DEFAULT 0,
        Total_Times_Fired_SCANNER INTEGER DEFAULT 0,
        Total_Times_Fired_TEAMWARCRY INTEGER DEFAULT 0,
        Total_Times_Fired_TONIC INTEGER DEFAULT 0,
        Total_Times_Fired_VENDINGMACHINE INTEGER DEFAULT 0,
        FOREIGN KEY (Run_ID) REFERENCES Run_Meta_Data(Run_ID)
    );

    CREATE TABLE Stage_Info (
        Run_ID TEXT NOT NULL,
        Total_Stages_Completed INTEGER DEFAULT 0,
        Highest_Stages_Completed INTEGER DEFAULT 0,
        Total_Times_Visited_BLACKBEACH INTEGER DEFAULT 0,
        Total_Times_Visited_GOLEMPLAINS INTEGER DEFAULT 0,
        Total_Times_Visited_GOOLAKE INTEGER DEFAULT 0,
        Total_Times_Visited_BAZAAR INTEGER DEFAULT 0,
        Total_Times_Visited_FROZENWALL INTEGER DEFAULT 0,
        Total_Times_Visited_FOGGYSWAMP INTEGER DEFAULT 0,
        Total_Times_Visited_DAMPCAVE INTEGER DEFAULT 0,
        Total_Times_Visited_WISPGRAVEYARD INTEGER DEFAULT 0,
        Total_Times_Visited_MYSTERYSPACE INTEGER DEFAULT 0,
        Total_Times_Visited_GOLDSHORES INTEGER DEFAULT 0,
        Total_Times_Visited_SHIPGRAVEYARD INTEGER DEFAULT 0,
        Total_Times_Visited_ROOTJUNGLE INTEGER DEFAULT 0,
        Total_Times_Visited_ARENA INTEGER DEFAULT 0,
        Total_Times_Visited_LIMBO INTEGER DEFAULT 0,
        Total_Times_Visited_SKYMEADOW INTEGER DEFAULT 0,
        Total_Times_Visited_ARTIFACTWORLD INTEGER DEFAULT 0,
        Total_Times_Visited_MOON INTEGER DEFAULT 0,
        Total_Times_Visited_ANCIENTLOFT INTEGER DEFAULT 0,
        Total_Times_Visited_SNOWYFOREST INTEGER DEFAULT 0,
        Total_Times_Visited_SULFURPOOLS INTEGER DEFAULT 0,
        Total_Times_Visited_VOIDSTAGE INTEGER DEFAULT 0,
        Total_Times_Visited_VOIDRAID INTEGER DEFAULT 0,
        Total_Times_Completed_BLACKBEACH INTEGER DEFAULT 0,
        Total_Times_Completed_GOLEMPLAINS INTEGER DEFAULT 0,
        Total_Times_Completed_GOOLAKE INTEGER DEFAULT 0,
        Total_Times_Completed_BAZAAR INTEGER DEFAULT 0,
        Total_Times_Completed_FROZENWALL INTEGER DEFAULT 0,
        Total_Times_Completed_FOGGYSWAMP INTEGER DEFAULT 0,
        Total_Times_Completed_DAMPCAVE INTEGER DEFAULT 0,
        Total_Times_Completed_WISPGRAVEYARD INTEGER DEFAULT 0,
        Total_Times_Completed_MYSTERYSPACE INTEGER DEFAULT 0,
        Total_Times_Completed_GOLDSHORES INTEGER DEFAULT 0,
        Total_Times_Completed_SHIPGRAVEYARD INTEGER DEFAULT 0,
        Total_Times_Completed_ROOTJUNGLE INTEGER DEFAULT 0,
        Total_Times_Completed_ARENA INTEGER DEFAULT 0,
        Total_Times_Completed_LIMBO INTEGER DEFAULT 0,
        Total_Times_Completed_SKYMEADOW INTEGER DEFAULT 0,
        Total_Times_Completed_ARTIFACTWORLD INTEGER DEFAULT 0,
        Total_Times_Completed_MOON INTEGER DEFAULT 0,
        Total_Times_Completed_ANCIENTLOFT INTEGER DEFAULT 0,
        Total_Times_Completed_SNOWYFOREST INTEGER DEFAULT 0,
        Total_Times_Completed_SULFURPOOLS INTEGER DEFAULT 0,
        Total_Times_Completed_VOIDSTAGE INTEGER DEFAULT 0,
        Total_Times_Completed_VOIDRAID INTEGER DEFAULT 0,
        FOREIGN KEY (Run_ID) REFERENCES Run_Meta_Data(Run_ID)
    );
    '''
)

con.commit()
con.close()