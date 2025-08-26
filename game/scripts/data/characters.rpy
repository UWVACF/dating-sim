# Image and character definitions/declarations for personnel
# Base image transform
transform base_char_transform(x = 600, y = 900, xoff = 0, yoff = 0):
    xsize x
    ysize y
    xoffset xoff
    yoffset yoff

# Personnel images
transform jessie_transform:
    base_char_transform

image jessie = At(ConditionSwitch("speaking_char == 'jessie'", "images/personnel/jessie/jessie talk.png", "True", "images/personnel/jessie/jessie neutral.png"), sprite_highlight("jessie"), jessie_transform)
image jessie neutral = "jessie"
image jessie talk = At("images/personnel/jessie/jessie talk.png", sprite_highlight("jessie"), jessie_transform)
image jessie happy = At("images/personnel/jessie/jessie happy.png", sprite_highlight("jessie"), jessie_transform)
image jessie sad = At("images/personnel/jessie/jessie sad.png", sprite_highlight("jessie"), jessie_transform)
image jessie upset = At("images/personnel/jessie/jessie upset.png", sprite_highlight("jessie"), jessie_transform)
image jessie surprise = At("images/personnel/jessie/jessie surprise.png", sprite_highlight("jessie"), jessie_transform)
image jessie panic = At("images/personnel/jessie/jessie panic.png", sprite_highlight("jessie"), jessie_transform)
image jessie fury = At("images/personnel/jessie/jessie fury.png", sprite_highlight("jessie"), jessie_transform)
image jessie pensive = At("images/personnel/jessie/jessie pensive.png", sprite_highlight("jessie"), jessie_transform)
image jessie unique = At("images/personnel/jessie/jessie unique.png", sprite_highlight("jessie"), jessie_transform)


transform aikha_transform:
    base_char_transform(x = 700, y = 1050, yoff = 100)

image aikha = At(ConditionSwitch("speaking_char == 'aikha'", "images/personnel/aikha/aikha talk.png", "True", "images/personnel/aikha/aikha neutral.png"), sprite_highlight("aikha"), aikha_transform)
image aikha neutral = "aikha"
image aikha talk = At("images/personnel/aikha/aikha talk.png", sprite_highlight("aikha"), aikha_transform)
image aikha happy = At("images/personnel/aikha/aikha happy.png", sprite_highlight("aikha"), aikha_transform)
image aikha sad = At("images/personnel/aikha/aikha sad.png", sprite_highlight("aikha"), aikha_transform)
image aikha upset = At("images/personnel/aikha/aikha upset.png", sprite_highlight("aikha"), aikha_transform)
image aikha surprise = At("images/personnel/aikha/aikha surprise.png", sprite_highlight("aikha"), aikha_transform)
image aikha panic = At("images/personnel/aikha/aikha panic.png", sprite_highlight("aikha"), aikha_transform)
image aikha fury = At("images/personnel/aikha/aikha fury.png", sprite_highlight("aikha"), aikha_transform)
image aikha pensive = At("images/personnel/aikha/aikha pensive.png", sprite_highlight("aikha"), aikha_transform)
image aikha unique = At("images/personnel/aikha/aikha unique.png", sprite_highlight("aikha"), aikha_transform)


transform alex_transform:
    base_char_transform

image alex = At(ConditionSwitch("speaking_char == 'alex'", "images/personnel/alex/alex talk.png", "True", "images/personnel/alex/alex neutral.png"), sprite_highlight("alex"), alex_transform)
image alex neutral = "alex"
image alex talk = At("images/personnel/alex/alex talk.png", sprite_highlight("alex"), alex_transform)
image alex happy = At("images/personnel/alex/alex happy.png", sprite_highlight("alex"), alex_transform)
image alex sad = At("images/personnel/alex/alex sad.png", sprite_highlight("alex"), alex_transform)
image alex upset = At("images/personnel/alex/alex upset.png", sprite_highlight("alex"), alex_transform)
image alex surprise = At("images/personnel/alex/alex surprise.png", sprite_highlight("alex"), alex_transform)
image alex panic = At("images/personnel/alex/alex panic.png", sprite_highlight("alex"), alex_transform)
image alex fury = At("images/personnel/alex/alex fury.png", sprite_highlight("alex"), alex_transform)
image alex pensive = At("images/personnel/alex/alex pensive.png", sprite_highlight("alex"), alex_transform)
image alex unique = At("images/personnel/alex/alex unique.png", sprite_highlight("alex"), alex_transform)


transform helco_transform:
    base_char_transform

image helco = At(ConditionSwitch("speaking_char == 'helco'", "images/personnel/helco/helco talk.png", "True", "images/personnel/helco/helco neutral.png"), sprite_highlight("helco"), helco_transform)
image helco neutral = "helco"
image helco talk = At("images/personnel/helco/helco talk.png", sprite_highlight("helco"), helco_transform)
image helco happy = At("images/personnel/helco/helco happy.png", sprite_highlight("helco"), helco_transform)
image helco sad = At("images/personnel/helco/helco sad.png", sprite_highlight("helco"), helco_transform)
image helco upset = At("images/personnel/helco/helco upset.png", sprite_highlight("helco"), helco_transform)
image helco surprise = At("images/personnel/helco/helco surprise.png", sprite_highlight("helco"), helco_transform)
image helco panic = At("images/personnel/helco/helco panic.png", sprite_highlight("helco"), helco_transform)
image helco fury = At("images/personnel/helco/helco fury.png", sprite_highlight("helco"), helco_transform)
image helco pensive = At("images/personnel/helco/helco pensive.png", sprite_highlight("helco"), helco_transform)
image helco unique = At("images/personnel/helco/helco unique.png", sprite_highlight("helco"), helco_transform)


transform ryz_transform:
    base_char_transform

image ryz = At(ConditionSwitch("speaking_char == 'ryz'", "images/personnel/ryz/ryz talk.png", "True", "images/personnel/ryz/ryz neutral.png"), sprite_highlight("ryz"), ryz_transform)
image ryz neutral = "ryz"
image ryz talk = At("images/personnel/ryz/ryz talk.png", sprite_highlight("ryz"), ryz_transform)
image ryz happy = At("images/personnel/ryz/ryz happy.png", sprite_highlight("ryz"), ryz_transform)
image ryz sad = At("images/personnel/ryz/ryz sad.png", sprite_highlight("ryz"), ryz_transform)
image ryz upset = At("images/personnel/ryz/ryz upset.png", sprite_highlight("ryz"), ryz_transform)
image ryz surprise = At("images/personnel/ryz/ryz surprise.png", sprite_highlight("ryz"), ryz_transform)
image ryz panic = At("images/personnel/ryz/ryz panic.png", sprite_highlight("ryz"), ryz_transform)
image ryz fury = At("images/personnel/ryz/ryz fury.png", sprite_highlight("ryz"), ryz_transform)
image ryz pensive = At("images/personnel/ryz/ryz pensive.png", sprite_highlight("ryz"), ryz_transform)
image ryz unique = At("images/personnel/ryz/ryz unique.png", sprite_highlight("ryz"), ryz_transform)


transform roose_transform:
    base_char_transform(x = 400, y=600, yoff = -100)

image roose = At(ConditionSwitch("speaking_char == 'roose'", "images/personnel/roose/roose talk.png", "True", "images/personnel/roose/roose neutral.png"), sprite_highlight("roose"), roose_transform)
image roose neutral = "roose"
image roose talk = At("images/personnel/ryz/roose talk.png", sprite_highlight("roose"), roose_transform)
image roose upset = At("images/personnel/ryz/roose upset.png", sprite_highlight("roose"), roose_transform)


transform uriel_transform:
    base_char_transform

image uriel = At(ConditionSwitch("speaking_char == 'uriel'", "images/personnel/uriel/uriel talk.png", "True", "images/personnel/uriel/uriel neutral.png"), sprite_highlight("uriel"), uriel_transform)
image uriel neutral = "uriel"
image uriel talk = At("images/personnel/uriel/uriel talk.png", sprite_highlight("uriel"), uriel_transform)
image uriel happy = At("images/personnel/uriel/uriel happy.png", sprite_highlight("uriel"), uriel_transform)
image uriel sad = At("images/personnel/uriel/uriel sad.png", sprite_highlight("uriel"), uriel_transform)
image uriel upset = At("images/personnel/uriel/uriel upset.png", sprite_highlight("uriel"), uriel_transform)
image uriel surprise = At("images/personnel/uriel/uriel surprise.png", sprite_highlight("uriel"), uriel_transform)
image uriel panic = At("images/personnel/uriel/uriel panic.png", sprite_highlight("uriel"), uriel_transform)
image uriel fury = At("images/personnel/uriel/uriel fury.png", sprite_highlight("uriel"), uriel_transform)
image uriel pensive = At("images/personnel/uriel/uriel pensive.png", sprite_highlight("uriel"), uriel_transform)
image uriel unique = At("images/personnel/uriel/uriel unique.png", sprite_highlight("uriel"), uriel_transform)


transform deceased_transform:
    base_char_transform

image deceased = At(ConditionSwitch("speaking_char == 'deceased'", "images/personnel/deceased/deceased talk.png", "True", "images/personnel/deceased/deceased neutral.png"), sprite_highlight("deceased"), deceased_transform)
image deceased neutral = "deceased"
image deceased talk = At("images/personnel/deceased/deceased talk.png", sprite_highlight("deceased"), deceased_transform)
image deceased happy = At("images/personnel/deceased/deceased happy.png", sprite_highlight("deceased"), deceased_transform)
image deceased sad = At("images/personnel/deceased/deceased sad.png", sprite_highlight("deceased"), deceased_transform)
image deceased upset = At("images/personnel/deceased/deceased upset.png", sprite_highlight("deceased"), deceased_transform)
image deceased surprise = At("images/personnel/deceased/deceased surprise.png", sprite_highlight("deceased"), deceased_transform)
image deceased panic = At("images/personnel/deceased/deceased panic.png", sprite_highlight("deceased"), deceased_transform)
image deceased fury = At("images/personnel/deceased/deceased fury.png", sprite_highlight("deceased"), deceased_transform)
image deceased pensive = At("images/personnel/deceased/deceased pensive.png", sprite_highlight("deceased"), deceased_transform)
image deceased unique = At("images/personnel/deceased/deceased unique.png", sprite_highlight("deceased"), deceased_transform)
image deceased objection = At("images/personnel/deceased/deceased objection.png", sprite_highlight("deceased"), deceased_transform)

transform lee_transform:
    base_char_transform

image lee = At(ConditionSwitch("speaking_char == 'lee'", "images/personnel/lee/lee talk.png", "True", "images/personnel/lee/lee neutral.png"), sprite_highlight("lee"), lee_transform)
image lee neutral = "lee"
image lee talk = At("images/personnel/lee/lee talk.png", sprite_highlight("lee"), lee_transform)
image lee happy = At("images/personnel/lee/lee happy.png", sprite_highlight("lee"), lee_transform)
image lee sad = At("images/personnel/lee/lee sad.png", sprite_highlight("lee"), lee_transform)
image lee upset = At("images/personnel/lee/lee upset.png", sprite_highlight("lee"), lee_transform)
image lee surprise = At("images/personnel/lee/lee surprise.png", sprite_highlight("lee"), lee_transform)
image lee panic = At("images/personnel/lee/lee panic.png", sprite_highlight("lee"), lee_transform)
image lee fury = At("images/personnel/lee/lee fury.png", sprite_highlight("lee"), lee_transform)
image lee pensive = At("images/personnel/lee/lee pensive.png", sprite_highlight("lee"), lee_transform)
image lee unique = At("images/personnel/lee/lee unique.png", sprite_highlight("lee"), lee_transform)


transform firewal_transform:
    base_char_transform

image firewal = At(ConditionSwitch("speaking_char == 'firewal'", "images/personnel/firewal/firewal talk.png", "True", "images/personnel/firewal/firewal neutral.png"), sprite_highlight("firewal"), firewal_transform)
image firewal neutral = "firewal"
image firewal talk = At("images/personnel/firewal/firewal talk.png", sprite_highlight("firewal"), firewal_transform)
image firewal happy = At("images/personnel/firewal/firewal happy.png", sprite_highlight("firewal"), firewal_transform)
image firewal sad = At("images/personnel/firewal/firewal sad.png", sprite_highlight("firewal"), firewal_transform)
image firewal upset = At("images/personnel/firewal/firewal upset.png", sprite_highlight("firewal"), firewal_transform)
image firewal surprise = At("images/personnel/firewal/firewal surprise.png", sprite_highlight("firewal"), firewal_transform)
image firewal panic = At("images/personnel/firewal/firewal panic.png", sprite_highlight("firewal"), firewal_transform)
image firewal fury = At("images/personnel/firewal/firewal fury.png", sprite_highlight("firewal"), firewal_transform)
image firewal pensive = At("images/personnel/firewal/firewal pensive.png", sprite_highlight("firewal"), firewal_transform)
image firewal unique = At("images/personnel/firewal/firewal unique.png", sprite_highlight("firewal"), firewal_transform)


transform pocketwal_transform:
    base_char_transform

image pocketwal = At(ConditionSwitch("speaking_char == 'pocketwal'", "images/personnel/firewal/pocketwal talk.png", "True", "images/personnel/firewal/pocketwal neutral.png"), sprite_highlight("pocketwal"), pocketwal_transform)
image pocketwal neutral = "pocketwal"
image pocketwal talk = At("images/personnel/firewal/pocketwal talk.png", sprite_highlight("pocketwal"), pocketwal_transform)
image pocketwal upset = At("images/personnel/firewal/pocketwal upset.png", sprite_highlight("pocketwal"), pocketwal_transform)

transform chan_transform:
    base_char_transform

image chan = At(ConditionSwitch("speaking_char == 'chan'", "images/personnel/chan/chan talk.png", "True", "images/personnel/chan/chan neutral.png"), sprite_highlight("chan"), chan_transform)
image chan neutral = "chan"
image chan talk = At("images/personnel/chan/chan talk.png", sprite_highlight("chan"), chan_transform)
image chan happy = At("images/personnel/chan/chan happy.png", sprite_highlight("chan"), chan_transform)
image chan sad = At("images/personnel/chan/chan sad.png", sprite_highlight("chan"), chan_transform)
image chan upset = At("images/personnel/chan/chan upset.png", sprite_highlight("chan"), chan_transform)
image chan surprise = At("images/personnel/chan/chan surprise.png", sprite_highlight("chan"), chan_transform)
image chan panic = At("images/personnel/chan/chan panic.png", sprite_highlight("chan"), chan_transform)
image chan fury = At("images/personnel/chan/chan fury.png", sprite_highlight("chan"), chan_transform)
image chan pensive = At("images/personnel/chan/chan pensive.png", sprite_highlight("chan"), chan_transform)
image chan unique = At("images/personnel/chan/chan unique.png", sprite_highlight("chan"), chan_transform)


transform syg_transform:
    base_char_transform(x = 550, y = 825)

image syg = At(ConditionSwitch("speaking_char == 'syg'", "images/personnel/syg/syg talk.png", "True", "images/personnel/syg/syg neutral.png"), sprite_highlight("syg"), syg_transform)
image syg neutral = "syg"
image syg talk = At("images/personnel/syg/syg talk.png", sprite_highlight("syg"), syg_transform)
image syg happy = At("images/personnel/syg/syg happy.png", sprite_highlight("syg"), syg_transform)
image syg sad = At("images/personnel/syg/syg sad.png", sprite_highlight("syg"), syg_transform)
image syg upset = At("images/personnel/syg/syg upset.png", sprite_highlight("syg"), syg_transform)
image syg surprise = At("images/personnel/syg/syg surprise.png", sprite_highlight("syg"), syg_transform)
image syg panic = At("images/personnel/syg/syg panic.png", sprite_highlight("syg"), syg_transform)
image syg fury = At("images/personnel/syg/syg fury.png", sprite_highlight("syg"), syg_transform)
image syg pensive = At("images/personnel/syg/syg pensive.png", sprite_highlight("syg"), syg_transform)
image syg unique = At("images/personnel/syg/syg unique.png", sprite_highlight("syg"), syg_transform)


transform caffi_transform:
    base_char_transform

image caffi = At(ConditionSwitch("speaking_char == 'caffi'", "images/personnel/caffi/caffi talk.png", "True", "images/personnel/caffi/caffi neutral.png"), sprite_highlight("caffi"), caffi_transform)
image caffi neutral = "caffi"
image caffi talk = At("images/personnel/caffi/caffi talk.png", sprite_highlight("caffi"), caffi_transform)
image caffi happy = At("images/personnel/caffi/caffi happy.png", sprite_highlight("caffi"), caffi_transform)
image caffi sad = At("images/personnel/caffi/caffi sad.png", sprite_highlight("caffi"), caffi_transform)
image caffi upset = At("images/personnel/caffi/caffi upset.png", sprite_highlight("caffi"), caffi_transform)
image caffi surprise = At("images/personnel/caffi/caffi surprise.png", sprite_highlight("caffi"), caffi_transform)
image caffi panic = At("images/personnel/caffi/caffi panic.png", sprite_highlight("caffi"), caffi_transform)
image caffi fury = At("images/personnel/caffi/caffi fury.png", sprite_highlight("caffi"), caffi_transform)
image caffi pensive = At("images/personnel/caffi/caffi pensive.png", sprite_highlight("caffi"), caffi_transform)
image caffi unique = At("images/personnel/caffi/caffi unique.png", sprite_highlight("caffi"), caffi_transform)


transform paul_transform:
    base_char_transform

image paul = At(ConditionSwitch("speaking_char == 'paul'", "images/personnel/paul/paul talk.png", "True", "images/personnel/paul/paul neutral.png"), sprite_highlight("paul"), paul_transform)
image paul neutral = "paul"
image paul talk = At("images/personnel/paul/paul talk.png", sprite_highlight("paul"), paul_transform)
image paul happy = At("images/personnel/paul/paul happy.png", sprite_highlight("paul"), paul_transform)
image paul sad = At("images/personnel/paul/paul sad.png", sprite_highlight("paul"), paul_transform)
image paul upset = At("images/personnel/paul/paul upset.png", sprite_highlight("paul"), paul_transform)
image paul surprise = At("images/personnel/paul/paul surprise.png", sprite_highlight("paul"), paul_transform)
image paul panic = At("images/personnel/paul/paul panic.png", sprite_highlight("paul"), paul_transform)
image paul fury = At("images/personnel/paul/paul fury.png", sprite_highlight("paul"), paul_transform)
image paul pensive = At("images/personnel/paul/paul pensive.png", sprite_highlight("paul"), paul_transform)
image paul unique = At("images/personnel/paul/paul unique.png", sprite_highlight("paul"), paul_transform)


transform plutoes_transform:
    base_char_transform

image plutoes = At(ConditionSwitch("speaking_char == 'plutoes'", "images/personnel/plutoes/plutoes talk.png", "True", "images/personnel/plutoes/plutoes neutral.png"), sprite_highlight("plutoes"), plutoes_transform)
image plutoes neutral = "plutoes"
image plutoes talk = At("images/personnel/plutoes/plutoes talk.png", sprite_highlight("plutoes"), plutoes_transform)
image plutoes happy = At("images/personnel/plutoes/plutoes happy.png", sprite_highlight("plutoes"), plutoes_transform)
image plutoes upset = At("images/personnel/plutoes/plutoes upset.png", sprite_highlight("plutoes"), plutoes_transform)
image plutoes unique = At("images/personnel/plutoes/plutoes unique.png", sprite_highlight("plutoes"), plutoes_transform)
# image plutoes sad = At("images/personnel/plutoes/plutoes sad.png", sprite_highlight("plutoes"), plutoes_transform)
# image plutoes surprise = At("images/personnel/plutoes/plutoes surprise.png", sprite_highlight("plutoes"), plutoes_transform)
# image plutoes panic = At("images/personnel/plutoes/plutoes panic.png", sprite_highlight("plutoes"), plutoes_transform)
# image plutoes fury = At("images/personnel/plutoes/plutoes fury.png", sprite_highlight("plutoes"), plutoes_transform)
# image plutoes pensive = At("images/personnel/plutoes/plutoes pensive.png", sprite_highlight("plutoes"), plutoes_transform)


transform venture_transform:
    base_char_transform

image venture = At(ConditionSwitch("speaking_char == 'venture'", "images/personnel/venture/venture talk.png", "True", "images/personnel/venture/venture neutral.png"), sprite_highlight("venture"), venture_transform)
image venture neutral = "venture"
image venture talk = At("images/personnel/venture/venture talk.png", sprite_highlight("venture"), venture_transform)
image venture happy = At("images/personnel/venture/venture happy.png", sprite_highlight("venture"), venture_transform)
image venture sad = At("images/personnel/venture/venture sad.png", sprite_highlight("venture"), venture_transform)
image venture upset = At("images/personnel/venture/venture upset.png", sprite_highlight("venture"), venture_transform)
image venture surprise = At("images/personnel/venture/venture surprise.png", sprite_highlight("venture"), venture_transform)
image venture panic = At("images/personnel/venture/venture panic.png", sprite_highlight("venture"), venture_transform)
image venture fury = At("images/personnel/venture/venture fury.png", sprite_highlight("venture"), venture_transform)
image venture pensive = At("images/personnel/venture/venture pensive.png", sprite_highlight("venture"), venture_transform)
image venture unique = At("images/personnel/venture/venture unique.png", sprite_highlight("venture"), venture_transform)


transform b6_transform:
    base_char_transform

image b6 = At(ConditionSwitch("speaking_char == 'b6'", "images/personnel/b6/b6 talk.png", "True", "images/personnel/b6/b6 neutral.png"), sprite_highlight("b6"), b6_transform)
image b6 neutral = "b6"
image b6 talk = At("images/personnel/b6/b6 talk.png", sprite_highlight("b6"), b6_transform)
image b6 happy = At("images/personnel/b6/b6 happy.png", sprite_highlight("b6"), b6_transform)
image b6 sad = At("images/personnel/b6/b6 sad.png", sprite_highlight("b6"), b6_transform)
image b6 upset = At("images/personnel/b6/b6 upset.png", sprite_highlight("b6"), b6_transform)
image b6 surprise = At("images/personnel/b6/b6 surprise.png", sprite_highlight("b6"), b6_transform)
image b6 panic = At("images/personnel/b6/b6 panic.png", sprite_highlight("b6"), b6_transform)
image b6 fury = At("images/personnel/b6/b6 fury.png", sprite_highlight("b6"), b6_transform)
image b6 pensive = At("images/personnel/b6/b6 pensive.png", sprite_highlight("b6"), b6_transform)
image b6 unique = At("images/personnel/b6/b6 unique.png", sprite_highlight("b6"), b6_transform)


transform meme_transform:
    base_char_transform

image meme = At(ConditionSwitch("speaking_char == 'meme'", "images/personnel/meme/meme talk.png", "True", "images/personnel/meme/meme neutral.png"), sprite_highlight("meme"), meme_transform)
image meme neutral = "meme"
image meme talk = At("images/personnel/meme/meme talk.png", sprite_highlight("meme"), meme_transform)
image meme happy = At("images/personnel/meme/meme happy.png", sprite_highlight("meme"), meme_transform)
image meme sad = At("images/personnel/meme/meme sad.png", sprite_highlight("meme"), meme_transform)
image meme upset = At("images/personnel/meme/meme upset.png", sprite_highlight("meme"), meme_transform)
image meme surprise = At("images/personnel/meme/meme surprise.png", sprite_highlight("meme"), meme_transform)
image meme panic = At("images/personnel/meme/meme panic.png", sprite_highlight("meme"), meme_transform)
image meme fury = At("images/personnel/meme/meme fury.png", sprite_highlight("meme"), meme_transform)
image meme pensive = At("images/personnel/meme/meme pensive.png", sprite_highlight("meme"), meme_transform)
image meme unique = At("images/personnel/meme/meme unique.png", sprite_highlight("meme"), meme_transform)


transform moon_transform:
    base_char_transform

image moon = At(ConditionSwitch("speaking_char == 'moon'", "images/personnel/moon/moon talk.png", "True", "images/personnel/moon/moon neutral.png"), sprite_highlight("moon"), moon_transform)
image moon neutral = "moon"
image moon talk = At("images/personnel/moon/moon talk.png", sprite_highlight("moon"), moon_transform)
image moon happy = At("images/personnel/moon/moon happy.png", sprite_highlight("moon"), moon_transform)
image moon sad = At("images/personnel/moon/moon sad.png", sprite_highlight("moon"), moon_transform)
image moon upset = At("images/personnel/moon/moon upset.png", sprite_highlight("moon"), moon_transform)
image moon surprise = At("images/personnel/moon/moon surprise.png", sprite_highlight("moon"), moon_transform)
image moon panic = At("images/personnel/moon/moon panic.png", sprite_highlight("moon"), moon_transform)
image moon fury = At("images/personnel/moon/moon fury.png", sprite_highlight("moon"), moon_transform)
image moon pensive = At("images/personnel/moon/moon pensive.png", sprite_highlight("moon"), moon_transform)
image moon unique = At("images/personnel/moon/moon unique.png", sprite_highlight("moon"), moon_transform)


transform egg_transform:
    base_char_transform(yoff = -60)

image egg = At(ConditionSwitch("speaking_char == 'egg'", "images/personnel/egg/egg talk.png", "True", "images/personnel/egg/egg neutral.png"), sprite_highlight("egg"), egg_transform)
image egg neutral = "egg"
image egg talk = At("images/personnel/egg/egg talk.png", sprite_highlight("egg"), egg_transform)
image egg happy = At("images/personnel/egg/egg happy.png", sprite_highlight("egg"), egg_transform)
image egg sad = At("images/personnel/egg/egg sad.png", sprite_highlight("egg"), egg_transform)
image egg upset = At("images/personnel/egg/egg upset.png", sprite_highlight("egg"), egg_transform)
image egg surprise = At("images/personnel/egg/egg surprise.png", sprite_highlight("egg"), egg_transform)
image egg panic = At("images/personnel/egg/egg panic.png", sprite_highlight("egg"), egg_transform)
image egg fury = At("images/personnel/egg/egg fury.png", sprite_highlight("egg"), egg_transform)
image egg pensive = At("images/personnel/egg/egg pensive.png", sprite_highlight("egg"), egg_transform)
image egg unique = At("images/personnel/egg/egg unique.png", sprite_highlight("egg"), egg_transform)


transform hampter_transform:
    base_char_transform

image hampter = At(ConditionSwitch("speaking_char == 'hampter'", "images/personnel/hampter/hampter talk.png", "True", "images/personnel/hampter/hampter neutral.png"), sprite_highlight("hampter"), hampter_transform)
image hampter neutral = "hampter"
image hampter talk = At("images/personnel/hampter/hampter talk.png", sprite_highlight("hampter"), hampter_transform)
image hampter happy = At("images/personnel/hampter/hampter happy.png", sprite_highlight("hampter"), hampter_transform)
image hampter sad = At("images/personnel/hampter/hampter sad.png", sprite_highlight("hampter"), hampter_transform)
image hampter upset = At("images/personnel/hampter/hampter upset.png", sprite_highlight("hampter"), hampter_transform)
image hampter surprise = At("images/personnel/hampter/hampter surprise.png", sprite_highlight("hampter"), hampter_transform)
image hampter panic = At("images/personnel/hampter/hampter panic.png", sprite_highlight("hampter"), hampter_transform)
image hampter fury = At("images/personnel/hampter/hampter fury.png", sprite_highlight("hampter"), hampter_transform)
image hampter pensive = At("images/personnel/hampter/hampter pensive.png", sprite_highlight("hampter"), hampter_transform)
image hampter unique = At("images/personnel/hampter/hampter unique.png", sprite_highlight("hampter"), hampter_transform)

# Characters
define base_char = Character("", callback=name_callback)

define jessie = Character("Dr. Jessie", kind=base_char, color="#ff6dcf", cb_name="jessie", image="jessie")
define jessie_unknown = Character("???", kind=jessie)

define firewal = Character("Dr. Firewal", kind=base_char, color="#961e44", cb_name="firewal", image="firewal")
define wal = Character(kind=firewal)
define firewal_unknown = Character("???", kind=firewal)
define wal1 = Character("Wal No.1", kind=firewal)
define wal387 = Character("Wal No.387", kind=firewal)
define wal641 = Character("Wal No.641", kind=firewal)
define wal1986 = Character("Wal No.1986", kind=firewal)
define walbots = Character("Walbots", kind=firewal)
define pocketwal = Character("Pocket Wal", kind=firewal, what_size=30, cb_name="pocketwal", image="pocketwal")

define helco = Character("Dr. Helco", kind=base_char, color="#fffda1", cb_name="helco", image="helco")
define helco_unknown = Character("???", kind=helco)

define aikha = Character("Dr. Aikha", kind=base_char, color="#8f76ff", cb_name="aikha", image="aikha")
define aikha_unknown = Character("???", kind=aikha)

define plutoes = Character("Plutoes", kind=base_char, color="#62ff58", cb_name="plutoes", image="plutoes", what_color="#ff2d00", what_bold = True)
define plutoes_unknown = Character("???", kind=plutoes)

define alex = Character("Dr. Alex", kind=base_char, color="#000000", cb_name="alex", image="alex")
define alex_unknown = Character("???", kind=alex)

define deceased = Character("Dr. Deceased", kind=base_char, color="#894bb2", cb_name="deceased", image="deceased")
define deceased_unknown = Character("???", kind=deceased)

define syg = Character("Dr. Syg", kind=base_char, color="#6e7384", cb_name="syg", image="syg")
define syg_unknown = Character("???", kind=syg)

define chan = Character("Dr. Chan", kind=base_char, color="#46bdc6", cb_name="chan", image="chan")
define chan_unknown = Character("???", kind=chan)
define ethy = Character("Ethy", kind=chan, color="#000000")

define lee = Character("Dr. Lee", kind=base_char, color="#ff0000", cb_name="lee", image="lee")
define lee_unknown = Character("???", kind=lee)

define b6 = Character("b6c5b6", kind=base_char, color="#364036", cb_name="b6", image="b6")
define b6_unknown = Character("???", kind=b6)

define paul = Character("Paul Demure Johnson", kind=base_char, color="#6e7f55", cb_name="paul", image="paul")
define paul_unknown = Character("???", kind=paul)

define uriel = Character("Uriel", kind=base_char, color="#acced2", cb_name="uriel", image="uriel")
define uriel_unknown = Character("???", kind=uriel)

define egg = Character("Egg's Assistant", kind=base_char, color="#ff8561", cb_name="egg", image="egg")
define egg_unknown = Character("???", kind=egg)

define caffi = Character("\"Dr\" Caffi", kind=base_char, color="#000000", cb_name="caffi", image="caffi") # change colour
define caffi_unknown = Character("???", kind=caffi)

define moon = Character("Hustlemoon", kind=base_char, color="#caff85", cb_name="moon", image="moon")
define moon_unknown = Character("???", kind=moon)

define hampter = Character("Hampter", kind=base_char, color="#6b78ac", cb_name="hampter", image="hampter")
define hampter_unknown = Character("???", kind=hampter)

define meme = Character("Meme", kind=base_char, color="#e4f8fe", cb_name="meme", image="meme") # change colour
define meme_unknown = Character("???", kind=meme)

define ryz = Character("Dr. Ryz", kind=base_char, color="#f9be82", cb_name="ryz", image="ryz")
define ryz_unknown = Character("???", kind=ryz)
define roose = Character("Pebbles", kind=ryz, image="roose", cb_name="roose")
define roose_unknown = Character("???", kind=roose)

define venture = Character("Dr. Wayne Venture", kind=base_char, color="#8f7557", cb_name="venture", image="venture") # change colour
define venture_unknown = Character("???", kind=venture)

define player = Character("[player_name]", kind=base_char, color="#444444", cb_name="player")

define trickster = Character("?", kind=base_char, color="#095a10", cb_name="trickster", what_bold = True, what_size = 45)

define n = Character("", kind=base_char, cb_name="") # narrator, required to unhighlight characters whenever narration is occurring
define unknown = Character("???", kind=base_char, color="#000000", cb_name="???")
define speaker = Character("Security Speakers", kind=base_char, color="#000000", cb_name="Speakers")
define crowd = Character("Crowd", kind=base_char, color="#000000", cb_name="Crowd")
define person = Character("Person", kind=base_char, color="#000000", cb_name="Person")
define josh = Character("Josh", kind=base_char, color="#000000", cb_name="Josh")