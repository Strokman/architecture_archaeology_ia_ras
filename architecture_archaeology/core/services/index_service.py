from django.db import connection


def sequence_id():
    with connection.cursor() as cursor:
        cursor.execute("""SELECT nextval('artwork_artefact_seq')""")
        return cursor.fetchone()[0]
