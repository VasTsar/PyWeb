from data import db_session
from data.objects import Objects

if __name__ == '__main__':
    db_session.global_init('../db/architecture.db')
    db_sess = db_session.create_session()
    object = Objects(
        name='Дом Наркомфина',
        address='Новинский бул., 25, корп. 1, Москва',
        information='«Дом Наркомфина» — это жилой дом, '
                    'построенный в стиле конструктивизма по проекту архитектора Моисея Гинзбурга '
                    'и Николая Милютина.',
        similar='Дом-корабль',
        user_id=1,
        image='Narkomfin.jpg'
    )
    db_sess.add(object)
    object = Objects(
        name='Коломенское',
        address='просп. Андропова, 39, Москва, Парк Коломенское',
        information='Излюбленная резиденция великих русских правителей, Коломенское, '
                    'сегодня входит в Московское государственное объединенное художественное '
                    'историко-архитектурное и природно-ландшафтное музей-заповедник.',
        similar='Царицыно, Кусково',
        user_id=1,
        image='Kolomenskoye.jpg'
    )
    db_sess.add(object)
    object = Objects(
        name='Церковь Вознесения',
        address='просп. Андропова, 39, Москва, Парк Коломенское',
        information='Церковь Вознесения входит сегодня в список культурного наследия ЮНЕСКО, '
                    'и неслучайно: это настоящее архитектурное чудо, '
                    'выдающийся образец храмового зодчества на Руси.',
        similar='Церковь Николая Чудотворца в Хамовниках',
        user_id=1,
        image='Ascension.jpg'
    )
    db_sess.add(object)
    object = Objects(
        name='Симонов монастырь',
        address='Восточная ул., 4 строение 8, Москва',
        information='Один из наиболее пострадавших московских монастырей и один из самых значимых в истории столицы. '
                    'Симонов монастырь был утрачен более чем на две трети, '
                    'в ХХ веке был уничтожен его собор – один из древнейших в Москве. '
                    'И всё же осколки его истории дошли до наших дней, словно показывая, '
                    'к чему может привести неуемная жажда разрушений.',
        similar='Данилов монастырь',
        user_id=1,
        image='Simonov.jpg'
    )
    db_sess.add(object)
    db_sess.commit()
