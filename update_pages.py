import os
import shutil

def update_index():
    print("正在更新 index.html...")
    shutil.copy('backup_original/index_backup.html', 'index.html')
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 調整漸層與色彩（藍色系 -> 黃綠色系）
    content = content.replace(
        "background: radial-gradient(circle at center, #153c5e 0%, #092338 100%);",
        "background: radial-gradient(circle at center, #113521 0%, #081a10 100%);"
    )
    content = content.replace(
        "border-top-color: #60a5fa;",
        "border-top-color: #c3fa36; /* 螢光黃綠色 */"
    )
    content = content.replace(
        "border-right-color: #60a5fa;",
        "border-right-color: #c3fa36;"
    )
    content = content.replace(
        "box-shadow: 0 0 15px rgba(96, 165, 250, 0.4);",
        "box-shadow: 0 0 15px rgba(195, 250, 54, 0.4);"
    )
    content = content.replace(
        "border-top-color: #93c5fd;",
        "border-top-color: #52b788; /* 葉綠色 */"
    )
    content = content.replace(
        "border-left-color: #93c5fd;",
        "border-left-color: #52b788;"
    )
    content = content.replace(
        "box-shadow: 0 0 10px rgba(147, 197, 253, 0.3);",
        "box-shadow: 0 0 10px rgba(82, 183, 136, 0.3);"
    )
    content = content.replace(
        "background: linear-gradient(to right, #ffffff, #93c5fd);",
        "background: linear-gradient(to right, #ffffff, #c3fa36);"
    )
    content = content.replace(
        "filter: drop-shadow(0 0 2px rgba(147, 197, 253, 0));",
        "filter: drop-shadow(0 0 2px rgba(195, 250, 54, 0));"
    )
    content = content.replace(
        "filter: drop-shadow(0 0 8px rgba(147, 197, 253, 0.6));",
        "filter: drop-shadow(0 0 8px rgba(195, 250, 54, 0.6));"
    )

    # 2. 插入載入畫面螢火蟲 CSS & HTML
    firefly_css = """
        /* 簡單的載入畫面螢火蟲 */
        .loading-firefly {
            position: absolute;
            width: 5px;
            height: 5px;
            background: #c3fa36;
            border-radius: 50%;
            box-shadow: 0 0 10px #c3fa36, 0 0 20px #adff2f;
            opacity: 0;
            animation: lf-float infinite ease-in-out;
            pointer-events: none;
        }
        .loading-firefly:nth-child(1) { left: 15%; top: 75%; animation: lf-float 10s infinite; }
        .loading-firefly:nth-child(2) { left: 80%; top: 25%; animation: lf-float 12s infinite 1s; }
        .loading-firefly:nth-child(3) { left: 45%; top: 85%; animation: lf-float 8s infinite 2s; }
        .loading-firefly:nth-child(4) { left: 85%; top: 70%; animation: lf-float 14s infinite 0.5s; }

        @keyframes lf-float {
            0%, 100% { transform: translate(0, 0); opacity: 0; }
            30% { opacity: 0.8; }
            60% { transform: translate(3vw, -8vh); opacity: 0.2; }
            80% { opacity: 0.7; }
        }
    """
    content = content.replace(
        "        /* 現代感雙環發光旋轉器 */",
        firefly_css + "\n        /* 現代感雙環發光旋轉器 */"
    )
    content = content.replace(
        '<div id="loading-screen">',
        '<div id="loading-screen">\n        <div class="loading-firefly"></div>\n        <div class="loading-firefly"></div>\n        <div class="loading-firefly"></div>\n        <div class="loading-firefly"></div>'
    )

    # 3. 實作 iframe 載入的版本控制
    content = content.replace(
        "            // 2. 決定要讀取的檔案名稱\n            var targetPage = (mode === 'pc') ? 'information.html' : 'information_phone.html';",
        "            const VERSION = '1.0.1';\n            // 2. 決定要讀取的檔案名稱\n            var targetPage = (mode === 'pc') ? 'information.html' : 'information_phone.html';\n            targetPage += '?v=' + VERSION;"
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

def get_shared_css():
    return """
        body {
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
            color: #efeee1;
            overflow: hidden;
            margin: 0;
            background-color: #08120e;
        }

        #slides-container {
            width: 100%;
            height: 100vh;
            position: relative;
            overflow: hidden;
            z-index: 5;
        }

        /* 🌲 田園夜色背景容器 */
        #bg-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            background: linear-gradient(135deg, #0b132b 0%, #0d2818 50%, #153a22 100%);
            transition: filter 0.8s cubic-bezier(0.25, 0.8, 0.25, 1), brightness 0.8s cubic-bezier(0.25, 0.8, 0.25, 1);
            overflow: hidden;
        }

        /* 景深模糊效果 */
        .bg-blurred {
            filter: blur(6px) brightness(0.85);
        }

        /* ✨ 閃爍星空 */
        #bg-container::before {
            content: '';
            position: absolute;
            width: 200%;
            height: 200%;
            top: -50%;
            left: -50%;
            background-image: 
                radial-gradient(1.5px 1.5px at 20px 30px, #fff, rgba(0,0,0,0)),
                radial-gradient(2px 2px at 40px 70px, #fff, rgba(0,0,0,0)),
                radial-gradient(1px 1px at 50px 160px, #fff, rgba(0,0,0,0)),
                radial-gradient(2px 2px at 80px 120px, #c3fa36, rgba(0,0,0,0)),
                radial-gradient(1.5px 1.5px at 110px 220px, #fff, rgba(0,0,0,0)),
                radial-gradient(2px 2px at 150px 180px, #fff, rgba(0,0,0,0));
            background-repeat: repeat;
            background-size: 250px 250px;
            opacity: 0.4;
            animation: star-glow 4s ease-in-out infinite alternate;
        }

        @keyframes star-glow {
            0% { opacity: 0.3; transform: scale(1); }
            100% { opacity: 0.6; transform: scale(1.02); }
        }

        /* 🌾 隨風擺動稻穗作物 */
        .crops-container {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 18vh;
            pointer-events: none;
            display: flex;
            align-items: flex-end;
            z-index: 2;
        }

        .crops-svg {
            width: 100%;
            height: 100%;
        }

        .crop-back {
            fill: #061c0f;
            transform-origin: bottom center;
            animation: sway-back 6s ease-in-out infinite alternate;
        }

        .crop-front {
            fill: #082d18;
            transform-origin: bottom center;
            animation: sway-front 8s ease-in-out infinite alternate;
        }

        @keyframes sway-back {
            0% { transform: rotate(-1.5deg) skewX(-1deg); }
            100% { transform: rotate(2deg) skewX(1deg); }
        }

        @keyframes sway-front {
            0% { transform: rotate(1.5deg) skewX(1deg); }
            100% { transform: rotate(-2.5deg) skewX(-1.5deg); }
        }
    """

def get_shared_html_bg(mobile=False):
    fireflies = ""
    num_fireflies = 4 if mobile else 7
    for _ in range(num_fireflies):
        fireflies += '        <div class="firefly"></div>\n'
        
    crops_height = "12vh" if mobile else "18vh"
    
    return f"""
    <div id="bg-container">
        <!-- 螢火蟲 -->
{fireflies}        <!-- 隨風擺動稻穗 -->
        <div class="crops-container" style="height: {crops_height};">
            <svg viewBox="0 0 1200 120" preserveAspectRatio="none" class="crops-svg">
                <!-- 後層作物 (較深/暗綠) -->
                <path class="crop-back" d="
                    M 0,120 L 0,110 
                    Q 20,40 10,10 Q 30,50 40,110
                    Q 60,30 50,5 Q 75,45 80,112
                    Q 110,35 95,0 Q 120,40 130,115
                    Q 155,50 145,20 Q 170,55 180,110
                    Q 210,40 190,8 Q 215,45 225,113
                    Q 250,30 240,5 Q 265,40 270,115
                    Q 300,50 290,15 Q 315,55 320,110
                    Q 345,35 335,0 Q 360,40 370,112
                    Q 395,45 385,10 Q 410,50 420,114
                    Q 445,30 435,5 Q 460,40 470,110
                    Q 495,50 485,20 Q 510,55 520,115
                    Q 545,35 535,0 Q 560,40 570,113
                    Q 595,45 585,10 Q 610,50 620,110
                    Q 645,30 635,5 Q 660,40 670,114
                    Q 695,50 685,20 Q 710,55 720,111
                    Q 745,35 735,0 Q 760,40 770,115
                    Q 795,45 785,10 Q 810,50 820,112
                    Q 845,30 835,5 Q 860,40 870,110
                    Q 895,50 885,20 Q 910,55 920,114
                    Q 945,35 935,0 Q 960,40 970,111
                    Q 995,45 985,10 Q 1010,50 1020,115
                    Q 1045,30 1035,5 Q 1060,40 1070,113
                    Q 1095,50 1085,20 Q 1110,55 1120,110
                    Q 1145,35 1135,0 Q 1160,40 1170,115
                    Q 1195,45 1185,10 L 1200,110 L 1200,120 Z" />
                <!-- 前層作物 (較亮綠) -->
                <path class="crop-front" d="
                    M 0,120 L 0,115
                    Q 30,55 20,20 Q 40,65 50,115
                    Q 80,45 70,15 Q 90,55 100,112
                    Q 130,60 120,30 Q 140,70 150,114
                    Q 180,50 170,20 Q 190,60 200,111
                    Q 230,55 220,25 Q 240,65 250,115
                    Q 280,45 270,10 Q 290,55 300,113
                    Q 330,60 320,30 Q 340,70 350,110
                    Q 380,50 370,15 Q 390,60 400,114
                    Q 430,55 420,25 Q 440,65 450,112
                    Q 480,45 470,10 Q 490,55 500,115
                    Q 530,60 520,30 Q 540,70 550,113
                    Q 580,50 570,20 Q 590,60 600,111
                    Q 630,55 620,25 Q 640,65 650,115
                    Q 680,45 670,10 Q 690,55 700,112
                    Q 730,60 720,30 Q 740,70 750,114
                    Q 780,50 770,15 Q 790,60 800,110
                    Q 830,55 820,25 Q 840,65 850,113
                    Q 880,45 870,10 Q 890,55 900,115
                    Q 930,60 920,30 Q 940,70 950,112
                    Q 980,50 970,20 Q 990,60 1000,114
                    Q 1030,55 1020,25 Q 1040,65 1050,111
                    Q 1080,45 1070,10 Q 1090,55 1100,115
                    Q 1130,60 1120,30 Q 1140,70 1150,113
                    Q 1180,50 1170,15 Q 1190,60 1200,115 L 1200,120 Z" />
            </svg>
        </div>
    </div>
"""

def update_pc():
    print("正在更新 PC 版 information.html...")
    shutil.copy('backup_original/information_backup.html', 'information.html')
    with open('information.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 替換原有 CSS 樣式為田園星空、稻穗與螢火蟲樣式
    old_css_block = """        body {
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
            background-color: #092338;
            color: #efeee1;
            overflow: hidden;
            margin: 0;
        }

        #slides-container {
            width: 100%;
            height: 100vh;
            position: relative;
            overflow: hidden;
        }

        .slide {
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0;
            left: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 3rem;
            box-sizing: border-box;
            background-color: #092338;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            line-height: 1.6;
        }"""
    
    new_css_block = get_shared_css() + """
        .slide {
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0;
            left: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 3rem;
            box-sizing: border-box;
            background: transparent;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            line-height: 1.6;
        }
        
        .firefly {
            position: absolute;
            width: 6px;
            height: 6px;
            background: #c3fa36;
            border-radius: 50%;
            box-shadow: 0 0 10px #c3fa36, 0 0 20px #9ef01a;
            opacity: 0;
            pointer-events: none;
        }

        .firefly:nth-child(1) { left: 12%; top: 78%; animation: float-1 14s infinite ease-in-out; }
        .firefly:nth-child(2) { left: 28%; top: 65%; animation: float-2 18s infinite ease-in-out 2s; }
        .firefly:nth-child(3) { left: 47%; top: 82%; animation: float-3 16s infinite ease-in-out 1s; }
        .firefly:nth-child(4) { left: 63%; top: 72%; animation: float-4 15s infinite ease-in-out 3s; }
        .firefly:nth-child(5) { left: 79%; top: 85%; animation: float-5 20s infinite ease-in-out 0.5s; }
        .firefly:nth-child(6) { left: 91%; top: 68%; animation: float-6 17s infinite ease-in-out 4s; }
        .firefly:nth-child(7) { left: 35%; top: 88%; animation: float-7 13s infinite ease-in-out 1.5s; }

        @keyframes float-1 {
            0%, 100% { transform: translate(0, 0) scale(0.8); opacity: 0; }
            20% { opacity: 0.8; }
            50% { transform: translate(6vw, -12vh) scale(1.1); opacity: 0.3; }
            80% { opacity: 0.9; }
        }
        @keyframes float-2 {
            0%, 100% { transform: translate(0, 0) scale(1); opacity: 0; }
            30% { opacity: 0.9; }
            60% { transform: translate(-8vw, -18vh) scale(0.7); opacity: 0.2; }
            85% { opacity: 0.8; }
        }
        @keyframes float-3 {
            0%, 100% { transform: translate(0, 0) scale(0.9); opacity: 0; }
            25% { opacity: 0.7; }
            55% { transform: translate(8vw, -15vh) scale(1.2); opacity: 0.4; }
            75% { opacity: 0.8; }
        }
        @keyframes float-4 {
            0%, 100% { transform: translate(0, 0) scale(1.1); opacity: 0; }
            40% { opacity: 0.9; }
            70% { transform: translate(-5vw, -10vh) scale(0.8); opacity: 0.3; }
            90% { opacity: 0.7; }
        }
        @keyframes float-5 {
            0%, 100% { transform: translate(0, 0) scale(0.7); opacity: 0; }
            15% { opacity: 0.8; }
            45% { transform: translate(10vw, -20vh) scale(1); opacity: 0.2; }
            80% { opacity: 0.9; }
        }
        @keyframes float-6 {
            0%, 100% { transform: translate(0, 0) scale(1); opacity: 0; }
            35% { opacity: 0.7; }
            65% { transform: translate(-7vw, -14vh) scale(0.9); opacity: 0.3; }
            85% { opacity: 0.8; }
        }
        @keyframes float-7 {
            0%, 100% { transform: translate(0, 0) scale(0.8); opacity: 0; }
            20% { opacity: 0.9; }
            50% { transform: translate(4vw, -16vh) scale(1.1); opacity: 0.2; }
            80% { opacity: 0.8; }
        }
    """
    content = content.replace(old_css_block, new_css_block)

    # 2. 插入背景 HTML 結構
    content = content.replace('<body>', '<body>\n' + get_shared_html_bg(mobile=False))

    # 3. 實作 PC 動態背景模糊
    old_update = """        function update() {
            slides.forEach((s, i) => {
                s.style.transform = `translateX(${(i - current) * 100}%)`;
            });
            prevBtn.disabled = current === 0;
            nextBtn.disabled = current === slides.length - 1;
            // 同步寬字距 01 格式
            counter.innerText = `${(current + 1).toString().padStart(2, '0')} / ${(slides.length).toString().padStart(2, '0')}`;
        }"""
    
    new_update = """        function update() {
            slides.forEach((s, i) => {
                s.style.transform = `translateX(${(i - current) * 100}%)`;
            });
            prevBtn.disabled = current === 0;
            nextBtn.disabled = current === slides.length - 1;
            counter.innerText = `${(current + 1).toString().padStart(2, '0')} / ${(slides.length).toString().padStart(2, '0')}`;
            
            // 背景動態模糊與亮度調整
            const bgContainer = document.getElementById('bg-container');
            if (bgContainer) {
                if (current === 0) {
                    bgContainer.classList.remove('bg-blurred');
                } else {
                    bgContainer.classList.add('bg-blurred');
                }
            }
        }"""
    content = content.replace(old_update, new_update)

    # 4. 更新 PC 版投影片的文字資料 (05期末包棟)
    content = content.replace(
        '<div class="w-40 h-2.5 bg-blue-400 mx-auto mb-12"></div>\n                <h2 class="text-3xl opacity-60 tracking-[0.6em] mb-8 font-bold">NTNU CAMPING CLUB</h2>\n                <h1 class="text-8xl md:text-[8rem] font-black mb-10 leading-tight">海邊的露營</h1>',
        '<div class="w-40 h-2.5 bg-lime-400 mx-auto mb-12 animate-pulse"></div>\n                <h2 class="text-3xl opacity-60 tracking-[0.6em] mb-8 font-bold text-lime-300">NTNU CAMPING CLUB</h2>\n                <h1 class="text-8xl md:text-[8rem] font-black mb-10 leading-tight">期末包棟</h1>'
    )
    content = content.replace('<div class="toc-item p-6 rounded-2xl card-bg" onclick="goToSlide(8)">07 Day 3</div>', '')
    content = content.replace('05/01 (五) 14:00', '06/29 (一) 14:00')
    content = content.replace('05/03 (日) 11:00', '07/01 (三) 13:00')
    content = content.replace('三芝老農夫農場', '歸巢民宿Villa')
    content = content.replace('新北市三芝區芝蘭路62之5號', '宜蘭縣礁溪鄉二龍村砂港路77號')
    
    # 費用更新為社員/非社員
    old_cost = """                <div class="flex flex-col items-center justify-center py-20 card-bg text-center rounded-3xl">
                    <p class="text-3xl opacity-60 mb-6 font-bold">每一位社員僅需</p>
                    <div class="flex items-baseline">
                        <span class="text-6xl mr-4 font-bold">$</span>
                        <span class="text-[10rem] font-black leading-none">1,300</span>
                    </div>
                    <div class="mt-12 px-10 py-4 bg-blue-500/40 text-blue-200 rounded-full font-black text-2xl">
                        原價 1,500，社團補助 200
                    </div>
                </div>"""
    
    new_cost = """                <div class="flex flex-col items-center justify-center py-14 card-bg text-center rounded-3xl">
                    <p class="text-3xl opacity-60 mb-8 font-bold">本期費用規劃</p>
                    <div class="w-full max-w-lg flex flex-col gap-6 mb-8">
                        <div class="flex items-center justify-between border-b border-white/10 pb-4">
                            <span class="text-3xl font-bold opacity-80">社員</span>
                            <span class="text-5xl font-black text-lime-400">$ 2,000</span>
                        </div>
                        <div class="flex items-center justify-between border-b border-white/10 pb-4">
                            <span class="text-3xl font-bold opacity-80">非社員</span>
                            <span class="text-5xl font-black text-yellow-300">$ 2,200</span>
                        </div>
                    </div>
                    <div class="px-8 py-3 bg-lime-500/20 text-lime-300 rounded-full font-bold text-lg">
                        暫定多退少補，已加一成設備維護費用
                    </div>
                </div>"""
    content = content.replace(old_cost, new_cost)

    # 交通與大眾交通更新
    old_transport = """                    <div class="card-bg p-10 rounded-3xl flex flex-col justify-center">
                        <p class="font-black text-xl text-blue-400 mb-2 uppercase tracking-widest">BUS 861/863</p>
                        <p class="text-3xl font-black mb-4">捷運淡水或紅樹林站</p>
                        <p class="text-xl opacity-60">搭乘 861 或 863 公車<br>至「芝蘭入口」站後步行約 9 分鐘</p>

                        <div class="h-1 bg-white/10 my-8"></div>

                        <p class="font-black text-xl text-blue-400 mb-2 uppercase tracking-widest">MOTORCYCLE</p>
                        <p class="text-3xl font-black">直接導航「校門口」</p>
                    </div>
                    <iframe class="card-bg rounded-3xl w-full h-full min-h-[400px]"
                        src="https://maps.google.com/maps?q=三芝老農夫農場&t=&z=13&ie=UTF8&iwloc=&output=embed"
                        style="border:0;" allowfullscreen="" loading="lazy">
                    </iframe>"""
                    
    new_transport = """                    <div class="card-bg p-10 rounded-3xl flex flex-col justify-center border-l-[8px] border-lime-400">
                        <p class="font-black text-xl text-lime-400 mb-2 uppercase tracking-widest">1. 大眾交通</p>
                        <p class="text-3xl font-black mb-4">台北車站大廳（一樓黑白格）</p>
                        <p class="text-xl opacity-80 leading-relaxed mb-4">
                            11:50~12:00 集合一同出發礁溪（選擇性參加）<br>
                            地圖連結：<a href="https://www.google.com/maps/dir/%E5%8F%B0%E5%8C%9F%E8%BB%8A%E7%AB%99/%E7%A4%81%E6%BA%AA%E8%BB%8A%E7%AB%99" target="_blank" class="text-lime-300 underline font-bold">北車往礁溪</a>
                        </p>

                        <div class="h-1 bg-white/10 my-6"></div>

                        <p class="font-black text-xl text-lime-400 mb-2 uppercase tracking-widest">2. 自行騎車</p>
                        <p class="text-2xl font-black mb-1">要吃午餐 (12:30)：礁溪站</p>
                        <p class="text-2xl font-black">直接到民宿 (15:00後)：歸巢民宿Villa</p>
                    </div>
                    <iframe class="card-bg rounded-3xl w-full h-full min-h-[400px]"
                        src="https://maps.google.com/maps?q=宜蘭縣礁溪鄉二龍村砂港路77號&t=&z=13&ie=UTF8&iwloc=&output=embed"
                        style="border:0;" allowfullscreen="" loading="lazy">
                    </iframe>"""
    content = content.replace(old_transport, new_transport)

    # 準備物品清單更新
    old_packing_body = """                            <tr>
                                <td>👕 換洗衣物/拖鞋</td>
                                <td>🧼 沐浴用品/毛巾</td>
                                <td><span class="highlight-blue">🍽️ 餐具</span></td>
                            </tr>
                            <tr>
                                <td>🔋 充電用品/藥品</td>
                                <td>⛺ 睡袋/墊/枕頭*</td>
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
                            </tr>"""
    
    new_packing_body = """                            <tr>
                                <td>🪥 牙刷、牙膏</td>
                                <td>👕 換洗衣物</td>
                                <td>🧼 *沐浴用品</td>
                            </tr>
                            <tr>
                                <td>🧣 *毛巾</td>
                                <td>🍽️ *餐具</td>
                                <td>🔋 充電用品</td>
                            </tr>
                            <tr>
                                <td>☂️ 雨具</td>
                                <td>🩴 *拖鞋</td>
                                <td>🧻 衛生紙</td>
                            </tr>
                            <tr>
                                <td>💊 個人藥品</td>
                                <td>🩱 *游泳用品</td>
                                <td></td>
                            </tr>"""
    content = content.replace(old_packing_body, new_packing_body)
    
    old_packing_note = """                <div class="card-bg p-6 rounded-2xl bg-blue-900/30 text-lg opacity-80 font-bold">
                    <p class="mb-2">※ "*" 表示非必要，可用其他物品（如被子、衣物）替代。</p>
                    <p class="mb-2">※ <span class="highlight-blue">餐具</span> 請務必自備，響應環保。</p>
                    <p>※ 附近海邊可戲水，攜帶 <span class="highlight-blue">泳具</span> 請注意安全。</p>
                </div>"""
                
    new_packing_note = """                <div class="card-bg p-6 rounded-2xl bg-emerald-900/30 text-lg opacity-90 font-bold border-l-4 border-emerald-400">
                    <p class="mb-2">※ <span class="text-lime-300">"*" 表示非必要項目</span>：毛巾、沐浴用品、拖鞋等可依個人習慣準備。</p>
                    <p class="mb-2">※ <span class="text-lime-300">餐具</span>：習慣使用環保筷子/湯匙的社員可自備。</p>
                    <p>※ 第二天有 <span class="text-lime-300">海邊行程</span>，請視個人需求準備游泳用品，並務必注意安全。</p>
                </div>"""
    content = content.replace(old_packing_note, new_packing_note)

    # 注意事項更新
    old_notes = """                    <div class="card-bg border-l-[12px] border-red-500 p-8 rounded-2xl">
                        <p class="text-3xl font-black mb-2">🍱 第一天中午不供餐</p>
                        <p class="opacity-60 text-xl">請在出發集合前先行用餐，以免下午肚子餓。</p>
                    </div>
                    <div class="card-bg border-l-[12px] border-blue-500 p-8 rounded-2xl">
                        <p class="text-3xl font-black mb-2">🌊 注意戲水安全</p>
                        <p class="opacity-60 text-xl">附近海邊戲水請確保自身安全。</p>
                    </div>
                    <div class="card-bg border-l-[12px] border-green-500 p-8 rounded-2xl">
                        <p class="text-3xl font-black mb-2">🦟 防蚊與保暖</p>
                        <p class="opacity-60 text-xl">留意氣候準備防蚊液與雨具，夜晚氣溫可能較低。</p>
                    </div>"""
                    
    new_notes = """                    <div class="card-bg border-l-[12px] border-red-500 p-8 rounded-2xl">
                        <p class="text-3xl font-black mb-2 text-red-400">🍱 第一天午餐與食材</p>
                        <p class="opacity-80 text-xl">12:30~13:30 為午餐時間，14:05 全聯礁溪店集合購買晚餐與活動食材。</p>
                    </div>
                    <div class="card-bg border-l-[12px] border-lime-500 p-8 rounded-2xl">
                        <p class="text-3xl font-black mb-2 text-lime-400">🌊 注意戲水安全</p>
                        <p class="opacity-80 text-xl">第二天海邊活動時，請務必聽從指揮，注意自身安全。</p>
                    </div>
                    <div class="card-bg border-l-[12px] border-emerald-500 p-8 rounded-2xl">
                        <p class="text-3xl font-black mb-2 text-emerald-400">🦟 攜帶個人毛巾與拖鞋</p>
                        <p class="opacity-80 text-xl">民宿倡導環保，若介意衛生可自備個人毛巾。拖鞋可視活動穿戴。</p>
                    </div>"""
    content = content.replace(old_notes, new_notes)

    # 行程表更新
    old_schedules = """        <div class="slide" style="transform: translateX(700%);">
            <div class="content-box">
                <h2 class="slide-title" style="margin-bottom: 2rem;">行程安排</h2>

                <div class="flex flex-col gap-6">
                    <div class="card-bg p-8 rounded-3xl flex items-center gap-8">
                        <div class="w-1/3 border-r-2 border-white/10 pr-6">
                            <h3 class="text-4xl font-black text-blue-400 mb-2">Day 1</h3>
                            <p class="text-xl opacity-60">05/01 (五)</p>
                        </div>
                        <div class="w-2/3 space-y-3 content-text text-xl pr-4">
                            <div class="flex justify-between"><span class="font-black">14:00</span> <span
                                    class="opacity-80">集合</span></div>
                            <div class="flex justify-between"><span class="font-black">14:10</span> <span
                                    class="opacity-80">搭建帳篷</span></div>
                            <div class="flex justify-between text-blue-400 font-black text-2xl py-1"><span>15:40</span>
                                <span>活動時間</span>
                            </div>
                            <div class="flex justify-between"><span class="font-black">17:00</span> <span
                                    class="opacity-80">準備晚餐</span></div>
                            <div class="flex justify-between"><span class="font-black">18:30</span> <span
                                    class="opacity-80">晚間活動</span></div>
                            <div class="flex justify-between"><span class="font-black">20:30</span> <span
                                    class="opacity-80">梳洗就寢</span></div>
                        </div>
                    </div>

                    <div class="card-bg p-8 rounded-3xl flex items-center gap-8">
                        <div class="w-1/3 border-r-2 border-white/10 pr-6">
                            <h3 class="text-4xl font-black text-blue-400 mb-2">Day 2</h3>
                            <p class="text-xl opacity-60">05/02 (六)</p>
                        </div>
                        <div class="w-2/3 space-y-3 content-text text-xl pr-4">
                            <div class="flex justify-between"><span class="font-black">08:00</span> <span
                                    class="opacity-80">早餐</span></div>
                            <div class="flex justify-between"><span class="font-black">10:00</span> <span
                                    class="opacity-80">晨間閱讀</span></div>
                            <div class="flex justify-between"><span class="font-black">11:30</span> <span
                                    class="opacity-80">午餐時間</span></div>
                            <div class="flex justify-between text-blue-400 font-black text-2xl py-1"><span>13:30</span>
                                <span>海邊走走 🌊</span>
                            </div>
                            <div class="flex justify-between"><span class="font-black">17:30</span> <span
                                    class="opacity-80">晚餐時間</span></div>
                            <div class="flex justify-between"><span class="font-black">19:30</span> <span
                                    class="opacity-80">晚間活動</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 行程安排 (Day 3) -->
        <div class="slide" style="transform: translateX(800%);">
            <div class="content-box">
                <h2 class="slide-title" style="margin-bottom: 2rem;">行程安排 (Day 3)</h2>

                <div class="flex flex-col gap-6">
                    <div class="card-bg p-8 rounded-3xl flex items-center gap-8">
                        <div class="w-1/3 border-r-2 border-white/10 pr-6">
                            <h3 class="text-4xl font-black text-blue-400 mb-2">Day 3</h3>
                            <p class="text-xl opacity-60">05/03 (日)</p>
                        </div>
                        <div class="w-2/3 space-y-3 content-text text-xl pr-4">
                            <div class="flex justify-between"><span class="font-black">08:00</span> <span
                                    class="opacity-80">起床用膳</span></div>
                            <div class="flex justify-between"><span class="font-black">10:00</span> <span
                                    class="opacity-80">場復收拾</span></div>
                            <div class="flex justify-between text-red-400 font-black text-2xl py-1"><span>11:30</span>
                                <span>快樂回家 🚌</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""
        
    new_schedules = """        <div class="slide" style="transform: translateX(700%);">
            <div class="content-box">
                <h2 class="slide-title" style="margin-bottom: 2rem;">行程安排</h2>

                <div class="flex flex-col gap-6">
                    <!-- Day 1 -->
                    <div class="card-bg p-6 rounded-3xl flex items-center gap-8 border-l-[8px] border-lime-400">
                        <div class="w-1/4 border-r-2 border-white/10 pr-6">
                            <h3 class="text-4xl font-black text-lime-300 mb-2">Day 1</h3>
                            <p class="text-xl opacity-60">06/29 (一)</p>
                        </div>
                        <div class="w-3/4 grid grid-cols-2 gap-x-8 gap-y-1 content-text text-lg pr-4">
                            <div class="flex justify-between"><span class="font-black">11:50-12:00</span> <span class="opacity-80">火車站集合</span></div>
                            <div class="flex justify-between"><span class="font-black">15:05-18:00</span> <span class="opacity-80">活動時間</span></div>
                            <div class="flex justify-between"><span class="font-black">12:00-13:30</span> <span class="opacity-80">出發礁溪 (選)</span></div>
                            <div class="flex justify-between"><span class="font-black">18:00-18:45</span> <span class="opacity-80">前往羅東夜市</span></div>
                            <div class="flex justify-between"><span class="font-black">12:30-13:30</span> <span class="opacity-80">午餐時間</span></div>
                            <div class="flex justify-between"><span class="font-black">18:45-20:00</span> <span class="opacity-80 text-lime-300 font-bold">夜市晚餐</span></div>
                            <div class="flex justify-between"><span class="font-black">14:05-14:50</span> <span class="opacity-80">採買食材 (全聯)</span></div>
                            <div class="flex justify-between"><span class="font-black">20:00-20:45</span> <span class="opacity-80">回到民宿</span></div>
                            <div class="flex justify-between"><span class="font-black">14:50-15:05</span> <span class="opacity-80">前往民宿</span></div>
                            <div class="flex justify-between"><span class="font-black">20:45~</span> <span class="opacity-80 text-lime-300 font-bold">晚間活動</span></div>
                        </div>
                    </div>

                    <!-- Day 2 -->
                    <div class="card-bg p-6 rounded-3xl flex items-center gap-8 border-l-[8px] border-emerald-400">
                        <div class="w-1/4 border-r-2 border-white/10 pr-6">
                            <h3 class="text-4xl font-black text-emerald-300 mb-2">Day 2</h3>
                            <p class="text-xl opacity-60">06/30 (二)</p>
                        </div>
                        <div class="w-3/4 space-y-1 content-text text-lg pr-4">
                            <div class="flex justify-between"><span class="font-black">08:00 - 10:00</span> <span class="opacity-80">早餐 ＋ 健康操 🤸</span></div>
                            <div class="flex justify-between"><span class="font-black">10:00 - 11:30</span> <span class="opacity-80">晨間閱讀 📖</span></div>
                            <div class="flex justify-between"><span class="font-black">11:30 - 13:30</span> <span class="opacity-80">午餐時間 🍱</span></div>
                            <div class="flex justify-between text-lime-300 font-black py-0.5"><span>13:30 - 17:30</span> <span>海邊走走 / 戲水 🌊</span></div>
                            <div class="flex justify-between"><span class="font-black">17:30 - 19:30</span> <span class="opacity-80">晚餐時間 🍽️</span></div>
                            <div class="flex justify-between"><span class="font-black">19:30 ~</span> <span class="opacity-80">晚間活動 💬</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 行程安排 (Day 3) -->
        <div class="slide" style="transform: translateX(800%);">
            <div class="content-box">
                <h2 class="slide-title" style="margin-bottom: 2rem;">行程安排 (Day 3)</h2>

                <div class="flex flex-col gap-6">
                    <div class="card-bg p-8 rounded-3xl flex items-center gap-8 border-l-[8px] border-yellow-400">
                        <div class="w-1/3 border-r-2 border-white/10 pr-6">
                            <h3 class="text-4xl font-black text-yellow-300 mb-2">Day 3</h3>
                            <p class="text-xl opacity-60">07/01 (三)</p>
                        </div>
                        <div class="w-2/3 space-y-3 content-text text-xl pr-4">
                            <div class="flex justify-between"><span class="font-black">08:00 - 10:00</span> <span class="opacity-80">起床用膳 🍳</span></div>
                            <div class="flex justify-between"><span class="font-black">10:00 - 10:30</span> <span class="opacity-80">場復收拾 🧹</span></div>
                            <div class="flex justify-between text-lime-300 font-black text-2xl py-1"><span>10:30 ~</span> <span>快樂回家 🚌</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""
    content = content.replace(old_schedules, new_schedules)

    # 結尾笑話與色彩更換
    content = content.replace(
        '<h1 class="text-[6rem] md:text-[8rem] font-black mb-6 leading-none text-blue-400">Camping Time</h1>',
        '<h1 class="text-[6rem] md:text-[8rem] font-black mb-6 leading-none text-lime-300">Enjoy the Villa</h1>'
    )
    content = content.replace('<p class="text-3xl md:text-4xl opacity-60 italic mb-8">享受大自然的美好</p>', '<p class="text-3xl md:text-4xl opacity-60 italic mb-8">期末包棟，好好放鬆一下！</p>')
    content = content.replace('border-blue-400', 'border-lime-400')
    content = content.replace('text-blue-400', 'text-lime-300')
    content = content.replace('text-blue-300', 'text-lime-200')

    with open('information.html', 'w', encoding='utf-8') as f:
        f.write(content)

def update_mobile():
    print("正在更新手機版 information_phone.html...")
    shutil.copy('backup_original/information_phone_backup.html', 'information_phone.html')
    with open('information_phone.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS 樣式更換為田園星空、稻穗與螢火蟲樣式
    old_css_block = """    body {
        font-family: 'Inter', 'Noto Sans TC', sans-serif;
        background-color: #092338;
        color: #efeee1;
        overflow: hidden;
        margin: 0;
        touch-action: pan-y pinch-zoom;
    }

    #slides-container {
        width: 100%;
        height: 100vh;
        position: relative;
        overflow: hidden;
    }

    .slide {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 1rem 0.5rem 6.5rem 0.5rem;
        box-sizing: border-box;
        background-color: #092338;
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        line-height: 1.3;
    }"""
    
    new_css_block = """    body {
        font-family: 'Inter', 'Noto Sans TC', sans-serif;
        color: #efeee1;
        overflow: hidden;
        margin: 0;
        touch-action: pan-y pinch-zoom;
        background-color: #08120e;
    }

    #slides-container {
        width: 100%;
        height: 100vh;
        position: relative;
        overflow: hidden;
        z-index: 5;
    }

    .slide {
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        left: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 1rem 0.5rem 6.5rem 0.5rem;
        box-sizing: border-box;
        background: transparent;
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        line-height: 1.3;
    }""" + get_shared_css().replace("width: 100%;\n            height: 18vh;", "width: 100%;\n            height: 12vh;") + """
    /* 🌟 螢火蟲 (行動端輕量化) */
    .firefly {
        position: absolute;
        width: 5px;
        height: 5px;
        background: #c3fa36;
        border-radius: 50%;
        box-shadow: 0 0 8px #c3fa36, 0 0 16px #9ef01a;
        opacity: 0;
        pointer-events: none;
    }

    .firefly:nth-child(1) { left: 15%; top: 80%; animation: float-1 12s infinite ease-in-out; }
    .firefly:nth-child(2) { left: 45%; top: 72%; animation: float-3 15s infinite ease-in-out 1s; }
    .firefly:nth-child(3) { left: 75%; top: 82%; animation: float-5 16s infinite ease-in-out 0.5s; }
    .firefly:nth-child(4) { left: 88%; top: 70%; animation: float-6 14s infinite ease-in-out 2s; }

    @keyframes float-1 {
        0%, 100% { transform: translate(0, 0) scale(0.8); opacity: 0; }
        20% { opacity: 0.8; }
        50% { transform: translate(6vw, -12vh) scale(1.1); opacity: 0.3; }
        80% { opacity: 0.9; }
    }
    @keyframes float-3 {
        0%, 100% { transform: translate(0, 0) scale(0.9); opacity: 0; }
        25% { opacity: 0.7; }
        55% { transform: translate(8vw, -15vh) scale(1.2); opacity: 0.4; }
        75% { opacity: 0.8; }
    }
    @keyframes float-5 {
        0%, 100% { transform: translate(0, 0) scale(0.7); opacity: 0; }
        15% { opacity: 0.8; }
        45% { transform: translate(10vw, -20vh) scale(1); opacity: 0.2; }
        80% { opacity: 0.9; }
    }
    @keyframes float-6 {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0; }
        35% { opacity: 0.7; }
        65% { transform: translate(-7vw, -14vh) scale(0.9); opacity: 0.3; }
        85% { opacity: 0.8; }
    }"""
    content = content.replace(old_css_block, new_css_block)

    # 2. 插入背景 HTML 結構
    content = content.replace('<body>', '<body>\n' + get_shared_html_bg(mobile=True))

    # 3. 實作手機版動態背景模糊
    old_update = """    function update() {
        slides.forEach((s, i) => {
            s.style.transform = `translateX(${(i - current) * 100}%)`;
        });
        prevBtn.disabled = current === 0;
        nextBtn.disabled = current === slides.length - 1;
        counter.innerText = `${(current + 1).toString().padStart(2, '0')} / ${slides.length}`;
    }"""
    
    new_update = """    function update() {
        slides.forEach((s, i) => {
            s.style.transform = `translateX(${(i - current) * 100}%)`;
        });
        prevBtn.disabled = current === 0;
        nextBtn.disabled = current === slides.length - 1;
        counter.innerText = `${(current + 1).toString().padStart(2, '0')} / ${slides.length}`;
        
        // 背景動態模糊與亮度調整
        const bgContainer = document.getElementById('bg-container');
        if (bgContainer) {
            if (current === 0) {
                bgContainer.classList.remove('bg-blurred');
            } else {
                bgContainer.classList.add('bg-blurred');
            }
        }
    }"""
    content = content.replace(old_update, new_update)

    # 4. 更新手機版投影片文字 (05期末包棟)
    content = content.replace(
        '<div class="w-40 h-2.5 bg-blue-400 mx-auto mb-16"></div>\n            <h2 class="text-2xl opacity-60 tracking-[0.6em] mb-8">NTNU CAMPING CLUB</h2>\n            <h1 class="text-8xl font-black mb-10 leading-tight">海邊的露營</h1>',
        '<div class="w-40 h-2.5 bg-lime-400 mx-auto mb-16 animate-pulse"></div>\n            <h2 class="text-2xl opacity-60 tracking-[0.6em] mb-8 text-lime-300">NTNU CAMPING CLUB</h2>\n            <h1 class="text-8xl font-black mb-10 leading-tight">期末包棟</h1>'
    )
    content = content.replace('<div class="toc-item card-bg" onclick="goToSlide(8)">07 Day 3</div>', '')
    content = content.replace('05/01 (五) 14:00', '06/29 (一) 14:00')
    content = content.replace('05/03 (日) 11:00', '07/01 (三) 13:00')
    content = content.replace('三芝老農夫農場', '歸巢民宿Villa')
    content = content.replace('新北市三芝區芝蘭路62之5號', '宜蘭縣礁溪鄉二龍村砂港路77號')

    # 費用更新為社員/非社員
    old_cost = """            <div class="flex flex-col items-center justify-center py-24 card-bg text-center">
                <p class="text-3xl opacity-60 mb-8">每一位社員僅需</p>
                <div class="flex items-baseline">
                    <span class="text-6xl mr-4">$</span>
                    <span class="text-[12rem] font-black leading-none">1,300</span>
                </div>
                <div class="mt-16 px-12 py-5 bg-blue-500/40 text-blue-200 rounded-full font-black text-2xl">
                    原價 1,500，社團補助 200
                </div>
            </div>"""
            
    new_cost = """            <div class="flex flex-col items-center justify-center py-12 card-bg text-center">
                <p class="text-3xl opacity-60 mb-8 font-bold">本期費用規劃</p>
                <div class="w-full flex flex-col gap-5 mb-8">
                    <div class="flex items-center justify-between border-b border-white/10 pb-3 px-6">
                        <span class="text-3xl font-bold opacity-80">社員</span>
                        <span class="text-5xl font-black text-lime-400">$ 2,000</span>
                    </div>
                    <div class="flex items-center justify-between border-b border-white/10 pb-3 px-6">
                        <span class="text-3xl font-bold opacity-80">非社員</span>
                        <span class="text-5xl font-black text-yellow-300">$ 2,200</span>
                    </div>
                </div>
                <div class="px-8 py-3 bg-lime-500/20 text-lime-300 rounded-full font-bold text-lg leading-snug">
                    暫定多退少補，已加一成設備維護
                </div>
            </div>"""
    content = content.replace(old_cost, new_cost)

    # 交通與大眾交通更新
    old_transport = """            <div class="card-bg mb-8">
                <p class="font-black text-2xl text-blue-400 mb-2 uppercase tracking-widest">BUS 861/863</p>
                <p class="text-3xl font-black">捷運淡水或紅樹林站</p>
                <p class="opacity-60 text-xl mt-3 leading-relaxed">至「芝蘭入口」站後步行約 9 分鐘</p>
                <div class="h-1 bg-white/10 my-8"></div>
                <p class="font-black text-2xl text-blue-400 mb-2 uppercase tracking-widest">MOTORCYCLE</p>
                <p class="text-3xl font-black">直接導航「三芝老農夫農場」</p>
            </div>
            <a href="https://maps.google.com/maps?q=三芝老農夫農場&t=&z=13&ie=UTF8&iwloc=&output=embed"
                class="card-bg map-btn !p-0 rounded-[2rem] overflow-hidden" style="height: 320px;" target="_blank">
                <div class="flex flex-col items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-24 h-24 mb-4" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                            d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                            d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                    <p class="text-3xl font-black">開啟 Google Maps</p>
                    <p class="text-xl opacity-60 mt-2">啟動導航至三芝老農夫農場</p>
                </div>
            </a>"""
            
    new_transport = """            <div class="card-bg mb-6 border-l-[8px] border-lime-400">
                <p class="font-black text-2xl text-lime-400 mb-2 uppercase tracking-widest">1. 大眾交通</p>
                <p class="text-3xl font-black">台北車站大廳一樓黑白格</p>
                <p class="opacity-80 text-xl mt-3 leading-relaxed">
                    11:50~12:00 集合出發礁溪 (選擇性)<br>
                    地圖連結：<a href="https://www.google.com/maps/dir/%E5%8F%B0%E5%8C%9F%E8%BB%8A%E7%AB%99/%E7%A4%81%E6%BA%AA%E8%BB%8A%E7%AB%99" target="_blank" class="text-lime-300 underline font-bold">北車往礁溪</a>
                </p>
                <div class="h-1 bg-white/10 my-6"></div>
                <p class="font-black text-2xl text-lime-400 mb-2 uppercase tracking-widest">2. 自行騎車</p>
                <p class="text-2xl font-black">午餐(12:30)：礁溪站</p>
                <p class="text-2xl font-black">民宿(15:00後)：歸巢民宿Villa</p>
            </div>
            <a href="https://maps.google.com/maps?q=宜蘭縣礁溪鄉二龍村砂港路77號"
                class="card-bg map-btn !p-6 rounded-[2rem] overflow-hidden" target="_blank">
                <div class="flex flex-col items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-16 h-16 mb-2" fill="none" viewBox="0 0 24 24"
                        stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                            d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
                            d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                    <p class="text-3xl font-black">開啟 Google Maps</p>
                    <p class="text-lg opacity-60 mt-1">導航至歸巢民宿Villa</p>
                </div>
            </a>"""
    content = content.replace(old_transport, new_transport)

    # 準備物品
    old_packing_body = """                        <tr>
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
                        </tr>"""
                        
    new_packing_body = """                        <tr>
                            <td>🪥 牙刷/膏</td>
                            <td>👕 換衣</td>
                            <td>🧼 *沐浴</td>
                        </tr>
                        <tr>
                            <td>🧣 *毛巾</td>
                            <td>🍽️ *餐具</td>
                            <td>🔋 充電器</td>
                        </tr>
                        <tr>
                            <td>☂️ 雨具</td>
                            <td>🩴 *拖鞋</td>
                            <td>🧻 衛生紙</td>
                        </tr>
                        <tr>
                            <td>💊 個人藥</td>
                            <td>🩱 *泳具</td>
                            <td></td>
                        </tr>"""
    content = content.replace(old_packing_body, new_packing_body)
    
    old_packing_note = """            <div class="card-bg p-10 bg-blue-900/30">
                <p class="text-blue-300 font-black mb-4 text-3xl">特別說明：</p>
                <p class="text-2xl opacity-90 leading-relaxed">"*" 標記可用衣物替代。餐具為必備。海邊戲水攜帶泳具請注意安全。</p>
            </div>"""
            
    new_packing_note = """            <div class="card-bg p-8 bg-emerald-900/30 border-l-4 border-emerald-400">
                <p class="text-lime-300 font-black mb-2 text-2xl">特別說明：</p>
                <p class="text-xl opacity-90 leading-relaxed">"*" 表示非必要項目。民宿宣導環保，餐具建議自備，第二天有海邊活動請注意戲水安全。</p>
            </div>"""
    content = content.replace(old_packing_note, new_packing_note)

    # 注意事項
    old_notes = """            <div class="card-bg border-l-[16px] border-red-500 mb-10 py-10">
                <p class="text-4xl font-black">🍱 第一天中午不供餐</p>
                <p class="opacity-60 text-2xl mt-4">請在出發集合前先行用餐</p>
            </div>
            <div class="card-bg border-l-[16px] border-blue-500 mb-10 py-10">
                <p class="text-4xl font-black">🌊 注意戲水安全</p>
                <p class="opacity-60 text-2xl mt-4">附近海邊戲水請確保自身安全</p>
            </div>
            <div class="card-bg border-l-[16px] border-green-500 py-10">
                <p class="text-4xl font-black">🦟 防蚊與保暖</p>
                <p class="opacity-60 text-2xl mt-4">留意氣候準備防蚊液與雨具</p>
            </div>"""
            
    new_notes = """            <div class="card-bg border-l-[16px] border-red-500 mb-6 py-6">
                <p class="text-3xl font-black text-red-400">🍱 第一天午餐與採買</p>
                <p class="opacity-80 text-xl mt-2">12:30~13:30 為午餐，14:05 全聯礁溪店集合買晚餐食材</p>
            </div>
            <div class="card-bg border-l-[16px] border-lime-500 mb-6 py-6">
                <p class="text-3xl font-black text-lime-400">🌊 注意戲水安全</p>
                <p class="opacity-80 text-xl mt-2">第二天海邊活動請確保安全，視需求攜帶泳具</p>
            </div>
            <div class="card-bg border-l-[16px] border-emerald-500 py-6">
                <p class="text-3xl font-black text-emerald-400">🦟 個人拖鞋與毛巾</p>
                <p class="opacity-80 text-xl mt-2">民宿倡導環保，拖鞋視活動穿戴，介意衛生可自備毛巾</p>
            </div>"""
    content = content.replace(old_notes, new_notes)

    # 行程表
    old_schedules = """    <!-- 8. 行程安排 (Day 1) - 新增回補 -->
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
                <div class="flex justify-between text-3xl text-blue-400 font-black"><span>11:30</span> <span>快樂回家 🚌</span></div>
            </div>
        </div>
    </div>"""
    
    new_schedules = """    <!-- 8. 行程安排 (Day 1 & Day 2) -->
    <div class="slide" style="transform: translateX(700%);">
        <h2 class="slide-title">第一天行程</h2>
        <div class="content-box" style="margin-bottom:1rem">
            <div class="card-bg space-y-4 py-4">
                <div class="flex justify-between text-2xl font-black"><span>11:50</span> <span>火車站集合</span></div>
                <div class="flex justify-between text-2xl"><span>12:00</span> <span class="opacity-80">出發礁溪 (選)</span></div>
                <div class="flex justify-between text-2xl"><span>14:05</span> <span class="opacity-80">採買食材 (全聯)</span></div>
                <div class="flex justify-between text-2xl"><span>18:00</span> <span class="opacity-80">前往羅東夜市</span></div>
                <div class="flex justify-between text-2xl text-lime-300 font-black"><span>20:45</span> <span>晚間活動 💬</span></div>
            </div>
        </div>

        <h2 class="slide-title">第二天行程</h2>
        <div class="content-box">
            <div class="card-bg space-y-4 py-4">
                <div class="flex justify-between text-2xl font-black"><span>08:00</span> <span>早餐＋健康操 🤸</span></div>
                <div class="flex justify-between text-2xl"><span>10:00</span> <span class="opacity-80">晨間閱讀 📖</span></div>
                <div class="flex justify-between text-2xl text-lime-300 font-black"><span>13:30</span> <span>海邊走走 / 戲水 🌊</span></div>
                <div class="flex justify-between text-2xl"><span>19:30</span> <span class="opacity-80">晚間活動 💬</span></div>
            </div>
        </div>
    </div>

    <!-- 9. 行程安排 (Day 3) -->
    <div class="slide" style="transform: translateX(800%);">
        <h2 class="slide-title">第三天行程</h2>
        <div class="content-box">
            <div class="card-bg text-center space-y-10 py-16 border-l-[8px] border-yellow-400">
                <div class="flex justify-between text-3xl font-black px-6"><span>08:00</span> <span>起床用膳 🍳</span></div>
                <div class="flex justify-between text-3xl px-6"><span>10:00</span> <span class="opacity-70">場復收拾 🧹</span></div>
                <div class="flex justify-between text-3xl text-lime-300 font-black px-6"><span>10:30</span> <span>快樂回家 🚌</span></div>
            </div>
        </div>
    </div>"""
    content = content.replace(old_schedules, new_schedules)

    # 結尾更換
    content = content.replace(
        '<h1 class="text-[6rem] md:text-[8rem] font-black mb-6 leading-none text-blue-400">Camping Time</h1>',
        '<h1 class="text-[6rem] md:text-[8rem] font-black mb-6 leading-none text-lime-300">Enjoy the Villa</h1>'
    )
    content = content.replace('<p class="text-3xl md:text-4xl opacity-60 italic mb-8">享受大自然的美好</p>', '<p class="text-3xl md:text-4xl opacity-60 italic mb-8">期末包棟，好好放鬆一下！</p>')
    content = content.replace('border-blue-400', 'border-lime-400')
    content = content.replace('text-blue-400', 'text-lime-300')
    content = content.replace('text-blue-300', 'text-lime-200')
    content = content.replace('瞌睡蟲！💤', '瞌睡蟲！💤') # Ensure it is the same

    with open('information_phone.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_index()
    update_pc()
    update_mobile()
    print("網頁更新完成！")
