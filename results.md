# Some output

I love playing with this word similarity. For such a small sample of
text, with such a narrow focus, this is pretty remarkable.

### The classic gender vectors (note that 0.82996 is *really* high)
```
>>> word
"girl's"

>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model

['[("boy\'s", 0.8299641609191895),<br>\n("man\'s", 0.7393919825553894),<br>\n("guy\'s", 0.7309567928314209),<br>\n("woman\'s", 0.7253532409667969),<br>\n("filmmaker\'s", 0.6536828279495239),<br>\n("lady\'s", 0.651617169380188),<br>\n("cop\'s", 0.646100640296936),<br>\n("couple\'s", 0.6419130563735962),<br>\n("doctor\'s", 0.6308389902114868),<br>\n("director\'s", 0.6147785782814026),<br>\n("villain\'s", 0.6128612756729126),<br>\n("victim\'s", 0.6014924049377441),<br>\n("killer\'s", 0.6007323265075684),<br>\n("latter\'s", 0.6000511646270752),<br>\n("detective\'s", 0.5994700193405151),<br>\n("pilot\'s", 0.5895627737045288),<br>\n("viewer\'s", 0.5883914232254028),<br>\n("nerd\'s", 0.5879437923431396),<br>\n("girls\'", 0.5783867835998535),<br>\n("protagonist\'s", 0.5780603885650635)]']
```

### Praise

```
>>> word
'lush'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('beautiful', 0.6194934248924255),<br>\n('stunning', 0.5849698781967163),<br>\n('breathtaking', 0.5708267092704773),<br>\n('vibrant', 0.5466954708099365),<br>\n('lovely', 0.5379860401153564),<br>\n('vivid', 0.534378170967102),<br>\n('colorful', 0.5296449661254883),<br>\n('gorgeous', 0.5279978513717651),<br>\n('sumptuous', 0.5179687142372131),<br>\n('elegant', 0.5123969316482544),<br>\n('drab', 0.511672854423523),<br>\n('evocative', 0.5070104598999023),<br>\n('stylish', 0.49958324432373047),<br>\n('atmoshpere', 0.49884212017059326),<br>\n('haunting', 0.49370983242988586),<br>\n('texture', 0.4914795756340027),<br>\n('gauzy', 0.49054208397865295),<br>\n('glorious', 0.48608019948005676),<br>\n('splendid', 0.4770998954772949),<br>\n('photography', 0.4763798415660858)]"]
```

```
>>> word
'first-rate'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('top-notch', 0.8059890270233154),<br>\n('superb', 0.7795922756195068),<br>\n('terrific', 0.7663544416427612),<br>\n('fine', 0.7528128623962402),<br>\n('fantastic', 0.7432597875595093),<br>\n('great', 0.703092098236084),<br>\n('wonderful', 0.7029855251312256),<br>\n('stellar', 0.7015502452850342),<br>\n('solid', 0.6985502243041992),<br>\n('brilliant', 0.6984843015670776),<br>\n('fabulous', 0.6785246729850769),<br>\n('phenomenal', 0.670339822769165),<br>\n('splendid', 0.650468111038208),<br>\n('flawless', 0.646262526512146),<br>\n('marvelous', 0.644767165184021),<br>\n('terrible', 0.6328909397125244),<br>\n('stunning', 0.6261956691741943),<br>\n('competent', 0.6204208731651306),<br>\n('decent', 0.6184316277503967),<br>\n('superlative', 0.6146631836891174)]"]
```

### Note: this word seems to capture the *context* of movie reviews

```
'cheap'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('cheesy', 0.6911131143569946),<br>\n('fake', 0.6412746906280518),<br>\n('lame', 0.6321353912353516),<br>\n('crappy', 0.6254785656929016),<br>\n('silly', 0.6061266660690308),<br>\n('hokey', 0.6002886891365051),<br>\n('phony', 0.5998878479003906),<br>\n('shoddy', 0.5949713587760925),<br>\n('low-budget', 0.5943334102630615),<br>\n('slapdash', 0.5856012105941772),<br>\n('sloppy', 0.5769343376159668),<br>\n('good', 0.5748993158340454),<br>\n('corny', 0.5747735500335693),<br>\n('lousy', 0.5731701850891113),<br>\n('quick', 0.5710335373878479),<br>\n('amateurish', 0.5680219531059265),<br>\n('clumsy', 0.566576361656189),<br>\n('poor', 0.5660935640335083),<br>\n('glossy', 0.5585795640945435),<br>\n('dumb', 0.5490933656692505)]"]
```

### Spatial concepts

```
>>> word
'made'
>>> similars_per_model
["[('created', 0.7522087097167969),<br>\n('produced', 0.718218982219696),<br>\n('ruined', 0.7093406319618225),<br>\n('followed', 0.6888588666915894),<br>\n('provided', 0.6852389574050903),<br>\n('makes', 0.678665816783905),<br>\n('represented', 0.6753371953964233),<br>\n('captured', 0.6460093259811401),<br>\n('making', 0.6290754079818726),<br>\n('played', 0.6278656721115112),<br>\n('struck', 0.6191168427467346),<br>\n('caused', 0.6156330108642578),<br>\n('showed', 0.6079094409942627),<br>\n('spawned', 0.6059475541114807),<br>\n('served', 0.6052937507629395),<br>\n('matched', 0.6027909517288208),<br>\n('inspired', 0.6027482748031616),<br>\n('won', 0.5956460237503052),<br>\n('penned', 0.5937151908874512),<br>\n('preceded', 0.5932760238647461)]"]
```

```
>>> word
'packs'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('holds', 0.7112924456596375),<br>\n('carries', 0.710108757019043),<br>\n('puts', 0.697668194770813),<br>\n('boasts', 0.69142746925354),<br>\n('maintains', 0.6843779683113098),<br>\n('throws', 0.6656831502914429),<br>\n('delivers', 0.6625145673751831),<br>\n('displays', 0.6622449159622192),<br>\n('offers', 0.6617070436477661),<br>\n('takes', 0.6587049961090088),<br>\n('provides', 0.6563002467155457),<br>\n('retains', 0.6551932096481323),<br>\n('creates', 0.6531840562820435),<br>\n('drops', 0.6525987386703491),<br>\n('raises', 0.6518259048461914),<br>\n('requires', 0.6474635601043701),<br>\n('contains', 0.644067645072937),<br>\n('features', 0.6408087015151978),<br>\n('pushes', 0.6375831365585327),<br>\n('gives', 0.6334232091903687)]"]
```

```
>>> word
'installments'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('episodes', 0.8144651651382446),<br>\n('entries', 0.7977363467216492),<br>\n('seasons', 0.7464076280593872),<br>\n('shorts', 0.7366950511932373),<br>\n('films', 0.7200137376785278),<br>\n('cartoons', 0.7140017151832581),<br>\n('outings', 0.704132080078125),<br>\n('sequels', 0.7003395557403564),<br>\n('movies', 0.6888891458511353),<br>\n('westerns', 0.6786016821861267),<br>\n('season', 0.6408534049987793),<br>\n('segments', 0.6361736059188843),<br>\n('pairings', 0.6239889860153198),<br>\n('days', 0.6215971112251282),<br>\n('flicks', 0.6199459433555603),<br>\n('collaborations', 0.6191555261611938),<br>\n('chapters', 0.6187926530838013),<br>\n('titles', 0.6111135482788086),<br>\n('specials', 0.602582573890686),<br>\n('worlds', 0.5993162393569946)]"]
```

```
>>> word
"hero's"
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
['[("cop\'s", 0.6337592601776123),<br>\n("protagonist\'s", 0.6221911311149597),<br>\n("latter\'s", 0.5726263523101807),<br>\n("captain\'s", 0.5639528036117554),<br>\n("boys\'", 0.5572121143341064),<br>\n("narrator\'s", 0.5557647943496704),<br>\n("girl\'s", 0.5469956398010254),<br>\n("heroine\'s", 0.5446479916572571),<br>\n("star\'s", 0.5410529971122742),<br>\n(\'titular\', 0.5388111472129822),<br>\n("viewer\'s", 0.5332425236701965),<br>\n("boy\'s", 0.5158419609069824),<br>\n(\'protagonists\', 0.5127913951873779),<br>\n("killer\'s", 0.5098795890808105),<br>\n("couple\'s", 0.506056547164917),<br>\n("sheriff\'s", 0.5014190077781677),<br>\n("audience\'s", 0.49549078941345215),<br>\n(\'groom-to-be\', 0.48879337310791016),<br>\n(\'fbi\', 0.4818602204322815),<br>\n(\'lovebirds\', 0.4811992049217224)]']
```

```
>>> word
'gameplay'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('animation', 0.6741321086883545),<br>\n('cgi', 0.6070172190666199),<br>\n('storyline', 0.6067904233932495),<br>\n('dialogue', 0.6036345958709717),<br>\n('plot', 0.5964829325675964),<br>\n('graphics', 0.5905351638793945),<br>\n('music', 0.5841403007507324),<br>\n('story-line', 0.5767802000045776),<br>\n('dialog', 0.5719113349914551),<br>\n('pacing', 0.5666353702545166),<br>\n('cg', 0.5598408579826355),<br>\n('cinematography', 0.549915075302124),<br>\n('narrative', 0.5481268763542175),<br>\n('set-up', 0.54716956615448),<br>\n('outcome', 0.5464971661567688),<br>\n('menus', 0.5418481826782227),<br>\n('acting', 0.5416570901870728),<br>\n('dubbing', 0.5410113334655762),<br>\n('storytelling', 0.539592981338501),<br>\n('editing', 0.5380603075027466)]"]
```

```
'refuge'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('shelter', 0.6924057602882385),<br>\n('place', 0.6539802551269531),<br>\n('solace', 0.6313884258270264),<br>\n('position', 0.5824686288833618),<br>\n('lodgings', 0.5810263156890869),<br>\n('bath', 0.5541285872459412),<br>\n('cave', 0.5494455099105835),<br>\n('nearby', 0.5466607213020325),<br>\n('footsteps', 0.5435929298400879),<br>\n('castle', 0.5362998247146606),<br>\n('room', 0.5339670181274414),<br>\n('comfort', 0.5334790349006653),<br>\n('existence', 0.5231665372848511),<br>\n('glimpse', 0.519077718257904),<br>\n('celebration', 0.5185189247131348),<br>\n('maze', 0.517688512802124),<br>\n('midst', 0.512773334980011),<br>\n('role', 0.5104367733001709),<br>\n('town', 0.5089086294174194),<br>\n('convent', 0.5062904357910156)]"]
```

```
>>> word
'intimidate'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('manipulate', 0.6305797100067139),<br>\n('seduce', 0.6068636178970337),<br>\n('befriend', 0.597912073135376),<br>\n('kill', 0.5854027271270752),<br>\n('lure', 0.571258544921875),<br>\n('humiliate', 0.5662961602210999),<br>\n('persuade', 0.5611627101898193),<br>\n('attach', 0.555056095123291),<br>\n('convert', 0.5538538098335266),<br>\n('respond', 0.55177241563797),<br>\n('protect', 0.5487220287322998),<br>\n('belittle', 0.5424045324325562),<br>\n('kidnap', 0.5409039855003357),<br>\n('bribe', 0.5349352955818176),<br>\n('defend', 0.5317119359970093),<br>\n('empower', 0.5315194129943848),<br>\n('sell', 0.5312007665634155),<br>\n('push', 0.5299375057220459),<br>\n('eliminate', 0.528980016708374),<br>\n('react', 0.5278134346008301)]"]
```

```
>>> word
'etched'
>>> similars_per_model = [str(model.most_similar(word, topn=20)).replace('), ','),<br>\n')]
>>> similars_per_model
["[('imprinted', 0.5431563854217529),<br>\n('placed', 0.524910569190979),<br>\n('shoved', 0.5198550224304199),<br>\n('woven', 0.5132993459701538),<br>\n('folds', 0.49804532527923584),<br>\n('engraved', 0.49088791012763977),<br>\n('reflected', 0.48917967081069946),<br>\n('implanted', 0.48829710483551025),<br>\n('seared', 0.4871458411216736),<br>\n('flung', 0.4824492335319519),<br>\n('experimented', 0.48146021366119385),<br>\n('slipped', 0.4808548390865326),<br>\n('falling', 0.47620558738708496),<br>\n('drilled', 0.4753063917160034),<br>\n('jiggled', 0.471981406211853),<br>\n('spliced', 0.4711209535598755),<br>\n('embedded', 0.47037604451179504),<br>\n('planted', 0.4698184132575989),<br>\n('perusing', 0.4635252356529236),<br>\n('transformed', 0.4634949564933777)]"]
```
