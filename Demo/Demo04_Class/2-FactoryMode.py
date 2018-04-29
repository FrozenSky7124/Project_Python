#!/usr/bin/python
# -*- coding:utf-8 -*-

# Factory Mode Test
# 工厂模式


class BaseStore(object):

    # Define method No Realize
    def createItem(self, typeName)
        pass

    def order(self, typeName)
        self.item = self.createItem(typeName)
        self.item.demo1()
        self.item.demo2()


class XStore(BaseStore):

    def createItem(self, typeName)
        self.itemFactory = ItemFactory()
        return self.itemFactory.createItem(typeName)


class AItem(object):

    def demo1(self):
        pass

    def demo2(self):
        pass


class BItem(object):

    def demo1(self):
        pass

    def demo2(self):
        pass

# Item Factory Class


class ItemFactory(object):

    def createItem(self, typeName):
        self.typeName = typeName
        if self.typeName == 'AItem':
            self.item = AItem()
        elif self.typeName == 'BItem':
            self.item = BItem()
        return self.item


a = XStore()
a.order('AItem')

b = XStore()
b.order('BItem')
