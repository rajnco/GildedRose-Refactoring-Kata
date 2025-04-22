# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            match item.name:
                case "Sulfuras, Hand of Ragnaro": # legendary item, never has to be sold or decreases in `Quality`
                    pass
                case "Aged Brie":
                    item.quality = item.quality+1 if item.sell_in > 0 else item.quality+2
                    item.quality = 50 if item.quality > 50 else item.quality
                    item.sell_in += -1
                case "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in > 10:
                        item.quality = 50 if item.quality+1 > 50 else item.quality+1
                    elif item.sell_in > 5: 
                        item.quality = 50 if item.quality+2 > 50 else item.quality+2
                    elif item.sell_in > 0: 
                        item.quality = 50 if item.quality+3 > 50 else item.quality+3
                    else:
                        item.quality = 0
                    item.sell_in += -1
                case "Conjured":
                    item.quality = item.quality-2 if item.sell_in > 0 else item.quality-4
                    item.quality = 0 if item.quality < 0 else item.quality
                    item.sell_in += -1
                case _:     # defaut - other items
                    item.quality = item.quality-1 if item.sell_in > 0 else item.quality-2
                    item.quality = 0 if item.quality < 0 else item.quality
                    item.sell_in += -1
            

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
