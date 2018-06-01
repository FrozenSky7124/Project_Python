#-*- coding:utf-8 -*-

def upper_attr(future_class_name, future_class_parents, future_class_attr)

    #遍历属性字典， 把不是__开头的属性名字变为⼤写
    newAttr = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value
    #调⽤type来创建⼀个类
    return type(future_class_name, future_class_parents, newAttr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)