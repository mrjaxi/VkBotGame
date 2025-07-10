from vkbottle import Keyboard, KeyboardButtonColor, Text

keyboard_first_part_one = {
    0: (
        Keyboard(inline=True)
        .add(Text("помощь в определении будущей профессии"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("просто так"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("чтобы узнать о всех текущих профессиях"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("чтобы было не скучно"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    1: (
        Keyboard(inline=True)
        .add(Text("кафедра,факультет/институт,университет"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("факультет/институт,кафедра,университет"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("факультет/институт,университет,кафедра"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("кафедра,университет,факультет/институт"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    2: (
        Keyboard(inline=True)
        .add(Text("подбор персонала"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("расчет зарплаты"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("выдача работникам справок"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("ведение документации"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    3: (
        Keyboard(inline=True)
        .add(Text("разделения смеси на компоненты"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("кипения нефти"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("получения товарного бензина"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("отделения газов от жидкости"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    4: (
        Keyboard(inline=True)
        .add(Text("метанол"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("бутан"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("пропан"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("этан"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    5: (
        Keyboard(inline=True)
        .add(Text("мера стойкости топлива к самовозгоранию"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("концентрация изомеров в бензине"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("количество октанов в бензине"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("мера неустойчивости топлива"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    6: (
        Keyboard(inline=True)
        .add(Text("гидрирования серосодержащих соединений"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("поддержания высокой температуры"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("увеличения скорости реакций"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("уменьшения объема газовой смеси"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    7: (
        Keyboard(inline=True)
        .add(Text("перегонка"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("гидроочистка"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("гидрирование"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("крекинг"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    8: (
        Keyboard(inline=True)
        .add(Text("для окисления гудрона"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для поддержания давления"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для увеличения температуры в колонне"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для проветривания колонны"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    9: (
        Keyboard(inline=True)
        .add(Text("Ж/Д транспортом"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("автотранспортом"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("по трубопроводам"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("на вертолетах"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
}

keyboard_first_part_one_answer = {
    0: "помощь в определении будущей профессии",
    1: "кафедра,факультет/институт,университет",
    2: "подбор персонала",
    3: "разделения смеси на компоненты",
    4: "метанол",
    5: "мера стойкости топлива к самовозгоранию",
    6: "гидрирования серосодержащих соединений",
    7: "перегонка",
    8: "для окисления гудрона",
    9: "на вертолетах",

}


keyboard_first_part_two = {
    0: (
        Keyboard(inline=True)
        .add(Text("для анализа процессов производства"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для знакомства с предприятием"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("чтобы пропустить уроки"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("просто посмотреть"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    1: (
        Keyboard(inline=True)
        .add(Text("оператор технологической установки"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("оператор компрессорной установки"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("лаборант"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("директор завода"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    2: (
        Keyboard(inline=True)
        .add(Text("в отделе кадров"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("в корпоративном университете"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("в традиционном университете"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("нет верного ответа"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    3: (
        Keyboard(inline=True)
        .add(Text("электрообессоливающей установки"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("атмосферного блока перегонки нефти"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("вакуумного блока перегонки нефти"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("установки получения кокса"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    4: (
        Keyboard(inline=True)
        .add(Text("пропан"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("пентан"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("бутан"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("метан"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    5: (
        Keyboard(inline=True)
        .add(Text("ароматические"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("все ответы верны"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("непредельные"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("разветвленные"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    6: (
        Keyboard(inline=True)
        .add(Text("мешает сгоранию топлива"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("вызывает коррозию"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("загрязняет металл"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("выделяет вредные пары"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    7: (
        Keyboard(inline=True)
        .add(Text("мазут"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("дизельное топливо"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("вакуумный газойль"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("пентан"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    8: (
        Keyboard(inline=True)
        .add(Text("из бензина коксования"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("из гудрона"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("из газойля"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("из мазута"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    9: (
        Keyboard(inline=True)
        .add(Text("для хранения нефти"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для хранения нефтепродуктов"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для продажи нефтепродуктов"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("все ответы неверны"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
}

keyboard_first_part_two_answer = {
    0: "для знакомства с предприятием",
    1: "оператор технологической установки",
    2: "в корпоративном университете",
    3: "атмосферного блока перегонки нефти",
    4: "пентан",
    5: "все ответы верны",
    6: "вызывает коррозию",
    7: "дизельное топливо",
    8: "из гудрона",
    9: "для хранения нефтепродуктов",

}



keyboard_first_part_three = {
    0: (
        Keyboard(inline=True)
        .add(Text("мероприятия от предприятий"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("участие в профориентационных проектах"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("все ответы верны"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("игра"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    1: (
        Keyboard(inline=True)
        .add(Text("оператор технологической установки"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("оператор компрессорной установки"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("лаборант"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("директор завода"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    2: (
        Keyboard(inline=True)
        .add(Text("проведение корпоративных мероприятий"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("подбор персонала"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("все ответы верны"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("подготовка планов повышения квалификации"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    3: (
        Keyboard(inline=True)
        .add(Text("получить более чистые продукты"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("компоненты нефти разлагались"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("снизить температуру кипения компонентов"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("повысить температуру кипения компонентов"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    4: (
        Keyboard(inline=True)
        .add(Text("для испарения газов"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для опоры колонны"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для проведения процесса ректификации"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для красоты"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    5: (
        Keyboard(inline=True)
        .add(Text("реакции дегидроциклизации"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("реакции дегидрирования"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("реакции гидрирования"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("реакции изомеризации"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    6: (
        Keyboard(inline=True)
        .add(Text("в печь"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("в колонну окисления"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("в ректификационную колонну"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("в следующий реактор"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    7: (
        Keyboard(inline=True)
        .add(Text("тяжелый газойль"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("гудрон"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("вакуумный газойль"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("дизельное топливо"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    8: (
        Keyboard(inline=True)
        .add(Text("с установки замедленного коксования"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("с нефтяного месторождения"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("с установки АВТ"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("с лаборатории"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
    9: (
        Keyboard(inline=True)
        .add(Text("металл"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("железобетон"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("пластмасса"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("все ответы верны"), color=KeyboardButtonColor.POSITIVE)
    ).get_json(),
}

keyboard_first_part_three_answer = {
    0: "игра",
    1: "лаборант",
    2: "все ответы верны",
    3: "снизить температуру кипения компонентов",
    4: "для проведения процесса ректификации",
    5: "реакции гидрирования",
    6: "в ректификационную колонну",
    7: "вакуумный газойль",
    8: "с установки АВТ",
    9: "все ответы верны",

}


