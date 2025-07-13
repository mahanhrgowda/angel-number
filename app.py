import streamlit as st
import datetime
import pytz
import time

# Expanded detailed descriptions for angel numbers, synthesized from thorough research
angel_descriptions = {
    1: """
🌟 **Angel Number 1: The Primal Force of New Beginnings and Leadership**

From a spiritual perspective, Angel Number 1 is the foundational essence of creation, symbolizing the primal force from which all other numbers emerge. It represents divine support, new phases of life, and self-actualization, often appearing as a cosmic affirmation that you're on the right path. In numerology, it's associated with independence, leadership, and individuality, embodying an unrelenting drive to achieve goals and venture into undiscovered paths. People aligned with this number possess an innate sense of uniqueness, self-perseverance, and healthy pride, making them natural pioneers who thrive on initiating fresh starts.

**Key Traits and Strengths:** Bold, assertive, goal-oriented, and creative, Number 1 individuals are strong leaders with helpful traits for success in any endeavor. They excel in manifesting their reality through positive thoughts and actions, often moving quickly to the top in careers due to their achievement-oriented nature. Their upright, unbending shape symbolizes resilience and directness, reflecting a personality that's in-your-face yet inspiring. Spiritually, it urges gratitude towards the creator for life's blessings, emphasizing a 'I can do' mindset that attracts abundance and success.

**Weaknesses and Challenges:** However, this rigidity can lead to aggression or combativeness during conflicts, and under pressure, it may break due to a lack of flexibility. There's a risk of an inflated ego, preoccupation with self, and difficulty accepting help, which can hinder relationships and personal growth. Stepping into the shadow side might result in stepping on others or becoming overly self-focused, potentially isolating oneself from collaborative opportunities.

**Life Path and Spiritual Significance:** As a life path number, 1 signifies new beginnings and the start of the numerological cycle, encouraging you to embrace your individuality and take initiative. It's a sign of divine support, especially in moments of vulnerability or when pursuing love and opportunities. Biblically and spiritually, it highlights rewards for hard work, luck, and the importance of self-belief, with recurring sequences like 11, 111, or 1111 indicating big promotions or rapid manifestation of thoughts. When seeing 1 repeatedly, trust yourself and your guides—it's a reminder that fresh opportunities are on the horizon, urging you to step out of your comfort zone with confidence.

**What to Do When Seeing It:** Acknowledge it as a wake-up call to focus on positivity, as your intentions are amplifying. Offer a prayer of gratitude, breathe deeply, and take bold steps toward your goals. Meditate on clarifying desires, trusting the universe's support for transformation and spiritual awakening. In relationships, express feelings openly; in career, initiate projects; financially, seize opportunities to attract abundance.

**Other Insights:** This number holds a special place in numerology as the archetype of creation, often linked to rebirth and stepping-stones in life's journey. It's amplified in master numbers like 11, but as a single digit, it stands alone in its primal power, reminding you that you have the innate ability to co-create your reality with divine guidance.
""",
    2: """
⚖️ **Angel Number 2: The Harmonious Peacemaker and Collaborator**

Spiritually, Angel Number 2 is the epitome of balance, harmony, and unity, often symbolizing a coming together—whether in reunions, new unions, or partnerships. It's the most feminine and underestimated number, embodying gentleness, tact, diplomacy, forgiveness, and understanding. In numerology, it represents collaboration and peacemaking, with a subtle, sensitive nature that acts as a bridge between opposites. Its shape, humble and bowing, reflects resilience and flexibility, allowing it to endure where rigid numbers fail.

**Key Traits and Strengths:** Diplomatic, fair, cooperative, and intuitive, Number 2 individuals crave companionship and excel in group efforts, making them welcomed in negotiations or arguments. They possess a deep inner knowing, promoting adaptability and emotional equilibrium, which helps manifest desires through teamwork. Their cooperative qualities foster peace and mutual respect, often leading to supportive energies that align with divine timing.

**Weaknesses and Challenges:** Hypersensitivity can lead to being easily hurt, and under too much weight, it may struggle, though it bounces back. There's a potential for co-dependency, pushing others away in favor of self-interest, or difficulty balancing personal needs with collective ones, which can strain relationships.

**Life Path and Spiritual Significance:** As a life path, 2 is the path of the peacemaker, moving away from individuality to co-creation for a shared purpose. It urges following instincts over external advice, starting over after mistakes, and using unique abilities to improve life for loved ones. Recurring sequences like 22, 222, or 2222 signal imminent changes, requiring a step of faith for abundance, with angels cheering your belief in guidance. Biblically, it emphasizes forgetting past pains and reforming, highlighting responsibility for initiating positive shifts.

**What to Do When Seeing It:** Take it as a sign of alignment in relationships or decisions, urging patience and trust in the process. Breathe, offer gratitude, and nurture connections while maintaining emotional balance. In love, seek mutual understanding; in work, foster teamwork; financially, attract stability through equilibrium. Reflect on partnerships, embracing faith that everything unfolds perfectly with angelic support.

**Other Insights:** Though underestimated, 2's power lies in its resilience and intuitive understanding, often outlasting others. It's the foundation for master numbers like 22, amplifying manifestation through harmony. Seeing 2s is a reminder you're never alone—the universe supports your journey toward love and camaraderie.
""",
    3: """
🎨 **Angel Number 3: The Creative Expressionist and Optimist**

Angel Number 3 is a beacon of creativity, joy, and self-expression, spiritually signifying trust in your magic, wisdom, and inner strength. It's associated with femininity, intuition, and optimism, often appearing as a sign from ascended masters to embrace growth and communicate openly. In numerology, it's like a gifted, playful teenager—scattered yet magnetic, charming, and artistic, focused on authenticity and spreading joy.

**Key Traits and Strengths:** Sensitive, outgoing, optimistic, and highly creative, Number 3 individuals are social butterflies with artistic talent, excelling in expressive fields. They attract abundance through positive energy, fostering enthusiasm and social connections that lead to fulfilling experiences.

**Weaknesses and Challenges:** Unfocused and disorganized tendencies can make workplace integration difficult, with a propensity for jealousy, living beyond means, or extravagance. It urges patience amid others' blessings, emphasizing perseverance through temporary challenges.

**Life Path and Spiritual Significance:** As a life path, 3 merges energies of 1 and 2, representing imagination, joy, and authentic living. It comforts you not to feel left out, as heavens hear your prayers, urging strength against temptations and a bigger picture to overcome poverty. Sequences like 33, 333, or 3333 boost creative endeavors, cautioning against biases and promoting mind-body-spirit alignment. Biblically significant, it symbolizes utilizing abilities for happiness and prosperity.

**What to Do When Seeing It:** Embrace it as support from ascended masters, expressing yourself freely and trusting divine help. Offer gratitude, communicate openly in love, innovate in career, and attract prosperity financially. Meditate on growth, overcoming obstacles with enthusiasm and optimism.

**Other Insights:** Considered an easy, enjoyable path, 3's creative energy is amplified in master 33, but as a single digit, it invites you to tap into artistic talents and stand clear about your desires, reminding you of your divine connection.
""",
    4: """
🏗️ **Angel Number 4: The Stable Builder and Grounded Foundation**

Spiritually, Angel Number 4 embodies stability, grounding, and divine protection, urging you to build solid foundations and balance life's aspects. It's the most dependable number, reflecting strength, endurance, and responsibility, often a sign angels are nearby offering guidance.

**Key Traits and Strengths:** Dependable, productive, punctual, patient, and detail-oriented, Number 4 individuals have a strong work ethic and organizational skills, making them the 'rock' in families or communities. They excel in structured environments, providing reliability and consistency.

**Weaknesses and Challenges:** Rigidity and resistance to change can lead to workaholic tendencies or imbalance. It emphasizes planning and responsibility, warning against neglecting spiritual development or family.

**Life Path and Spiritual Significance:** As a life path, 4 offers structure, focused on brick-by-brick building and including all aspects like health, relationships, and career for stability. Sequences like 44, 444, or 4444 signify angelic presence, self-realization, and breaking barriers for growth. It relates to having a plan, never giving up, and adding spiritual routines.

**What to Do When Seeing It:** Ground yourself, organize efforts, and plan wisely. In relationships, seek balance; in work, persevere; financially, invest reliably. Offer gratitude, embracing discipline for long-term success and divine reassurance.

**Other Insights:** The most grounded number, 4's stability is amplified in master 22, but as a single, it symbolizes conventional reliability, reminding you of angelic support in building secure bases.
""",
    5: """
🌪️ **Angel Number 5: The Dynamic Adventurer and Transformer**

Angel Number 5 signifies transformation, freedom, and adventure, spiritually heralding major changes and personal liberation. It's the most dynamic number, unpredictable and energetic, molded from masculine and feminine qualities, craving change and new experiences.

**Key Traits and Strengths:** Adventurous, magnetic, witty, and positive, Number 5 individuals thrive on freedom, excelling in dynamic environments and exploration. They draw others with their personality, adapting boldly to shifts.

**Weaknesses and Challenges:** Overindulgence in food, drink, or sex can lead to addiction, misusing freedom and harming others. It urges social expansion for new insights, overcoming fear in decisions.

**Life Path and Spiritual Significance:** As a life path, 5 represents limitless freedom, not for the faint-hearted, focused on experiencing life fully. Sequences like 55, 555, or 5555 signal shifts, encouraging release of baggage for autonomy. It promotes trying new habits and trusting intuition for success.

**What to Do When Seeing It:** Embrace change, adapt in love, explore careers, and welcome financial shifts. Breathe, offer gratitude, and pursue adventures with angelic backing.

**Other Insights:** Its fluid energy suggests movement, amplified in higher forms, reminding you to break patterns for positive evolution.
""",
    6: """
❤️ **Angel Number 6: The Nurturing Caretaker and Harmonizer**

Spiritually, Angel Number 6 is the most harmonious, embodying unconditional love, compassion, and nurturing, often the 'motherhood number.' It urges introspection and balance between material and spiritual, focusing on family and community.

**Key Traits and Strengths:** Loving, caring, responsible, and cool-headed, Number 6 individuals are natural caregivers, thriving in supportive roles and fostering harmony.

**Weaknesses and Challenges:** Too giving can lead to martyrdom, neglecting self-health. It warns of financial imbalances, urging strategy changes and savings.

**Life Path and Spiritual Significance:** As a life path, 6 combines 2 and 4, centered on home, responsibility, and helping others thrive. Sequences like 66, 666, or 6666 call for realignment and self-care. Despite myths, it's about positive changes and compassion.

**What to Do When Seeing It:** Focus internally, foster compassion in relationships, take responsibility at work, and balance finances. Offer gratitude, prioritizing self-care.

**Other Insights:** Its nurturing energy is amplified in master 33, reminding you to value yourself beyond service.
""",
    7: """
🔮 **Angel Number 7: The Introspective Philosopher and Seeker**

Angel Number 7 is the seeker of truth, spiritually signaling awakening and deeper esoteric digging. It's introspective, wise, and philosophical, gravitating toward meditation and spiritual studies.

**Key Traits and Strengths:** Thinker, intuitive, and analytical, Number 7 individuals excel in uncovering hidden truths, stepping into sage roles.

**Weaknesses and Challenges:** Detached demeanor can push others away, struggling with solitude vs. connection. It urges balancing work with personal life.

**Life Path and Spiritual Significance:** As a life path, 7 lets go of material concerns for personal growth, focused on wisdom. Sequences like 77, 777, or 7777 indicate alignment and re-evaluation. It reminds of mortality, urging enjoyment now.

**What to Do When Seeing It:** Reflect, pursue knowledge, and introspect financially. Offer gratitude, embracing meditation for enlightenment.

**Other Insights:** Its depth suggests spiritual quests, amplified in higher forms.
""",
    8: """
💰 **Angel Number 8: The Abundant Authority and Manifestor**

Spiritually, Angel Number 8 represents abundance, karma, and power, signifying cycle ends and letting go for security. It's concerned with material success, authoritative and confident.

**Key Traits and Strengths:** Generous, dependable, courageous, Number 8 individuals excel in business, manifesting through integrity.

**Weaknesses and Challenges:** Greed or power obsession can arise, succumbing to materialism.

**Life Path and Spiritual Significance:** As a life path, 8 steps into influence, focused on tangible achievements. Sequences like 88, 888, or 8888 signal blessings and balance. It urges surrender and trust.

**What to Do When Seeing It:** Let go, lead confidently, manifest prosperity. Offer gratitude for paying off manifestations.

**Other Insights:** Infinite flow reminds of giving-receiving balance.
""",
    9: """
🌍 **Angel Number 9: The Compassionate Humanitarian and Completer**

Angel Number 9 symbolizes completion, forgiveness, and service, spiritually up-leveling through learning and teaching. It's compassionate and humanitarian, marking cycle ends.

**Key Traits and Strengths:** Wise, fulfilling, Number 9 individuals embrace lightworker roles, releasing past for new beginnings.

**Weaknesses and Challenges:** Holding onto old can hinder, but it urges grace and renewal.

**Life Path and Spiritual Significance:** As a life path, 9 prepares for rebirth, focused on enlightenment. Sequences like 99, 999, or 9999 indicate closures and mastery.

**What to Do When Seeing It:** Forgive, serve humanity, release old financially. Offer gratitude for closure.

**Other Insights:** Ultimate completion, urging selfless service.
""",
    11: """
✨ **Master Number 11: The Psychic Intuitive and Enlightener**

As a master number, 11 amplifies intuition, enlightenment, and inspiration, spiritually bridging subconscious and conscious. It's highly sensitive, psychic-like, with universal insight.

**Key Traits and Strengths:** Old soul, healer, intuitive, sharing accrued wisdom.

**Weaknesses and Challenges:** Heavy lessons, sensitivity overload.

**Life Path and Spiritual Significance:** Wake humanity to divine potential, leading by example. Trust guidance for growth.

**What to Do When Seeing It:** Align with purpose, make intentions.

**Other Insights:** Amplified 2, mastered over lifetimes.
""",
    22: """
🛠️ **Master Number 22: The Master Builder and Manifestor**

22 is the most powerful, carrying manifesting energy, spiritually architecting change.

**Key Traits and Strengths:** Productivity master, expert builder, influencing positively.

**Weaknesses and Challenges:** Intense energy, high expectations.

**Life Path and Spiritual Significance:** Create lasting change, turning dreams to reality.

**What to Do When Seeing It:** Collaborate, persevere on goals.

**Other Insights:** Supercharged 4, for global impact.
""",
    33: """
🙏 **Master Number 33: The Enlightened Nurturer and Teacher**

33 embodies unconditional love, spiritually the master teacher, evolved frequency.

**Key Traits and Strengths:** Healer, guide, embodying pure love.

**Weaknesses and Challenges:** Maintaining high energy, heavier lessons.

**Life Path and Spiritual Significance:** Teach love, selfless service.

**What to Do When Seeing It:** Embrace caregiving, foster harmony.

**Other Insights:** Intensified 6, mastered nurturing.
"""
}

repeating_groups = {
    "111": "Angel Number 111: Signifies manifestation, new beginnings, and alignment with your thoughts. Your ideas are coming to fruition. ✨",
    "222": "Angel Number 222: Represents balance, harmony, and faith. Trust that everything is unfolding as it should. ⚖️",
    "333": "Angel Number 333: Indicates creativity, growth, and support from ascended masters. Express yourself freely. 🎨",
    "444": "Angel Number 444: Symbolizes protection, stability, and the presence of angels. You are supported. 🏗️",
    "555": "Angel Number 555: Signifies change, transformation, and adventure. Embrace the shifts coming your way. 🌪️",
    "666": "Angel Number 666: Reminds you to balance your thoughts and focus on spiritual rather than material concerns. ❤️",
    "777": "Angel Number 777: Represents spiritual awakening, divine guidance, and good fortune. 🔮",
    "888": "Angel Number 888: Symbolizes abundance, success, and the flow of karma. 💰",
    "999": "Angel Number 999: Indicates completion, letting go, and humanitarian service. 🌍",
    "1111": "Angel Number 1111: Amplifies spiritual awakening, intuition, and new opportunities. ✨",
    "2222": "Angel Number 2222: Emphasizes harmony, patience, and the manifestation of dreams. ⚖️",
    "3333": "Angel Number 3333: Boosts creativity and self-expression on a larger scale. 🎨",
    "4444": "Angel Number 4444: Represents strong foundations and the rewards of hard work. 🏗️",
    "5555": "Angel Number 5555: Signals major life changes and the need for adaptability. 🌪️",
    "6666": "Angel Number 6666: Focuses on harmony in home and relationships, nurturing. ❤️",
    "7777": "Angel Number 7777: Enhances inner wisdom and mystical experiences. 🔮",
    "8888": "Angel Number 8888: Signifies infinite abundance and personal power. 💰",
    "9999": "Angel Number 9999: Marks the end of a cycle and spiritual enlightenment. 🌍"
}

clock_meanings = {
    '00:00': "Mentally prepare for an absence or loss. Prepares for potential loss or absence. ⏳",
    '01:01': "You feel the need to isolate yourself. Indicates a desire for isolation. 🏞️",
    '01:10': "Someone watches over you with protective love. Suggests protective love from someone. ❤️",
    '01:11': "Manifestation and new beginnings. Align your thoughts positively. 🌟",
    '02:02': "You won't achieve anything on your own. Highlights the need for collaboration. 🤝",
    '02:20': "Luck is definitely on your side. Indicates favorable luck. 🍀",
    '02:22': "Balance and harmony. Trust the process. ⚖️",
    '03:03': "You manage to formulate your ideas accurately. Reflects clarity in expressing ideas. 💡",
    '03:30': "Someone loves you in secret. Suggests hidden affection. 💕",
    '03:33': "Creativity and growth. Support from ascended masters. 🎨",
    '04:04': "Your desire for power may be a sign of a lack of grounding. Warns of lack of grounding. 🌱",
    '04:40': "Will you be remorseful after this betrayal? Questions remorse after betrayal. 😔",
    '04:44': "Protection and stability. Angels are with you. 🏗️",
    '05:05': "Your current creativity is matched only by your thirst for life. Highlights creativity and vitality. 🔥",
    '05:50': "Smile! A pleasant surprise awaits you. Promises a pleasant surprise. 😊",
    '05:55': "Change and transformation. Embrace shifts. 🌪️",
    '06:06': "Your instinct guides you to the right people. Instinct leads to beneficial connections. 🧭",
    '07:07': "Maturity or lucidity? Either way, you change your perspective. Shift in perspective. 🔄",
    '08:08': "Let justice be done! Calls for justice. ⚖️",
    '09:09': "Seek to cultivate yourself to enrich your spiritual life. Encourages spiritual enrichment. 🌿",
    '10:01': "There is still time to catch up with the loved one. Opportunity to reconnect. ⏰",
    '10:10': "You gain confidence and the results are positive for your career. Career success through confidence. 📈",
    '11:11': "Your fierce ambition can take you to the highest peaks. Ambition leads to achievements. 🏔️",
    '12:12': "Wisdom wins you over! You renounce material temptations. Choosing wisdom over material. 🧠",
    '12:21': "Beware! Gossip and betrayals lie in wait for you. Warns of gossip and betrayal. ⚠️",
    '13:13': "A change of cycle is coming. Upcoming life cycle change. 🔄",
    '13:31': "Avoid any new initiatives for now. Advises against new projects. 🚫",
    '14:14': "Things are moving but still lacking stability. Progress with instability. 🏃",
    '14:41': "You have the feeling of having lost an object that is dear to you. Sense of loss. 😞",
    '15:15': "A consuming passion prevents you from seeing clearly. Passion clouding judgment. 🔥",
    '15:51': "Someone loves you, but is it really mutual? Questions mutuality of love. ❓",
    '16:16': "Your pride pushes you to isolate yourself. Pride leads to isolation. 🏞️",
    '17:17': "An overflowing creative energy animates you. High creative energy. 🎨",
    '18:18': "You are more sensitive to the secrets of the soul and the vagaries of fate. Heightened sensitivity. 🔮",
    '19:19': "Patience will bring you success. Encourages patience. ⏳",
    '20:02': "You are about to receive good news. Good news incoming. 📩",
    '20:20': "Balance in relationships. Harmony in partnerships. ❤️",
    '21:12': "Success is near, but be cautious. Caution in success. ⚠️",
    '21:21': "Achievement and fulfillment. Goals being met. 🏆",
    '22:22': "Great ambitions realized. Master builder energy. 🛠️",
    '23:23': "End of a phase, new beginning. Completion. 🌅",
    '23:32': "Spiritual guidance is strong. Trust your intuition. 🙏"
}

st.title("Angel Number and Special Times Explorer ✨")

st.markdown("""
This app allows you to input your birth date, time, and timezone to calculate your personal angel number (life path number) with a detailed description. It also provides lengthy explanations of repeating master numbers up to 9999, interpretations of special clock times (including symmetrical and repeating patterns), and checks if your birth time matches any special angel times across multiple timezones, displaying them in 12-hour format with relevant meanings if matched. 🌟⏰
""")

mode = st.selectbox("Mode", ["Birth", "Real Time"], index=0)

selected_tz = st.selectbox("Select Timezone (default IST) 🌍", options=pytz.common_timezones, index=pytz.common_timezones.index('Asia/Kolkata'))

local_tz = pytz.timezone(selected_tz)

if mode == "Birth":
    birth_date = st.date_input("Birth Date 📅", min_value=datetime.date(1900, 1, 1), max_value=datetime.date(2100, 12, 31))
    birth_time = st.time_input("Birth Time ⏱️", step=60)
    if birth_date and birth_time:
        dt = datetime.datetime(birth_date.year, birth_date.month, birth_date.day, birth_time.hour, birth_time.minute)
        dt_local = local_tz.localize(dt)
        # Calculate angel number from date
        def reduce_number(n):
            while n > 9 and n not in [11, 22, 33]:
                n = sum(int(d) for d in str(n))
            return n
        month_sum = sum(int(d) for d in str(birth_date.month))
        day_sum = sum(int(d) for d in str(birth_date.day))
        year_sum = sum(int(d) for d in str(birth_date.year))
        total = month_sum + day_sum + year_sum
        angel_num_date = reduce_number(total)
        st.header(f"Your Angel Number from Birth Date: {angel_num_date} 🌟")
        st.write(angel_descriptions.get(angel_num_date, "No description available."))
        # Angelic numerology for birth time
        hour_sum = sum(int(d) for d in str(birth_time.hour))
        min_sum = sum(int(d) for d in str(birth_time.minute))
        total_time = hour_sum + min_sum
        angel_num_time = reduce_number(total_time)
        st.header(f"Your Angel Number from Birth Time: {angel_num_time} ⏰")
        st.write(angel_descriptions.get(angel_num_time, "No description available."))
else:
    if st.button("Refresh 🔄"):
        st.rerun()
    now = datetime.datetime.now(local_tz)
    dt_local = now
    st.write(f"Current time in {selected_tz}: {now.strftime('%I:%M %p')} ⏰")
    st.info("In Real Time mode, angel numbers are calculated based on the current date and time. 📌")
    # Calculate angel number from current date
    def reduce_number(n):
        while n > 9 and n not in [11, 22, 33]:
            n = sum(int(d) for d in str(n))
        return n
    month_sum = sum(int(d) for d in str(now.month))
    day_sum = sum(int(d) for d in str(now.day))
    year_sum = sum(int(d) for d in str(now.year))
    total = month_sum + day_sum + year_sum
    angel_num_date = reduce_number(total)
    st.header(f"Angel Number from Current Date: {angel_num_date} 🌟")
    st.write(angel_descriptions.get(angel_num_date, "No description available."))
    # Angelic numerology for current time
    hour_sum = sum(int(d) for d in str(now.hour))
    min_sum = sum(int(d) for d in str(now.minute))
    total_time = hour_sum + min_sum
    angel_num_time = reduce_number(total_time)
    st.header(f"Angel Number from Current Time: {angel_num_time} ⏰")
    st.write(angel_descriptions.get(angel_num_time, "No description available."))

# Collapsible sections using st.expander
with st.expander("Repeating Master Numbers till 9999 📜"):
    for group, desc in repeating_groups.items():
        st.subheader(group)
        st.write(desc)

with st.expander("Explanations Regarding Times Like 1:11, 2:22, etc., Expanded for Symmetry ⏰"):
    for time_key, meaning in clock_meanings.items():
        display_time = time_key.lstrip('0') if time_key.startswith('0') else time_key
        st.write(f"**{display_time}**: {meaning}")

with st.expander("Time in Multiple Timezones and Special Matches 🔄"):
    timezones_list = ['UTC', 'America/New_York', 'America/Los_Angeles', 'Europe/London', 'Europe/Paris', 'Asia/Tokyo', 'Australia/Sydney', 'Asia/Kolkata']
    special_times = set(clock_meanings.keys())
    for tz in set(timezones_list + [selected_tz]):
        target_tz = pytz.timezone(tz)
        converted_dt = dt_local.astimezone(target_tz)
        conv_time_str = converted_dt.strftime('%H:%M')
        display_time = converted_dt.strftime('%I:%M %p')
        is_special = conv_time_str in special_times
        emoji = " ✨ Special Angel Time!" if is_special else ""
        st.write(f"**{tz}**: {display_time}{emoji}")
        if is_special:
            st.write(clock_meanings[conv_time_str])

if mode == "Real Time":
    time.sleep(60)
    st.rerun()
