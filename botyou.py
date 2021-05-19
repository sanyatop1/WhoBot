import telebot
bot = telebot.TeleBot("1894255065:AAFy6g_V8FrIaZz0kR8f-j_K2tQdoPgUpHg")
import random 
import time
timing = time.time()
while True:
    if time.time() - timing >86400.0:
        timing = time.time()
        from telegram.ext import Updater
        def main():
          chat_id='-1001417968903'
          updater=Updater("1894255065:AAFy6g_V8FrIaZz0kR8f-j_K2tQdoPgUpHg",use_context=True)
          b="Сегодня бот:  "
          a =["@NoI3y"," @OlyaBlg"," @volcha123"," @grabelka"," @Aleksan_Sergeevich"," @M00nTiger"," @Pollyy_k"," @Yuli_lev"," @Sahakuieru"," @Dungeon_masterrr"," @TheGreatest_One"," @mrtimego"," @VladoSik202"," @Anya_233"," @joly_yurii"," @Innnnnn_a"," @garnven"," @like4nime"," @danilium137"," @kirilit0"," @yablokooooo"," @blessedqq"," @Yaroslav2404"]
          c =b+random.choice(a)
          updater.bot.send_message(chat_id=chat_id,text=c)
          @bot.message_handler ( commands=['reshka'])
          def  send_message ( message ):
            updater.bot.send_message(chat_id=chat_id, text=c)
          

        if __name__ == '__main__':
           main()
        

          
bot.polling()