# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
        items = [Item("Aged Brie", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(10, items[0].sell_in)
        
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)
        self.assertEqual(6, items[0].sell_in)
        
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 11)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

    def test_conjured(self):
        items = [Item("Conjured", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured", items[0].name)
        self.assertEqual(8, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_others(self):
        items = [Item("others", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("others", items[0].name)
        self.assertEqual(1, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

        
if __name__ == '__main__':
    unittest.main()
