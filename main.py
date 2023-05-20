import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
import sqlite3

conn = sqlite3.connect('best_orders.db', check_same_thread=False)
cursor = conn.cursor()
print("Подключен к SQLite")

bot = telebot.TeleBot(token=Config.token)

@bot.message_handler(commands=["start"])
def start_msg(message):
    query = f"INSERT INTO user_orders (user_id) VALUES({message.from_user.id})"
    cursor.execute(query)
    conn.commit()
    start_keyboard = InlineKeyboardMarkup()
    callback_button = InlineKeyboardButton(text="Оформить поставку", callback_data="Оформить поставку")
    start_keyboard.add(callback_button)
    user_first_name = str(message.chat.first_name)
    bot.reply_to(message,
                 f"Привет {user_first_name} ✌️ я бот помошник по оформлению поставок!",
                 reply_markup=start_keyboard)
    
     

@bot.callback_query_handler(func=lambda call: True)
def main(call):
    market_plc = ""
    type_delivery = ""
    town = ""
    where_date = "" 
    cnt_boxes = 0 
    price = ""  
    
       
           
    def market(bot, call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=1)
        callback_button1 = InlineKeyboardButton(text="WB", callback_data="WB")
        callback_button2 = InlineKeyboardButton(text="Ozone", callback_data="Ozone")
        button_keyboard.add(callback_button1, callback_button2)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Выберите маркетплейс',
            reply_markup=button_keyboard) 
           
    def what_delivery(bot,call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=2)
        callback_button1 = InlineKeyboardButton(text="Короб", callback_data="Короб")
        callback_button2 = InlineKeyboardButton(text="Палета", callback_data="Палета")
        callback_button3 = InlineKeyboardButton(text="Назад", callback_data="back1")
        button_keyboard.add(callback_button1, 
                            callback_button2,
                            callback_button3)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Выберите тип поставки',
            reply_markup=button_keyboard)
        
    def what_size(bot,call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=2)
        callback_button1 = InlineKeyboardButton(text="Да", callback_data="Да")
        callback_button2 = InlineKeyboardButton(text="Нет", callback_data="Нет")
        callback_button3 = InlineKeyboardButton(text="Назад", callback_data="back2")
        button_keyboard.add(callback_button1, 
                            callback_button2,
                            callback_button3)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='У вас стандартный размер коробки?',
            reply_markup=button_keyboard)       
        
    def towns(bot, call, type_delivery): 
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=2)
        callback_button1 = InlineKeyboardButton(text="Алексин", callback_data="Алексин")
        callback_button2 = InlineKeyboardButton(text="Домодедово", callback_data="Домодедово")
        callback_button3 = InlineKeyboardButton(text="Казань", callback_data="Казань")
        callback_button4 = InlineKeyboardButton(text="Коледино", callback_data="Коледино")
        callback_button5 = InlineKeyboardButton(text="Краснодар", callback_data="Краснодар")
        callback_button6 = InlineKeyboardButton(text="Невинномысск", callback_data="Невинномысск")
        callback_button7 = InlineKeyboardButton(text="Подольск", callback_data="Подольск")
        callback_button8 = InlineKeyboardButton(text="Рязань", callback_data="Рязань")
        callback_button9 = InlineKeyboardButton(text="Шушары", callback_data="Шушары")
        callback_button10 = InlineKeyboardButton(text="Электросталь", callback_data="Электросталь")        
        callback_button11 = [InlineKeyboardButton(text="Назад", callback_data="back2")]
        if type_delivery == "Короб":       
            button_keyboard.add(callback_button1, 
                            callback_button2,
                            callback_button3,
                            callback_button4,
                            callback_button5,
                            callback_button6,
                            callback_button7,
                            callback_button8).row(*callback_button11)
        else:
            button_keyboard.add(callback_button1, 
                            callback_button2,
                            callback_button3,
                            callback_button4,
                            callback_button5,
                            callback_button6,
                            callback_button7,
                            callback_button8,
                            callback_button9,
                            callback_button10).row(*callback_button11)
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Выберите склад',
            reply_markup=button_keyboard)  
             
    def date_delivery(bot,call,gorod):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=2)
        # Aleksin
        callback_button1 = InlineKeyboardButton(text="05.04.2023", callback_data="05.04.2023")
        callback_button2 = InlineKeyboardButton(text="12.04.2023", callback_data="12.04.2023")
        callback_button3 = InlineKeyboardButton(text="19.04.2023", callback_data="19.04.2023")
        callback_button4 = InlineKeyboardButton(text="26.04.2023", callback_data="26.04.2023")
        # Kazan
        callback_button5 = InlineKeyboardButton(text="06.04.2023", callback_data="06.04.2023")
        callback_button6 = InlineKeyboardButton(text="13.04.2023", callback_data="13.04.2023")
        callback_button7 = InlineKeyboardButton(text="20.04.2023", callback_data="20.04.2023")
        callback_button8 = InlineKeyboardButton(text="27.04.2023", callback_data="27.04.2023")
        # Moscow
        callback_button9 = InlineKeyboardButton(text="04.04.2023", callback_data="04.04.2023")
        callback_button10 = InlineKeyboardButton(text="08.04.2023",callback_data="08.04.2023")
        callback_button11 = InlineKeyboardButton(text="11.04.2023",callback_data="11.04.2023")
        callback_button12 = InlineKeyboardButton(text="15.04.2023",callback_data="15.04.2023")
        callback_button13 = InlineKeyboardButton(text="18.04.2023",callback_data="18.04.2023")
        callback_button14 = InlineKeyboardButton(text="22.04.2023",callback_data="22.04.2023")
        callback_button15 = InlineKeyboardButton(text="25.04.2023",callback_data="25.04.2023")
        callback_button16 = InlineKeyboardButton(text="29.04.2023",callback_data="29.04.2023")
        # Krasnodar
        callback_button17 = InlineKeyboardButton(text="14.04.2023",callback_data="14.04.2023")
        callback_button18 = InlineKeyboardButton(text="28.04.2023",callback_data="28.04.2023")
        # Piter
        callback_button19 = InlineKeyboardButton(text="07.04.2023",callback_data="07.04.2023")
        callback_button20 = InlineKeyboardButton(text="21.04.2023",callback_data="21.04.2023")
        callback_button21 = InlineKeyboardButton(text="Назад", callback_data="back3")    
        match gorod:
            case "Алексин":
                button_keyboard.add(callback_button1, 
                callback_button1,
                callback_button2,
                callback_button3,
                callback_button4).row(callback_button21)
            case "Казань":
                button_keyboard.add( 
                callback_button5,
                callback_button6,
                callback_button7,
                callback_button8,
                callback_button21)
            case "Краснодар":
                button_keyboard.add(
                callback_button17,
                callback_button18,
                callback_button21)
            case "Шушары":
                 button_keyboard.add(
                 callback_button19,
                 callback_button20,
                callback_button21)
            case _:
                button_keyboard.add(
                callback_button9,
                callback_button10,
                callback_button11,
                callback_button12,
                callback_button13,
                callback_button14,
                callback_button15,
                callback_button16,
                callback_button21)   
        bot.send_message(
            chat_id=call.message.chat.id,
            text='ВЫБЕРИТЕ ДАТУ',
            reply_markup=button_keyboard) 
          
    def boxes(bot, call, type_delivery):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=8)
        callback_button1 = InlineKeyboardButton(text="1",   callback_data=1)
        callback_button2 = InlineKeyboardButton(text="2",   callback_data=2)
        callback_button3 = InlineKeyboardButton(text="3",   callback_data=3)
        callback_button4 = InlineKeyboardButton(text="4",   callback_data=4)
        callback_button5 = InlineKeyboardButton(text="5",   callback_data=5)
        callback_button6 = InlineKeyboardButton(text="6",   callback_data=6)
        callback_button7 = InlineKeyboardButton(text="7",   callback_data=7)
        callback_button8 = InlineKeyboardButton(text="8",   callback_data=8)
        callback_button9 = InlineKeyboardButton(text="9",   callback_data=9)
        callback_button10 = InlineKeyboardButton(text="10", callback_data=10)
        callback_button11 = InlineKeyboardButton(text="11", callback_data=11)
        callback_button12 = InlineKeyboardButton(text="12", callback_data=12)
        callback_button13 = InlineKeyboardButton(text="13", callback_data=13)
        callback_button14 = InlineKeyboardButton(text="14", callback_data=14)
        callback_button15 = InlineKeyboardButton(text="15", callback_data=15) 
        callback_button16 = InlineKeyboardButton(text="16", callback_data=16)
        callback_button17 = InlineKeyboardButton(text="17", callback_data=17)
        callback_button18 = InlineKeyboardButton(text="18", callback_data=18)
        callback_button19 = InlineKeyboardButton(text="19", callback_data=19)
        callback_button20 = InlineKeyboardButton(text="20", callback_data=20)
        callback_button21 = InlineKeyboardButton(text="21", callback_data=21)
        callback_button22 = InlineKeyboardButton(text="22", callback_data=22)
        callback_button23 = InlineKeyboardButton(text="23", callback_data=23)
        callback_button24 = InlineKeyboardButton(text="24", callback_data=24)
        callback_button25 = InlineKeyboardButton(text="25", callback_data=25)
        callback_button26 = InlineKeyboardButton(text="26", callback_data=26)
        callback_button27 = InlineKeyboardButton(text="27", callback_data=27)
        callback_button28 = InlineKeyboardButton(text="28", callback_data=28)
        callback_button29 = InlineKeyboardButton(text="29", callback_data=29)
        callback_button30 = InlineKeyboardButton(text="30", callback_data=30)   
        callback_button31 = InlineKeyboardButton(text="31", callback_data=31)
        callback_button32 = InlineKeyboardButton(text="32", callback_data=32)
        callback_button33 = InlineKeyboardButton(text="33", callback_data=33)
        callback_button34 = InlineKeyboardButton(text="34", callback_data=34)
        callback_button35 = InlineKeyboardButton(text="35", callback_data=35)
        callback_button36 = InlineKeyboardButton(text="36", callback_data=36) 
        callback_button37 = InlineKeyboardButton(text="37", callback_data=37)
        callback_button38 = InlineKeyboardButton(text="38", callback_data=38)
        callback_button39 = InlineKeyboardButton(text="39", callback_data=39)
        callback_button40 = InlineKeyboardButton(text="40", callback_data=40)
        callback_button41 = InlineKeyboardButton(text="41", callback_data=41)
        callback_button42 = InlineKeyboardButton(text="42", callback_data=42)
        callback_button43 = InlineKeyboardButton(text="43", callback_data=43)
        callback_button44 = InlineKeyboardButton(text="44", callback_data=44)
        callback_button45 = InlineKeyboardButton(text="45", callback_data=45)
        callback_button46 = InlineKeyboardButton(text="46", callback_data=46)
        callback_button47 = InlineKeyboardButton(text="47", callback_data=47)
        callback_button48 = InlineKeyboardButton(text="48", callback_data=48)
        callback_button49 = InlineKeyboardButton(text="49", callback_data=49)
        callback_button50 = InlineKeyboardButton(text="50", callback_data=50)  
        callback_button51 = [InlineKeyboardButton(text="Назад", callback_data="back4")]
        if type_delivery == "Короб":
            button_keyboard.add(callback_button1,callback_button2,callback_button3,callback_button4,callback_button5, 
                            callback_button6,callback_button7, callback_button8,callback_button9,callback_button10,
                            callback_button11,callback_button12,callback_button13,callback_button14,callback_button15,
                            callback_button16,callback_button17,callback_button18,callback_button19,callback_button20,
                            callback_button21,callback_button22,callback_button23,callback_button24,callback_button25,
                            callback_button26,callback_button27,callback_button28,callback_button29,callback_button30,
                            callback_button31,callback_button32,callback_button33,callback_button34,callback_button35,
                            callback_button36,callback_button37,callback_button38,callback_button39,callback_button40,
                            callback_button41,callback_button42,callback_button43,callback_button44,callback_button45,
                            callback_button46,callback_button47,callback_button48,callback_button49,callback_button50
                            ).row(*callback_button51)
            bot.send_message(
            chat_id=call.message.chat.id,
            text='Укажите кол-во коробок',
            reply_markup=button_keyboard)
            
        else:
            button_keyboard.add(callback_button1,callback_button2,callback_button3,callback_button4,callback_button5, 
                            callback_button6,callback_button7, callback_button8,callback_button9,callback_button10,
                            callback_button11,callback_button12,callback_button13,callback_button14,callback_button15,
                            callback_button16,callback_button17,callback_button18,callback_button19,callback_button20,
                            callback_button21,callback_button22,callback_button23,callback_button24,callback_button25,
                            callback_button26,callback_button27,callback_button28,callback_button29,callback_button30,
                            callback_button31,callback_button32,callback_button33).row(*callback_button51)
            bot.send_message(
            chat_id=call.message.chat.id,
            text='Укажите кол-во палет',
            reply_markup=button_keyboard) 
          
    def choice_of_delivery(bot, call):  
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            button_keyboard = InlineKeyboardMarkup(row_width=2)
            callback_button = InlineKeyboardButton(text="Склад", callback_data="Склад")
            callback_button2 = InlineKeyboardButton(text="С вашего адреса", callback_data="С вашего адреса")
            callback_button3 = InlineKeyboardButton(text="Назад", callback_data="back5")
            button_keyboard.add(callback_button, 
                                callback_button2, 
                                callback_button3)
            msg = bot.send_message(
                chat_id=call.message.chat.id,
                text='Выберите способ забора',
                reply_markup=button_keyboard)
    
    def choice_of_adress(bot, call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=2)
        callback_button = InlineKeyboardButton(text="Карцево", callback_data="Карцево")
        callback_button2 = InlineKeyboardButton(text="Дом художника", callback_data="Дом художника")
        callback_button3 = InlineKeyboardButton(text="Назад", callback_data="back6")
        button_keyboard.add(callback_button, 
                            callback_button2,
                            callback_button3)
        msg = bot.send_message(
            chat_id=call.message.chat.id,
            text='Выберите склад',
            reply_markup=button_keyboard)   
    
    def providing_name_callback(msg):
            if msg.text == "/start":
                bot.send_message(chat_id=call.message.chat.id,
                             text="Адрес введен некоректно")
                adres_name2(bot,call)  
            else:      
                update_query = f"Update user_orders set sklad = '{msg.text}' where id = {max_id} and user_id={call.from_user.id}"
                conn.execute(update_query)
                conn.commit()
                tt = conn.execute(f"select id,market,type_delivery,town,what_date,cnt_boxes,price,sklad,interval from user_orders where id={max_id} and user_id={call.from_user.id}")
                record = tt.fetchone()
                str = f'username: {msg.from_user.username}\nНомер заказа: {record[0]}\nМаркетплейс: {record[1]}\nТип поставки: {record[2]}\nПункт назначения: {record[3]}\nДата доставки: {record[4]}\nКол-во едениц: {record[5]}\nЦена: {record[6]} рублей\nСклад: {record[7]}\nИнтервал: {record[8]}'
                # # chat_id = -1001719217516
                # bot.send_message(chat_id=chat_id, text=str) 
                button_keyboard = InlineKeyboardMarkup(row_width=1)
                callback_button1 = InlineKeyboardButton(text="Подтвердить", callback_data="Подтвердить")
                callback_button2 = InlineKeyboardButton(text="Упс, я передумал", callback_data="Упс, я передумал")
                button_keyboard.add(callback_button1,
                                    callback_button2)
                bot.send_message(chat_id=call.message.chat.id,
                                 text=str,
                                 reply_markup=button_keyboard)           
        
    def providing_name_callback2(msg):
        if msg.text == "/start":
            bot.send_message(chat_id=call.message.chat.id,
                         text="Данные введены некоректно")
            message_manager2(bot,call)  
        else:      
            update_query = f"Update user_orders set data_client = '{msg.text}' where id = {max_id} and user_id={call.from_user.id}"
            conn.execute(update_query)
            conn.commit()
            
            tt = conn.execute(f"select id,data_client from user_orders where id={max_id} and user_id={call.from_user.id}")
            record = tt.fetchone()
            str = f'Номер заказа: {record[0]}\nСвязаться с клиентом: {record[1]}'
            chat_id = -1001719217516
            bot.send_message(chat_id=chat_id, text=str)      
        
    def approved(bot,call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tt = conn.execute(f"select id,market,type_delivery,town,what_date,cnt_boxes,price,sklad,interval from user_orders where id={max_id} and user_id={call.from_user.id}")
        record = tt.fetchone()
        str = f'username: {call.from_user.username}\nНомер заказа: {record[0]}\nМаркетплейс: {record[1]}\nТип поставки: {record[2]}\nПункт назначения: {record[3]}\nДата доставки: {record[4]}\nКол-во едениц: {record[5]}\nЦена: {record[6]} рублей\nСклад: {record[7]}\nИнтервал: {record[8]}'           
        button_keyboard = InlineKeyboardMarkup(row_width=1)
        callback_button1 = InlineKeyboardButton(text="Подтвердить", callback_data="Подтвердить")
        callback_button2 = InlineKeyboardButton(text="Упс, я передумал", callback_data="Упс, я передумал")
        button_keyboard.add(callback_button1,
                            callback_button2)
        bot.send_message(chat_id=call.message.chat.id,
                             text=str,
                             reply_markup=button_keyboard)
       
    def final(bot,call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tt = conn.execute(f"select id from user_orders where id={max_id} and user_id={call.from_user.id}")
        record = tt.fetchone()
        str = f'Заказ №{record[0]} подтвержден'
        bot.send_message(chat_id=call.message.chat.id,
                             text={str}) 
        
        tt = conn.execute(f"select id,market,type_delivery,town,what_date,cnt_boxes,price,sklad,interval from user_orders where id={max_id} and user_id={call.from_user.id}")
        record = tt.fetchone()
        str = f'username: {call.from_user.username}\nНомер заказа: {record[0]}\nМаркетплейс: {record[1]}\nТип поставки: {record[2]}\nПункт назначения: {record[3]}\nДата доставки: {record[4]}\nКол-во едениц: {record[5]}\nЦена: {record[6]} рублей\nСклад: {record[7]}\nИнтервал: {record[8]}'
        chat_id = -1001719217516
        bot.send_message(chat_id=chat_id, text=str)
    
    def final_cancel(bot,call):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        tt = conn.execute(f"select id from user_orders where id={max_id} and user_id={call.from_user.id}")
        record = tt.fetchone()
        str = f'Заказ №{record[0]} отменён'
        bot.send_message(chat_id=call.message.chat.id,
                             text={str})    
                                        
    def adres_name(bot, call):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            msg = bot.send_message(
                chat_id=call.message.chat.id,
                text="Напишите ваш адрес!",
                parse_mode='Markdown')
            bot.register_next_step_handler(msg,providing_name_callback)  
            
    def message_manager(bot,call):
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            msg = bot.send_message(
                chat_id=call.message.chat.id,
                text="Оставьте контактные данные, с вами свяжется менеджер!",
                parse_mode='Markdown')
            bot.register_next_step_handler(msg,providing_name_callback2)
            
    def message_manager2(bot,call):
            msg = bot.send_message(
                chat_id=call.message.chat.id,
                text="Оставьте контактные данные, с вами свяжется менеджер!",
                parse_mode='Markdown')
            bot.register_next_step_handler(msg,providing_name_callback2)        
            
    def adres_name2(bot, call):
            msg = bot.send_message(
                chat_id=call.message.chat.id,
                text="Напишите ваш адрес!",
                parse_mode='Markdown')
            bot.register_next_step_handler(msg,providing_name_callback)         
            
    def time_interval(bot, call, interval):
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        button_keyboard = InlineKeyboardMarkup(row_width=2)
        callback_button1 = InlineKeyboardButton(text="с 11 до 13", callback_data="с 11 до 13")
        callback_button2 = InlineKeyboardButton(text="с 13 до 15", callback_data="с 13 до 15")
        callback_button3 = InlineKeyboardButton(text="с 15 до 18", callback_data="с 15 до 18")
        callback_button4 = InlineKeyboardButton(text="после 18", callback_data="после 18")
        callback_button5 = InlineKeyboardButton(text="с 9 до 11", callback_data="с 9 до 11")
        callback_button6 = InlineKeyboardButton(text="с 11 до 13", callback_data="с 11 до 13")
        callback_button7 = InlineKeyboardButton(text="с 13 до 15", callback_data="с 13 до 15")
        callback_button8 = InlineKeyboardButton(text="с 15 до 16", callback_data="с 15 до 16")
        callback_button9 = InlineKeyboardButton(text="с 10 до 14", callback_data="с 10 до 14")
        callback_button10 = InlineKeyboardButton(text="с 14 до 18", callback_data="с 14 до 18")
        callback_button11 = InlineKeyboardButton(text="Назад", callback_data="back7")
        match interval:
            case "Карцево":
                button_keyboard.add(callback_button1, 
                                    callback_button2,
                                    callback_button3,
                                    callback_button4,
                                    callback_button11)
            case "Дом художника": 
                button_keyboard.add(callback_button5, 
                                    callback_button6,
                                    callback_button7,
                                    callback_button8,
                                    callback_button11)
            case "С вашего адреса":
                button_keyboard.add(callback_button9,
                                    callback_button10,
                                    callback_button11)                  
        bot.send_message(
            chat_id=call.message.chat.id,
            text='Выберите время',
            reply_markup=button_keyboard)                
            
    def prices(town, cnt_boxes):  
       match town:
          case "Краснодар":
             if cnt_boxes <= 10:
                price = 950 * cnt_boxes 
                return price
             else:
                price = 850 * cnt_boxes 
                return price
          case "Казань":
             if cnt_boxes <= 10:
                price = 800 * cnt_boxes 
                return price
             else:
                price = 600 * cnt_boxes 
                return price
          case "Шушары":
             if cnt_boxes <= 10:
                price = 890 * cnt_boxes 
                return price
             else:
                price = 700 * cnt_boxes
                return price 
          case "Алексин":
             if cnt_boxes <= 10:
                price = 500 * cnt_boxes 
                return price
             else:
                price = 450 * cnt_boxes 
                return price   
          case "Рязань":
             if cnt_boxes >= 1:
                price = 100 * cnt_boxes 
                return price                        
          case _:
             if cnt_boxes <= 10:
                price = 400 * cnt_boxes
                return price
             elif cnt_boxes > 10 and cnt_boxes <= 20:
                price = 380 * cnt_boxes
                return price
             else:
                price = 360 * cnt_boxes
                return price 
       
    def prices_paleta(town, cnt_boxes):  
       match town:
          case "Краснодар"|"Шушары":
             if cnt_boxes == 1:
                price = 10000 
                return price
             elif cnt_boxes > 1 and cnt_boxes < 4:
                 price = 9000 * cnt_boxes
                 return price
             elif cnt_boxes > 3 and cnt_boxes < 6:
                 price = 8000 * cnt_boxes
                 return price
             else:
                price = 7000 * cnt_boxes 
                return price
            
          case "Казань":
             if cnt_boxes == 1:
                price = 9000 
                return price
             elif cnt_boxes > 1 and cnt_boxes < 4:
                 price = 8000 * cnt_boxes
                 return price
             elif cnt_boxes > 3 and cnt_boxes < 6:
                 price = 7000 * cnt_boxes
                 return price
             else:
                price = 6000 * cnt_boxes 
                return price
          
          case "Алексин":
             if cnt_boxes == 1:
                price = 6000 
                return price
             elif cnt_boxes > 1 and cnt_boxes < 4:
                 price = 5500 * cnt_boxes
                 return price
             elif cnt_boxes > 3 and cnt_boxes < 6:
                 price = 5000 * cnt_boxes
                 return price
             else:
                price = 4000 * cnt_boxes 
                return price 
                                  
          case _:
             if cnt_boxes == 1:
                price = 5000 
                return price
             elif cnt_boxes > 1 and cnt_boxes < 4:
                 price = 4500 * cnt_boxes
                 return price
             elif cnt_boxes > 3 and cnt_boxes < 6:
                 price = 4000 * cnt_boxes
                 return price
             else:
                price = 3000 * cnt_boxes 
                return price   
       
    def add_price(cnt_boxes):
        return 400+((cnt_boxes-1)*100)   
            
    query = f"select max(id) from user_orders where user_id={call.from_user.id}"
    records = conn.execute(query)
    records = records.fetchone()
    max_id = records[0]   
         
    match call.data:
        case "back1":
            market(bot,call)
            
        case "back2":
            what_delivery(bot,call)
        
        case "back3":
            tt = conn.execute(f"select type_delivery from user_orders where id={max_id} and user_id={call.from_user.id}")
            records = tt.fetchone()
            type = records[0]
            print(type)
            towns(bot,call,type)
            
        case "back4":
            tt = conn.execute(f"select town from user_orders where id={max_id} and user_id={call.from_user.id}")
            records = tt.fetchone()
            city = records[0]
            date_delivery(bot,call,city)  
            
        case "back5":
            update_query = f"Update user_orders set price = NULL where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            tt = conn.execute(f"select type_delivery from user_orders where id={max_id} and user_id={call.from_user.id}")
            records = tt.fetchone()
            type = records[0]
            print(type)
            boxes(bot,call,type)
            
            
        case "back6":            
            choice_of_delivery(bot,call)
            
        case "back7":
            choice_of_adress(bot, call) 
                       
        case "Оформить поставку":
            market(bot, call)
            
        case "WB"|"Ozone":
            update_query = f"Update user_orders set market = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit() 
            what_delivery(bot, call)
            
        case "Короб":
            update_query = f"Update user_orders set type_delivery = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            what_size(bot, call)
            
        case "Да":
            towns(bot, call, call.data)   
            
        case "Нет":
            message_manager(bot,call)     
        
        case "Палета":
            update_query = f"Update user_orders set type_delivery = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            towns(bot, call, call.data)    
            
        case "Коледино"|"Электросталь"|"Подольск"|"Шушары"|"Краснодар"|"Алексин"|"Казань"|"Домодедово"|"Невинномысск"|"Рязань":
            update_query = f"Update user_orders set town = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            date_delivery(bot, call, call.data)
            
        case "05.04.2023"|"12.04.2023"|"19.04.2023"|"26.04.2023"|"06.04.2023"|"13.04.2023"|"20.04.2023"|"27.04.2023"|"04.04.2023"|"08.04.2023"|"11.04.2023"|"15.04.2023"|"18.04.2023"|"22.04.2023"|"25.04.2023"|"29.04.2023"|"14.04.2023"|"28.04.2023"|"07.04.2023"|"21.04.2023":
            update_query = f"Update user_orders set what_date = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            tt = conn.execute(f"select type_delivery from user_orders where id={max_id} and user_id={call.from_user.id}")
            records = tt.fetchone()
            type = records[0]
            boxes(bot, call, type)
            
        case "Склад":
            choice_of_adress(bot,call)
        
        case "Карцево"|"Дом художника":
            update_query = f"Update user_orders set sklad = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            time_interval(bot, call, call.data)
        
        case "С вашего адреса":
            tt = conn.execute(f"select cnt_boxes, price from user_orders where id={max_id} and user_id={call.from_user.id}")
            records = tt.fetchone()
            createprice = add_price(records[0])
            newprice = createprice+records[1]
            update_query = f"Update user_orders set price = '{newprice}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            time_interval(bot, call, call.data)
            
        case "с 11 до 13"|"с 13 до 15"|"с 15 до 18"|"после 18"|"с 9 до 11"|"с 11 до 13"|"с 13 до 15"|"с 15 до 16":
            update_query = f"Update user_orders set interval = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()   
            approved(bot, call)
            
        case "с 10 до 14"|"с 14 до 18":
            update_query = f"Update user_orders set interval = '{call.data}' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            adres_name(bot, call)   
            
        case "Подтвердить":
            update_query = f"Update user_orders set status = 'Заказ подтвержден' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            final(bot, call)
            
        case "Упс, я передумал":
            update_query = f"Update user_orders set status = 'Заказ отменён' where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            final_cancel(bot, call)
            
        case _:
            tt = conn.execute(f"select town,type_delivery from user_orders where id={max_id} and user_id={call.from_user.id}")
            records = tt.fetchone()
            city = records[0]
            cnt_boxes = int(call.data)
            if records[1] == "Короб":
                price = prices(city, cnt_boxes)
            else:
                price = prices_paleta(city, cnt_boxes)
            update_query = f"Update user_orders set cnt_boxes = '{call.data}', price = {price} where id = {max_id} and user_id={call.from_user.id}"
            records = conn.execute(update_query)
            conn.commit()
            choice_of_delivery(bot,call)
            
       
    
                    
    
if __name__ == '__main__':
    bot.polling()
    # bot.infinity_polling(timeout=10, long_polling_timeout=5)            