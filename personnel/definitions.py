from enum import Enum


class Gender(Enum):
    Unset = (0, 'Unset')
    Male = (1, 'Male')
    Female = (2, 'Female')
    Privacy = (3, 'Privacy')

#
# class MilitaryRank(Enum):
#     LieutenantGeneral = ('Lieutenant General', '中將')
#     MajorGeneral = ('Major General', '少將')
#     Colonel = ('Colonel', '上校')
#     LieutenantColonel = ('Lieutenant Colonel', '中校')
#
#
# class PoliceStaff(Enum):
#     pass
#
#
# class ClericalStaff(Enum):
#     pass
