"""

def loadSkill(**cs):
    '''
    Load skill for class.
    :param cs: class and skill pairs.
    :return: None
    '''
    print('Class:' , cs.keys())
    print('Skill:' , cs.values())

#loadSkill(妙法 = '五音繁会', 御剑 = '剑影凝神', 咒隐 = '尘烟隐')
#help(loadSkill)



string1 = "照之以日月，经之以星辰，纪之以四时，要之以太岁。"
result = string1.split('，')
print(result)

string2 = ['照之以日月', '经之以星辰', '纪之以四时', '要之以太岁。']
result_join = '！'.join(string2)
print(result_join)

print('技能：%s 技能描述：%s 攻击力加成：%f 属性伤害加成：%f' % ('天街巡游', '喵？', 1.5, 1.6))



str1 = '技能：{0[0]} 攻击力：{0[1]} 元素伤害：{0[2]}'
str2 = ['画雨笼山', 1700, '水属性']
result = str1.format(str2)
print(result)
"""
str1 = '技能：{0:#<10}'
result = str1.format('天街巡游')
print(result)