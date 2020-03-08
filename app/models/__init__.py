class ViviDict(dict):
    """
    循环赋值，可以直接将DB查询处理出来的数据处理成不同层级的字典
    """

    def __getitem__(self, item):
        try:
            print(item,'normal')
            return dict.__getitem__(self,item)

        except KeyError:
            print(item,'exception')
            # print(type(self)())
            # print(self[item], item)
            value = self[item] = type(self)()
            return value


v = ViviDict()

# v['a']['b']['c']=1
v['1']['bb']=3
# v['aa']=2
# print(v['1']/)