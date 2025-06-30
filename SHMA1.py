import random
import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_box(text, variable_line_indices=None):
    if variable_line_indices is None:
        variable_line_indices = []

    lines = text.split('\n')
    padding_v = 1
    max_length = max(len(line) for line in lines)
    width = max_length + 4

    print('┌' + '─' * width + '┐')
    for _ in range(padding_v):
        print('│' + ' ' * width + '│')

    for i, line in enumerate(lines):
        if i in variable_line_indices:
            # بدون دیواره چپ و راست
            print('  ' + line.ljust(width - 2))
        else:
            # با دیواره چپ و راست و padding داخلی
            spaces_needed = width - 4 - len(line)
            print('│  ' + line + ' ' * spaces_needed + '  │')

    for _ in range(padding_v):
        print('│' + ' ' * width + '│')

    print('└' + '─' * width + '┘')



def draw_box_only_top_bottom(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    width = max_length + 4  # فاصله دو طرف

    # خط بالایی
    print('─' * width)

    # خطوط متن با فاصله دو طرف
    for line in lines:
        padding = width - len(line) - 2
        print('  ' + line + ' ' * padding)

    # خط پایینی
    print('─' * width)



def main_menu():
    while True:
        clear_screen()
        print("🎲 SHMA1 - Shans Meter Amjadi 🎲")
        print(" ╔══════════════════════════════╗")
        print("|  |  1️⃣  Test Your Day        |  |")
        print("|  |  2️⃣  About Game           |  |")
        print("|  |  3️⃣  Exit                 |  |")
        print(" ╚══════════════════════════════╝")
        choice = input("📥 Entekhab kon (Your Choice 1/2/3): ")

        if choice == '1':
            test_your_day()
        elif choice == '2':
            show_about()
        elif choice == '3':
            goodbye()
        else:
            input("❌ Ghalat zadi! (Invalid) ➡️ Press Enter...")

def test_your_day():
    clear_screen()
    print("👤 Ghadam 1 (Step 1): Esme khod ra vared kon (Enter First Name)")
    first_name = input("🧑 Esme shoma (First Name): ")

    clear_screen()
    print("👥 Ghadam 2 (Step 2): Famil ra vared kon (Enter Last Name)")
    last_name = input("👨‍💼 Famil shoma (Last Name): ")

    clear_screen()
    print("📅 Ghadam 3 (Step 3): Rooze hafte ro entekhab kon (Choose Day of the Week)")
    print("   🟢 Shanbeh       (Saturday)")
    print("   🟡 Yekshanbeh    (Sunday)")
    print("   🔵 Doshanbeh     (Monday)")
    print("   🟣 Seshanbeh     (Tuesday)")
    print("   🟠 Chaharshanbeh (Wednesday)")
    print("   🔴 Panjshanbeh   (Thursday)")
    print("   ⚫ Jomeh         (Friday)")
    day = input("📆 Rooz (Day): ")

    clear_screen()
    print("📆 Ghadam 4 (Step 4): Mah ro entekhab kon (Choose a Month)")
    print("   🌸 Farvardin     (March-April)")
    print("   🌼 Ordibehesht   (April-May)")
    print("   🌞 Khordad       (May-June)")
    print("   🔥 Tir           (June-July)")
    print("   ☀️  Mordad        (July-August)")
    print("   🍂 Shahrivar     (August-September)")
    print("   🍁 Mehr          (September-October)")
    print("   🍃 Aban          (October-November)")
    print("   ❄️  Azar          (November-December)")
    print("   ☃️  Dey           (December-January)")
    print("   🌨️  Bahman        (January-February)")
    print("   🌧️  Esfand        (February-March)")
    
    month = input("🗓️  Mah (Month): ")

    clear_screen()
    print("📅 Ghadam 5 (Step 5): Sale tavalodet ro benevis (Enter Your Birth Year)")
    year = input("📆 Sal (Year): ")

    fates = [
        # Funny Good Fates (50)
        "Shansi Ke Az Mashin Oftad Tu Jibat", "Ghodrat-e Khar-e Khandeh", "Movafaghiat-e Mahdood be Pizza",
        "Rooz-e Ghandi ba Adas Polo", "Tanha Boodi vali Ba Wi-Fi", "Hame Chi Khoobe Ageh Internet Npare",
        "Jadoo Shodi az Khoshbakhti", "Shans Dige Too Rooznameh Nemiad", "Yek Rooz-e Dige Zendeh",
        "Shans be Soorate Random Set Shodeh", "Tark-e Khoshhal Shodan", "Movafagh Shodi dar Khandidan",
        "Donya Dige Behet Namikhande, Mikhande", "Mooz Shodi Baraye Khoshbakhti", "Shanset Zang Zad",
        "Be Soorat Gheyre Ghanooni Khoshbakhti", "Gerefti 100 Dar Khoshhal-khone", "Jayezeh Ghand-e Sefid",
        "Ba Ye Sheytan-e Mehman Khosh Gozashti", "Shans be Soorate 720p Baz Shod", "Ghalbat Tik Tik Khoshbakhti",
        "Fekr Kardi Shabihe Super Mario Hasti (Boodi)", "Movafaghiat be Sabk-e Abnabat", "Bargasht-e Shans-e Qadimi",
        "Khoshbakhti be Soorate Rahgiri Posti", "Shansat zade too Sagh", "Bozorgtarin Bazi-e Donya ro Bordi (Uno)",
        "Khoshhal Shodi be Dalil-e Namaloom", "Bargashti be Form-e Asli", "Ghand-e Rooz Shodi",
        "Barg-e Mozaffar-e Rooz", "Harfi Nadashti, Rooz Khoob Shod", "Movafaghiat ba Rageh Laghv",
        "Shanset ba Soundtrack Umad", "Be Soorate Cartoon Khoshbakht Shodi", "Rooz-e Mashti ba Daste Chap",
        "Charkhesh-e Ghaza be Soode To", "Zendeh-i Ba Style", "Delkhoshi be Sabk-e Meme",
        "Mozakere ba Shans Movafagh Bood", "Hame Chi Mikhandeh behet", "Bakhteh Shodi vali Khoob",
        "Del Khorshidi ba Batteri Full", "Rooz-e Ba Dard Valy Khandedar", "Khoshbakht Shodi ba Shokolat",
        "Bargasht-e Shansi ke Fekr Mikardi Mordeh", "Fekr Kardi Badi, Khoob Shod", "Ashghal Khasti vali Khoshbakhti",
        "Rooz-e Ghazaaye Mamani", "Shanset daresho zade va Umade tu Zendegit",

        # Funny Bad Fates (50)
        "Zadeh be Derakht-e Badbakhti", "Fekr Kardi Khoobe, Nabood", "Bug Shodi tu Zendegi",
        "Shanset Gozaresh Dad be Police", "Mosibat ba App Update", "Hame Chi Raft tu Cache",
        "Shanset Offline Bood", "Dasteh Khali vali Del Por Goh", "Rooz-e Bi Soond",
        "Khodet Ghalat Login Kardi", "Bedehkareh Shansi", "Too Mozakhrafgir Gir Kardi",
        "Khodet Report Dadi be Zendegi", "Crash Kardi be Hame Chi", "Shanset be URL Eshtebah Raft",
        "Narmafzar-e Shans Pak Shode", "Tikeh Shodi tu Ghazaye Dirooz", "Az Rooze Ghabl Tasmim Gheyre Logik",
        "Zendeh-i Ba Version-e Bugdar", "Fekr Kardi Ye Chi Shodi", "Be Soorate Joghrafiaei Ghom Shodi",
        "Az Khoshbakhti Bypass Shodi", "Update Zad va Sabketo Shekast", "Delkhoori be Sabk-e Mashin-e Zabt",
        "Rooz-e Bad vali Ba Namak", "Badbakht Shodi vali Maamiz Daar", "Chizi ke Shekast, To Boodi",
        "Server-e Shansat Paeen Bood", "Bi Majmooei, Bi Tozih", "Gir Kardi tu Rooz-e Sheytan",
        "Hame Chi Raft tu Zobaleh-ye Rooz", "Error-e Zendegi 404", "Rooz-e Sard be Sabk-e Conditioner",
        "Offline Shodi dar Onlinei", "Too Rooz-e Havaei Set Shodi", "Khabe Shomare 13 Didam",
        "Daste Shansat Rooze Tarkide", "Movafaghiat Cancel Shode", "Shekast be Soorate Silent",
        "Fekr Kardi Khoshbakhti, Tizer Bood", "Gir Kardi tu Cycle-e Manfi", "Hame Chi Lag Zad",
        "Zadeh be Divar-e Shak", "Gerefti Shansi ke Male Kasi Dige Bood", "Zendegi Crash Dad vali Bug Report Nisti",
        "Bi Rahkar vali Por Mashghaleh", "To Alan Ham Naboodi", "Bargashti be Factory Reset",
        "Shanset Vasat Gireh Karde", "Rooz-e Fool Shodi vali Khodeti",
    ]

    fate = random.choice(fates)

    clear_screen()
    message = message = (
    f"👨  Salam Bar To  {first_name} {last_name}\n"
    f"⚡  Shoma Dar Roz {day} Dar Mah {month} To Sal {year}.\n"
    f"💎  Dar Entzar To Hast {fate}.\n"
    f"✨  Mofag Bashe\n"
    f"🧿  Alireza Hamishe Dost Dar Shoma."
)

    
    draw_box(message, variable_line_indices=[0,1,2,3,4])
    input("\n🔁 Baraye bazgasht Enter bezan (Press Enter to return)...")






def show_about():
    clear_screen()
    about_text = (
        "📘 GAME SHMA - Shans Meter Amjadi\n"
        "────────────────────────────────────────────\n"
        "🔤 SHMA1 (Meaning): Shans + Meter + Amjadi + Ver 1\n"
        "🪓 Sazande (Creator): Alireza Amjadi \n"
        "📆 Saal (Year): 2024 (۱۴۰۳)\n"
        "💻 Zaban (Language): Python\n"
        "🔢 Version: 1.0\n"
        "────────────────────────────────────────────\n"
        "🎮 Rahnama-ye Bazi (How to Play):\n"
        "1️⃣  Esme khodet ro benevis (Enter your first name)\n"
        "2️⃣  Famil ro benevis (Last name)\n"
        "3️⃣  Rooze hafte ro entekhab kon (Pick a weekday)\n"
        "4️⃣  Mah va sale tavalod ro vared kon (Enter month and year)\n"
        "5️⃣  Fate bekhoon (Read your fate!) 🔮\n"
        "🎲  Natayej 100% random hastan! (Fully random!)"
    )

    draw_box_only_top_bottom(about_text)

    input("\n🔁 Bazgasht be menu (Enter to return)")


def goodbye():
    clear_screen()
    print("👋 Khodahafez! (Goodbye!) Be omid-e shansi bala 🔮")
    time.sleep(1)
    sys.exit()

if __name__ == "__main__":
    main_menu()

# --- SHMA1: 100+ Lines of Pure Farsi-English Fun and Fate! 🎯 ---
