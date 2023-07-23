import re


class RuleConvert:
    """
    命名规则转换 Tips：大小驼峰及下划线互转
    @descript 大驼峰: 首字母大写其余每一个逻辑断点（单词）都用大写字母标记,同帕斯卡命名法
    @descript 小驼峰: 首字母小写其余每一个逻辑断点（单词）都用大写字母标记
    @descript 下划线: 逻辑断点（单词）用的是下划线隔开
    """

    @staticmethod
    def to_underline(x):
        """转下划线命名"""
        return re.sub('(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])', '_\g<0>', x).lower()

    @staticmethod
    def to_upper_camel_case(x):
        """转大驼峰法命名"""
        s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x.lower())
        return s[0].upper() + s[1:]

    @staticmethod
    def to_lower_camel_case(x):
        """转小驼峰法命名"""
        s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x.lower())
        return s[0].lower() + s[1:]
