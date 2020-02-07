import telebot
import constant
import time
import types
from test import list1
import locations

mybot = telebot.TeleBot(constant.token, threaded=False)
lang = "en"

"""

upd = mybot.get_updates()
last_upd=upd[-1]
message_from_user = last_upd.message
#print(message_from_user)

"""


# print(mybot.get_me())
def log(message):
    print("\n -------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Команда - {3}".format(message.from_user.first_name,
                                                                     message.from_user.last_name,
                                                                     str(message.from_user.id), message.text))


def language(s):
    lang = s
    print(lang)

##########

###########
#######Addresss########
# UZB
def handle_address_uzb(message):
    language("uz")
    markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_uzb.row('Bosh ofis', 'Toshkent', 'Toshkent viloyati')
    markup_uzb.row('Namangan', 'Andijon', "Farg`ona")
    markup_uzb.row('Buxoro', 'Jizzax', 'Qashqadaryo')
    markup_uzb.row('Navoiy', 'Samarqand', 'Sirdaryo')
    markup_uzb.row('Surxondaryo', 'Xorazm', 'Qoraqalpog`iston ')
    markup_uzb.row('Orqaga')
    mybot.send_message(message.from_user.id, "Filiallni tanlang", parse_mode="HTML", reply_markup=markup_uzb)


def handle_address_uzb_kiril(message):
    language("uz")
    markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_uzb.row('Бош офис', 'Тошкент', 'Тошкент вилояти')
    markup_uzb.row('Наманган', 'Андижон', "Фаргона")
    markup_uzb.row('Бухоро', 'Джиззах', 'Қашқадарё')
    markup_uzb.row('Навои', 'Самарқанд', 'Сирдарьё')
    markup_uzb.row('Сурхандарьё', 'Хоразм', 'Қорақолпогистон')
    markup_uzb.row('Орқага')
    mybot.send_message(message.from_user.id, "Филилални Танланг", parse_mode="HTML", reply_markup=markup_uzb)


def handle_address_ru(message):
    language("uz")
    markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_uzb.row('Головной офис', 'Ташкент', 'Ташкентская область')
    markup_uzb.row('Наманган', 'Андижан', "Фергана")
    markup_uzb.row('Бухара', 'Жиззах', 'Кашкадарья')
    markup_uzb.row('Наваи', 'Самарканд', 'Сирдарья')
    markup_uzb.row('Сурхандарья', 'Хорезм', 'Каракалпакистан')
    markup_uzb.row('Назад')
    mybot.send_message(message.from_user.id, "Филилални Танланг", parse_mode="HTML", reply_markup=markup_uzb)


#######################

# Key Only back UZB
##################################---------------------------###############################################
def handle_back_uzb(message, sendmessage):
    language("uz")
    markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_uzb.row('Orqaga')
    mybot.send_message(message.from_user.id, sendmessage, parse_mode="HTML", reply_markup=markup_uzb)


# def handle_back_uzb_jis_xizmat(message, sendmessage):
#     language("uz")
#     markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     markup_uzb.row('Оrqaga')
#     mybot.send_message(message.from_user.id, sendmessage, parse_mode="HTML", reply_markup=markup_uzb)
# def handle_back_kr_jis_xizmat(message, sendmessage):
#     language("uz")
#     markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     markup_uzb.row('Oрқага')
#     mybot.send_message(message.from_user.id, sendmessage, parse_mode="HTML", reply_markup=markup_uzb)
# def handle_back_ru_jis_xizmat(message, sendmessage):
#     language("uz")
#     markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     markup_uzb.row('Нaзад')
#     mybot.send_message(message.from_user.id, sendmessage, parse_mode="HTML", reply_markup=markup_uzb)


###########################---------------------------------------#####################################
# Key Bank xizmatlari
def handle_korrespschet_uzb(message):
    language("uz")
    markup_xizmat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_xizmat_uzb.row('OAJ «Sberbank»', 'OAJ «Rosselxozbank»')
    markup_xizmat_uzb.row('ATB «Aziya Invest Bank»', 'OAJ «Transkapitalbank»')
    markup_xizmat_uzb.row('Oʻz.Res. TIF Milliy banki', 'AITB «Ipak Yoʻli»')
    markup_xizmat_uzb.row('ATB «Oʻzsanoatqurilishbank»', 'Orqаga')
    mybot.send_message(message.from_user.id, constant.bank_xizmatlari, parse_mode="HTML",
                       reply_markup=markup_xizmat_uzb)


def handle_xizmat_uzb(message):
    language("uz")
    markup_xizmat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_xizmat_uzb.row('👕 Jismoniy shaxslar uchun', '👔Yuridik shaxslar uchun')
    markup_xizmat_uzb.row('🏦Filiallar', '💵Valyuta kurslari')
    markup_xizmat_uzb.row('☎️Biz bilan bogʻlanish', 'Tilni o`zgartirish /Изменить язык')
    mybot.send_message(message.from_user.id, constant.bank_xizmatlari, parse_mode="HTML",
                       reply_markup=markup_xizmat_uzb)


def valyuta_uz(message):
    mybot.send_message(message.from_user.id,
                       'Joriy kurs:\n\n'  'AQSH dollari - 🇺🇸1{0}\nValyuta kursi (Xarid qilish): {1}\nValyuta kursi (Sotuv): {2}\nO`RMB kursi: {3}\n\n'  'EvrO - 🇪🇺1{4}\nValyuta kursi (Xarid qilish): {5}\nValyuta kursi (Sotuv): {6}\nO`RMB kursi: {7}\n\n'  'Angliya funt sterlingi - 🇬🇧1{8}\nValyuta kursi (Xarid qilish): {9}\nValyuta kursi (Sotuv): {10}\nO`RMB kursi: {11}\n\n'  'Yaponiya iyenasi - 🇯🇵1{12}\nValyuta kursi (Xarid qilish): {13}\nValyuta kursi (Sotuv): {14}\nO`RMB kursi: {15}'.format(
                           list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], list1[7], list1[8],
                           list1[9], list1[10], list1[11], list1[12], list1[13], list1[14], list1[15]))


# Key yuridik shaxslar uchun
def handle_yuridik_uzb(message):
    language("uz")
    markup_yuridik_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_yuridik_uzb.row('💼Kredit', '🏛Korrespondent banklar')
    markup_yuridik_uzb.row('Interaktiv hizmatlar','Orqaga')
    mybot.send_message(message.from_user.id, constant.jismoniy, parse_mode="HTML", reply_markup=markup_yuridik_uzb)


def handle_interaktiv_uzb(message):
    language("uz")
    markup_yuridik_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_yuridik_uzb.row('SMS Bank', 'Internet Bank')
    markup_yuridik_uzb.row('Orqаga')
    mybot.send_message(message.from_user.id, constant.jismoniy, parse_mode="HTML", reply_markup=markup_yuridik_uzb)


# Key jismoniy shaxslar uchun
def handle_jismoniy_uzb(message):
    language("uz")
    markup_jismoniy_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_jismoniy_uzb.row('🏦 Omonatlar', '💰Kreditlar')
    markup_jismoniy_uzb.row('💳Plastik kartalar', '💸Pul o`tkazmalari')
    markup_jismoniy_uzb.row('MKB mobayl', 'Orqaga', )
    mybot.send_message(message.from_user.id, constant.jismoniy, parse_mode="HTML", reply_markup=markup_jismoniy_uzb)


# Key Kreditlar
def handle_kredit_uzb_jis(message):
    language("uz")
    markup_kredit_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_kredit_uzb.row('Avtokredit', 'Istemol Kreditlari')
    markup_kredit_uzb.row('Ichki va Tashqi Turizm', 'Mikroqarz')
    markup_kredit_uzb.row('Overdraft Krediti', 'Оrqaga')
    mybot.send_message(message.from_user.id, "<b>Kredit turini tanlang!</b>", parse_mode="HTML",
                       reply_markup=markup_kredit_uzb)


def handle_omonat_uzb_jis(message):
    language("uz")
    markup_omonat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_omonat_uzb.row('Muddatli omonatlar', 'Jamg`arma omonatlari')
    markup_omonat_uzb.row('Horijiy valyutadagi depozitlar', 'Оrqaga')
    mybot.send_message(message.from_user.id, "<b>Omonat turini tanlang!</b>", parse_mode="HTML",
                       reply_markup=markup_omonat_uzb)


def handle_kredit_uzb_yur(message):
    language("uz")
    markup_kredit_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_kredit_uzb.row('Hunarmand', 'Savdo')
    markup_kredit_uzb.row('Kollej bitiruvchilariga', 'Mikrokreditlar')
    markup_kredit_uzb.row('Orqаga')
    mybot.send_message(message.from_user.id, "<b>Kredit turini tanlang!</b>", parse_mode="HTML",
                       reply_markup=markup_kredit_uzb)


def handle_boglanish_uzb(message):
    language("uz")
    markup_boglanish_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_boglanish_uzb.row('📞Bankga qoʻngiroq qilinпg', '✍️Operatorga yozing')
    markup_boglanish_uzb.row('🗣Taklif va shikoyatlar', 'Orqaga')
    mybot.send_message(message.from_user.id, "Bo'limni tanlang", parse_mode="HTML",
                       reply_markup=markup_boglanish_uzb)


# Key Omonatlar
#####################################################################
def handle_back_uzb_kiril(message, sendmessage):
    language("uz")
    markup_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_uzb.row('Орқага')
    mybot.send_message(message.from_user.id, sendmessage, parse_mode="HTML", reply_markup=markup_uzb)


# Key Bank xizmatlari
def handle_xizmat_uzb_kiril(message):
    language("uz")
    markup_xizmat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_xizmat_uzb.row('👕 Жисмоний шахслар учун', '👔Юридик шахслар учун')
    markup_xizmat_uzb.row('🏦Филиаллар', '💵Валюта курслари')
    markup_xizmat_uzb.row('☎️Биз билан богланиш', 'Тилни ўзгартириш /Изменить язык')
    mybot.send_message(message.from_user.id, constant.bank_xizmatlari_kr, parse_mode="HTML",
                       reply_markup=markup_xizmat_uzb)


def valyuta_uz_kiril(message):
    mybot.send_message(message.from_user.id,
                       'Жорий курс:\n\n'  'АҚШ доллори - 🇺🇸1{0}\nВалюта курси (Харид қилиш): {1}\nВалюта курси (Сотиш): {2}\nЎРМБ қурси: {3} \n\n'  'Евро - 🇪🇺1{4}\nВалюта курси (Харид қилиш): {5}\nВалюта курси (Сотиш): {6}\nЎРМБ қурси: {7} \n\n'  'Англия фунт стерлинг - 🇬🇧1{8}\nВалюта курси (Харид қилиш): {9}\nВалюта курси (Сотиш): {10}\nЎРМБ қурси: {11}\n\n'  'Япония йенаси - 🇯🇵1{12}\nВалюта курси (Харид қилиш): {13}\nВалюта курси (Сотиш): {14}\nЎРМБ қурси: {15}'.format(
                           list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], list1[7], list1[8],
                           list1[9], list1[10], list1[11], list1[12], list1[13], list1[14], list1[15]))


# Key jismoniy shaxslar uchun
def handle_jismoniy_uzb_kiril(message):
    language("uz")
    markup_jismoniy_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_jismoniy_uzb.row('🏦 Омонатлар', '💰Кредитлар')
    markup_jismoniy_uzb.row('💳Пластик карталар', '💸Пул ўтказмалари')
    markup_jismoniy_uzb.row('МКБ мобил', 'Орқага', )
    mybot.send_message(message.from_user.id, constant.jismoniy_kr, parse_mode="HTML", reply_markup=markup_jismoniy_uzb)


def handle_interaktiv_kr(message):
    language("uz")
    markup_yuridik_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_yuridik_uzb.row('СМС Банк', 'Интернет Банк')
    markup_yuridik_uzb.row('Орқaга')
    mybot.send_message(message.from_user.id, constant.jismoniy, parse_mode="HTML", reply_markup=markup_yuridik_uzb)


def handle_kredit_uzb_kiril_jis(message):
    language("uz")
    markup_kredit_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_kredit_uzb.row('Автокредит', 'Истеъмол Кредити')
    markup_kredit_uzb.row('Ички ва Ташқи Туризм', 'Микроқарз')
    markup_kredit_uzb.row('Овердрафт Кредити', 'Орқага')
    mybot.send_message(message.from_user.id, "<b>Kredit turini tanlang!</b>", parse_mode="HTML",
                       reply_markup=markup_kredit_uzb)


def handle_omonat_uzb_kiril_jis(message):
    language("uz")
    markup_omonat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_omonat_uzb.row('Муддатли омонатлар', 'Жамғарма омонатлар')
    markup_omonat_uzb.row('Ҳорижий валютадаги жамғарма омонатлар', 'Oрқага')
    mybot.send_message(message.from_user.id, "<b>Омонат турини танланг!</b>", parse_mode="HTML",
                       reply_markup=markup_omonat_uzb)


# Key yuridik shaxslar uchun
def handle_yuridik_uzb_kiril(message):
    language("uz")
    markup_yuridik_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_yuridik_uzb.row('💼Кредит', '🏛Корреспондент банклар')
    markup_yuridik_uzb.row('Интерактив хизматлар', 'Орқага')

    mybot.send_message(message.from_user.id, constant.jismoniy_kr, parse_mode="HTML", reply_markup=markup_yuridik_uzb)


# Key Kreditlar
def handle_kredit_yur_uzb_kiril(message):
    language("uz")
    markup_kredit_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_kredit_uzb.row('Хунарманд', 'Савдо')
    markup_kredit_uzb.row('Колледж битирувчиларига', 'Микрокредитлар')
    markup_kredit_uzb.row('Орқaга')
    mybot.send_message(message.from_user.id, "<b>Кредит турини танланг!</b>", parse_mode="HTML",
                       reply_markup=markup_kredit_uzb)


# Key Omonatlar
def handle_boglanish_uzb_kiril(message):
    language("uz")
    markup_boglanish_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_boglanish_uzb.row('📞Банкга кўнгироқ қилинг', '✍️Операторга ёзинг')
    markup_boglanish_uzb.row('🗣Таклиф ва шикоятлар', 'Орқага')
    mybot.send_message(message.from_user.id, "Бўлимни танланг", parse_mode="HTML",
                       reply_markup=markup_boglanish_uzb)


def handle_korrespschet_ru(message):
    language("uz")
    markup_xizmat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_xizmat_uzb.row('ПАО «Сбербанк»', 'ОАО «Россельхозбанк»')
    markup_xizmat_uzb.row('АКБ «Азия Инвест Банк»', 'ПАО «ТрансКапиталбанк»')
    markup_xizmat_uzb.row('Национальный Банк ВЭД РУз', 'АИКБ «Ипак Йули»')
    markup_xizmat_uzb.row('АКБ «Узпромстройбанк»', 'Назaд')
    mybot.send_message(message.from_user.id, constant.bank_xizmatlari, parse_mode="HTML",
                       reply_markup=markup_xizmat_uzb)


#######################################################################
# Key command START
@mybot.message_handler(commands=['start'])
def handle_start(message):
    markup_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_start.row('O`zbek tili (Latin)', 'Узбек тили (Кирил)', 'Русский язык')
    log(message)
    mybot.send_message(message.from_user.id, constant.start_message, parse_mode="HTML", reply_markup=markup_start)


# Key Only back ru
def handle_back_ru(message, sendmessage):
    language("ru")
    markup_ru = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_ru.row('Назад')
    mybot.send_message(message.from_user.id, sendmessage, parse_mode="HTML", reply_markup=markup_ru)


def handle_interaktiv_ru(message):
    language("uz")
    markup_yuridik_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_yuridik_uzb.row('СМС Банкинг', 'Интернет Банкинг')
    markup_yuridik_uzb.row('Назaд')
    mybot.send_message(message.from_user.id, constant.jismoniy, parse_mode="HTML", reply_markup=markup_yuridik_uzb)


# Key Bank xizmatlari
def handle_xizmat_ru(message):
    language("ru")
    markup_xizmat_ru = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_xizmat_ru.row('👕Для физических лиц', '👔Для юридических лиц')
    markup_xizmat_ru.row('🏦Филиалы', '💵Курсы валют')
    markup_xizmat_ru.row('☎️Связаться с нами', 'Изменить язык / Tilni o`zgartirish', )
    mybot.send_message(message.from_user.id, constant.bank_xizmatlari_ru, parse_mode="HTML",
                       reply_markup=markup_xizmat_ru)


# Key jismoniy shaxslar uchun
def handle_jismoniy_ru(message):
    language("ru")
    markup_jismoniy_ru = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_jismoniy_ru.row('🏦 Вклады', '💰Кредиты')
    markup_jismoniy_ru.row('💳Пластиковые карты', '💸Денежные переводы')
    markup_jismoniy_ru.row('МКБ мобайл', 'Назад')
    mybot.send_message(message.from_user.id, constant.jismoniy_ru, parse_mode="HTML", reply_markup=markup_jismoniy_ru)


def handle_kredit_ru_jis(message):
    language("uz")
    markup_kredit_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_kredit_uzb.row('Автокредиты', 'Потребительский кредит')
    markup_kredit_uzb.row('Внутренный и внешный туризм', 'Микрозайм')
    markup_kredit_uzb.row('Овердрафтный кредит', 'Нaзад')
    mybot.send_message(message.from_user.id, "<b>Выбериту пункт!</b>", parse_mode="HTML",
                       reply_markup=markup_kredit_uzb)


def handle_omonat_ru_jis(message):
    language("uz")
    markup_omonat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_omonat_uzb.row('Срочные депозиты', 'Сберегательные вклады')
    markup_omonat_uzb.row('Сбережении в иностранной валюте', 'Нaзад')
    mybot.send_message(message.from_user.id, "<b>Выбериту пункт!</b>", parse_mode="HTML",
                       reply_markup=markup_omonat_uzb)


def handle_yuridik_ru(message):
    language("ru")
    markup_yuridik_ru = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_yuridik_ru.row('💼Кредитование', '🏛Банки-корреспонденты')
    markup_yuridik_ru.row('Интерактивные услуги', 'Назад')
    mybot.send_message(message.from_user.id, constant.jismoniy_ru, parse_mode="HTML", reply_markup=markup_yuridik_ru)


# Key Kreditlar
def handle_kredit_yur_ru(message):
    language("ru")
    markup_kredit_ru = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_kredit_ru.row('Торогвые кредиты', 'Микрокредиты')
    markup_kredit_ru.row('Для выпускников колледжей')
    markup_kredit_ru.row('Назaд')
    mybot.send_message(message.from_user.id, "<b>Выберите выд кредита!</b>", parse_mode="HTML",
                       reply_markup=markup_kredit_ru)


def valyuta_ru(message):
    mybot.send_message(message.from_user.id,
                       'Курс валют на сегодня:\n\n'  'Доллара США - 🇺🇸1{0}\nВ обменных пунктах (Покупка): {1}\nВ обменных пунктах (Продажа): {2}\nКурс ЦБРУ: {3} \n\n'  'Евро - 🇪🇺1{4}\nВ обменных пунктах (Покупка): {5}\nВ обменных пунктах (Продажа): {6}\nКурс ЦБРУ: {7} \n\n'  'Фунт Стерлинг - 🇬🇧1{8}\nВ обменных пунктах (Покупка): {9}\nВ обменных пунктах (Продажа): {10}\nКурс ЦБРУ: {11} \n\n'  'Японская йена - 🇯🇵1{0}\nВ обменных пунктах (Покупка): {1}\nВ обменных пунктах (Продажа): {2}\nКурс ЦБРУ: {3}'.format(
                           list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], list1[7], list1[8],
                           list1[9], list1[10], list1[11], list1[12], list1[13], list1[14], list1[15]))


def handle_boglanish_uzb_ru(message):
    language("uz")
    markup_boglanish_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup_boglanish_uzb.row('📞Позвонить в Банк', '✍️Написать оператору')
    markup_boglanish_uzb.row('🗣Предложения и жалобы', 'Назад')
    mybot.send_message(message.from_user.id, "Бўлимни танланг", parse_mode="HTML",
                       reply_markup=markup_boglanish_uzb)


def handle_korrespschet_kiril(message):
    language("uz")
    markup_xizmat_uzb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=False)
    markup_xizmat_uzb.row('ОАЖ «Сбербанк»', 'ОАЖ «Россельхозбанк»')
    markup_xizmat_uzb.row('АТБ «Азия Инвест Банк»', 'ОАЖ «ТрансКапиталбанк»')
    markup_xizmat_uzb.row('Ўз.Рес. ТИФ Миллий банки', 'АИТБ «Ипак Йули»')
    markup_xizmat_uzb.row('АТБ «Ўзсаноатқурилишбанк»', 'Орқaга')
    mybot.send_message(message.from_user.id, constant.bank_xizmatlari, parse_mode="HTML",
                       reply_markup=markup_xizmat_uzb)


@mybot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "O`zbek tili (Latin)":
        language("uz")
        log(message)
        handle_xizmat_uzb(message)
    elif message.text == "Русский язык":
        language("ru")
        log(message)
        handle_xizmat_ru(message)
    elif message.text == "Узбек тили (Кирил)":
        language("uz")
        log(message)
        handle_xizmat_uzb_kiril(message)
    ######################UZB####################################
    elif message.text == "Orqaga":
        # language("uz")
        log(message)
        handle_xizmat_uzb(message)
    elif message.text == "Оrqaga":
        # language("uz")
        log(message)
        handle_jismoniy_uzb(message)
    elif message.text == "Orqаga":
        # language("uz")
        log(message)
        handle_yuridik_uzb(message)
    elif message.text == "Tilni o`zgartirish /Изменить язык":
        # language("uz")
        log(message)
        handle_start(message)
    elif message.text == "👕 Jismoniy shaxslar uchun":
        # language("uz")
        log(message)
        handle_jismoniy_uzb(message)
    elif message.text == "👔Yuridik shaxslar uchun":
        # language("uz")
        log(message)
        handle_yuridik_uzb(message)
    elif message.text == "💰Kreditlar":
        # language("uz")
        log(message)
        handle_kredit_uzb_jis(message)
    elif message.text == "Avtokredit":
        log(message)
        mybot.send_message(message.chat.id, constant.avtokredit_uzb)
    elif message.text == "Istemol Kreditlari":
        log(message)
        mybot.send_message(message.chat.id, constant.istemolkredit_uzb)
    elif message.text == "Ichki va Tashqi Turizm":
        log(message)
        mybot.send_message(message.chat.id, constant.turizm_uzb)
    elif message.text == "Mikroqarz":
        log(message)
        mybot.send_message(message.chat.id, constant.mikroqarz_uzb)
    elif message.text == "Overdraft Krediti":
        log(message)
        mybot.send_message(message.chat.id, constant.overdraft_uzb)
    elif message.text == "Orqaga":
        log(message)
        handle_kredit_uzb_jis(message)
    elif message.text == "Hunarmand":
        # language("uz")
        log(message)
        mybot.send_message(message.chat.id, constant.hunarmad_kredit_uz)
    elif message.text == "Savdo":
        # language("uz")
        log(message)
        mybot.send_message(message.chat.id, constant.savdo_kredit_uzb)
    elif message.text == "Mikrokreditlar":
        # language("uz")
        log(message)
        mybot.send_message(message.chat.id, constant.mikrokreditlar_yur_uzb)
    elif message.text == "Kollej bitiruvchilariga":
        # language("uz")
        log(message)
        mybot.send_message(message.chat.id, constant.kollej_uzb)
    elif message.text == "🏛Korrespondent banklar":
        # language("uz")
        log(message)
        handle_korrespschet_uzb(message)
    elif message.text == "🏛Корреспондент банклар":
        # language("uz")
        log(message)
        handle_korrespschet_kiril(message)
    elif message.text == "Mobil banking":
        # language("uz")
        log(message)
        handle_back_uzb(message, constant.modilbank_yur_uzb)

    elif message.text == "Interaktiv hizmatlar":
        log(message)
        handle_interaktiv_uzb(message)

    elif message.text == "Internet Bank":
        log(message)
        markup = telebot.types.InlineKeyboardMarkup()
        btn_my_site = telebot.types.InlineKeyboardButton(text='Interaktiv hizmatlar haqida batafsil',
                                                         url="https://mikrokreditbank.uz/uz/corporate/interactive-services/")
        markup.add(btn_my_site)
        mybot.send_message(message.chat.id, f'{constant.internet_uzb}\n{constant.img_internet_bank}',
                           reply_markup=markup)
    elif message.text == "SMS Bank":
        log(message)
        markup = telebot.types.InlineKeyboardMarkup()
        btn_my_site = telebot.types.InlineKeyboardButton(text='SMS bank hizmatlar haqida batafsil',
                                                         url="https://mikrokreditbank.uz/uz/corporate/interactive-services/")
        markup.add(btn_my_site)
        mybot.send_message(message.chat.id, f'{constant.sms_banking_uz}\n{constant.img_sms_bank}',
                           reply_markup=markup)

    elif message.text == "🏦 Omonatlar":
        # language("uz")
        log(message)
        handle_omonat_uzb_jis(message)
    else:
        if message.text == "Jamg`arma omonatlari":
            # language("uz")
            log(message)
            mybot.send_message(message.chat.id, constant.jamgarma_omonat_uzb)
        elif message.text == "Horijiy valyutadagi depozitlar":
            # language("uz")
            log(message)
            mybot.send_message(message.chat.id, constant.horijoy_valyutaomonat_uzb)
        elif message.text == "Muddatli omonatlar":
            # language("uz")
            log(message)
            mybot.send_message(message.chat.id, constant.mudatli_omonat_uzb)
        elif message.text == "💼Kredit":
            # language("uz")
            log(message)
            handle_kredit_uzb_yur(message)
        elif message.text == "💳Plastik kartalar":

            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Plastik Kartalar',
                                                             url="https://mikrokreditbank.uz/retail/plastic-cards/")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, f'{constant.plastik}\n{constant.img_plastik_karta}',
                               reply_markup=markup)
        elif message.text == "💸Pul o`tkazmalari":
            # language("uz")
            log(message)

            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Pul Otkazmalar batafsil',
                                                             url="https://mikrokreditbank.uz/retail/money-transfer/")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, f'{constant.pul_otkazmalar_uzb}\n{constant.img_pul_otkazma}',
                               reply_markup=markup)
        elif message.text == "MKB mobayl":
            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='MKB Mobayl',
                                                             url="https://play.google.com/store/apps/details?id=uz.fido_biznes.mobile.client.mkb")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, f'{constant.mobilbank_uzb}\n{constant.img_mbank}', reply_markup=markup)
        elif message.text == "🏦Filiallar":
            # language("uz")
            log(message)
            handle_address_uzb(message)
            # mybot.send_location(message.from_user.id, 41.297546, 69.204514)
        elif message.text == '✍️Operatorga yozing':
            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Chat Bot', url="t.me/@mkb_chat_bot")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, "Tugmani bosib chat botimizga o'ting.", reply_markup=markup)
        elif message.text == '💵Valyuta kurslari':
            log(message)
            valyuta_uz(message)
        elif message.text == '☎️Biz bilan bogʻlanish':
            handle_boglanish_uzb(message)
        elif message.text == '📞Bankga qoʻngiroq qilinпg':
            log(message)
            mybot.send_message(message.chat.id,
                               "Yagona qabul telefoni: (+998) 71-202-99-99\n\nYagona ishonch telefoni: (+998) 71-273-04-40 ")
        elif message.text == '🗣Taklif va shikoyatlar':
            handle_back_uzb(message, "Taklif yoki shikoyatingiz bormi? Bizga yozib qoldirishingiz mumkin.")
        elif message.text == "Bosh ofis":
            log(message)
            mybot.send_message(message.chat.id, locations.toshkent_uz)
            mybot.send_location(message.from_user.id, 41.297546, 69.204514)


        elif message.text == "Toshkent":
            log(message)
            mybot.send_message(message.chat.id, locations.toshkentsh_uz)
            mybot.send_location(message.from_user.id, 41.361258, 69.242641)
        elif message.text == "Toshkent viloyati":
            log(message)
            mybot.send_message(message.chat.id, locations.toshkent1_uz)
            mybot.send_location(message.from_user.id, 41.2624798, 69.2228512)
        elif message.text == "Andijon":
            log(message)
            mybot.send_message(message.chat.id, locations.andijon1_uz)
            mybot.send_location(message.from_user.id, 40.752063, 72.341996)
        elif message.text == "Farg`ona":
            log(message)
            mybot.send_message(message.chat.id, locations.fargona1_uz)
            mybot.send_location(message.from_user.id, 40.3757406, 71.809204)
        elif message.text == "Namangan":
            log(message)
            mybot.send_message(message.chat.id, locations.namangan1_uz)
            mybot.send_location(message.from_user.id, 40.996209, 71.612875)
        elif message.text == "Buxoro":
            log(message)
            mybot.send_message(message.chat.id, locations.buxoro1_uz)
            mybot.send_location(message.from_user.id, 39.744180, 64.519187)

        elif message.text == "Jizzax":
            log(message)
            mybot.send_message(message.chat.id, locations.jizzax1_uz)
            mybot.send_location(message.from_user.id, 40.114156, 67.846125)
        elif message.text == "Qashqadaryo":
            log(message)
            mybot.send_message(message.chat.id, locations.qarshi1_uz)
            mybot.send_location(message.from_user.id, 38.840984, 65.777014)
        elif message.text == "Navoiy":
            log(message)
            mybot.send_message(message.chat.id, locations.navoiy1_uz)
            mybot.send_location(message.from_user.id, 40.100387, 65.364838)
        elif message.text == "Samarqand":
            log(message)
            mybot.send_message(message.chat.id, locations.samarqand1_uz)
            mybot.send_location(message.from_user.id, 39.6503102, 66.9510076)
        elif message.text == "Sirdaryo":
            log(message)
            mybot.send_message(message.chat.id, locations.sirdaryo1_uz)
            mybot.send_location(message.from_user.id, 40.504731,68.778095)
        elif message.text == "Xorazm":
            log(message)
            mybot.send_message(message.chat.id, locations.xorazm1_uz)
            mybot.send_location(message.from_user.id, 41.549364, 60.633994)
        elif message.text == "Qoraqalpog`iston":
            log(message)
            mybot.send_message(message.chat.id, locations.qoraqalpogiston1_uz)
            mybot.send_location(message.from_user.id, 42.460163, 59.615756)
        elif message.text == "Surxondaryo":
            log(message)
            mybot.send_message(message.chat.id, locations.surxondaryo1_uz)
            mybot.send_location(message.from_user.id, 37.2387655, 67.280288)



        elif message.text == "OAJ «Sberbank»":
            log(message)
            mybot.send_message(message.chat.id, constant.sberbank_uzb)
        elif message.text == "OAJ «Rosselxozbank»":
            log(message)
            mybot.send_message(message.chat.id, constant.rosselxozbank_uzb)
        elif message.text == "ATB «Aziya Invest Bank»":
            log(message)
            mybot.send_message(message.chat.id, constant.aziyainvestbank_uzb)
        elif message.text == "OAJ «Transkapitalbank»":
            log(message)
            mybot.send_message(message.chat.id, constant.transkapitalbank_uzb)
        elif message.text == "Oʻz.Res. TIF Milliy banki":
            log(message)
            mybot.send_message(message.chat.id, constant.milliybank_uzb)
        elif message.text == "AITB «Ipak Yoʻli»":
            log(message)
            mybot.send_message(message.chat.id, constant.ipakyulibank_uzb)
        elif message.text == "ATB «Oʻzsanoatqurilishbank»":
            log(message)
            mybot.send_message(message.chat.id, constant.uzsanoatbank_uzb)

        ################UZB KIRIL########################
        elif message.text == "💰Кредитлар":
            # language("uz")
            log(message)
            handle_kredit_uzb_kiril_jis(message)
        elif message.text == 'Автокредит':
            log(message)
            mybot.send_message(message.chat.id, constant.avtokredit_uzb_kiril)
        elif message.text == 'Истеъмол Кредити':
            log(message)
            mybot.send_message(message.chat.id, constant.istemolkredit_uzb_kiril)
        elif message.text == 'Ички ва Ташқи Туризм':
            log(message)
            mybot.send_message(message.chat.id, constant.turizm_uzb_kiril)
        elif message.text == 'Микроқарз':
            log(message)
            mybot.send_message(message.chat.id, constant.mikroqarz_uzb_kiril)
        elif message.text == 'Овердрафт Кредити':
            log(message)
            mybot.send_message(message.chat.id, constant.overdraft_uzb_kiril)
        elif message.text == "🏦 Омонатлар":
            # language("uz")
            log(message)
            handle_omonat_uzb_kiril_jis(message)
        elif message.text == 'Муддатли омонатлар':
            log(message)
            mybot.send_message(message.chat.id, constant.mudatli_omonat_uzb_kiril)
        elif message.text == "💼Кредит":
            # language("uz")
            log(message)
            handle_kredit_yur_uzb_kiril(message)
        elif message.text == 'Ҳорижий валютадаги жамғарма омонатлар':
            log(message)
            mybot.send_message(message.chat.id, constant.horijoy_valyutaomonat_uzb_kiril)
        elif message.text == 'Жамғарма омонатлар':
            log(message)
            mybot.send_message(message.chat.id, constant.jamgarma_omonat_uzb_kiril)

        elif message.text  == "💼Кредит":
            log(message)
            handle_yuridik_uzb_kiril(message)
        elif message.text == "Колледж битирувчиларига":
            # language("uz")
            log(message)
            mybot.send_message(message.chat.id, constant.kollej_kr)
        elif message.text == "Микрокредитлар":
            # language("uz")
            log(message)
            mybot.send_message(message.chat.id, constant.mikrokreditlar_yur_kr)
        elif message.text == "Савдо":
            # language("uz")
            log(message)
            mybot.send_message(message.chat.id, constant.savdo_kredit_kr)
        elif message.text == "Хунарманд":
            # language("uz")
            log(message)
            mybot.send_message(message.chat.id, constant.hunarmad_kredit_kr)
        elif message.text == "👕 Жисмоний шахслар учун":
            # language("uz")
            log(message)
            handle_jismoniy_uzb_kiril(message)
        elif message.text == "🏦Филиаллар":
            # language("uz")
            log(message)
            handle_address_uzb_kiril(message)
        elif message.text == "Орқага":
            # language("uz")
            log(message)
            handle_xizmat_uzb_kiril(message)
        elif message.text == "Oрқага":
            # language("uz")
            log(message)
            handle_jismoniy_uzb_kiril(message)
        elif message.text == "Орқaга":
            # language("uz")
            log(message)
            handle_yuridik_uzb_kiril(message)
        elif message.text == "Тилни ўзгартириш /Изменить язык":
            # language("uz")
            log(message)
            handle_start(message)
        elif message.text == "👔Юридик шахслар учун":
            # language("uz")
            log(message)
            handle_yuridik_uzb_kiril(message)
        elif message.text == '💵Валюта курслари':
            log(message)
            valyuta_uz_kiril(message)
        elif message.text == '☎️Биз билан богланиш':
            handle_boglanish_uzb_kiril(message)
        elif message.text == '📞Банкга кўнгироқ қилинг':
            log(message)
            mybot.send_message(message.chat.id,
                               "Ягона қабул телефони: (+998) 71-202-99-99\n\nЯгона ишонч телефони: (+998) 71-273-04-40 ")
        elif message.text == '🗣Таклиф ва шикоятлар':
            handle_back_uzb_kiril(message, "Таклиф ёки шикоятларингиз борми? Бизга ёзиб қолдиришингиз мумкин.")
        elif message.text == '✍️Операторга ёзинг':
            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Чат Бот', url="t.me/mkb_chat_bot")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, "Тугмани босиб бизнинг чат ботимзга ўтинг.", reply_markup=markup)
        elif message.text == "Интерактив хизматлар":
            log(message)
            handle_interaktiv_kr(message)

        elif message.text == "Интернет Банк":
            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Интернет Банк хизматлари хақида батафсил',
                                                             url="https://mikrokreditbank.uz/uz/corporate/interactive-services/")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, f'{constant.internet_kr}\n{constant.img_internet_bank}',
                               reply_markup=markup)
        elif message.text == "СМС Банк":
            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='СМС Банк хизматлари хақида батафсил',
                                                             url="https://mikrokreditbank.uz/uz/corporate/interactive-services/")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, f'{constant.sms_banking_kr}\n{constant.img_sms_bank}',
                               reply_markup=markup)
        elif message.text == "Бош офис":
            log(message)
            mybot.send_message(message.chat.id, locations.toshkent_kr)
            mybot.send_location(message.from_user.id, 41.297546, 69.204514)

        elif message.text == "💳Пластик карталар":
            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Пластик карталар',
                                                             url="https://mikrokreditbank.uz/retail/plastic-cards/")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, f'{constant.plastik_kr}\n{constant.img_plastik_karta}',
                               reply_markup=markup)
        elif message.text == "💸Пул ўтказмалари":
            # language("uz")
            log(message)

            log(message)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Пул Ўтказмалари батафсил',
                                                             url="https://mikrokreditbank.uz/retail/money-transfer/")
            markup.add(btn_my_site)
            mybot.send_message(message.chat.id, f'{constant.pul_otkazmalar_kr}\n{constant.img_pul_otkazma}',
                               reply_markup=markup)

        elif message.text == "Тошкент":
            log(message)
            mybot.send_message(message.chat.id, locations.toshkentsh_kr)
            mybot.send_location(message.from_user.id, 41.361258, 69.242641)
        elif message.text == "Тошкент вилояти":
            log(message)
            mybot.send_message(message.chat.id, locations.toshkent1_kr)
            mybot.send_location(message.from_user.id, 41.2624798, 69.2228512)
        elif message.text == "Андижон":
            log(message)
            mybot.send_message(message.chat.id, locations.andijon1_kr)
            mybot.send_location(message.from_user.id, 40.752063, 72.341996)
        elif message.text == "Фаргона":
            log(message)
            mybot.send_message(message.chat.id, locations.fargona1_kr)
            mybot.send_location(message.from_user.id, 40.3757406, 71.809204)
        elif message.text == "Наманган":
            log(message)
            mybot.send_message(message.chat.id, locations.namangan1_kr)
            mybot.send_location(message.from_user.id, 40.996209, 71.612875)
        elif message.text == "Бухоро":
            log(message)
            mybot.send_message(message.chat.id, locations.buxoro1_kr)
            mybot.send_location(message.from_user.id, 39.744180, 64.519187)
        elif message.text == "Джиззах":
            log(message)
            mybot.send_message(message.chat.id, locations.jizzax1_kr)
            mybot.send_location(message.from_user.id, 40.114156, 67.846125)
        elif message.text == "Қашқадарё":
            log(message)
            mybot.send_message(message.chat.id, locations.qarshi1_kr)
            mybot.send_location(message.from_user.id, 38.840984, 65.777014)
        elif message.text == "Навои":
            log(message)
            mybot.send_message(message.chat.id, locations.navoiy1_kr)
            mybot.send_location(message.from_user.id, 40.100387, 65.364838)
        elif message.text == "Самарқанд":
            log(message)
            mybot.send_message(message.chat.id, locations.samarqand1_kr)
            mybot.send_location(message.from_user.id, 39.6503102, 66.9510076)
        elif message.text == "Сирдарьё":
            log(message)
            mybot.send_message(message.chat.id, locations.sirdaryo1_kr)
            mybot.send_location(message.from_user.id, 40.504731, 68.778095)
        elif message.text == "Хоразм":
            log(message)
            mybot.send_message(message.chat.id, locations.xorazm1_kr)
            mybot.send_location(message.from_user.id, 41.549364, 60.633994)
        elif message.text == "Қорақолпогистон":
            log(message)
            mybot.send_message(message.chat.id, locations.qoraqalpogiston1_kr)
            mybot.send_location(message.from_user.id, 42.460163, 59.615756)
        elif message.text == "Сурхандарьё":
            log(message)
            mybot.send_message(message.chat.id, locations.surxondaryo1_kr)
            mybot.send_location(message.from_user.id, 37.2387655, 67.280288)
        elif message.text == "💳Пластик карталар":
            # language("ru")
            log(message)
            handle_back_uzb_kiril(message, constant.plastik_ru)

        elif message.text == "💸Пул ўтказмалари":
            # language("uz")
            log(message)
            handle_back_uzb_kiril(message)


        elif message.text == "ОАЖ «Сбербанк»":
            log(message)
            mybot.send_message(message.chat.id, constant.sberbank_kr)
        elif message.text == "ОАЖ «Россельхозбанк»":
            log(message)
            mybot.send_message(message.chat.id, constant.rosselxozbank_kr)
        elif message.text == "АТБ «Азия Инвест Банк»":
            log(message)
            mybot.send_message(message.chat.id, constant.aziyainvestbank_kr)
        elif message.text == "ОАЖ «ТрансКапиталбанк»":
            log(message)
            mybot.send_message(message.chat.id, constant.transkapitalbank_kr)
        elif message.text == "Ўз.Рес. ТИФ Миллий банки":
            log(message)
            mybot.send_message(message.chat.id, constant.milliybank_kr)
        elif message.text == "АИТБ «Ипак Йули»":
            log(message)
            mybot.send_message(message.chat.id, constant.ipakyulibank_kr)
        elif message.text == "АТБ «Ўзсаноатқурилишбанк»":
            log(message)
            mybot.send_message(message.chat.id, constant.uzsanoatbank_kr)

        ###########################RUS#####################################
        elif message.text == "Назад":
            # language("ru")
            log(message)
            handle_xizmat_ru(message)
        elif message.text == "Нaзад":
            # language("ru")
            log(message)
            handle_jismoniy_ru(message)
        elif message.text == "Назaд":
            # language("ru")
            log(message)
            handle_yuridik_ru(message)
        elif message.text == "Изменить язык / Tilni o`zgartirish":
            # language("ru")
            log(message)
            handle_start(message)
        elif message.text == "Банковские услуги":
            # language("ru")
            log(message)
            handle_xizmat_ru(message)
        elif message.text == "👕Для физических лиц":
            # language("ru")
            log(message)
            handle_jismoniy_ru(message)
        elif message.text == "👔Для юридических лиц":
            # language("ru")
            log(message)
            handle_yuridik_ru(message)
        elif message.text == "💼Кредитование":
            # language("ru")
            log(message)
            handle_kredit_yur_ru(message)
        elif message.text == "Торогвые кредиты":
            # language("ru")
            log(message)
            mybot.send_message(message.chat.id, constant.savdo_kredit_ru)
        elif message.text == "Микрокредиты":
            # language("ru")
            log(message)
            mybot.send_message(message.chat.id, constant.mikrokreditlar_yur_ru)
        elif message.text == "Для выпускников колледжей":
            # language("ru")
            log(message)
            mybot.send_message(message.chat.id, constant.kollej_ru)
        elif message.text == "🏛Банки-корреспонденты":
            # language("ru")
            log(message)
            handle_korrespschet_ru(message)



        elif message.text == "🏦Филиалы":
            # language("ru")
            log(message)
            handle_address_ru(message)
        elif message.text == "🏦 Вклады":
            # language("ru")
            log(message)
            handle_omonat_ru_jis(message)
        else:
            if message.text == "До востребование":
                # language("ru")
                log(message)
                handle_back_ru(message, constant.dovostrebovaniye)
            elif message.text == "Сберегательные вклады":
                # language("ru")
                log(message)
                mybot.send_message(message.chat.id, constant.jamgarma_omonat_ru)
            elif message.text == "Сбережении в иностранной валюте":
                # language("ru")
                log(message)
                mybot.send_message(message.chat.id, constant.horijoy_valyutaomonat_ru)
            elif message.text == "Срочные депозиты":
                # language("ru")
                log(message)
                mybot.send_message(message.chat.id, constant.mudatli_omonat_ru)
            elif message.text == "💰Кредиты":
                # language("ru")
                log(message)
                handle_kredit_ru_jis(message)
            elif message.text == "Автокредиты":
                log(message)
                mybot.send_message(message.chat.id, constant.avtokredit_ru)
            elif message.text == "Потребительский кредит":
                log(message)
                mybot.send_message(message.chat.id, constant.istemolkredit_ru)
            elif message.text == "Внутренный и внешный туризм":
                log(message)
                mybot.send_message(message.chat.id, constant.turizm_ru)
            elif message.text == "Микрозайм":
                log(message)
                mybot.send_message(message.chat.id, constant.mikroqarz_ru)
            elif message.text == "Овердрафтный кредит":
                log(message)
                mybot.send_message(message.chat.id, constant.overdraft_ru)

            elif message.text == "💸Денежные переводы":
                # language("ru")
                log(message)
                handle_back_ru(message, constant.perevod_ru)
            elif message.text == "МКБ мобил":
                # language("ru")
                log(message)
                markup = telebot.types.InlineKeyboardMarkup()
                btn_my_site = telebot.types.InlineKeyboardButton(text='МКБ Мобил',
                                                                 url="https://play.google.com/store/apps/details?id=uz.fido_biznes.mobile.client.mkb")
                markup.add(btn_my_site)
                img = 'https://imbt.ga/2lF1DfUT5d'

                mybot.send_message(message.chat.id, f'{constant.mobilbank_kr}\n{img}', reply_markup=markup)

            elif message.text == "МКБ мобайл":
                # language("ru")
                log(message)
                markup = telebot.types.InlineKeyboardMarkup()
                btn_my_site = telebot.types.InlineKeyboardButton(text='МКБ Мобайл',
                                                                 url="https://play.google.com/store/apps/details?id=uz.fido_biznes.mobile.client.mkb")
                markup.add(btn_my_site)
                img = 'https://imbt.ga/2lF1DfUT5d'

                mybot.send_message(message.chat.id, f'{constant.mobilbank_ru}\n{img}', reply_markup=markup)

                # mybot.send_location(message.from_user.id, 41.297546, 69.204514)
            elif message.text == "💳Пластиковые карты":
                log(message)
                markup = telebot.types.InlineKeyboardMarkup()
                btn_my_site = telebot.types.InlineKeyboardButton(text='Пластиковые карты',
                                                                 url="https://mikrokreditbank.uz/ru/retail/plastic-cards/")
                markup.add(btn_my_site)
                mybot.send_message(message.chat.id, f'{constant.plastik_ru}\n{constant.img_plastik_karta}',
                                   reply_markup=markup)
            elif message.text == '💵Курсы валют':
                log(message)
                valyuta_ru(message)
            elif message.text == '☎️Связаться с нами':
                handle_boglanish_uzb_ru(message)
            elif message.text == '📞Позвонить в Банк':
                log(message)
                mybot.send_message(message.chat.id,
                                   "Ягона қабул телефони: (+998) 71-202-99-99\n\nЯгона ишонч телефони: (+998) 71-273-04-40 ")
            elif message.text == '🗣Предложения и жалобы':
                handle_back_uzb_kiril(message, "Есть предложение или жалоба? Напишите нам.")
            elif message.text == '✍️Написать оператору':
                log(message)
                markup = telebot.types.InlineKeyboardMarkup()
                btn_my_site = telebot.types.InlineKeyboardButton(text='Чат Бот', url="t.me/mkb_chat_bot")
                markup.add(btn_my_site)
                mybot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш чат бот.", reply_markup=markup)
            elif message.text == "Головной офис":
                log(message)
                mybot.send_message(message.chat.id, locations.toshkent_ru)
                mybot.send_location(message.from_user.id, 41.297546, 69.204514)
            elif message.text == "Интерактивные услуги":
                log(message)
                handle_interaktiv_ru(message)

            elif message.text == "Интернет Банкинг":
                log(message)
                markup = telebot.types.InlineKeyboardMarkup()
                btn_my_site = telebot.types.InlineKeyboardButton(text='Узнать большее об Интернет Банкинг',
                                                                 url="https://mikrokreditbank.uz/uz/corporate/interactive-services/")
                markup.add(btn_my_site)
                mybot.send_message(message.chat.id, f'{constant.internet_kr}\n{constant.img_internet_bank}',
                                   reply_markup=markup)
            elif message.text == "СМС Банкинг":
                log(message)
                markup = telebot.types.InlineKeyboardMarkup()
                btn_my_site = telebot.types.InlineKeyboardButton(text='Узнать большее об СМС Банкинг',
                                                                 url="https://mikrokreditbank.uz/uz/corporate/interactive-services/")
                markup.add(btn_my_site)
                mybot.send_message(message.chat.id, f'{constant.sms_banking_kr}\n{constant.img_sms_bank}',
                                   reply_markup=markup)
            elif message.text == "💸Денежные переводы":
                # language("uz")
                log(message)

                log(message)
                markup = telebot.types.InlineKeyboardMarkup()
                btn_my_site = telebot.types.InlineKeyboardButton(text='Денежные переводы узнать больше',
                                                                 url="https://mikrokreditbank.uz/ru/retail/money-transfer/")
                markup.add(btn_my_site)
                mybot.send_message(message.chat.id, f'{constant.pul_otkazmalar_ru}\n{constant.img_pul_otkazma}',
                                   reply_markup=markup)
            elif message.text == "Ташкент":
                log(message)
                mybot.send_message(message.chat.id, locations.toshkentsh_ru)
                mybot.send_location(message.from_user.id, 41.361258, 69.242641)
            elif message.text == "Ташкентская область":
                log(message)
                mybot.send_message(message.chat.id, locations.toshkent1_ru)
                mybot.send_location(message.from_user.id, 41.2624798, 69.2228512)
            elif message.text == "Андижан":
                log(message)
                mybot.send_message(message.chat.id, locations.andijon1_ru)
                mybot.send_location(message.from_user.id, 40.752063, 72.341996)
            elif message.text == "Фергана":
                log(message)
                mybot.send_message(message.chat.id, locations.fargona1_ru)
                mybot.send_location(message.from_user.id, 40.3757406, 71.809204)
            elif message.text == "Наманган":
                log(message)
                mybot.send_message(message.chat.id, locations.namangan1_ru)
                mybot.send_location(message.from_user.id, 40.996209, 71.612875)
            elif message.text == "Бухара":
                log(message)
                mybot.send_message(message.chat.id, locations.buxoro1_ru)
                mybot.send_location(message.from_user.id, 39.744180, 64.519187)
            elif message.text == "Жиззах":
                log(message)
                mybot.send_message(message.chat.id, locations.jizzax1_ru)
                mybot.send_location(message.from_user.id, 40.114156, 67.846125)
            elif message.text == "Кашкадарья":
                log(message)
                mybot.send_message(message.chat.id, locations.qarshi1_ru)
                mybot.send_location(message.from_user.id, 38.840984, 65.777014)
            elif message.text == "Наваи":
                log(message)
                mybot.send_message(message.chat.id, locations.navoiy1_ru)
                mybot.send_location(message.from_user.id, 40.100387, 65.364838)
            elif message.text == "Самарканд":
                log(message)
                mybot.send_message(message.chat.id, locations.samarqand1_ru)
                mybot.send_location(message.from_user.id, 39.6503102, 66.9510076)
            elif message.text == "Сирдарья":
                log(message)
                mybot.send_message(message.chat.id, locations.sirdaryo1_ru)
                mybot.send_location(message.from_user.id, 40.504731, 68.778095)
            elif message.text == "Хорезм":
                log(message)
                mybot.send_message(message.chat.id, locations.xorazm1_ru)
                mybot.send_location(message.from_user.id, 41.549364, 60.633994)
            elif message.text == "Каракалпакистан":
                log(message)
                mybot.send_message(message.chat.id, locations.qoraqalpogiston1_ru)
                mybot.send_location(message.from_user.id, 42.460163, 59.615756)
            elif message.text == "Сурхандарья":
                log(message)
                mybot.send_message(message.chat.id, locations.surxondaryo1_ru)
                mybot.send_location(message.from_user.id, 37.2387655, 67.280288)

            elif message.text == "ПАО «Сбербанк»":
                log(message)
                mybot.send_message(message.chat.id, constant.sberbank_ru)
            elif message.text == "ОАО «Россельхозбанк»":
                log(message)
                mybot.send_message(message.chat.id, constant.rosselxozbank_ru)
            elif message.text == "ПАО «ТрансКапиталбанк»":
                log(message)
                mybot.send_message(message.chat.id, constant.aziyainvestbank_ru)
            elif message.text == "АКБ «Азия Инвест Банк»":
                log(message)
                mybot.send_message(message.chat.id, constant.transkapitalbank_ru)
            elif message.text == "Национальный Банк ВЭД РУз":
                log(message)
                mybot.send_message(message.chat.id, constant.milliybank_ru)
            elif message.text == "АИКБ «Ипак Йули»":
                log(message)
                mybot.send_message(message.chat.id, constant.ipakyulibank_ru)
            elif message.text == "АКБ «Узпромстройбанк»":
                log(message)
                mybot.send_message(message.chat.id, constant.uzsanoatbank_ru)


            else:
                if lang == "uz":
                    mybot.send_message(message.chat.id, "Iltimos, kerakli bo'limni tanlang!!!")
                    log(message)
                elif lang == "ru":
                    mybot.send_message(message.chat.id, "Илтимос, керакли бўлимни танланг !!!")
                    log(message)
                elif lang == "ru":
                    mybot.send_message(message.chat.id, "Пожалуйста выберите пункт из меню!!!")
                    log(message)
                else:
                    mybot.send_message('@mikro_admin',
                                       text="Сообщение от {0} {1}. \nUsername @{2} \n\nТекст - {3}".format(
                                           message.from_user.first_name,
                                           message.from_user.last_name,
                                           str(message.from_user.username),
                                           message.text))
                    log(message)


while True:
    try:
        mybot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(15)
