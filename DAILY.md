# Ежедневный запуск фабрики

Запускается по расписанию каждые 8 часов (МСК): 08:00 — `full` (тренды + идеи + видео), 00:00 и 16:00 — `sounds` (только видео).
Всё общение с владельцем — через бота (`factory/tg.py`), по-русски, коротко.

## 0. Подготовка

```bash
cd lali-factory && git pull
python3 -c "import faster_whisper, shazamio" 2>/dev/null || pip install --only-binary=:all: faster-whisper shazamio
```

## 1. Забрать сообщения

```bash
python3 factory/tg.py pull && python3 factory/tg.py fetch && python3 factory/tg.py jobs
```

`pull` нужно сделать в каждом запуске: Telegram хранит непрочитанное только 24 часа.

## 2. Тренды и идеи (только режим `full`)

1. Прочитай `notes` (идеи владельца) из `python3 factory/tg.py jobs` — они в приоритете.
2. Через веб-поиск найди, что сейчас в тренде в русском TikTok/Reels: звуки и треки недели
   (рэп, хардстайл-ремиксы, вирусные строчки), мем-форматы. Нужны свежие, за последние 7 дней.
3. Отправь владельцу 5–8 идей одним сообщением (`python3 factory/tg.py text -`):
   для каждой — трек/звук (что искать в TikTok), какой кусок, и сценарий в 1–2 строки: какие карточки,
   что делает Лали. В конце: «Перешли мне звуки, которые понравились, — сделаю видео 🎬».
4. `python3 factory/tg.py clear-notes` после того, как учёл идеи.

## 3. Видео из присланных звуков (оба режима)

Для каждого задания со статусом `new` (и `fix` — с учётом `feedback`):

1. `python3 factory/shazam.py jobs/<id>/in.mp4` → SONG.
2. `python3 factory/transcribe.py jobs/<id>/in.mp4 large-v3 "<артист, трек, ключевые слова>" > jobs/<id>/transcript.txt`
   Если Whisper ошибся, а текст известен, — поправь слова вручную, таймкоды бери от Whisper.
3. Напиши `jobs/<id>/spec.py` (формат — в CLAUDE.md, образцы — `examples/v21…v30`).
4. Превью: `mkdir -p jobs/<id>/pv && python3 factory/build.py jobs/<id> && node factory/render.js jobs/<id>/scene_final.html jobs/<id>/pv 0 <START> <t1>,<t2>,<t3>` — посмотри кадры, поправь.
5. `./factory/make.sh jobs/<id>` → `jobs/<id>/out.mp4`.
6. `python3 factory/tg.py video jobs/<id>/out.mp4 "🎬 <SONG>\n✅ готово к публикации. Если нужно поправить — ответь на видео текстом." <id>`
   Владелец сам решает, что выкладывать. Ответ ✅/❌ — необязательный.

Если звуков нет — в режиме `sounds` ничего не пиши владельцу.
Если что-то сломалось — коротко напиши владельцу, что именно, не молчи.

## 4. Сохранить состояние

```bash
git add -A && git commit -m "Daily run $(date +%F) <mode>" && git push origin main
```

Обязательно, иначе следующий запуск потеряет очередь и статусы.
