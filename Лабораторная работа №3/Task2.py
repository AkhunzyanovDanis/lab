# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеpьте работу функции с разделителем отличным от запятой
def find_common_participants(participant_group_1, participant_group_2, divider=','):
    common_participant_list = []
    participant_group_1 = participant_group_1.split(divider)
    participant_group_2 = participant_group_2.split(divider)
    participants_set_1 = set(participant_group_1.split(divider))
    participants_set_2 = set(participant_group_2.split(divider))

    common_participants = participants_set_1.intersection(participants_set_2)

    return sorted(common_participant_list)
