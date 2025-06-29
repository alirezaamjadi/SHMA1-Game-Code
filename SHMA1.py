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
    print("   ☀️ Mordad        (July-August)")
    print("   🍂 Shahrivar     (August-September)")
    print("   🍁 Mehr          (September-October)")
    print("   🍃 Aban          (October-November)")
    print("   ❄️ Azar          (November-December)")
    print("   ☃️ Dey           (December-January)")
    print("   🌨️ Bahman        (January-February)")
    print("   🌧️ Esfand        (February-March)")
    
    month = input("🗓️  Mah (Month): ")

    clear_screen()
    print("📅 Ghadam 5 (Step 5): Sale tavalodet ro benevis (Enter Your Birth Year)")
    year = input("📆 Sal (Year): ")

    fates = [
        "rooze bad (Bad Day)", "badbakht (Unlucky)", "shans nadari (No Luck)", 
        "shanset khoobe (Good Luck)", "rooze khafan (Awesome Day)",
        "mamooli (Normal)", "daghooni (Messed Up)", "shanset balaas (High Luck)",
        "hazrat marg (Close to Death)", "baresi nashod (Error)", "ajab shansi (Wow, Lucky)",
        "kheili bad (Very Bad)", "mosbat bala (High Positive)", "eshtebah kardi (You Made a Mistake)",
        "ghabele goftan nist (Unspeakable)", "baz ham shans (Luck Again)", 
        "shanset to mochast (Your Luck is Trapped)", "shans gerefte (Blocked Luck)",
        "na bade na khobe (Not Good, Not Bad)", "yar nadari vali del dari (Alone but Brave)",
        "shanset sare zamine (Fallen Luck)", "khoshbakhtiye tasadofi (Random Happiness)",
        "shans zero (Zero Luck)", "mosbat vali mohr (Positive but Sealed)",
        "bekhand vali khatar dare (Smile, but It’s Dangerous)", "hazf shodi (You’re Eliminated)"
    ]
    fate = random.choice(fates)

    clear_screen()
    message = (
        "👋 Salam Agha-ye alireza amjadi!\n"
        "📅 Shoma dar rooz-e shande va dar mah-e tir ke mishe to sal-e 2026\n"
        "🔮 Shoma dar entezar-e yek 'hazf shodi (You’re Eliminated)' hastid.\n"
        "🌟 Movafagh bashid!\n"
        "❤️ Alireza Amjadi, doostar-e shoma."
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
