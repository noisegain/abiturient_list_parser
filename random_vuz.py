from random import randint


data = [
    ('ВШЭ', [
        "Нн Фундаментальная и прикладная лингвистика",
        "Спб Экономика",
        "Спб Менеджмент",
        "Нн Бизнес-информатика",
        "Спб Социология",
        "Нн Экономика"
    ]),
    ('ВАВТ', [
        "Экономика",
        "Менеджмент"
    ]),
    ('ИТМО', [
        "Бизнес-информатика",
        "Интеллектуальные системы в гуманитарной сфере",
        "Инноватика"
    ]),
    ('ЛГУ', [
        "Лингвистика",
        "Пед"
    ]),
    ('ЛЭТИ', [
        "Инноватика"
    ]),
    ('МГТУ', [
        "Бизнес-информатика"
    ]),
    ('НГУ', [
        "Фундаментальная и прикладная лингвистика",
        "Экономика",
        "Бизнес-информатика"
    ]),
    ('РАНХиГС', [
        "Мск Бизнес-информатика",
        "Мск Экономика",
        "Мск Прикладная информатика",
        "Спб Бизнес-информатика",
        "Мск Менеджмент",
        "Спб Менеджмент",
        "Мск Прикладная информатика"
    ]),
    ('РГГУ', [
        "Интеллектуальные системы в гуманитарной сфере"
    ]),
    ('РТА', [
        "Таможня"
    ]),
    ('РУДН', [
        "Бизнес-информатика",
        "Прикладная информатика",
        "Прикладная математика и информатика"
    ]),
    ('РЭУ', [
        "Бизнес-информатика",
        "Экономика"
    ]),
    ('СПБГУ', [
        "Менеджмент",
        "Экономика"
    ]),
    ('СПБГЭУ', [
        "Бизнес-информатика",
        "Экономика"
    ]),
    ('СПБПУ', [
        "Бизнес-информатика",
        "Менеджмент",
        "Экономика"
    ]),
    ('ФУ', [
        "Экономика",
        "Бизнес-информатика"
    ])
]

x = randint(0, len(data) - 1)
print(data[x][0], data[x][1][randint(0, len(data[x][1]) - 1)])
