from storm.database import  create_database
from storm.store import  Store
from storm.locals import Int, Unicode, Reference

class Kind(object):
    __storm_table__ = 'kinds'
    id = Int(primary=True)
    name = Unicode()

class Thing(object):
    __storm_table__ = 'things'
    id = Int(primary=True)
    name = Unicode()
    kind_id = Int()
    kind = Reference(kind_id, Kind.id)

db = create_database('sqlite:')
store = Store(db)

store.execute("CREATE TABLE kinds  "
                      "(id INTEGER PRIMARY KEY, name VARCHAR)")
store.execute("CREATE TABLE things  "
                      "(id INTEGER PRIMARY KEY, name VARCHAR, kind_id INTEGER)")

flowers = Kind()
flowers.name = u"Flowers"
store.add(flowers)

red_rose = Thing()
red_rose.name = u'Red Rose'
red_rose.kind = flowers
store.add(red_rose)

violet = Thing()
violet.name = u'Violet'
violet.kind = flowers
store.add(violet)

vases = Kind()
vases.name = u"Vases"
store.add(vases)

amphora = Thing()
amphora.name= u'Amphora'
amphora.kind = vases;
store.add(amphora)

store.commit()

all_flowers = store.find((Kind, Thing),
        Thing.kind_id == Kind.id,
        Kind.name == u'Flowers')

print [(kind.name, thing.name) for kind, thing in all_flowers]

all_vases = store.find((Kind, Thing),
        Thing.kind_id == Kind.id,
        Kind.name == u'Vases')

print [(kind.name, thing.name) for kind, thing in all_vases]
