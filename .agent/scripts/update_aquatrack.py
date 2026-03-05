import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. NEW CSS AESTHETIC (Liquid Silver / Brutalist Tech)
new_css = """    :root {
      --primary: #00E5FF; /* Cyber Cyan */
      --primary-light: #80F2FF;
      --primary-dark: #00B3CC;
      --bg: #050505;
      --bg-card: #0A0A0A;
      --surface: #111111;
      --surface-light: #1A1A1A;
      --text: #F3F4F6;
      --text-muted: #8B929A;
      --border: #333333;
      --border-focus: #00E5FF;
      --success: #00FF41;
      --error: #FF003C;
      --warning: #FFEA00;
      --info: #00E5FF;
      --font-mono: 'SF Mono', 'Fira Code', 'Courier New', monospace;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
    html { font-size: 16px; scroll-behavior: smooth; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      overflow-x: hidden;
      letter-spacing: -0.02em;
    }

    .gradient-bg {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 50% 0%, #151515 0%, #050505 100%);
      z-index: -1;
    }

    .app-container { max-width: 390px; margin: 0 auto; min-height: 100vh; position: relative; padding-bottom: 100px; display: flex; flex-direction: column;}
    
    .screen { display: none; padding: 40px 20px 40px; }
    .screen.active { display: block; animation: sharpFade 0.3s cubic-bezier(0.0, 0.0, 0.2, 1); }

    @keyframes sharpFade {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ===== ONBOARDING ===== */
    .onboarding-screen {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      text-align: center;
      padding: 40px 20px;
    }
    .onboarding-screen.active { display: flex; }

    .vibrant-drop {
      width: 120px;
      height: 120px;
      margin-bottom: 40px;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 2px solid var(--primary);
      transform: rotate(45deg);
      box-shadow: 8px 8px 0 rgba(0, 229, 255, 0.2);
    }
    .vibrant-drop::after {
      content: '💧';
      font-size: 48px;
      transform: rotate(-45deg);
    }

    .onboarding-title {
      font-size: 42px;
      font-weight: 900;
      color: var(--text);
      margin-bottom: 14px;
      text-transform: uppercase;
      letter-spacing: -1.5px;
      line-height: 1;
    }

    .onboarding-subtitle {
      font-size: 14px;
      color: var(--text-muted);
      margin-bottom: 40px;
      line-height: 1.6;
      font-family: var(--font-mono);
      text-transform: uppercase;
    }

    .vibrant-cta {
      width: 100%;
      height: 60px;
      background: var(--primary);
      color: #000;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-weight: 800;
      font-size: 16px;
      text-transform: uppercase;
      letter-spacing: 1px;
      transition: all 0.2s cubic-bezier(0.0, 0.0, 0.2, 1);
      box-shadow: 4px 4px 0 var(--border);
    }

    .vibrant-cta:active { 
      transform: translate(2px, 2px); 
      box-shadow: 2px 2px 0 var(--border);
    }

    .scroll-to-app { animation: scrollToApp 0.5s cubic-bezier(0.0, 0.0, 0.2, 1) forwards; }
    @keyframes scrollToApp { 0% { transform: translateY(0); opacity: 1; } 100% { transform: translateY(-100vh); opacity: 0; } }

    /* ===== COMMON COMPONENTS ===== */
    .header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 32px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }

    .header-title {
      font-size: 24px;
      font-weight: 800;
      color: var(--text);
      text-transform: uppercase;
      letter-spacing: -0.5px;
    }

    .icon-btn {
      width: 40px;
      height: 40px;
      background: var(--surface);
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .icon-btn:hover { border-color: var(--primary); color: var(--primary); }
    .icon-btn:active { transform: translate(2px, 2px); }
    .icon-btn svg { width: 18px; height: 18px; stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: square; }

    .card {
      background: var(--surface);
      padding: 24px;
      border: 1px solid var(--border);
      margin-bottom: 16px;
      position: relative;
    }

    .card::before {
      content: '';
      position: absolute;
      top: -1px; left: -1px;
      width: 10px; height: 10px;
      border-top: 2px solid var(--primary);
      border-left: 2px solid var(--primary);
      opacity: 0;
      transition: opacity 0.3s;
    }
    
    .card:hover::before { opacity: 1; }

    .card-title {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
      text-transform: uppercase;
      letter-spacing: 1px;
      font-family: var(--font-mono);
    }

    .btn {
      padding: 14px 20px;
      border: 1px solid transparent;
      font-size: 14px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      cursor: pointer;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }

    .btn-primary { background: var(--primary); color: #000; box-shadow: 4px 4px 0 var(--border); }
    .btn-primary:active { transform: translate(2px, 2px); box-shadow: 2px 2px 0 var(--border); }

    .btn-secondary { background: transparent; color: var(--text); border: 1px solid var(--border); }
    .btn-secondary:hover { border-color: var(--primary); color: var(--primary); }
    
    .btn-danger { background: var(--error); color: #000; box-shadow: 4px 4px 0 #80001e; }
    .btn-full { width: 100%; }

    .toggle {
      width: 48px;
      height: 24px;
      background: var(--surface-light);
      position: relative;
      cursor: pointer;
      transition: background 0.2s;
      border: 1px solid var(--border);
    }

    .toggle.active { background: var(--primary); border-color: var(--primary); }

    .toggle-knob {
      width: 20px;
      height: 20px;
      background: var(--text);
      position: absolute;
      top: 1px; left: 1px;
      transition: transform 0.2s cubic-bezier(0.0, 0.0, 0.2, 1);
    }

    .toggle.active .toggle-knob { transform: translateX(24px); background: #000; }

    /* ===== PROGRESS RING ===== */
    .progress-container {
      position: relative;
      width: 260px;
      height: 260px;
      margin: 20px auto 40px;
    }

    .progress-ring { transform: rotate(-90deg); filter: drop-shadow(0 0 10px rgba(0,229,255,0.2)); }
    .progress-ring__track { fill: none; stroke: var(--surface-light); stroke-width: 4; stroke-linecap: square; }
    .progress-ring__progress {
      fill: none;
      stroke: var(--primary);
      stroke-width: 6;
      stroke-linecap: square;
      transition: stroke-dashoffset 0.5s cubic-bezier(0.0, 0.0, 0.2, 1);
    }
    .progress-ring__thumb {
      fill: var(--primary);
      stroke: var(--bg);
      stroke-width: 2;
      transition: transform 0.5s cubic-bezier(0.0, 0.0, 0.2, 1);
    }

    .progress-center {
      position: absolute;
      top: 50%; left: 50%;
      transform: translate(-50%, -50%);
      text-align: center;
      width: 100%;
    }

    .progress-label { font-size: 10px; font-weight: 700; color: var(--text-muted); margin-bottom: 4px; text-transform: uppercase; letter-spacing: 2px; font-family: var(--font-mono); }
    .progress-value {
      font-size: 56px;
      font-weight: 900;
      color: var(--text);
      line-height: 1;
      letter-spacing: -2px;
    }
    .progress-unit { font-size: 12px; font-weight: 600; color: var(--text-muted); margin-top: 4px; font-family: var(--font-mono); }
    .progress-delta {
      font-size: 10px;
      font-weight: 700;
      margin-top: 16px;
      display: inline-block;
      padding: 4px 8px;
      border: 1px solid;
      font-family: var(--font-mono);
      text-transform: uppercase;
    }

    .progress-delta.positive { color: var(--success); border-color: var(--success); }
    .progress-delta.negative { color: var(--error); border-color: var(--error); }

    /* ===== QUICK ADD ===== */
    .quick-add {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-bottom: 24px;
    }

    .quick-add-btn {
      height: 70px;
      background: var(--surface);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .quick-add-btn:hover { border-color: var(--text-muted); }
    .quick-add-btn:active { transform: translateY(2px); }
    .quick-add-btn.selected {
      border-color: var(--primary);
      background: rgba(0, 229, 255, 0.1);
      box-shadow: inset 2px 2px 0 var(--primary);
    }

    .quick-add-icon svg { width: 24px; height: 24px; stroke: var(--text); fill: none; stroke-width: 1.5; stroke-linecap: square; }
    .quick-add-btn.selected .quick-add-icon svg { stroke: var(--primary); }
    .quick-add-label { font-size: 11px; font-weight: 700; color: var(--text-muted); font-family: var(--font-mono); }
    .quick-add-btn.selected .quick-add-label { color: var(--primary); }

    /* ===== DRINK TYPE SELECTOR ===== */
    .drink-types {
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: none;
    }
    .drink-types::-webkit-scrollbar { display: none; }

    .drink-type-btn {
      flex-shrink: 0;
      padding: 12px 16px;
      background: var(--surface);
      border: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      cursor: pointer;
      transition: all 0.15s;
    }

    .drink-type-btn.selected {
      border-color: var(--primary);
      box-shadow: 2px 2px 0 var(--primary);
    }

    .drink-type-icon { font-size: 20px; filter: grayscale(1); }
    .drink-type-btn.selected .drink-type-icon { filter: grayscale(0); }
    .drink-type-name { font-size: 10px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }
    .drink-type-btn.selected .drink-type-name { color: var(--primary); }
    .drink-type-coef { font-size: 10px; color: var(--border); font-family: var(--font-mono); }

    /* ===== STATS GRID ===== */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1px;
      background: var(--border);
      border: 1px solid var(--border);
      margin-bottom: 24px;
    }

    .stat-card {
      background: var(--surface);
      padding: 20px 16px;
      cursor: default;
    }

    .stat-icon { margin-bottom: 12px; }
    .stat-icon svg { width: 20px; height: 20px; stroke: var(--primary); fill: none; stroke-width: 1.5; stroke-linecap: square; }
    
    .stat-value { font-size: 28px; font-weight: 800; color: var(--text); margin-bottom: 4px; letter-spacing: -1px; }
    .stat-label { font-size: 10px; color: var(--text-muted); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; font-family: var(--font-mono); }

    /* ===== CALENDAR & ACHIEVEMENTS ===== */
    .calendar { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; margin-top: 16px; }
    .calendar-header { display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; margin-bottom: 8px; }
    .calendar-day-header { text-align: center; font-size: 10px; font-weight: 700; color: var(--text-muted); padding: 8px 0; text-transform: uppercase; font-family: var(--font-mono); }
    
    .calendar-day {
      aspect-ratio: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 700;
      background: var(--surface);
      border: 1px solid var(--border);
      position: relative;
    }

    .calendar-day.today { border-color: var(--primary); color: var(--primary); }
    .calendar-day.success { background: var(--success); color: #000; border-color: var(--success); }
    .calendar-day.success .percentage { color: rgba(0,0,0,0.6); }
    .calendar-day.partial { border-color: var(--warning); color: var(--warning); }
    .calendar-day.missed { border-color: var(--error); color: var(--error); opacity: 0.6; }
    .calendar-day.empty { opacity: 0; }
    .calendar-day .percentage { font-size: 8px; color: var(--text-muted); margin-top: 2px; font-family: var(--font-mono); }

    .achievements-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .achievement {
      background: var(--surface);
      padding: 16px 8px;
      text-align: center;
      border: 1px solid var(--border);
      transition: all 0.2s;
    }

    .achievement.locked { opacity: 0.3; filter: grayscale(1); border-style: dashed; }
    .achievement.unlocked { border-color: var(--primary); box-shadow: 2px 2px 0 rgba(0, 229, 255, 0.2); }
    .achievement-icon { font-size: 28px; margin-bottom: 12px; }
    .achievement-name { font-size: 10px; font-weight: 800; margin-bottom: 4px; text-transform: uppercase; }
    .achievement-desc { font-size: 9px; color: var(--text-muted); font-family: var(--font-mono); }

    /* ===== HOURLY CHART ===== */
    .hourly-chart { display: flex; align-items: flex-end; justify-content: space-between; height: 120px; padding: 16px 0; gap: 2px; }
    .hour-bar { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px; }
    .hour-bar-fill { width: 100%; max-width: 14px; background: var(--primary); transition: height 0.3s ease; min-height: 2px; }
    .hour-bar-label { font-size: 8px; color: var(--text-muted); font-family: var(--font-mono); transform: rotate(-90deg); margin-top: 10px; }

    /* ===== INPUTS ===== */
    .input-group { margin-bottom: 16px; }
    .input-label { font-size: 10px; font-weight: 700; color: var(--text-muted); margin-bottom: 8px; display: block; text-transform: uppercase; letter-spacing: 1px; }
    .input {
      width: 100%;
      height: 48px;
      padding: 0 16px;
      border: 1px solid var(--border);
      background: var(--bg);
      font-size: 16px;
      font-weight: 600;
      color: var(--text);
      transition: all 0.2s;
      font-family: var(--font-mono);
    }
    .input:focus { outline: none; border-color: var(--primary); box-shadow: inset 4px 0 0 var(--primary); }
    .input-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    
    .select {
      appearance: none;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%238B929A' stroke-width='2' stroke-linecap='square'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 12px center;
      background-size: 16px;
    }

    /* ===== BOTTOM NAV ===== */
    .bottom-nav {
      position: fixed;
      bottom: 0; left: 50%;
      transform: translateX(-50%);
      width: 100%;
      max-width: 390px;
      height: 80px;
      background: var(--bg);
      border-top: 1px solid var(--border);
      display: flex;
      align-items: flex-start;
      padding-top: 8px;
      z-index: 100;
    }
    .nav-items { display: flex; flex: 1; justify-content: space-around; align-items: center; }
    .nav-item {
      display: flex; flex-direction: column; align-items: center; gap: 6px;
      padding: 8px; cursor: pointer; border: none; background: transparent;
      min-width: 60px;
    }
    .nav-item svg { width: 22px; height: 22px; stroke: var(--text-muted); fill: none; stroke-width: 1.5; stroke-linecap: square; transition: all 0.2s; }
    .nav-item-label { font-size: 9px; font-weight: 700; color: var(--text-muted); transition: all 0.2s; text-transform: uppercase; letter-spacing: 0.5px; }
    .nav-item.active svg { stroke: var(--primary); }
    .nav-item.active .nav-item-label { color: var(--text); }
    .nav-item:active { transform: translateY(2px); }

    .fab-container { width: 64px; display: flex; justify-content: center; }
    .fab {
      width: 54px; height: 54px;
      background: var(--primary);
      border: none;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer;
      box-shadow: 4px 4px 0 var(--border);
      margin-top: -24px;
      transition: all 0.15s;
    }
    .fab:active { transform: translate(2px, 2px); box-shadow: 2px 2px 0 var(--border); }
    .fab svg { width: 24px; height: 24px; stroke: #000; fill: none; stroke-width: 2; stroke-linecap: square; }

    /* ===== TOAST & MODAL ===== */
    .toast {
      position: fixed;
      bottom: 100px; left: 50%;
      transform: translateX(-50%) translateY(20px);
      background: var(--surface);
      color: var(--text);
      border: 1px solid var(--primary);
      padding: 12px 20px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      opacity: 0;
      transition: all 0.2s;
      z-index: 200;
      text-align: center;
      box-shadow: 4px 4px 0 rgba(0, 229, 255, 0.2);
      font-family: var(--font-mono);
    }
    .toast.show { transform: translateX(-50%) translateY(0); opacity: 1; }

    .modal-overlay {
      position: fixed; inset: 0;
      background: rgba(0, 0, 0, 0.9);
      display: none; align-items: center; justify-content: center;
      z-index: 300; padding: 20px;
    }
    .modal-overlay.active { display: flex; }
    .modal {
      background: var(--bg);
      padding: 24px;
      width: 100%; max-width: 320px;
      border: 1px solid var(--border);
      box-shadow: 8px 8px 0 rgba(0, 229, 255, 0.1);
    }
    .modal-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; }
    .modal-title { font-size: 16px; font-weight: 800; text-transform: uppercase; }
    .modal-close { width: 24px; height: 24px; background: transparent; border: 1px solid var(--border); color: var(--text); cursor: pointer; display: flex; align-items: center; justify-content: center; }
    .modal-close:hover { border-color: var(--primary); color: var(--primary); }
    .modal-close svg { width: 14px; height: 14px; stroke: currentColor; fill: none; stroke-width: 2; }
    .modal-body { margin-bottom: 24px; font-size: 14px; color: var(--text-muted); line-height: 1.5; }
    .modal-buttons { display: flex; flex-direction: column; gap: 12px; }

    /* ===== CONFETTI ===== */
    .confetti { position: fixed; width: 6px; height: 6px; background: var(--primary); animation: confettiFall 2s ease-in forwards; z-index: 1000; }
    @keyframes confettiFall { 0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; } 100% { transform: translateY(100vh) rotate(720deg); opacity: 0; } }

    /* ===== BANNERS & TIPS ===== */
    .notification-banner {
      background: var(--surface);
      border: 1px solid var(--warning);
      padding: 16px; margin-bottom: 16px; display: none;
      box-shadow: 4px 4px 0 rgba(255, 234, 0, 0.2);
    }
    .notification-banner.show { display: block; }
    .notification-banner-title { font-size: 12px; font-weight: 800; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; color: var(--warning); text-transform: uppercase; }
    .notification-banner-text { font-size: 12px; color: var(--text-muted); margin-bottom: 16px; }
    .notification-banner-buttons { display: flex; gap: 8px; }
    
    .tip-card {
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 16px; margin-bottom: 24px;
      border-left: 2px solid var(--info);
    }
    .tip-card-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
    .tip-card-icon svg { width: 16px; height: 16px; stroke: var(--info); fill: none; stroke-width: 2; }
    .tip-card-title { font-size: 10px; font-weight: 800; text-transform: uppercase; color: var(--info); letter-spacing: 1px; }
    .tip-card-text { font-size: 12px; color: var(--text-muted); line-height: 1.5; font-family: var(--font-mono); }

    /* ===== LISTS ===== */
    .preset-item {
      display: flex; align-items: center; justify-content: space-between;
      padding: 16px; background: var(--surface);
      border: 1px solid var(--border);
      margin-bottom: 8px;
    }
    .preset-item-info { display: flex; align-items: center; gap: 12px; }
    .preset-item-name { font-size: 14px; font-weight: 700; color: var(--text); }
    .preset-item-amount { font-size: 12px; color: var(--text-muted); font-family: var(--font-mono); margin-top: 4px; }
    .preset-item-actions { display: flex; gap: 8px; }
    .preset-item-btn { width: 32px; height: 32px; background: var(--bg); border: 1px solid var(--border); color: var(--text); cursor: pointer; display: flex; align-items: center; justify-content: center; }
    .preset-item-btn:hover { border-color: var(--primary); color: var(--primary); }
    .preset-item-btn svg { width: 16px; height: 16px; stroke: currentColor; fill: none; stroke-width: 1.5; }

    .reminder-time {
      display: flex; align-items: center; justify-content: space-between;
      padding: 16px; background: var(--surface);
      border: 1px solid var(--border);
      margin-bottom: 8px;
    }
    .reminder-time-label { font-size: 12px; font-weight: 700; text-transform: uppercase; }
    .reminder-time-value { font-size: 14px; color: var(--primary); font-family: var(--font-mono); margin-top: 4px; font-weight: 700; }
    
    .section-title {
      font-size: 10px; font-weight: 800; color: var(--text-muted);
      text-transform: uppercase; letter-spacing: 1.5px;
      margin: 32px 0 16px; padding-bottom: 8px; border-bottom: 1px solid var(--border);
    }
    .section-title:first-child { margin-top: 0; }
"""

# Replace CSS
content = re.sub(r' +:root \{.*?</style>', new_css + '\n  </style>', content, flags=re.DOTALL)

# HTML Adjustments: Remove SVG defs and redundant classes
content = re.sub(r'<div class="orb orb-\d+"></div>', '', content)
content = re.sub(r'<svg style="position: absolute; width: 0; height: 0;">.*?</svg>', '', content, flags=re.DOTALL)

# SVG track uses url(#vibrantGradient), update it to use strokes
content = content.replace('stroke: url(#vibrantGradient);', 'stroke: var(--primary);')
content = content.replace('stroke: url(#navGradient);', 'stroke: var(--primary);')

# Find duplicate isDndActive function and remove it
isDndActive_func_count = content.count('function isDndActive()')
if isDndActive_func_count > 1:
    # Use split to isolate and remove one
    parts = content.split('function isDndActive() {')
    # Reassemble, omitting the last duplicate
    new_content = 'function isDndActive() {'.join(parts[:-1])
    
    # We still need to grab the closing brace of the omitted function
    # A bit crude via python, but since it's exactly 18 lines we can regex:
    content = re.sub(r'    function isDndActive\(\) \{\n(?:.*\n){17}    \}\n', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
