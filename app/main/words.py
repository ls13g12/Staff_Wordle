from random import randint

def get_new_word():
    index = randint(0, len(words))
    return words[index]

words = [
'which',
'their',
'would',
'there',
'could',
'about',
'other',
'these',
'first',
'after',
'think',
'years',
'those',
'being',
'three',
'there',
'still',
'where',
'might',
'world',
'again',
'never',
'under',
'while',
'house',
'where',
'about',
'local',
'place',
'great',
'small',
'group',
'quite',
'party',
'every',
'women',
'often',
'given',
'money',
'point',
'night',
'state',
'taken',
'right',
'thing',
'water',
'right',
'large',
'asked',
'power',
'later',
'young',
'since',
'times',
'court',
'doing',
'early',
'today',
'using',
'words',
'child',
'until',
'level',
'known',
'major',
'began',
'areas',
'after',
'woman',
'among',
'clear',
'staff',
'black',
'whole',
'sense',
'seems',
'third',
'white',
'death',
'shall',
'heard',
'table',
'whose',
'order',
'range',
'study',
'trade',
'hours',
'hands',
'based',
'leave',
'human',
'cases',
'class',
'voice',
'since',
'short',
'value',
'paper',
'seven',
'eight',
'price',
'right',
'until',
'makes',
'union',
'terms',
'south',
'north',
'stage',
'comes',
'bring',
'weeks',
'start',
'shown',
'music',
'month',
'tried',
'wrong',
'issue',
'award',
'royal',
'moved',
'light',
'basis',
'field',
'added',
'means',
'round',
'heart',
'above',
'story',
'force',
'board',
'stood',
'books',
'legal',
'model',
'built',
'final',
'close',
'space',
'along',
'total',
'thank',
'prime',
'costs',
'takes',
'happy',
'parts',
'spent',
'floor',
'round',
'allow',
'rates',
'sorry',
'hotel',
'meant',
'lower',
'ideas',
'basic',
'write',
'aware',
'style',
'rules',
'needs',
'maybe',
'gives',
'sales',
'event',
'sound',
'ready',
'lines',
'looks',
'worth',
'press',
'blood',
'goods',
'carry',
'wrote',
'green',
'shows',
'offer',
'forms',
'miles',
'needs',
'plans',
'earth',
'title',
'girls',
'means',
'glass',
'heavy',
'speak',
'river',
'above',
'mouth',
'piece',
'stand',
'extra',
'whole',
'older',
'fully',
'peace',
'wants',
'types',
'below',
'radio',
'civil',
'fifty',
'start',
'knows',
'trees',
'learn',
'truth',
'works',
'lived',
'share',
'agree',
'front',
'media',
'avoid',
'stone',
'apply',
'lives',
'later',
'chair',
'horse',
'queen',
'names',
'cells',
'early',
'visit',
'stock',
'chief',
'drawn',
'firms',
'begin',
'image',
'views',
'scale',
'plant',
'spend',
'voice',
'alone',
'trust',
'ended',
'cause',
'crime',
'units',
'speed',
'along',
'spoke',
'stuff',
'front',
'match',
'build',
'reach',
'fresh',
'scene',
'items',
'phone',
'steps',
'watch',
'forty',
'sight',
'banks',
'claim',
'enjoy',
'users',
'video',
'worse',
'train',
'trial',
'joint',
'doubt',
'cover',
'usual',
'smile',
'sides',
'while',
'works',
'ahead',
'rural',
'twice',
'games',
'funds',
'shape',
'light',
'quiet',
'pound',
'raise',
'ought',
'noted',
'equal',
'homes',
'walls',
'talks',
'offer',
'cause',
'break',
'sites',
'quick',
'prove',
'notes',
'track',
'birds',
'route',
'liked',
'occur',
'under',
'rooms',
'daily',
'below',
'exist',
'check',
'alone',
'urban',
'youth',
'empty',
'lunch',
'upper',
'share',
'drugs',
'serve',
'enter',
'waste',
'facts',
'shook',
'faith',
'shops',
'moral',
'heads',
'birth',
'broke',
'entry',
'crown',
'vital',
'hoped',
'total',
'visit',
'tests',
'owner',
'wider',
'broad',
'drink',
'clean',
'doors',
'hence',
'teeth',
'brain',
'brief',
'signs',
'cover',
'claim',
'goals',
'guide',
'drive',
'ideal',
'bound',
'kinds',
'worry',
'minor',
'seats',
'noise',
'thick',
'loved',
'metal',
'grand',
'phase',
'coast',
'lying',
'worst',
'adult',
'faced',
'index',
'sport',
'judge',
'brown',
'funny',
'inner',
'least',
'pages',
'sharp',
'drive',
'named',
'sixty',
'agent',
'badly',
'place',
'cross',
'grown',
'crowd',
'argue',
'catch',
'tears',
'alive',
'begun',
'yours',
'angry',
'sheet',
'motor',
'shock',
'close',
'dress',
'grass',
'fruit',
'towns',
'lucky',
'touch',
'plate',
'tired',
'fight',
'sleep',
'teams',
'stars',
'cheap',
'cards',
'roads',
'grant',
'theme',
'error',
'dream',
'hello',
'chest',
'refer',
'beach',
'focus',
'clubs',
'bread',
'admit',
'chief',
'steel',
'leads',
'wages',
'tasks',
'panel',
'yards',
'chain',
'tells',
'armed',
'sleep',
'shoes',
'drove',
'false',
'sugar',
'block',
'aside',
'store',
'break',
'rapid',
'fixed',
'aimed',
'owned',
'drama',
'uncle',
'fifth',
'links',
'solid',
'apart',
'skill',
'close',
'dealt',
'films',
'round',
'taste',
'plane',
'scope',
'fault',
'enemy',
'rough',
'limit',
'abuse',
'tower',
'anger',
'sweet',
'arise',
'point',
'faces',
'feels',
'costs',
'input',
'tough',
'saved',
'truly',
'drink',
'turns',
'tools',
'cycle',
'nurse',
'frame',
'proud',
'pilot',
'calls',
'given',
'votes',
'cream',
'fewer',
'throw',
'awful',
'threw',
'hills',
'prize',
'novel',
'depth',
'calls',
'bills',
'reply',
'treat',
'green',
'sheep',
'study',
'cried',
'sound',
'dance',
'sorts',
'press',
'files',
'fight',
'still',
'rocks',
'plain',
'watch',
'since',
'finds',
'ratio',
'coach',
'fears',
'smoke',
'rugby',
'songs',
'clock',
'fixed',
'helps',
'chose',
'minds',
'marks',
'trust',
'steam',
'silly',
'teach',
'unity',
'taxes',
'shirt',
'round',
'final',
'being',
'roles',
'score',
'loans',
'dozen',
'pride',
'newly',
'buyer',
'match',
'ships',
'waves',
'knife',
'proof',
'marry',
'lives',
'pitch',
'boxes',
'holes',
'above',
'apple',
'dirty',
'holds',
'trend',
'loose',
'state',
'blind',
'knees',
'boots',
'smell',
'mummy',
'keeps',
'wheel',
'touch',
'shift',
'draft',
'squad',
'flesh',
'split',
'sixth',
'level',
'roots',
'stick',
'layer',
'risks',
'curve',
'adopt',
'guard',
'outer',
'topic',
'tends',
'hopes',
'angle',
'guess',
'wings',
'clear',
'meals',
'ruled',
'plays',
'texts',
'tight',
'opera',
'pupil',
'blame',
'mixed',
'guest',
'logic',
'acute',
'voted',
'acted',
'delay',
'valid',
'habit',
'bones',
'cross',
'urged',
'storm',
'gross',
'stuck',
'males',
'paint',
'posts',
'exact',
'daddy',
'audit',
'lists',
'album',
'leave',
'force',
'falls',
'canal',
'focus',
'mayor',
'worth',
'count',
'doubt',
'crash',
'print',
'laugh',
'pairs',
'lease',
'gains',
'foods',
'alarm',
'sheer',
'count',
'cloud',
'genes',
'likes',
'lands',
'swept',
'naked',
'asset',
'bands',
'actor',
'craft',
'plans',
'diary',
'ocean',
'bench',
'mixed',
'boats',
'judge',
'known',
'bible',
'moves',
'fired',
'cloth',
'shell',
'piano',
'clerk',
'gates',
'bonds',
'wives',
'solve',
'sadly',
'spare',
'grade',
'stake',
'asian',
'cheek',
'alter',
'shame',
'dates',
'abbey',
'fleet',
'stand',
'flats',
'debts',
'burst',
'stick',
'fails',
'local',
'cable',
'check',
'chips',
'order',
'brick',
'giant',
'hopes',
'farms',
'grain',
'fraud',
'swung',
'nasty',
'movie',
'shows',
'forum',
'relax',
'crazy',
'shots',
'reign',
'guilt',
'lover',
'slept',
'upset',
'forms',
'mouse',
'sizes',
'villa',
'edges',
'panic',
'label',
'theft',
'risen',
'devil',
'gifts',
'dying',
'magic',
'brave',
'laugh',
'opens',
'eaten',
'glory',
'fence',
'juice',
'hated',
'liver',
'seeds',
'moves',
'chaos',
'ranks',
'issue',
'clean',
'train',
'poems',
'drunk',
'pause',
'strip',
'super',
'acres',
'essay',
'arose',
'patch',
'crops',
'limit',
'races',
'climb',
'widow',
'steep',
'debut',
'chart',
'woods',
'grace',
'bases',
'harsh',
'lords',
'fibre',
'brass',
'balls',
'faint',
'roses',
'fluid',
'seeks',
'vague',
'virus',
'shift',
'naval',
'shoot',
'kings',
'waved',
'added',
'magic',
'sword',
'imply',
'blank',
'smart',
'tanks',
'tries',
'buses',
'shore',
'loads',
'stiff',
'cited',
'rigid',
'trick',
'mines',
'drank',
'tapes',
'eager',
'skirt',
'grief',
'parks',
'phone',
'shelf',
'waist',
'waste',
'sauce',
'coins',
'dance',
'winds',
'meets',
'bored',
'bonus',
'daily',
'cruel',
'faces',
'verse',
'ghost',
'shade',
'fatal',
'slope',
'angel',
'straw',
'upset',
'rival',
'loyal',
'paths',
'score',
'noble',
'nails',
'lorry',
'brand',
'looks',
'organ',
'cared',
'manor',
'crude',
'beans',
'brush',
'spell',
'dated',
'nerve',
'pence',
'serum',
'awake',
'bloke',
'forth',
'minus',
'ridge',
'posed',
'paint',
'grows',
'suite',
'reach',
'ozone',
'react',
'deals',
'jeans',
'tales',
'rally',
'grant',
'stuck',
'eagle',
'charm',
'grave',
'codes',
'reply',
'human',
'solar',
'poles',
'shake',
'black',
'bowel',
'photo',
'spots',
'knock',
'blues',
'sound',
'loves',
'prior',
'breed',
'guide',
'modes',
'bunch',
'fires',
'stops',
'toxic',
'lemon',
'basin',
'rings',
'swing',
'flood',
'trail',
'lakes',
'fetch',
'bombs',
'lined',
'penny',
'walks',
'venue',
'deals',
'blown',
'tiles',
'fancy',
'crack',
'heels',
'truck',
'plays',
'alike',
'smell',
'wiped',
'trace',
'usage',
'corps',
'zones',
'backs',
'pipes',
'width',
'white',
'smoke',
'camps',
'gazed',
'salad',
'array',
'major',
'plain',
'tenth',
'skull',
'jokes',
'pools',
'twins',
'borne',
'yield',
'thumb',
'dying',
'clash',
'armed',
'wound',
'cabin',
'medal',
'trips',
'mercy',
'blade',
'draws',
'stamp',
'ferry',
'alpha',
'flown',
'elbow',
'cliff',
'novel',
'sweat',
'pains',
'honey',
'weird',
'tutor',
'ports',
'flung',
'fever',
'tight',
'wines',
'smile',
'fined',
'march',
'polls',
'limbs',
'mount',
'trace',
'pulse',
'wrist',
'atoms',
'bride',
'realm',
'crews',
'flame',
'flour',
'print',
'boost',
'laser',
'yacht',
'arrow',
'vivid',
'noisy',
'quote',
'graph',
'boost',
'burnt',
'cease',
'shout',
'choir',
'acids',
'maker',
'tours',
'spare',
'adapt',
'civic',
'bells'
]