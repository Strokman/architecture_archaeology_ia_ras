from django.db import connection


def sequence_id():
    '''
    Для присвоения общего сквозного шифра фрескам и находкам в соотв. с ТЗ
    используется sequence (создается вручную при первом запуске базы,
    в дальнейшем, так как база данных будет существовать,
    ничего делать не понадобится) на уровне базы данных. Значение берется сырым
    запросом этой функцией. Название последовательности:
    artwork_artefact_seq. Дать можно любое название - соотв. здесь его нужно будет заменить
    '''
    with connection.cursor() as cursor:
        cursor.execute("""SELECT nextval('artwork_artefact_seq')""")
        return cursor.fetchone()[0]
