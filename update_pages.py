import os
import re

def update_pc():
    with open('information.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Title & TOC
    content = content.replace(
        '<h1 class="text-6xl md:text-8xl font-bold">烤披薩活動</h1>\n                <p class="text-3xl md:text-4xl font-light mt-4">行前說明</p>',
        '<h1 class="text-6xl md:text-8xl font-bold">04期中露營</h1>\n                <p class="text-3xl md:text-4xl font-light mt-4">行前說明</p>'
    )
    content = content.replace(
        '<div class="toc-item p-4 rounded-lg card-bg" onclick="goToSlide(8)">07 行程安排 (Day 2)</div>\n                </div>',
        '<div class="toc-item p-4 rounded-lg card-bg" onclick="goToSlide(8)">07 行程安排 (Day 2)</div>\n                    <div class="toc-item p-4 rounded-lg card-bg" onclick="goToSlide(9)">08 行程安排 (Day 3)</div>\n                </div>'
    )

    # 2. Basic Info
    content = content.replace(
        '<p>2026/03/28 (六) 14:00 - 03/29 (日) 13:00</p>',
        '<p>2026/05/01 (五) 14:00 - 05/03 (日) 11:00</p>'
    )
    content = content.replace(
        '<p>師大林口校區校門口</p>\n                        <p class="text-lg opacity-50">新北市林口區仁愛路一段 2 號</p>',
        '<p>三芝老農夫農場</p>\n                        <p class="text-lg opacity-50">新北市三芝區芝蘭路62之5號</p>'
    )

    # 3. Cost
    content = content.replace(
        '<p class="text-8xl font-bold">200</p>\n                    <p class="text-xl mt-4 opacity-70 font-bold">（由社團補貼）</p>',
        '<p class="text-8xl font-bold">1,300</p>\n                    <p class="text-xl mt-4 opacity-70 font-bold">（原價 1,500，社團補助 200）</p>'
    )

    # 4. Transport
    content = content.replace(
        '<p>捷運圓山站 2 號出口集合</p>\n                        <p>搭乘 <span class="highlight-blue">936 號公車</span></p>\n                        <p class="text-lg mt-2 opacity-50">直達師大林口校區 (約 20 分鐘一班)</p>',
        '<p>捷運淡水站或紅樹林站</p>\n                        <p>搭乘 <span class="highlight-blue">863 或 861 公車</span></p>\n                        <p class="text-lg mt-2 opacity-50">至「芝蘭入口」站後步行約9分鐘</p>'
    )
    content = content.replace(
        '<p>請導航至師大林口校區校門口</p>',
        '<p>請導航至三芝老農夫農場</p>'
    )
    content = re.sub(
        r'<iframe\s+src="https://www\.google\.com/maps/embed.*?".*?</iframe>',
        '<iframe src="https://maps.google.com/maps?q=三芝老農夫農場&t=&z=13&ie=UTF8&iwloc=&output=embed" width="100%" height="350" style="border:0; display: block; margin: 1rem auto; max-width: 56rem; border-radius: 1rem;" allowfullscreen="" loading="lazy"></iframe>',
        content,
        flags=re.DOTALL
    )

    # 5. Packing list
    old_packing = '''                    <tbody>
                        <tr>
                            <td>拖鞋</td>
                            <td>換洗衣物</td>
                            <td>沐浴用品</td>
                        </tr>
                        <tr>
                            <td>毛巾</td>
                            <td><span class="highlight-blue">餐具 (碗筷杯子)</span></td>
                            <td>充電用品</td>
                        </tr>
                        <tr>
                            <td>* 枕頭</td>
                            <td>* 睡袋/墊</td>
                            <td><span class="warning-tag">牙刷、牙膏</span></td>
                        </tr>
                        <tr>
                            <td>個人藥品</td>
                            <td>衛生紙</td>
                            <td></td>
                        </tr>
                    </tbody>'''
    new_packing = '''                    <tbody>
                        <tr>
                            <td>拖鞋 / 換洗衣物</td>
                            <td>沐浴用品 / 毛巾</td>
                            <td><span class="highlight-blue">餐具 (碗筷杯子)</span></td>
                        </tr>
                        <tr>
                            <td>充電用品 / 藥品</td>
                            <td>* 枕頭 / * 睡袋</td>
                            <td><span class="warning-tag">牙刷、牙膏</span></td>
                        </tr>
                        <tr>
                            <td>衛生紙</td>
                            <td><span class="highlight-blue">泳具</span></td>
                            <td>防蚊液</td>
                        </tr>
                        <tr>
                            <td>雨具</td>
                            <td>* 頭燈</td>
                            <td></td>
                        </tr>
                    </tbody>'''
    content = content.replace(old_packing, new_packing)
    content = content.replace(
        '<p>※ <span class="highlight-blue">餐具</span> 請務必自備，響應環保。</p>',
        '<p>※ <span class="highlight-blue">餐具</span> 請務必自備，響應環保。</p>\n                    <p>※ 附近海邊可戲水，攜帶 <span class="highlight-blue">泳具</span> 請注意安全。</p>'
    )

    # 6. Notes
    old_notes = '''                    <div class="flex items-start gap-4 p-4 card-bg rounded-xl border-l-4 border-red-500">
                        <p>第一天 <span class="warning-tag">中午不供餐</span>，建議吃飽後再前往集合。</p>
                    </div>
                    <div class="flex items-start gap-4 p-4 card-bg rounded-xl border-l-4 border-red-500">
                        <p>烤披薩用的食材請 <span class="warning-tag">自行準備</span> 並確保能吃完 (約 0.5~1 人份)。</p>
                    </div>
                    <div class="flex items-start gap-4 p-4 card-bg rounded-xl border-l-4 border-red-500">
                        <p>住宿地點 <span class="warning-tag">僅有一間浴室</span>，請大家儘早開始輪流洗澡。</p>
                    </div>'''
    new_notes = '''                    <div class="flex items-start gap-4 p-4 card-bg rounded-xl border-l-4 border-red-500">
                        <p>第一天 <span class="warning-tag">中午不供餐</span>，建議吃完午餐再前往集合。</p>
                    </div>
                    <div class="flex items-start gap-4 p-4 card-bg rounded-xl border-l-4 border-blue-500">
                        <p>附近海邊可以戲水，攜帶泳具請 <span class="highlight-blue">注意安全</span>。</p>
                    </div>
                    <div class="flex items-start gap-4 p-4 card-bg rounded-xl border-l-4 border-yellow-500">
                        <p>請留意天氣準備防蚊液與雨具，夜晚氣溫可能較低。</p>
                    </div>'''
    content = content.replace(old_notes, new_notes)

    # 7. Schedule
    old_day1 = '''                <div class="space-y-3 content-text card-bg p-8 rounded-2xl">
                    <p><strong>14:00 - 14:10</strong> 集合到 Patty 小屋</p>
                    <p><strong>14:10 - 14:40</strong> 參觀設備</p>
                    <p><strong>14:40 - 16:00</strong> 活動時間</p>
                    <p><strong>16:00 - 19:30</strong> <span class="highlight-blue">Pizza Time!</span> (動手做披薩)</p>
                    <p><strong>19:30 - 20:30</strong> 晚間活動</p>
                    <p><strong>20:30 - 21:00</strong> 梳洗就寢</p>
                    <p class="italic opacity-40">21:00 之後：i 珍食時光</p>
                </div>'''
    new_day1 = '''                <div class="space-y-3 content-text card-bg p-8 rounded-2xl">
                    <p><strong>14:00 - 14:10</strong> 集合</p>
                    <p><strong>14:10 - 15:40</strong> 搭建帳篷</p>
                    <p><strong>15:40 - 17:00</strong> 活動時間</p>
                    <p><strong>17:00 - 18:30</strong> 準備晚餐</p>
                    <p><strong>18:30 - 20:30</strong> 晚間活動</p>
                    <p><strong>20:30 - 21:00</strong> 梳洗就寢</p>
                    <p class="italic opacity-40">21:00 之後：i 珍食</p>
                </div>'''
    content = content.replace(old_day1, new_day1)

    old_day2 = '''<!-- 9. 行程安排 (Day 2) -->
        <div class="slide" style="transform: translateX(800%);">
            <div class="content-box">
                <h2 class="slide-title">行程表 (Day 2)</h2>
                <div class="space-y-8 content-text">
                    <div class="card-bg p-8 rounded-2xl">
                        <p><strong>08:00 - 10:00</strong> 林口在地早餐</p>
                        <p><strong>10:00 - 11:30</strong> 晨間閱讀時間</p>
                        <p class="font-bold text-white text-2xl mt-8">13:00 快樂回家</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- 10. 結尾 -->
        <div class="slide" style="transform: translateX(900%);">
            <div class="text-center">
                <h1 class="text-7xl md:text-9xl font-bold">開心地烤吧</h1>
                <p class="text-3xl md:text-4xl mt-8 opacity-40 italic">Pizza Party @ Linkou</p>'''

    new_day2_3_end = '''<!-- 9. 行程安排 (Day 2) -->
        <div class="slide" style="transform: translateX(800%);">
            <div class="content-box">
                <h2 class="slide-title">行程表 (Day 2)</h2>
                <div class="space-y-3 content-text card-bg p-8 rounded-2xl">
                    <p><strong>08:00 - 10:00</strong> 早餐</p>
                    <p><strong>10:00 - 11:30</strong> 晨間閱讀</p>
                    <p><strong>11:30 - 13:30</strong> 午餐時間</p>
                    <p><strong>13:30 - 17:30</strong> 海邊走走</p>
                    <p><strong>17:30 - 19:30</strong> 晚餐時間</p>
                    <p><strong>19:30 - 20:30</strong> 晚間活動</p>
                    <p><strong>20:30 - 21:00</strong> 梳洗就寢</p>
                    <p class="italic opacity-40">21:00 之後：友膳時光</p>
                </div>
            </div>
        </div>

        <!-- 10. 行程安排 (Day 3) -->
        <div class="slide" style="transform: translateX(900%);">
            <div class="content-box">
                <h2 class="slide-title">行程表 (Day 3)</h2>
                <div class="space-y-8 content-text">
                    <div class="card-bg p-8 rounded-2xl">
                        <p><strong>08:00 - 10:00</strong> 起床用膳</p>
                        <p><strong>10:00 - 11:30</strong> 場復收拾</p>
                        <p class="font-bold text-white text-2xl mt-8">11:30 快樂回家</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- 11. 結尾 -->
        <div class="slide" style="transform: translateX(1000%);">
            <div class="text-center">
                <h1 class="text-7xl md:text-9xl font-bold">盡情享受吧</h1>
                <p class="text-3xl md:text-4xl mt-8 opacity-40 italic">Camping @ Sanzhi</p>'''
    content = content.replace(old_day2, new_day2_3_end)

    # 8. Counter
    content = content.replace('<div id="slide-counter">1 / 10</div>', '<div id="slide-counter">1 / 11</div>')

    with open('information.html', 'w', encoding='utf-8') as f:
        f.write(content)

def update_mobile():
    with open('information_phone.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Title & TOC
    content = content.replace(
        '<h1 class="text-8xl font-black mb-10 leading-tight">烤披薩活動</h1>',
        '<h1 class="text-8xl font-black mb-10 leading-tight">04期中露營</h1>'
    )
    content = content.replace(
        '<div class="toc-item card-bg" onclick="goToSlide(7)">06 行程</div>',
        '<div class="toc-item card-bg" onclick="goToSlide(7)">06 行程</div>\n                <div class="toc-item card-bg" onclick="goToSlide(8)">07 Day 3</div>'
    )

    # 2. Basic Info
    content = content.replace('03/28 (六) 14:00', '05/01 (五) 14:00')
    content = content.replace('03/29 (日) 13:00', '05/03 (日) 11:00')
    content = content.replace('師大林口校區', '三芝老農夫農場')
    content = content.replace('新北市林口區仁愛路一段 2 號', '新北市三芝區芝蘭路62之5號')

    # 3. Cost
    content = content.replace(
        '<span class="text-[12rem] font-black leading-none">200</span>',
        '<span class="text-[10rem] font-black leading-none">1,300</span>'
    )
    content = content.replace(
        '社團經費已全額補貼',
        '原價 1,500，社團補助 200'
    )

    # 4. Transport
    content = content.replace('BUS 936', 'BUS 861/863')
    content = content.replace('圓山站 2 號出口', '捷運淡水/紅樹林')
    content = content.replace('直達校門口，班次約 20 分鐘', '至「芝蘭入口」站後步行 9 分鐘')
    content = content.replace('導航「校門口」', '導航「農場」')
    content = content.replace('國立臺灣師範大學林口校區', '三芝老農夫農場')
    content = content.replace('啟動導航至師大林口校區', '啟動導航至三芝老農夫農場')

    # 5. Packing list
    old_packing = '''                            <tr>
                                <td>🩴 拖鞋</td>
                                <td>👕 換衣</td>
                                <td>🧼 沐浴</td>
                            </tr>
                            <tr>
                                <td>🧣 毛巾</td>
                                <td><span class="highlight-blue">🍽️ 餐具</span></td>
                                <td>🔋 充電</td>
                            </tr>
                            <tr>
                                <td>☁️ 枕頭*</td>
                                <td>⛺ 睡墊*</td>
                                <td><span class="warning-tag">🪥 牙刷膏</span></td>
                            </tr>
                            <tr>
                                <td>💊 藥品</td>
                                <td>🧻 衛生紙</td>
                                <td></td>
                            </tr>'''
    new_packing = '''                            <tr>
                                <td>👕 換衣/拖</td>
                                <td>🧼 沐浴/巾</td>
                                <td><span class="highlight-blue">🍽️ 餐具</span></td>
                            </tr>
                            <tr>
                                <td>🔋 充電/藥</td>
                                <td>⛺ 睡墊枕*</td>
                                <td><span class="warning-tag">🪥 牙刷膏</span></td>
                            </tr>
                            <tr>
                                <td>🧻 衛生紙</td>
                                <td><span class="highlight-blue">🩱 泳具</span></td>
                                <td>🦟 防蚊液</td>
                            </tr>
                            <tr>
                                <td>☂️ 雨具</td>
                                <td>🔦 頭燈*</td>
                                <td></td>
                            </tr>'''
    content = content.replace(old_packing, new_packing)
    content = content.replace(
        '餐具為必備，請落實環境保護。',
        '餐具為必備。海邊戲水攜帶泳具請注意安全。'
    )

    # 6. Notes
    old_notes = '''                <div class="card-bg border-l-[16px] border-yellow-500 mb-10 py-10">
                    <p class="text-4xl font-black">🍅 披薩食材請自備</p>
                    <p class="opacity-60 text-2xl mt-4">一人份為限以免造成浪費</p>
                </div>
                <div class="card-bg border-l-[16px] border-blue-500 py-10">
                    <p class="text-4xl font-black">🚿 僅有一間浴室</p>
                    <p class="opacity-60 text-2xl mt-4">請配合幹部安排時間輪流</p>
                </div>'''
    new_notes = '''                <div class="card-bg border-l-[16px] border-blue-500 mb-10 py-10">
                    <p class="text-4xl font-black">🌊 注意戲水安全</p>
                    <p class="opacity-60 text-2xl mt-4">附近海邊戲水請確保自身安全</p>
                </div>
                <div class="card-bg border-l-[16px] border-green-500 py-10">
                    <p class="text-4xl font-black">🦟 防蚊與保暖</p>
                    <p class="opacity-60 text-2xl mt-4">留意氣候準備防蚊液與雨具</p>
                </div>'''
    content = content.replace(old_notes, new_notes)

    # 7. Schedule
    old_schedule = '''        <!-- 8. 行程安排 (Day 1) - 新增回補 -->
        <div class="slide" style="transform: translateX(700%);">
            <h2 class="slide-title">第一天行程</h2>
            <div class="content-box" style="margin-bottom:1rem">
                <div class="card-bg space-y-8 py-10">
                    <div class="flex justify-between text-3xl font-black"><span>14:00</span> <span>小屋集合</span></div>
                    <div class="flex justify-between text-3xl"><span>14:40</span> <span class="opacity-70">設備參觀</span>
                    </div>
                    <div class="flex justify-between text-3xl text-blue-400 font-black"><span>16:00</span> <span>Pizza
                            Time! 🍕</span></div>
                    <div class="flex justify-between text-3xl"><span>19:30</span> <span class="opacity-70">晚間活動</span>
                    </div>
                    <div class="flex justify-between text-3xl"><span>20:30</span> <span class="opacity-70">盥洗就寢</span>
                    </div>
                    <div class="flex justify-between text-3xl"><span>21:00</span> <span class="opacity-70">i 珍食時間</span>
                    </div>
                </div>
            </div>

            <h2 class="slide-title">第二天行程</h2>
            <div class="content-box">
                <div class="card-bg text-center space-y-12 py-20">
                    <div class="flex justify-between text-3xl font-black"><span>08:00</span> <span>林口在地早餐</span></div>
                    <div class="flex justify-between text-3xl"><span>10:00</span> <span class="opacity-70">晨間靜心閱讀</span>
                    </div>
                    <div class="flex justify-between text-3xl"><span>13:00</span> <span class="opacity-70">快樂踏上歸途</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- 9. 結尾 -->
        <div class="slide" style="transform: translateX(900%);">
            <div class="text-center">
                <h1 class="text-9xl font-black mb-14 leading-none">Pizza Time</h1>
                <p class="text-4xl opacity-60 italic mb-20">烤出屬於我們的驚喜</p>'''
    
    new_schedule = '''        <!-- 8. 行程安排 (Day 1) - 新增回補 -->
        <div class="slide" style="transform: translateX(700%);">
            <h2 class="slide-title">第一天行程</h2>
            <div class="content-box" style="margin-bottom:1rem">
                <div class="card-bg space-y-6 py-6">
                    <div class="flex justify-between text-3xl font-black"><span>14:00</span> <span>集合</span></div>
                    <div class="flex justify-between text-3xl"><span>14:10</span> <span class="opacity-70">搭建帳篷</span></div>
                    <div class="flex justify-between text-3xl text-blue-400 font-black"><span>15:40</span> <span>活動時間</span></div>
                    <div class="flex justify-between text-3xl"><span>17:00</span> <span class="opacity-70">準備晚餐</span></div>
                    <div class="flex justify-between text-3xl"><span>18:30</span> <span class="opacity-70">晚間活動</span></div>
                    <div class="flex justify-between text-3xl"><span>20:30</span> <span class="opacity-70">梳洗就寢</span></div>
                </div>
            </div>

            <h2 class="slide-title">第二天行程</h2>
            <div class="content-box">
                <div class="card-bg space-y-6 py-6">
                    <div class="flex justify-between text-3xl font-black"><span>08:00</span> <span>早餐</span></div>
                    <div class="flex justify-between text-3xl"><span>10:00</span> <span class="opacity-70">晨間閱讀</span></div>
                    <div class="flex justify-between text-3xl"><span>11:30</span> <span class="opacity-70">午餐時間</span></div>
                    <div class="flex justify-between text-3xl text-blue-400 font-black"><span>13:30</span> <span>海邊走走 🌊</span></div>
                    <div class="flex justify-between text-3xl"><span>17:30</span> <span class="opacity-70">晚餐時間</span></div>
                    <div class="flex justify-between text-3xl"><span>19:30</span> <span class="opacity-70">晚間活動</span></div>
                </div>
            </div>
        </div>

        <!-- 9. 行程安排 (Day 3) -->
        <div class="slide" style="transform: translateX(800%);">
            <h2 class="slide-title">第三天行程</h2>
            <div class="content-box">
                <div class="card-bg text-center space-y-12 py-20">
                    <div class="flex justify-between text-3xl font-black"><span>08:00</span> <span>起床用膳</span></div>
                    <div class="flex justify-between text-3xl"><span>10:00</span> <span class="opacity-70">場復收拾</span></div>
                    <div class="flex justify-between text-3xl text-blue-400 font-black"><span>11:30</span> <span>快樂回家</span></div>
                </div>
            </div>
        </div>

        <!-- 10. 結尾 -->
        <div class="slide" style="transform: translateX(900%);">
            <div class="text-center">
                <h1 class="text-9xl font-black mb-14 leading-none">Camping</h1>
                <p class="text-4xl opacity-60 italic mb-20">享受大自然的美好</p>'''
    content = content.replace(old_schedule, new_schedule)

    # 8. Counter
    content = content.replace('<div id="slide-counter">01 / 10</div>', '<div id="slide-counter">01 / 11</div>')

    with open('information_phone.html', 'w', encoding='utf-8') as f:
        f.write(content)

update_pc()
update_mobile()
print("Updated successfully")
