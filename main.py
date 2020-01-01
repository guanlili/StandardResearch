from excel.ahp import AHP
from excel.fuzzy import Fuzzy

if __name__ == '__main__':
    ahp = AHP()
    ahp.read()
    ahp.weight_normalize()

    grade_class_list = ['A','B','C']
    temp_name = grade_class_list[0]
    name_list = [temp_name]
    for i in grade_class_list:
        if i not in name_list:
            temp_name = ahp.deliver_grade_weight(temp_name, i)
            name_list.append(temp_name)

    fz = Fuzzy()
    fz.read()

    for i in name_list[::-1]:
        temp_list = ahp.get_weight_array(i)
        fz.calculate(temp_list)

    fz.judge()


    # A_name = 'A'
    # AB_name = ahp.deliver_grade_weight(A_name, 'B')
    # ABC_name = ahp.deliver_grade_weight(AB_name, 'C')
    #
    # fz = Fuzzy()
    # fz.read()
    #
    # ABC_list = ahp.get_weight_array(ABC_name)
    # fz.calculate(ABC_list)
    #
    # AB_list = ahp.get_weight_array(AB_name)
    # fz.calculate(AB_list)
    #
    # A = ahp.get_weight_array(A_name)
    # fz.calculate(A)
    #
    # fz.judge()


