import streamlit as st
import datetime
import pytz

# Descriptions for personal angel numbers (life path 1-9,11,22,33)
angel_descriptions = {
    1: "🌟 The angel number 1 symbolizes new beginnings, independence, and leadership. It encourages you to embrace your individuality and take initiative in pursuing your goals. This number is a reminder from the universe that you have the power to create your own reality through positive thoughts and actions. Trust in your abilities, as 1 signifies that fresh opportunities are on the horizon, urging you to step out of your comfort zone with confidence and determination.",
    2: "⚖️ Angel number 2 represents harmony, balance, and partnerships. It highlights the importance of cooperation and diplomacy in your relationships, whether personal or professional. This number encourages patience and adaptability, reminding you that everything unfolds in divine timing. By fostering peace and understanding, you align with supportive energies that help manifest your desires through teamwork and mutual respect.",
    3: "🎨 The number 3 is associated with creativity, self-expression, and optimism. It invites you to tap into your artistic talents and communicate openly with the world. Ascended masters are guiding you, providing inspiration and joy to overcome challenges. Embrace growth and social connections, as 3 signals that your positive energy attracts abundance and fulfilling experiences.",
    4: "🏗️ Angel number 4 embodies stability, hard work, and practicality. It reassures you that your efforts are building a solid foundation for future success. Angels are offering guidance and protection, encouraging discipline and organization in your endeavors. This number reminds you to stay grounded and focused, as perseverance will lead to long-term security and achievement.",
    5: "🌪️ Number 5 signifies change, freedom, and adventure. It heralds major transformations that bring growth and new experiences into your life. Embrace adaptability and curiosity, as this number encourages you to break free from old patterns. Your angels support your journey toward personal liberation, reminding you that positive changes align with your soul's purpose.",
    6: "❤️ Angel number 6 focuses on nurturing, responsibility, and love. It emphasizes balance between material and spiritual aspects, urging care for family and home. This number promotes compassion and service to others, while reminding you to prioritize self-care. Harmony in relationships and domestic matters will bring peace and fulfillment.",
    7: "🔮 The number 7 is linked to introspection, spirituality, and wisdom. It invites deep inner reflection and pursuit of knowledge, often signaling a time for spiritual awakening. Trust your intuition, as 7 indicates that you're on a path of enlightenment. Your angels encourage study and meditation to uncover profound truths.",
    8: "💰 Angel number 8 represents abundance, power, and karma. It signifies material success and financial prosperity through hard work and integrity. This number reminds you of the infinite flow of the universe, encouraging confident leadership. Balance giving and receiving to manifest ongoing rewards.",
    9: "🌍 Number 9 symbolizes compassion, humanitarianism, and completion. It marks the end of cycles, urging forgiveness and service to humanity. Embrace your role as a lightworker, as 9 signals spiritual fulfillment and wisdom gained from experiences. Prepare for new beginnings by releasing the old.",
    11: "✨ As a master number, 11 amplifies intuition, enlightenment, and inspiration. It calls you to align with your higher purpose and spiritual mission. This number enhances sensitivity and creativity, urging you to lead by example. Trust in divine guidance for profound personal growth.",
    22: "🛠️ Master number 22, the 'Master Builder,' represents manifestation, vision, and practicality. It empowers you to turn dreams into reality through disciplined action. This number signifies great potential for global impact, encouraging collaboration and perseverance. Your angels support ambitious goals that benefit others.",
    33: "🙏 Master number 33 embodies healing, guidance, and unconditional love. Known as the 'Master Teacher,' it inspires compassion and spiritual upliftment. This number urges selfless service and creative expression to help humanity. Embrace your role in fostering harmony and enlightenment."
}

# Updated Descriptions for repeating master number groups, expanded till 9999
repeating_groups = {
    "1, 11, 111, 1111": "🌟 The group 1, 11, 111, and 1111 is deeply connected to spiritual awakening and manifestation. Number 1 stands for independence, new beginnings, and leadership, encouraging you to forge your path with confidence. 11, a powerful master number, heightens intuition and enlightenment, serving as a bridge between the physical and spiritual realms. 111 acts as a wakeup call, signaling that your thoughts are rapidly manifesting—focus on positivity to attract desired outcomes. 1111 symbolizes new beginnings and rebirth, signifying the end of one life cycle and the start of another, urging you to embrace transformation and improve your life through bold steps. Together, these numbers remind you of your divine connection and the power to create reality through aligned intentions and actions, trusting in the universe's support for personal growth.",
    "2, 22, 222, 2222": "⚖️ Representing balance and harmony, the sequence 2, 22, 222, and 2222 emphasizes partnerships and trust. 2 promotes diplomacy, cooperation, and adaptability in relationships. Master number 22, the 'Master Builder,' amplifies manifestation and practicality, enabling you to construct lasting foundations. 222 reassures that everything is aligning in divine timing, urging patience and faith. 2222 connects to harmony and peace, indicating good times ahead and the dissipation of conflicts, inspiring self-belief and patience as desires materialize. This group signals angelic support for equilibrium in life, encouraging you to nurture connections and maintain peace amid challenges.",
    "3, 33, 333, 3333": "🎨 Creativity and joy define 3, 33, 333, and 3333. Number 3 sparks self-expression, optimism, and social energy. 33, the 'Master Teacher,' embodies compassion and spiritual guidance, inspiring healing and upliftment. 333 indicates ascended masters are near, boosting your creative endeavors and growth. 3333 serves as a cautionary message to be aware of prejudices and biases, promoting alignment between body, mind, and spirit for authentic living. These numbers collectively invite you to embrace enthusiasm, communicate freely, and trust in divine assistance for personal expansion and conscious awareness.",
    "4, 44, 444, 4444": "🏗️ Stability and protection are core to 4, 44, 444, and 4444. 4 emphasizes hard work, discipline, and building secure bases. 44 amplifies structure and endurance, acting as a power number for manifesting long-term goals. 444 signifies angels surrounding you, offering guidance and reassurance during efforts. 4444 is associated with self-realization and breaking emotional barriers, highlighting intuition and decision-making for personal growth and independence. This set encourages practicality and perseverance, promising success through grounded actions and angelic safeguarding.",
    "5, 55, 555, 5555": "🌪️ Change and freedom characterize 5, 55, 555, and 5555. Number 5 brings adventure, adaptability, and transformation. 55 enhances innovative energy and breaking free from limitations. 555 heralds major shifts, urging embrace of evolution for positive growth. 5555 symbolizes freedom and independent living, encouraging you to release past baggage and embrace a liberated lifestyle filled with autonomy and adventure. Together, they signal exciting transitions, encouraging flexibility and courage to explore new horizons with angelic backing.",
    "6, 66, 666, 6666": "❤️ Nurturing and balance define 6, 66, 666, and 6666. 6 focuses on love, responsibility, and harmony in home life. 66 elevates compassion and healing on a broader scale. 666, contrary to myths, calls for realigning material and spiritual aspects, promoting positive changes. 6666 appears when you need support, reminding you to prioritize self-care and value yourself beyond what you do for others, shifting mindset for better balance. This group reminds you to foster care, address imbalances, and trust in universal support.",
    "7, 77, 777, 7777": "🔮 Wisdom and spirituality shine in 7, 77, 777, and 7777. 7 invites introspection, knowledge-seeking, and inner trust. 77 deepens mystical awareness and philosophical insights. 777 signifies divine alignment and spiritual rewards, indicating enlightenment progress. 7777 is a reminder to re-evaluate your identity and desires, acknowledging personal growth and aligning with what truly fulfills you. These numbers encourage meditation, intuition, and embracing your soul's quest for truth and self-discovery.",
    "8, 88, 888, 8888": "💰 Abundance and power flow through 8, 88, 888, and 8888. 8 represents success, karma, and material mastery. 88 amplifies infinite prosperity and authority. 888 signals financial blessings and karmic balance. 8888 signifies amplified abundance, financial success, and the infinite loop of giving and receiving, urging confident pursuit of goals with integrity. This sequence urges confident pursuit of goals, reminding you of the universe's endless support for achievement and balanced karma.",
    "9, 99, 999, 9999": "🌍 Completion and humanitarianism mark 9, 99, 999, and 9999. 9 symbolizes endings, forgiveness, and service. 99 enhances universal love and enlightenment. 999 indicates cycle closures, preparing for rebirth. 9999 represents ultimate completion, spiritual mastery, and humanitarian efforts, marking the end of major phases and urging selfless service to others. Together, they call for releasing the past, embracing compassion, and fulfilling your lightworker role with wisdom gained from experiences.",
    "10, 1010": "🚀 The pair 10 and 1010 symbolizes positivity and spiritual growth. 10 combines 1's leadership with 0's infinite potential, urging optimism. 1010 signifies new opportunities, personal development, and alignment with higher purpose. This group encourages positive actions, self-improvement, and trusting divine timing for manifestations.",
    "11, 1111": "✨ Master energies in 11 and 1111 focus on intuition and portals. 11 heightens inspiration and spiritual mission. 1111 acts as a gateway to enlightenment, amplifying wishes and synchronicities. These numbers signal awakening, urging alignment with your soul's calling and heightened awareness.",
    "12, 1212": "🙌 Divine support defines 12 and 1212. 12 represents completion and harmony. 1212 encourages stepping beyond comfort zones, gratitude, and openness to new phases. This set reassures angelic guidance for spiritual advancement and balanced pursuits."
}

# Updated Explanations for special clock times, expanded for symmetry and added triple repeating times
clock_meanings = {
    '00:00': "⏰ 00:00, guided by Vehuiah, symbolizes infinite potential and new beginnings 🌌. Numerology of 0 emphasizes unity and cycles. Tarot: The Fool – adventure and trust. It's a call for renewal, trusting intuition, and embracing the unknown with faith. 😇 In love, open to new bonds; in work, take risks; in money, optimism with caution. Meditate to set intentions and align with your higher purpose.",
    '01:01': "⏰ 01:01, with Jeliel, empowers confidence and manifestation 🚀. Numerology of 1 highlights leadership. Tarot: The Magician – skill and action. Urges taking initiative, trusting tools for desires. 🌟 In relationships, express feelings; in career, showcase talents; financially, seize opportunities. Co-create reality with divine guidance.",
    '01:11': "⏰ 01:11 aligns with angel number 111, a wakeup call for manifestation and new beginnings 🌟. Numerology of 111 intensifies leadership and creation, signaling rapid thought manifestation. Tarot: The Magician – willpower and resourcefulness. It reminds you to focus on positivity as changes unfold for your highest good. 😇 In love, embrace fresh starts and open communication; in work, initiate bold projects with confidence; in money, attract abundance through optimistic intentions. Meditate to clarify desires and trust the universe's support for personal transformation and spiritual awakening.",
    '02:02': "⏰ 02:02, under Sitael, seeks harmony and inner peace ⚖️. Numerology of 2 promotes balance. Tarot: The High Priestess – intuition and wisdom. Calls for equilibrium in relationships and decisions. 🌙 Trust your gut in love; listen inwardly at work; patience with money. Connect with inner strength for peace.",
    '02:22': "⏰ 02:22 connects to angel number 222, urging balance, harmony, and partnerships ⚖️. Numerology of 222 emphasizes diplomacy and trust in divine timing. Tarot: The High Priestess – intuition and inner knowledge. It reassures alignment and encourages patience amid challenges. 😇 In love, nurture relationships and seek mutual understanding; in work, foster teamwork for success; in money, maintain equilibrium to attract stability. Reflect on connections, embracing faith that everything is unfolding perfectly with angelic guidance.",
    '03:03': "⏰ 03:03, guarded by Elemiah, sparks creativity and repair 🎨. Numerology of 3 fosters expression. Tarot: The Empress – abundance and nurturing. Signals divine help in mending situations, embracing optimism. 😇 In love, communicate openly; in career, innovate; financially, attract prosperity. Trust ascended masters for growth.",
    '03:33': "⏰ 03:33 resonates with angel number 333, aligning mind, body, and soul for creativity and growth 🎨. Numerology of 333 boosts optimism and self-expression. Tarot: The Empress – nurturing and abundance. Ascended masters are near, supporting your endeavors and spiritual expansion. 😇 In love, express feelings joyfully; in work, unleash innovative ideas; in money, expect fulfilling opportunities. Embrace social connections and enthusiasm, trusting divine assistance to overcome obstacles and manifest positive experiences.",
    '04:04': "⏰ 04:04, with Mahasiah, emphasizes stability and inner peace 🏗️. Numerology of 4 builds foundations. Tarot: The Emperor – structure and authority. Urges grounding and discipline for long-term success. 🌟 In relationships, seek balance; in work, organize efforts; in money, plan wisely. Angels protect your path to achievement.",
    '04:44': "⏰ 04:44 embodies angel number 444, offering protection, stability, and angelic presence 🏗️. Numerology of 444 stresses discipline and solid foundations. Tarot: The Emperor – authority and structure. Angels surround you, guiding your hard work toward security. 😇 In love, build lasting bonds; in work, persevere with focus; in money, invest in reliable plans. Stay grounded, embracing endurance and practicality for long-term achievements and divine reassurance.",
    '05:05': "⏰ 05:05, led by Lelahel, brings light and healing 🌪️. Numerology of 5 signifies change. Tarot: The Hierophant – tradition and guidance. Indicates transformation and recovery, embracing adventure. 😇 In love, adapt; in career, explore new paths; financially, embrace shifts. Trust in personal liberation.",
    '05:55': "⏰ 05:55 signals angel number 555, heralding major change, freedom, and transformation 🌪️. Numerology of 555 amplifies adaptability and adventure. Tarot: The Hierophant – spiritual wisdom and conformity breaking. Prepare for positive shifts that align with your soul's purpose. 😇 In love, welcome evolution in relationships; in work, pursue exciting opportunities; in money, adapt to new prospects. Embrace curiosity and flexibility, trusting angels to support your journey toward liberation and growth.",
    '06:06': "⏰ 06:06, under Achaiah, focuses on patience and understanding ❤️. Numerology of 6 nurtures harmony. Tarot: The Lovers – choices and unions. Calls for balance in home and self-care. 🌍 In relationships, foster compassion; in work, responsibility; in money, equilibrium. Realign material and spiritual aspects.",
    '07:07': "⏰ 07:07, with Cahetel, encourages gratitude and protection 🔮. Numerology of 7 deepens wisdom. Tarot: The Chariot – victory and willpower. Signals spiritual awakening and inner trust. ✨ In love, reflect; in career, pursue knowledge; financially, introspect. Embrace enlightenment and meditation.",
    '08:08': "⏰ 08:08, guarded by Haziel, promises mercy and forgiveness 💰. Numerology of 8 brings abundance. Tarot: Strength – courage and compassion. Indicates karmic balance and success. 😇 In relationships, forgive; in work, lead confidently; in money, manifest prosperity. Infinite flow supports you.",
    '09:09': "⏰ 09:09, with Aladiah, symbolizes grace and renewal 🌍. Numerology of 9 marks completion. Tarot: The Hermit – introspection and guidance. Urges service and letting go. 🌟 In love, forgive; in career, humanitarian efforts; financially, release old. Prepare for new cycles with compassion.",
    '10:10': "⏰ 10:10 promotes spiritual growth and new opportunities. Align with purpose through positive action. 🚀",
    '11:11': "⏰ 11:11 is a powerful portal for awakening and wishes. Heightened synchronicity calls for intentions. 🌌",
    '12:12': "⏰ 12:12 provides divine support for advancement. Find gratitude and openness to new cycles. 🙌",
    '13:13': "⏰ 13:13, under Iezalel, emphasizes fidelity and unity 🌟. Numerology of 13 (4) builds stability. Tarot: Death – transformation and endings. Signals positive changes and loyalty in bonds. 😇 In love, strengthen partnerships; in work, collaborate; financially, ground plans. Embrace renewal with trust.",
    '14:14': "⏰ 14:14, with Mebahel, protects truth and liberation 🏗️. Numerology of 14 (5) invites change. Tarot: Temperance – balance and moderation. Urges harmony and justice in actions. ✨ In relationships, seek equilibrium; in career, adapt; in money, moderate. Divine protection guides your path.",
    '15:15': "⏰ 15:15, guarded by Hariel, purifies and inspires 🎨. Numerology of 15 (6) nurtures love. Tarot: The Devil – materialism and release. Calls for breaking chains and creativity. 🌪️ In love, passion; in work, innovate; financially, balance desires. Spiritual cleansing leads to freedom.",
    '16:16': "⏰ 16:16, with Hekamiah, fosters loyalty and elevation 🔮. Numerology of 16 (7) deepens insight. Tarot: The Tower – sudden change and awakening. Signals breakthroughs and protection. 😇 In relationships, build trust; in career, rise above; in money, rebuild. Embrace sudden enlightenment.",
    '17:17': "⏰ 17:17, under Lauviah, reveals insights and victory ✨. Numerology of 17 (8) brings power. Tarot: The Star – hope and inspiration. Urges intuition and triumph over challenges. 🌟 In love, clarity; in work, succeed; financially, abundance. Divine revelations guide your success.",
    '18:18': "⏰ 18:18, with Caliel, upholds justice and truth 💰. Numerology of 18 (9) completes cycles. Tarot: The Moon – illusion and intuition. Calls for discernment and absolution. 🌙 In relationships, honesty; in career, fairness; in money, resolve. Angels support your quest for truth.",
    '19:19': "⏰ 19:19, guarded by Leuviah, offers expiation and intelligence 🌍. Numerology of 19 (10/1) new starts. Tarot: The Sun – joy and success. Signals forgiveness and wisdom. 😇 In love, heal; in work, innovate; financially, prosper. Embrace light and positive renewal.",
    '20:20': "⏰ 20:20, with Pahaliah, redeems and vocation ⚖️. Numerology of 20 (2) harmony. Tarot: Judgement – rebirth and calling. Urges spiritual purpose and liberation. 🌌 In relationships, balance; in career, align. inspiration.",
    '21:21': "⏰ 21:21, under Nelchael, thirsts for knowledge 🚀. Numerology of 21 (3) creativity. Tarot: The World – completion and fulfillment. Calls for learning and protection. 🎨 In love, express; in work, study; financially, grow. Conquer challenges with wisdom and faith.",
    '22:22': "⏰ 22:22, with Ieiaiel, brings fame and fortune 🛠. Numerology of 22 master builder. Tarot: The Fool – new adventures. Signals recognition and mastery. ✨ In relationships, harmony; in career, achieve; in money, abundance. Angels amplify your building power.",
    '23:23': "⏰ 23:23, guarded by Melahel, heals and protects 🌿. Numerology of 23 (5) change. Tarot: The Magician – manifestation. Urges natural healing and courage. 😇 In love, nurture; in work, transform; financially, adapt. Divine protection aids your evolution."
}

st.title("Angel Number and Special Times Explorer ✨")

st.markdown("""
This app allows you to input your birth date, time, and timezone to calculate your personal angel number (life path number) with a detailed description. It also provides lengthy explanations of repeating master numbers up to 9999, interpretations of special clock times (including symmetrical and repeating patterns), and checks if your birth time matches any special angel times across multiple timezones, displaying them in 12-hour format with relevant meanings if matched.
""")

selected_tz = st.selectbox("Select Birth Timezone (default IST)", options=pytz.common_timezones, index=pytz.common_timezones.index('Asia/Kolkata'))

birth_date = st.date_input("Birth Date 📅")

birth_time = st.time_input("Birth Time ⏱️")

if birth_date and birth_time:
    birth_dt = datetime.datetime(birth_date.year, birth_date.month, birth_date.day, birth_time.hour, birth_time.minute)
    local_tz = pytz.timezone(selected_tz)
    birth_dt_local = local_tz.localize(birth_dt)

    # Calculate angel number
    def reduce_number(n):
        while n > 9 and n not in [11, 22, 33]:
            n = sum(int(d) for d in str(n))
        return n

    month_sum = sum(int(d) for d in str(birth_date.month))
    day_sum = sum(int(d) for d in str(birth_date.day))
    year_sum = sum(int(d) for d in str(birth_date.year))
    total = month_sum + day_sum + year_sum
    angel_num = reduce_number(total)

    st.header(f"Your Angel Number: {angel_num} 🌟")
    st.write(angel_descriptions.get(angel_num, "No description available."))

    # Repeating master numbers
    st.header("Repeating Master Numbers till 9999 📜")
    for group, desc in repeating_groups.items():
        st.subheader(group)
        st.write(desc)

    # Special clock times explanations
    st.header("Explanations Regarding Times Like 1:11, 2:22, etc., Expanded for Symmetry ⏰")
    for time_key, meaning in clock_meanings.items():
        display_time = time_key.lstrip('0') if time_key.startswith('0') else time_key
        st.write(f"**{display_time}**: {meaning}")

    # Birth time across multiple timezones
    st.header("Your Birth Time in Multiple Timezones and Special Matches 🔄")
    timezones_list = ['UTC', 'America/New_York', 'America/Los_Angeles', 'Europe/London', 'Europe/Paris', 'Asia/Tokyo', 'Australia/Sydney', 'Asia/Kolkata']
    special_times = set(clock_meanings.keys())

    for tz in set(timezones_list + [selected_tz]):
        target_tz = pytz.timezone(tz)
        converted_dt = birth_dt_local.astimezone(target_tz)
        conv_time_str = converted_dt.strftime('%H:%M')
        display_time = converted_dt.strftime('%I:%M %p')  # 12-hour format with AM/PM
        is_special = conv_time_str in special_times
        emoji = " ✨ Special Angel Time!" if is_special else ""
        st.write(f"**{tz}**: {display_time}{emoji}")
        if is_special:
            st.write(clock_meanings[conv_time_str])
