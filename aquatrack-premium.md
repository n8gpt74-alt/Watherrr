# План Улучшения AquaTrack Pro (Premium / Функционал)

## Overview

Приложение AquaTrack имеет хорошую основу, но страдает от нескольких анти-паттернов дизайна и функциональных багов. Текущий дизайн использует запрещённые фиолетовые оттенки (Purple Ban) и устаревший Soft UI (ауры и размытия). Уведомления зависят от открытой вкладки браузера, а в коде есть дублирующиеся функции, что нарушает работу режима "Не беспокоить".

## Project Type

WEB (Vanilla PWA)

## Success Criteria

1. **Premium Aesthetic**: Удалён фиолетовый цвет, внедрена новая геометрия (Brutalist Tech / High-Contrast Teal + Black), улучшена читаемость и микроанимации.
2. **Рабочие уведомления**: Уведомления не зависят от открытой вкладки `setInterval` (внедрены таймеры Service Worker и системное планирование).
3. **Функциональные исправления**: Устранены конфликты в функциях (двойной `isDndActive`), отлажен быстрый ввод, статистика и календарь работают синхронно.

## Tech Stack

- HTML5 / CSS3 (кастомные стили, отказ от Rounded Grid в пользу асимметрии)
- Vanilla JavaScript (Local Storage, Push/Service Worker API)

## File Structure

- `index.html` — Основная логика и разметка
- `sw.js` — Service Worker для оффлайна и уведомлений

## Task Breakdown

### 1. Функциональный рефакторинг (Bugs & Logic)

- **Agent**: `frontend-specialist`
- **Skills**: `clean-code`
- Долгожданные багфиксы: Удалить дубликат функции `isDndActive`, исправить валидацию кастомного количества воды, отладить перерисовку Progress Ring.
- **INPUT**: Текущий `index.html` → **OUTPUT**: Исправленный JS-код → **VERIFY**: Тестирование быстрого добавления и статуса "Не беспокоить".

### 2. Автономные уведомления (Service Worker)

- **Agent**: `frontend-specialist`
- **Skills**: `nodejs-best-practices`
- Перенести логику `setInterval` в `sw.js` или использовать Scheduled Push. Так как мы PWA без бекенда, внедрим надежные интервалы в фоне через периодические запросы API (Periodic Background Sync API) или Alarm API.
- **INPUT**: Текущие `sw.js` и `setInterval` → **OUTPUT**: Фоновка уведомлений → **VERIFY**: Уведомления работают при закрытой вкладке.

### 3. Premium Design Overhaul

- **Agent**: `frontend-specialist`
- **Skills**: `frontend-design`, `ui-ux-pro-max`
- Полный отказ от Фиолетового (Purple Ban). Переход на **Tech Minimalist** (Black & Acid Green/Teal) или **Liquid Silver**.
- Отмена круглых краев везде (`border-radius: 2px` вместо `24px`).
- Изменение "Standard Layout": вместо сжатых карточек - слоистое перекрытие. Разработка более агрессивного прогресс-кольца.
- **INPUT**: Текущие CSS-стили → **OUTPUT**: Новая система CSS переменных и микроанимации → **VERIFY**: Мощный и незабываемый UX.

## Phase X: Verification

- [ ] Очистить код от `console.log`.
- [ ] Запуск `python .agent/scripts/checklist.py .`
- [ ] Проверить контрастность новых цветов (Web Design Guidelines).
- [ ] Убедиться, что режим "Не беспокоить" корректно мьютит Service Worker.
